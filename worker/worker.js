/**
 * Market Desk admin proxy — Cloudflare Worker.
 *
 * The one job: let admin.html run the review pipeline without a GitHub token ever
 * reaching the browser. The browser sends a passphrase you chose; the Worker holds a
 * fine-grained GitHub PAT as a secret and is the only thing that talks to GitHub.
 *
 * Secrets / vars (wrangler.toml + `wrangler secret put`):
 *   GITHUB_TOKEN    (secret) fine-grained PAT, THIS REPO ONLY,
 *                            Actions: Read+Write, Contents: Read+Write. Nothing else.
 *   ADMIN_PASSWORD  (secret) the passphrase you type into admin.html. Make it long.
 *   REPO            (var)    "owner/name"
 *   BRANCH          (var)    "main"
 *   ALLOWED_ORIGIN  (var)    exact origin of the site, e.g. "https://user.github.io"
 *
 * Endpoints (all require Authorization: Bearer <ADMIN_PASSWORD>):
 *   GET  /auth-check                 -> {ok:true}, only once the passphrase matches
 *   POST /gather   {mode}            -> dispatches "1 - Gather Review Input"
 *   GET  /status   ?workflow=&after= -> latest run newer than `after`
 *   GET  /raw                        -> raw_review_input.md + the run's snapshot
 *   POST /publish  {content}         -> commits review_output.json (fires publish), or
 *                                     dispatches the workflow when the content is
 *                                     unchanged; refuses anything not shaped like a review
 */

const GH = "https://api.github.com";
const GATHER_WORKFLOW = "gather_review.yml";
const PUBLISH_WORKFLOW = "publish_review.yml";

const VALID_MODES = [
  "daily_prep", "daily_summary", "weekly_summary", "weekly_prep",
  "intraday_update", "israel_prep", "israel_summary",
  "israel_weekly_summary", "israel_weekly_prep",
];

export default {
  async fetch(request, env) {
    const origin = env.ALLOWED_ORIGIN || "*";
    if (request.method === "OPTIONS") return new Response(null, { headers: cors(origin) });

    if (!(await authorized(request, env))) {
      // Slow down guessing. Workers have no shared counter without KV, and a
      // long passphrase plus this delay is enough for a single-user tool.
      await new Promise((r) => setTimeout(r, 1000));
      return json({ error: "unauthorized" }, 401, origin);
    }

    const url = new URL(request.url);
    try {
      switch (`${request.method} ${url.pathname}`) {
        case "POST /gather":  return await gather(request, env, origin);
        // Reached only after authorized() passed, so a 200 here proves the whole chain:
        // the URL resolves, CORS allows the origin, and the passphrase matches.
        case "GET /auth-check": return json({ ok: true }, 200, origin);
        case "GET /status":   return await status(url, env, origin);
        case "GET /raw":      return await raw(env, origin);
        case "GET /result":   return await result(env, origin);
        case "POST /publish": return await publish(request, env, origin);
        default:              return json({ error: "not found" }, 404, origin);
      }
    } catch (err) {
      return json({ error: String(err && err.message || err) }, 500, origin);
    }
  },
};

// ── helpers ────────────────────────────────────────────────────────

function cors(origin) {
  return {
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Headers": "Authorization, Content-Type",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Max-Age": "86400",
  };
}

function json(body, statusCode, origin) {
  return new Response(JSON.stringify(body), {
    status: statusCode,
    headers: { "Content-Type": "application/json; charset=utf-8", ...cors(origin) },
  });
}

function safeEqual(a, b) {
  const enc = new TextEncoder();
  const x = enc.encode(a || ""), y = enc.encode(b || "");
  if (x.length !== y.length) return false;
  let diff = 0;
  for (let i = 0; i < x.length; i++) diff |= x[i] ^ y[i];
  return diff === 0;
}

async function authorized(request, env) {
  const header = request.headers.get("Authorization") || "";
  const token = header.startsWith("Bearer ") ? header.slice(7) : "";
  // Both sides are trimmed. A passphrase is typed or pasted by hand into a browser
  // field, and stored with `wrangler secret put` which keeps whatever the shell fed
  // it — so a trailing newline or a stray space on EITHER side is invisible and would
  // fail a byte-exact compare with no way to tell it from a wrong passphrase.
  // Surrounding whitespace carries no entropy, so trimming costs nothing; the
  // comparison itself stays constant-time.
  const secret = String(env.ADMIN_PASSWORD || "").trim();
  return Boolean(secret) && safeEqual(token.trim(), secret);
}

