אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות בלבד, והחזר JSON בלבד.

You are writing a SHORT INTRADAY UPDATE in Hebrew for a financial website. The update is a
plain-language SUMMARY of what the curated X (Twitter) sources posted in the last two hours —
18:19–20:19 שעון ישראל, on 2026-11-05 (יום חמישי) — and nothing else.
Market state right now: השוק פתוח — שעות המסחר הרגילות בניו יורק. Never describe the market as trading or reacting when the regular
session is not open.

THE UPDATE SUMMARIZES THE SOURCES — it is NOT market analysis:
- Content comes EXCLUSIVELY from the source tweets at the bottom of this prompt. Nothing else enters the
  update: no price data, no daily-change percentages, no movers lists, no macro backdrop, no external
  headlines, no recap of earlier sessions, and no independent market interpretation of your own.
- The update does NOT determine who rose or fell in trading. Do NOT attach a price, percentage or direction
  to any story — unless the tweet itself states that figure/move explicitly, in which case report it as the
  source reported it.
- FILTER: keep only market-material posts. Ignore promotional posts, engagement bait, and posts with no
  market substance. A bare list of tickers with no story is NOT material.
- ONE bullet per topic. Several tweets about the same topic/company → merge into ONE bullet.
- Include EVERY material topic from the window — there is NO fixed bullet count, no minimum and no cap.
- Each bullet: 1-2 short, clear Hebrew sentences. Open with a short Hebrew topic label, then the summary.
  Anchor a bullet to its time when known using "בשעה 22:40" only. All times in this update are Israel time
  (already stated once in the window line above), so do NOT append "שעון ישראל" to individual bullets — it is
  redundant. At most one bullet may carry it if truly needed for clarity.
- If the window does not contain enough material posts, return a single bullet saying simply:
  "* אין מספיק עדכונים משמעותיים מהמקורות בחלון הזמן הזה." — nothing else. Never pad.
- FORBIDDEN PHRASES: never write "מסחר במזומן" or "שוק המזומן" in the Hebrew text. Refer to the regular
  session as "המסחר הרגיל".
- Web search may be used ONLY to verify a name, time or figure that already appears in a tweet — NEVER to
  discover or add stories, prices or data.

Rules:
- Write ONLY in Hebrew. English only for tickers ($AAPL), index names (S&P 500), and well-known financial terms in parentheses on first use.
- EVERY number in the update must appear in a source tweet. NEVER invent, estimate, or recall numbers from memory. A topic whose tweet has no figures is summarized WITHOUT figures.
- No buy/sell recommendations, no price targets, no "כדאי לקנות/למכור".
- Attribution: Claude→Anthropic, ChatGPT→OpenAI, Gemini→Google. Donald Trump is the CURRENT US President — never "לשעבר".
- No URLs, no Markdown links, no source domains in brackets. Attribution style: לפי Reuters / לפי Bloomberg only, and only when the tweet itself cites them.
- SINGLE-SOURCE ATTRIBUTION: a story appearing in only ONE source post with no outlet attribution is written with a hedge: "לפי דיווחים" — never as an established fact.
- Dates in visible text: Israeli format ONLY, e.g. "יום שני, 6.7.2026". NEVER write an ISO date (2026-07-06) inside the title or the bullets.
- NEVER use the ";" character anywhere. Use a comma or start a new sentence instead.
- NEVER use an em dash / double hyphen ("—" or "--") as a clause separator. Use a comma, a colon, or start a new sentence instead.
- Never OPEN a bullet with a raw ticker like "$TSLA:" or "$AMZN:". Open with the Hebrew company name: "מניית טסלה (TSLA):", "מניית אמזון (AMZN):", "מניית מטא (META):".
- NATURAL HEBREW: the update must read as if a person wrote it — modern, standard Hebrew (עברית תקנית), flowing and clear, professional but plain. NO translated-English phrasing (תרגומית), no literal English idioms, correct gender and number agreement. A sentence that would sound odd spoken aloud gets rewritten in simpler Hebrew.
- Never mention in the review that the items came from tweets/posts/X accounts.

══ PRE-OUTPUT SELF-VERIFICATION (MANDATORY — do this BEFORE returning the JSON) ══
Go over every bullet you wrote and check, one by one:
1. NUMBERS: every percentage, price and figure traces to a specific source post.
   Any number you cannot point to a source line for — DELETE it or the whole claim.
