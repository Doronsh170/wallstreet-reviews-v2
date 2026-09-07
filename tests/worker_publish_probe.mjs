/**
 * Drives worker.js's POST /publish against a stubbed GitHub, and prints what it did
 * as JSON on stdout. tests/test_worker_publish.py reads that and asserts on it.
 *
 * Usage: node worker_publish_probe.mjs '<content to publish>' '<content already on the branch>'
 */
import worker from "../worker/worker.js";

const [pasted, onBranch] = process.argv.slice(2);

const env = {
  ADMIN_PASSWORD: "pw",
  GITHUB_TOKEN: "gh-token",
  REPO: "owner/repo",
  BRANCH: "main",
  ALLOWED_ORIGIN: "https://owner.github.io",
};

const calls = [];

globalThis.fetch = async (url, init = {}) => {
  const method = init.method || "GET";
  calls.push({ method, url: String(url), body: init.body ? JSON.parse(init.body) : null });

  if (url.includes("/actions/workflows/") && url.includes("/runs")) {
    return new Response(JSON.stringify({
      workflow_runs: [{
        id: 4242, status: "completed", conclusion: "failure",
        html_url: "https://run", run_started_at: "2026-09-07T16:21:19Z",
      }],
    }), { status: 200 });
  }
  if (url.includes("/contents/review_output.json") && method === "GET") {
    if (onBranch === "__missing__") return new Response("", { status: 404 });
    const b64 = Buffer.from(onBranch, "utf-8").toString("base64");
    return new Response(JSON.stringify({ content: b64, sha: "sha-on-branch" }), { status: 200 });
  }
  if (url.includes("/contents/review_output.json") && method === "PUT") {
    return new Response(JSON.stringify({ commit: { sha: "new-sha" } }), { status: 201 });
  }
  // 204 is what GitHub answers a dispatch with, and a 204 may carry no body at all.
  if (url.includes("/dispatches")) return new Response(null, { status: 204 });
  return new Response(JSON.stringify({ error: "unexpected" }), { status: 500 });
};

const response = await worker.fetch(
  new Request("https://admin.example/publish", {
    method: "POST",
    headers: { Authorization: "Bearer pw", "Content-Type": "application/json" },
    body: JSON.stringify({ content: pasted }),
  }),
  env,
);

console.log(JSON.stringify({
  status: response.status,
  body: await response.json(),
  committed: calls.filter((c) => c.method === "PUT").length,
  dispatched: calls.filter((c) => c.url.includes("/dispatches")).length,
  dispatch_body: (calls.find((c) => c.url.includes("/dispatches")) || {}).body,
}));