async function gh(env, path, init = {}) {
  const r = await fetch(GH + path, {
    ...init,
    headers: {
      Authorization: `Bearer ${env.GITHUB_TOKEN}`,
      Accept: "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28",
      "User-Agent": "market-desk-admin",
      ...(init.headers || {}),
    },
  });
  return r;
}

async function ghJson(env, path, init) {
  const r = await gh(env, path, init);
  if (!r.ok) throw new Error(`GitHub ${r.status}: ${(await r.text()).slice(0, 300)}`);
  return r.json();
}

/** Newest run of a workflow, optionally only if it is newer than `after`. */
async function latestRun(env, workflow, after) {
  const path = `/repos/${env.REPO}/actions/workflows/${workflow}/runs?per_page=5&branch=${env.BRANCH}`;
  const data = await ghJson(env, path);
  const runs = data.workflow_runs || [];
  if (!runs.length) return null;
  const run = runs[0];
  // `after` is the run id that was newest before we dispatched. While the new run is
  // still being created GitHub keeps returning the old one — report "queued" for that
  // gap instead of reading the previous run's conclusion as ours.
  if (after && String(run.id) === String(after)) return { pending: true };
  return {
    id: run.id,
    status: run.status,             // queued | in_progress | completed
    conclusion: run.conclusion,     // success | failure | cancelled | null
    url: run.html_url,
    startedAt: run.run_started_at,
  };
}

// ── endpoints ──────────────────────────────────────────────────────

async function gather(request, env, origin) {
  const body = await request.json();
  const mode = String(body.mode || "");
  if (!VALID_MODES.includes(mode)) return json({ error: `bad mode: ${mode}` }, 400, origin);

  // Remember what the newest run was, so /status can tell ours apart from it.
  const before = await latestRun(env, GATHER_WORKFLOW);
  const r = await gh(env, `/repos/${env.REPO}/actions/workflows/${GATHER_WORKFLOW}/dispatches`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ ref: env.BRANCH, inputs: { review_mode: mode } }),
  });
  if (!r.ok) return json({ error: `dispatch failed: ${await r.text()}` }, 502, origin);
  return json({ ok: true, mode, after: before && before.id ? before.id : null }, 200, origin);
}

async function status(url, env, origin) {
  const workflow = url.searchParams.get("workflow") === "publish"
    ? PUBLISH_WORKFLOW : GATHER_WORKFLOW;
  const run = await latestRun(env, workflow, url.searchParams.get("after"));
  if (!run) return json({ state: "queued" }, 200, origin);
  if (run.pending) return json({ state: "queued" }, 200, origin);
  const state = run.status !== "completed" ? "running"
    : run.conclusion === "success" ? "success" : "failure";
  return json({ state, id: run.id, url: run.url, conclusion: run.conclusion }, 200, origin);
}

async function file(env, path) {
  const r = await gh(env, `/repos/${env.REPO}/contents/${path}?ref=${env.BRANCH}`);
  if (r.status === 404) return null;
  if (!r.ok) throw new Error(`GitHub ${r.status} reading ${path}`);
  const meta = await r.json();
  // atob gives latin-1 bytes; re-decode as UTF-8 so Hebrew survives.
  const bytes = Uint8Array.from(atob(meta.content.replace(/\n/g, "")), (c) => c.charCodeAt(0));
  return { text: new TextDecoder("utf-8").decode(bytes), sha: meta.sha };
}

async function raw(env, origin) {
  const md = await file(env, "raw_review_input.md");
  if (!md) return json({ error: "raw_review_input.md not found" }, 404, origin);
  const snapshotFile = await file(env, "raw_review_input.json");
  let snapshot = {};
  try { snapshot = snapshotFile ? JSON.parse(snapshotFile.text) : {}; } catch { snapshot = {}; }
  return json({
    content: md.text,
    mode: snapshot.mode || "",
    title: snapshot.expected_title || "",
    generatedAt: snapshot.generated_at || "",
  }, 200, origin);
}