2. SCOPE: no story, price, index level or data point appears that is absent from the source posts.
3. DIRECTIONS: every directional claim (עלה/ירד/זינק/צנח) is stated by a source post — you did not determine
   any direction or magnitude yourself.
4. ATTRIBUTION: a story a source reports citing a news outlet keeps "לפי <outlet>". A story appearing in only
   ONE source post with no outlet attribution carries "לפי דיווחים" — never stated as an established fact.
5. FORMAT: no ";", no em dash, no ISO dates, no raw-ticker bullet openings, and the bullet count fits the
   instructions above (one bullet per material topic, no minimum and no cap).
6. SUMMARY ARRAY: one item per bullet, same order, same headlines, distilled (not copied) sentences, and every
   number/direction in the summary passes checks 1-4 as well.
7. LANGUAGE: every sentence reads like natural, standard Hebrew written by a person — no translated-English
   phrasing, correct gender/number agreement, professional but plain. A machine-sounding sentence gets rewritten.
If ANY check fails — fix the bullet and re-run the checks. Only then return the JSON.
══════════════════════════════════════════════════════════════════════════════

CRITICAL — OUTPUT FORMAT (MANDATORY):
- Return ONLY a JSON object, no backticks, no explanations, in EXACTLY this structure:
{
  "title": "עדכון ביניים מוול סטריט 🇺🇸 – יום חמישי, 5.11.2026, 20:19",
  "date": "2026-11-05",
  "summary": ["כותרת הנקודה: תמצית אמיתית של הנקודה במשפט קצר אחד", "כותרת שנייה: ...", "..."],
  "sections": [
    {
      "heading": "עדכון ביניים",
      "content": "* נושא ראשון: משפט אנליטי תמציתי עם מספרים.\n* נושא שני: ...\n* נושא שלישי: ..."
    }
  ]
}
- EXACTLY 1 section. Heading EXACTLY "עדכון ביניים". Title EXACTLY as given above.
- content = one string, bullets separated by \n, each bullet starts with "* ".
- The concluding bottom-line point is a REGULAR bullet inside content — never a separate section.
- No **, no ##, no HTML, no URLs inside content.
- "summary" = an array with ONE item per bullet in content, in the SAME order (include the bottom-line point too).
  Each item is "<אותה כותרת קצרה של הנקודה>: <משפט תמציתי אחד>". The sentence must DISTILL the essence of the point —
  what happened and why it matters — in your own words, up to ~20 words. Do NOT copy the first sentence of the
  bullet verbatim. All the same verification and direction rules apply to the summary as to the bullets.

US-ISRAEL TIME OFFSET TODAY: +7 hours (add 7 hours to US Eastern Time)
Key times in Israel time today:
- US economic data releases (CPI, NFP, PPI, GDP, Jobless Claims): 15:30 שעון ישראל
- ISM PMI, JOLTS, Consumer Confidence: 17:00 שעון ישראל
- FOMC rate decision / minutes: 21:00 שעון ישראל | Fed Chair press conference: 21:30 שעון ישראל
- US market open: 16:30 שעון ישראל | US market close: 23:00 שעון ישראל
USE ONLY THESE TIMES. Do NOT calculate your own offset.

══ WEB SEARCH POLICY ══
Web search is for VERIFICATION ONLY — confirming a name, time or figure that already appears in the source
tweets, for the window 18:19–20:19 Israel time on 2026-11-05. Do NOT use it to find additional news, headlines,
prices or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════

══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══
Already published on the site. Your update covers ONLY the last two hours. Mention an item below ONLY if there is a genuinely NEW development about it inside the two-hour window.

[עדכון ביניים]
* מניית אינטל ממשיכה להיחלש: מניית אינטל (INTC) יורדת בכ-6% נוספים היום, לאחר שצנחה בכ-29% ביום שישי. לפי דיווחים, המניה איבדה 57% מהשיא שנרשם לפני 86 ימי מסחר, אך עדיין מציגה עלייה של 58% מתחילת השנה.
* אפל לקראת פרסום הדוחות: אפל (AAPL) צפויה לפרסם את תוצאותיה הכספיות לאחר נעילת המסחר היום. לפי הדיווח, פרסום התוצאות מתוכנן לשעה 16:30 בחוף המזרחי בארה״ב, ולאחריו תתקיים שיחת המשקיעים.
* קראודסטרייק מרחיבה שיתופי פעולה: קראודסטרייק (CRWD) הודיעה בכנס Fal.Con Europe על שילוב פתרונות האבטחה שלה בתשתיות הבינה המלאכותית של דל ואנבידיה. במקביל, החברה מרחיבה את שיתוף הפעולה עם קורוויב להגנה על עומסי מחשוב ותשתיות ענן.
* תקשורת לוויינית מתקדמת: לפי דיווחים, AST ספייסמובייל (ASTS) ו-AT&T (T) השלימו בהצלחה העברת חיבור פעיל מרשת סלולרית קרקעית לרשת לוויינית באמצעות טלפון רגיל ללא התאמות. השלב הבא שעליו דיווחו החברות הוא בדיקות בטא בתנאי שימוש אמיתיים לקראת שירות מסחרי.
* מארוול ולומנטום במוקד האנליסטים: בנק ההשקעות B. Riley הותיר המלצת קנייה למארוול (MRVL), אך הפחית את מחיר היעד מ-365 ל-275 דולר בשל חששות מדילול ומסיכוני מיזוג עם לומנטום (LITE). במקביל, Stifel הוריד את המלצתו ללומנטום מהמלצת קנייה להחזק והפחית את מחיר היעד מ-1,232 ל-806 דולרים.
* מניית סנדיסק מציגה שיפור ברווחיות: לפי דיווחים, שיעור הרווח הגולמי של סנדיסק (SNDK) עלה מ-29.8% ברבעון הפיסקלי הראשון של 2026 ל-85% ברבעון המקביל של 2027. מדובר בשיפור משמעותי ברווח הגולמי ביחס להכנסות.
* מטא בוחנת גיוס חוב: לפי Bloomberg, מטא (META) בוחנת הנפקות אג״ח אפשריות בהיקף של לפחות 20 מיליארד דולר. הדיווח מתייחס לאפשרות לגיוס חוב, ולא להנפקה שכבר הושלמה.
* סייפר מיינינג במוקד: בנק H.C. Wainwright חזר על המלצת קנייה לסייפר מיינינג (CIFR) עם מחיר יעד של 20 דולר, תוך ציון ביקוש לתשתיות מחשוב וצבר פרויקטים בהיקף של 5.9 גיגה-ואט. מנגד, Northland הותיר המלצת תשואת יתר אך הפחית את מחיר היעד מ-27.50 ל-14 דולר.
* רוקט לאב משלימה שיגור: לפי דיווחים, רוקט לאב (RKLB) השלימה בהצלחה את המשימה ה-99 של משגר Electron. מדובר באבן דרך נוספת בפעילות השיגורים של החברה.
* אנתרופיק בוחנת הנפקה בבריטניה: לפי Bloomberg, אנתרופיק מתכננת לאפשר השתתפות של משקיעים פרטיים בבריטניה במקביל להנפקה המתוכננת בארה״ב. הדיווח מתייחס לתכנון ההנפקה ולא להשלמתה.
* מניות נוספות בשיא שנתי: לפי דיווחים, מניות ויזה (V), מאסטרקארד (MA), קוקה קולה (KO), ברקשייר האת'וויי (BRK.B), ריג'נרון (REGN) וורטקס (VRTX) הגיעו במהלך המסחר לשיאים של 52 שבועות. הנתון מתייחס לשיאים שנרשמו במהלך היום ולא בהכרח למחירי הנעילה.
* נובמבר בראייה היסטורית: לפי נתונים שפורסמו, מאז 1980 עלה מדד S&P 500 בחודש נובמבר בשיעור ממוצע של 2.1%, עם תשואה חיובית ב-74% מהשנים. מדובר בנתון עונתי היסטורי שאינו מעיד בהכרח על כיוון המסחר בנובמבר הנוכחי.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-11-05. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Thu Nov 05 17:38:00 +0000 2026]: Anthropic has now disclosed a record $895 billion in future AI infrastructure spending commitments. This includes both purchase commitments and leases for computing power and related infrastructure. $448 billion, or 50%, is expected to be incurred by the end of 2030, with ~$70 billion due over the next 12 months. The biggest commitments are to Broadcom, $AVGO, at $161 billion, followed by Google …