/** The publish step's own verdict, in Hebrew — written by paste_review.py. */
async function result(env, origin) {
  const f = await file(env, "publish_status.json");
  if (!f) return json({ ok: null }, 200, origin);
  try {
    return json(JSON.parse(f.text), 200, origin);
  } catch {
    return json({ ok: null }, 200, origin);
  }
}

/* The gathered prompt embeds a JSON template of its own, so raw material pasted in
   place of the chat answer parses as a two-bullet review. admin.html refuses it
   before it gets here; this is the same check on the only path that can write
   review_output.json, so a stale page or a stray client cannot spend a commit and a
   CI run on something that was never a review.
   Kept in step with checkPayload() in admin.html and basic_payload_check() in
   paste_review.py. */
const PASTE_HINT = "יש להדביק כאן את תשובת ה-JSON המלאה של Claude.";
const PROMPT_MARKERS = [
  "אתה כותב סקירה פיננסית בעברית לאתר",
  "החזר עכשיו אך ורק את ה-JSON",
  "CRITICAL — OUTPUT FORMAT (MANDATORY)",
];

/** null when the content may go to the guards; a Hebrew reason when it may not. */
function payloadProblem(content) {
  if (PROMPT_MARKERS.some((m) => content.includes(m)))
    return `הודבק חומר הגלם (הפרומפט) ולא תשובת הצ'אט. ${PASTE_HINT}`;
  const text = content.replace(/```(?:json)?/g, "");
  const start = text.indexOf("{");
  if (start < 0) return `לא נמצא אובייקט JSON. ${PASTE_HINT}`;
  let depth = 0, inStr = false, esc = false, parsed = null;
  for (let i = start; i < text.length; i++) {
    const ch = text[i];
    if (inStr) {
      if (esc) esc = false;
      else if (ch === "\\") esc = true;
      else if (ch === '"') inStr = false;
      continue;
    }
    if (ch === '"') inStr = true;
    else if (ch === "{") depth++;
    else if (ch === "}" && --depth === 0) {
      try { parsed = JSON.parse(text.slice(start, i + 1)); } catch { parsed = null; }
      break;
    }
  }
  if (!parsed || typeof parsed !== "object" || Array.isArray(parsed))
    return `לא נמצא אובייקט JSON שלם. ${PASTE_HINT}`;
  if (!Array.isArray(parsed.sections))
    return `ה-JSON אינו נראה כמו סקירה — אין בו sections. ${PASTE_HINT}`;
  return null;
}

async function publish(request, env, origin) {
  const body = await request.json();
  const content = String(body.content || "").trim();
  if (!content) return json({ error: "empty content" }, 400, origin);
  const problem = payloadProblem(content);
  if (problem) return json({ error: problem }, 400, origin);

  const before = await latestRun(env, PUBLISH_WORKFLOW);
  const existing = await file(env, "review_output.json");
  const after = before && before.id ? before.id : null;

  // Re-publishing the very same text: the Contents API still writes a commit, but it
  // is an EMPTY one, and the workflow only fires `on: push: paths: [review_output.json]`
  // — so no run is ever created and the screen waits out its whole budget for a run
  // that cannot arrive. Dispatch the workflow directly instead: the file on the branch
  // already holds this content, so the guards run over exactly what was pasted.
  if (existing && existing.text.trim() === content) {
    const d = await gh(env, `/repos/${env.REPO}/actions/workflows/${PUBLISH_WORKFLOW}/dispatches`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ref: env.BRANCH }),
    });
    if (!d.ok) return json({ error: `dispatch failed: ${await d.text()}` }, 502, origin);
    return json({ ok: true, after, unchanged: true }, 200, origin);
  }

  const bytes = new TextEncoder().encode(content);
  let binary = "";
  for (const b of bytes) binary += String.fromCharCode(b);

  const r = await gh(env, `/repos/${env.REPO}/contents/review_output.json`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      message: "review: paste from admin screen",
      content: btoa(binary),
      branch: env.BRANCH,
      ...(existing ? { sha: existing.sha } : {}),
    }),
  });
  if (!r.ok) return json({ error: `commit failed: ${await r.text()}` }, 502, origin);
  return json({ ok: true, after, unchanged: false }, 200, origin);
}