@KobeissiLetter [Thu Nov 05 17:20:26 +0000 2026]: Tech Stocks in Bear Market Territory: 1. SanDisk, $SNDK: -66% 2. Arm Holdings, $ARM: -64% 3. Coinbase, $COIN: -63% 4. Nebius, $NBIS: -62% 5. Seagate, $STX: -60% 6. Marvell Technology, $MRVL: -59% 7. ServiceNow, $NOW: -57% 8. Oracle, $ORCL: -56% 9. AppLovin, $APP: -54% 10. Circle, $CRCL: -54% 11. Super Micro Computer, $SMCI: -51% 12. Micron, $MU: -48% 13. Dell, $DELL: -47% 14. SpaceX, $SPCX: -47% …

@StockMKTNewz [Thu Nov 05 16:30:41 +0000 2026]: MICROSOFT $MSFT HAS PASSED ON EXTRA DATA CENTER CAPACITY FROM AI CLOUD STARTUP NSCALE IN TEXAS Microsoft had an option to add hundreds of megawatts at Nscale's Ward County site, but decided not to move forward because the project was still waiting on approval for a power connection, per Bloomberg. Microsoft also pulled out of a UK data center deal with Nscale last month.

@AIStockSavvy [Thu Nov 05 17:10:04 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $GOOGL Google Gemini Omni 1.2 Flash is generally available on Google Cloud effective today. Gemini Omni 1.2 Flash video generation priced at $0.07 per second for 720p video; now supports video generation and editing up to 15 seconds.

@wallstengine [Thu Nov 05 16:22:51 +0000 2026]: DEMOCRATS ARE GEARING UP TO PROBE JPMORGAN'S $JPM RELATIONSHIP WITH JEFFREY EPSTEIN, PER CNBC https://t.co/CJCCwP5LKa

@AIStockSavvy [Thu Nov 05 17:05:10 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $GOOGL Google will invest $17 bln to build its first data center in Wyoming.

@wallstengine [Thu Nov 05 17:14:46 +0000 2026]: $ARM CEO SAYS THE TECH SELLOFF SHOWS SHORT-TERM THINKING ON AI

@AIStockSavvy [Thu Nov 05 17:03:52 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: OpenAI launches GPT-6 Cyber. - $MSFT $NVDA $AMD

@AIStockSavvy [Thu Nov 05 17:01:18 +0000 2026]: $ARM | ARM CEO: Tech Selloff Shows Short-Term Thinking on AI - WSJ Arm CEO Rene Haas says the post-midterms tech selloff ignores the longer-term thesis about AI's impact on the economy. "The short-term blitz that happened in terms of the election, and people talking about spending, etc., etc.," Haas says on CNBC. "To me, I look at that as very, very short-term thinking." He says intelligence as a …

@AIStockSavvy [Thu Nov 05 16:59:26 +0000 2026]: $RIOT | Bernstein 𝗺𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝘀 𝗢𝘂𝘁𝗽𝗲𝗿𝗳𝗼𝗿𝗺 on 𝗥𝗶𝗼𝘁 𝗣𝗹𝗮𝘁𝗳𝗼𝗿𝗺𝘀, raises PT to $𝟯𝟬 from $𝟭𝟴 https://t.co/Ot2LHnP5AN

@AIStockSavvy [Thu Nov 05 16:49:00 +0000 2026]: $U | BTIG 𝗺𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝘀 𝗕𝘂𝘆 on 𝗨𝗻𝗶𝘁𝘆 𝗦𝗼𝗳𝘁𝘄𝗮𝗿𝗲, raises PT to $𝟲𝟬 from $𝟱𝟯 Analyst sees healthy growth as product adoption, ad spend, Runtime, non-gaming, and AI opportunities ramp. https://t.co/edNKuzZ1Cu

@KobeissiLetter [Thu Nov 05 16:26:42 +0000 2026]: On today's stock market crash: As an investor, on days like today, you have to ask yourself one question: What fundamentally changed over the last 24 hours? The shift in the fundamental backdrop cannot be attributed solely to the Midterm Election results; markets had already largely priced in the outcome. So, what changed between yesterday and today? What is the fundamental reason for today's …

@AIStockSavvy [Thu Nov 05 16:36:52 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Iran Reviewing ‘Concrete Proposals’ On Nuclear Program - NYT - $QQQ $SPY $USO

@AIStockSavvy [Thu Nov 05 16:35:59 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Hedge Fund Walleye To Return Part Of Its Capital: Client Letter - Bloomberg - $SPY $QQQ

@KobeissiLetter [Thu Nov 05 17:59:00 +0000 2026]: Today's chart is for the history books. Yesterday's post-election rally now looks like a rounding error in the S&amp;P 500. The S&amp;P 500 has now erased -$3 trillion today. That's -$750 billion per hour since the market opened. https://t.co/9RDiIVEFsP

@AIStockSavvy [Thu Nov 05 17:05:38 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: OpenAI Launches GPT-6 Cyber, Rated “Critical” for Cybersecurity Capabilities 👉 𝗞𝗲𝘆 𝗛𝗶𝗴𝗵𝗹𝗶𝗴𝗵𝘁𝘀: ➤ 𝗢𝗽𝗲𝗻𝗔𝗜 releases 𝗚𝗣𝗧-𝟲 𝗖𝘆𝗯𝗲𝗿 to select vetted security customers. ➤ Model receives 𝗖𝗿𝗶𝘁𝗶𝗰𝗮𝗹 cybersecurity classification, upgraded from GPT-5.6 Cyber's High rating. ➤ Researchers identified 𝟴𝟭 previously unknown, high-severity 𝗙𝗶𝗿𝗲𝗳𝗼𝘅 vulnerabilities. ➤ 𝗠𝗼𝘇𝗶𝗹𝗹𝗮 has begun releasing fixes for …

@wallstengine [Thu Nov 05 17:37:58 +0000 2026]: PERPLEXITY JUST LAUNCHED AI TEAMMATES. You can now hire an entire team of AI agents inside Perplexity and have them work together without constantly telling them what to do. Each teammate gets its own desktop, browser and persistent conversation. Here's what they can do: Work proactively: Give them ongoing jobs, and they'll monitor things in the background and take action when something changes, …

@wallstengine [Thu Nov 05 17:52:54 +0000 2026]: Serval is offering new engineers a paid first-week vacation worth up to $10,000. Eligible engineering and deployment hires get a weeklong trip planned with a dedicated concierge. If a current employee refers an eligible hire who joins, the employee and new hire each receive $30,000, in addition to the new hire’s vacation. Co-founder and CTO @AlexAtServal announced the offer as part of …

@wallstengine [Thu Nov 05 17:16:50 +0000 2026]: OPENAI INTRODUCES GPT-6 CYBER OpenAI has introduced GPT-6 Cyber, a specialized AI model designed to discover software vulnerabilities, validate exploits and develop fixes, with stronger safeguards to keep its actions within authorized boundaries. The model powered OpenAI's recent Linux kernel research, where autonomous AI agents: • Reproduced 1,724 vulnerabilities. • Developed working exploits …

@KobeissiLetter [Thu Nov 05 16:35:02 +0000 2026]: RT @TKL_Adam: Our perspective on today's market crash. In the era of AI, the biggest technological revolution in human history, people are…

@StockMKTNewz [Thu Nov 05 18:01:46 +0000 2026]: Anthropic owned Claude just posted this: “Introducing Personal Finance in Claude, in beta in the US.“ https://t.co/NPf4YBYFb9

@AIStockSavvy [Thu Nov 05 18:16:47 +0000 2026]: Dems promised to make life more affordable. So far, it’s just the stocks. 😂😂

@wallstengine [Thu Nov 05 17:54:01 +0000 2026]: General Mills is weighing a sale of its international Häagen-Dazs business, with planning in early stages, per WSJ https://t.co/5C6LWRHwvy

@KobeissiLetter [Thu Nov 05 17:41:54 +0000 2026]: RT @WhiteWhaleLabs: One account worth following.

@gurgavin [Thu Nov 05 17:01:15 +0000 2026]: RT @Wealthsimple: Wealthsimple Presents: Something Good is Going to Happen https://t.co/CbJNrcazdL

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.