אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are a senior Wall Street investment advisor writing your signature PRE-MARKET briefing in Hebrew.
Script run date: 2026-07-08 (יום רביעי). Briefing target date: 2026-07-08 (יום רביעי).
The briefing is for TODAY. The US cash market has NOT opened yet — never describe it as open, trading, or having reacted. Use 'השוק צפוי להיפתח', 'המשקיעים יעקבו אחר'. Futures may be described in present tense; the cash market may not.

SIGNATURE POINT FORMAT (the author's own style — follow it exactly):
- Each point is ONE bullet: "* <כותרת קצרה>: <גוף הנקודה>".
- The opening mini-headline: 2-6 Hebrew words, SPECIFIC to the story — e.g. "מניות השבבים ממשיכות לרכז עניין",
  "הנפט ממשיך לטפס", "אבן דרך במגזר הבריאות", "סנטימנט מעורב בפתיחה" — never a generic label like
  "חדשות" / "מאקרו" / "מניות". Up to 40 characters, and NO ":" inside the headline itself.
  A single-stock story opens with "מניית <שם בעברית> (TICKER)".
- After the headline: flowing, professional Hebrew prose — 2-3 concise sentences (a 4th only when the story
  truly demands it). EVERY point must deliver real depth: (1) what happened, with the few figures that carry
  the story, (2) the background and context (על רקע..., בעקבות...), and (3) why it matters — the mechanism or
  the implication for investors. Never leave a point as a bare headline-fact.
- STRONG points only: fewer, deeper points beat many thin ones. This is a briefing, not an article — no
  filler points, no padding.
- Voice: a senior investment advisor who lives and breathes Wall Street, explaining the market to clients —
  analytical, confident, readable. Weave the numbers into the story, don't stack them.

This is a professional BRIEFING — NOT a data dump. FORWARD-LOOKING ONLY: no yesterday's index performance,
no closing levels, and nothing that already appears in the prior-context block.
6-9 points TOTAL, opening with the market picture and closing with the bottom line:
* FIRST point — the opening picture (headline like "סנטימנט מעורב בפתיחה" / "אופטימיות זהירה לקראת הפתיחה"):
  futures direction and the mood heading into the session, plus the single most important backdrop theme.
  Futures percentages ONLY if a specific futures figure appears in the sources — never copy an ETF
  percentage as a futures percentage.
* MIDDLE points — ONE point per real story. Pick the STRONGEST stories of the morning from the menu below —
  do NOT force every category, and never pad to reach a count:
  - The day's macro releases and Fed events: Israel time, consensus and the previous reading, and why the
    number matters for rates and equities. Nothing scheduled → one short point saying so and naming the next key date.
  - The central story investors will watch today, with the transmission mechanism explained simply
    (אירוע → נפט → אינפלציה → ריבית → מניות) when genuinely relevant.
  - 1-3 overnight stock/sector stories: expected earnings, major company news, analyst moves. Each significant
    story gets its OWN point. Positive news about a falling stock → "למרות החדשות, המניה ירדה".
  - Commodities when moving: oil with its geopolitical/supply backdrop, gold.
  - שוק החוב והתנודתיות: the 10Y yield and the VIX level (verified via web search) and what they signal about positioning.
  - Geopolitics / Washington politics with market impact.
  - Overnight sessions in Europe and Asia, a notable investor move, IPO or M&A — when truly material.
* LAST point — "שורה תחתונה: ..." — what will decide the direction of the session, in 1-2 sentences.
No ETF proxies, no Finnhub, no ISO dates.

Rules:
- Write ONLY in Hebrew. English only for tickers ($AAPL), index names (S&P 500), and well-known financial terms in parentheses on first use.
- Be specific: every claim must include a number, percentage, or ticker. No vague statements.
- Do NOT repeat information across bullets. One company = one bullet (merge multiple news items).
- No buy/sell recommendations, no price targets of your own, no "כדאי לקנות/למכור".
- EVERY number must come from: (1) the verified Finnhub data above, (2) a specific tweet, or (3) your web search. NEVER invent, estimate, or recall numbers from memory. When in doubt, omit.
- If a tweet contradicts the Finnhub data, the Finnhub data is correct.
- Directional words (צונח/יורד/מזנק/עולה) are factual claims — they MUST match the DIRECTIONAL FACTS block.
- Sector percentages (XLE/XLK/...) — ONLY from the Finnhub data. Missing sector → omit.
- Never claim an all-time high (שיא כל הזמנים) without web-search verification.
- CPI mentioned → ALWAYS both headline AND Core CPI. Economic data → always actual vs forecast vs previous.
- IPO (הנפקה ראשונית) ≠ ETF (תעודת סל). Nasdaq 100 (QQQ, ~NDX) ≠ Nasdaq Composite (IXIC) — never mix their levels.
- Attribution: Claude→Anthropic, ChatGPT→OpenAI, Gemini→Google. Donald Trump is the CURRENT US President — never "לשעבר".
- No URLs, no Markdown links, no source domains in brackets. Attribution style: לפי Reuters / לפי Bloomberg only.
- Dates in visible text: Israeli format ONLY, e.g. "יום שני, 6.7.2026". NEVER write an ISO date (2026-07-06) inside the title or the bullets.
- NEVER use the ";" character anywhere. Use a comma or start a new sentence instead.
- Never write "נתון בפועל עדיין לא קיים". If a figure has not been released yet, give only the forecast (צפי) and the previous reading (נתון קודם).
- Never OPEN a bullet with a raw ticker like "$TSLA:" or "$AMZN:". Open with the Hebrew company name: "מניית טסלה (TSLA):", "מניית אמזון (AMZN):", "מניית מטא (META):".
- Finnhub and the measurement ETFs (SPY/QQQ/DIA/USO/BNO/GLD/UUP/VIXY/TLT...) are a hidden verification layer ONLY. NEVER mention Finnhub, "proxy", "דרך USO", "האינדיקציה מ-", or any technical data-source wording in the visible text — describe the asset itself (נפט, זהב, דולר, תשואות) directly.
- SIGN-FLIP: if the verified data shows a stock DOWN, do NOT describe it positively (עלתה/התחזקה/הובילה/בלטה לחיוב). If the news is positive but the stock fell, write: "למרות החדשות, המניה ירדה".

CRITICAL — OUTPUT FORMAT (MANDATORY):
- Return ONLY a JSON object, no backticks, no explanations, in EXACTLY this structure:
{
  "title": "נקודות חשובות לקראת פתיחת המסחר בוול סטריט 🇺🇸 – יום רביעי, 8.7.2026",
  "date": "2026-07-08",
  "sections": [
    {
      "heading": "נקודות מרכזיות",
      "content": "* כותרת קצרה וספציפית: שניים עד ארבעה משפטים של פרוזה אנליטית עם המספרים המרכזיים, ההקשר והמשמעות.\n* כותרת נוספת: ..."
    }
  ]
}
- EXACTLY 1 section. Heading EXACTLY "נקודות מרכזיות". Title EXACTLY as given above.
- content = one string, bullets separated by \n, each bullet starts with "* ".
- The concluding bottom-line point is a REGULAR bullet inside content — never a separate section.
- No **, no ##, no HTML, no URLs inside content.

US-ISRAEL TIME OFFSET TODAY: +7 hours (add 7 hours to US Eastern Time)
Key times in Israel time today:
- US economic data releases (CPI, NFP, PPI, GDP, Jobless Claims): 15:30 שעון ישראל
- ISM PMI, JOLTS, Consumer Confidence: 17:00 שעון ישראל
- FOMC rate decision / minutes: 21:00 שעון ישראל | Fed Chair press conference: 21:30 שעון ישראל
- US market open: 16:30 שעון ישראל | US market close: 23:00 שעון ישראל
USE ONLY THESE TIMES. Do NOT calculate your own offset.

══ VERIFIED MARKET DATA (from Finnhub API — these are FACTS, do NOT override with guesses) ══
DAILY PERFORMANCE:
  S&P 500 (SPY ETF): $747.71 (daily: -0.48%), prev close: $751.28
  Nasdaq 100 (QQQ ETF): $709.43 (daily: -1.85%), prev close: $722.82
  Dow Jones (DIA ETF): $528.45 (daily: -0.31%), prev close: $530.09
  Russell 2000 (IWM ETF): $296.19 (daily: -0.91%), prev close: $298.90
  Energy Sector (XLE ETF): $54.64 (daily: +2.84%), prev close: $53.13
  Technology Sector (XLK ETF): $179.18 (daily: -2.39%), prev close: $183.57
  Financials Sector (XLF ETF): $56.05 (daily: -0.16%), prev close: $56.14
  Consumer Discretionary Sector (XLY ETF): $117.39 (daily: -0.53%), prev close: $118.01
  Healthcare Sector (XLV ETF): $164.44 (daily: +1.53%), prev close: $161.96
  Industrials Sector (XLI ETF): $182.38 (daily: -1.71%), prev close: $185.56
  Consumer Staples Sector (XLP ETF): $84.86 (daily: +0.90%), prev close: $84.10
  Utilities Sector (XLU ETF): $45.70 (daily: +0.88%), prev close: $45.30
  WTI Crude Oil (USO ETF): $108.92 (daily: +4.38%), prev close: $104.35
  Brent Crude Oil (BNO ETF): $41.93 (daily: +4.98%), prev close: $39.94
  Gold (GLD ETF): $377.49 (daily: -1.21%), prev close: $382.13
  Silver (SLV ETF): $54.46 (daily: -2.94%), prev close: $56.11
  Bitcoin (IBIT ETF): $36.15 (daily: +0.08%), prev close: $36.12
  US 20Y+ Bonds (TLT ETF): $84.55 (daily: -1.05%), prev close: $85.45
  US Dollar (UUP ETF): $28.40 (daily: +0.28%), prev close: $28.32
  VIX Volatility (VIXY ETF): $20.87 (daily: +1.07%), prev close: $20.65

INDIVIDUAL STOCKS mentioned in the source tweets (verified quotes):
  $SPCX: $149.47 (daily: -6.83%), prev close: $160.42
  $USO: $108.92 (daily: +4.38%), prev close: $104.35
  $QQQ: $709.43 (daily: -1.85%), prev close: $722.82
  $SPY: $747.71 (daily: -0.48%), prev close: $751.28
  $PENG: $62.71 (daily: -7.38%), prev close: $67.71
  $NVDA: $196.93 (daily: +0.71%), prev close: $195.55
  $IEMG: $79.79 (daily: -2.70%), prev close: $82.00
  $VWO: $58.88 (daily: -1.98%), prev close: $60.07
  $XOM: $141.69 (daily: +3.85%), prev close: $136.44
  $MU: $938.38 (daily: -4.71%), prev close: $984.75
  $FIGR: $31.05 (daily: -9.78%), prev close: $34.41
  $META: $615.58 (daily: +2.55%), prev close: $600.29

DIRECTIONAL FACTS — Hebrew direction words (עולה/יורד/צונח/מזנק) MUST match these:
  נפט (WTI/ברנט): עולה (USO: +4.38%, BNO: +4.98%)
  זהב: יורד (GLD: -1.21%)
  ביטקוין: יציב/כמעט ללא שינוי (IBIT: +0.08%)
  דולר: עולה (UUP: +0.28%)
  תנודתיות / VIX: עולה (VIXY: +1.07%)
  אג"ח ארוכות / TLT: יורד (TLT: -1.05%)

The % changes above are ACCURATE — use them for direction and magnitude.
The ETF tickers above (SPY/QQQ/DIA/USO/GLD/...) are measurement instruments for YOUR verification only — NEVER name them, Finnhub, or the word 'proxy' in the visible Hebrew text.
For exact index LEVELS (points), gold/oil absolute prices, VIX level, Bitcoin price, 10Y yield: verify via web search. Do NOT estimate them from ETF prices.
For sector performance (XLE/XLK/...): USE ONLY the Finnhub numbers above — never invent sector percentages.
If ANY percentage you write contradicts the data above, you are WRONG. Fix it.
══════════════════════════════════════════════════════════════════════════════

══ SCHEDULED DATA CHECK ══
Use web search to find what US economic data is scheduled for release on 2026-07-08.
Include the release time in Israel time and the market consensus/forecast.
══════════════════════════════════

══ CONTEXT: YESTERDAY'S DAILY SUMMARY — DO NOT REPEAT THIS CONTENT ══
Already published. Your briefing is FORWARD-LOOKING. Mention an item below ONLY if there is a genuinely NEW overnight development about it.

[סיכום המסחר]
* יום אדום בצל הסלמה גיאופוליטית: המסחר ננעל בירידות רוחביות אחרי יום תנודתי שנשלט על ידי המתיחות במפרץ הפרסי. מדד S&P 500 ירד כ-0.5%, הדאו ג'ונס נסוג כ-0.3% ומדד ראסל 2000 של המניות הקטנות איבד כ-0.9%, אך הבורח הגדול היה נאסד"ק 100 שצלל כ-1.85% בהובלת מניות השבבים. השוק נפתח תחת רוטציה מהטכנולוגיה, וכשהחריפה ההסלמה מול איראן במהלך היום התחזק הזרם אל הנפט ואל הסקטורים הדפנסיביים על חשבון הצמיחה.
* ההסלמה מול איראן מזיזה את השוק: הסיפור המרכזי היה גיאופוליטי. איראן תקפה ספינה מסחרית שלישית במיצר הורמוז, ארה"ב הגיבה בביטול הרישיון הכללי שאפשר לאיראן לייצא נפט, ובהמשך היום הודיע הצבא האמריקאי על גל מתקפות נגד יעדים באיראן. מיצר הורמוז מעביר כחמישית מצריכת הנפט העולמית, ולכן כל איום על השיט בו מתומחר מיידית בפרמיית סיכון על מחירי האנרגיה ובבריחה מנכסי סיכון.
* הנפט מזנק וסקטור האנרגיה מוביל: מחירי הנפט קפצו בחדות על רקע ההסלמה, כשה-WTI עלה כ-4.4% והברנט טיפס כ-5% אל מעל 76 דולר לחבית. סקטור האנרגיה היה הבולט לחיוב עם עלייה של 2.84%, והמוטב הישיר היה מניית אקסון מוביל (XOM) שעלתה 3.85% אחרי שדיווחה כי הכנסות הרבעון השני צמחו בכמעט 4 מיליארד דולר בזכות זינוק מחירי הנפט. כשהאנרגיה היא המחלקה שנהנית ישירות מהמשבר, המשקיעים הסיטו אליה כספים כגידור טבעי.
* מניות השבבים גוררות את נאסד"ק מטה: הצניחה בנאסד"ק 100 הובלה על ידי נסיגה במניות השבבים, שהיו החוליה החלשה של היום. מניית מיקרון (MU) בלטה לשלילה וירדה 4.71% על רקע דיווחים שמייקל ביורי פתח נגדה פוזיציית שורט, זאת למרות שהנשיא טראמפ המשיך לתמוך בה בפומבי. אפילו מניית אנבידיה (NVDA), שקיבלה חדשות חיוביות על אימוץ מעבדי Vera החדשים שלה על ידי Perplexity, סיימה בעלייה מתונה של 0.71% בלבד, עדות לסנטימנט השלילי שרבץ על המגזר.
* מניית טסלה (TSLA): המניה איבדה 4.02% והייתה בין הבולטות לשלילה בקבוצת המגה-קאפ הטכנולוגית. הרקע כפול: מצד אחד דיווח כי החברה הטילה תקרה על הוצאות הבינה המלאכותית של עובדיה בסך 200 דולר לשבוע, ומצד שני הלחץ הרוחבי על מניות הצמיחה בסביבת ההסלמה הגיאופוליטית. למרות הבשורות התפעוליות סביב שירות הרובוטקסי, יום המסחר הזה שייך למוכרים.
* רוטציה אל הסקטורים הדפנסיביים: מתחת לפני השטח נמשך סבב יציאה מהצמיחה אל ההגנה. בעוד הטכנולוגיה נחלשה ב-2.39% והתעשייה נסוגה ב-1.71%, סקטור הבריאות עלה 1.53%, מוצרי הצריכה הבסיסיים הוסיפו 0.90% והתשתיות (יוטיליטיס) התחזקו ב-0.88%. זהו דפוס קלאסי של שוק שמעדיף ודאות תזרימית על פני צמיחה עתידית כשהסיכון הגיאופוליטי עולה.
* הזהב יורד למרות המלחמה: דווקא ביום של הסלמה צבאית, הזהב לא תפקד כעוגן הבטוח המסורתי וירד 1.21%, הכסף נחלש ב-2.94%, בעוד הדולר התחזק ב-0.28%. ההסבר ככל הנראה בחוזק הדולר ובעליית התשואות שהעלו את עלות ההחזקה במתכת שאינה נושאת ריבית. עם זאת, סקר OMFIF שפורסם היום הצביע על מגמה ארוכת טווח הפוכה: 82% מהבנקים המרכזיים כבר מחזיקים זהב פיזי לעומת 71% אשתקד, כשהמוסדות מגוונים אל מחוץ לדולר.
* ספייס-אקס (SPCX) נכנסת לנאסד"ק 100: אירוע נדיר בזירת המדדים, ספייס-אקס נכללה במדד נאסד"ק 100 בכניסה המהירה ביותר של חברה למדד בכל תולדותיו. עם זאת, למרות היוקרה שבצירוף, המניה עצמה ירדה 6.83% ביום המסחר ונסחפה עם המכירה הרוחבית במניות הטכנולוגיה והצמיחה. הכניסה המהירה ממחישה עד כמה משקל הענקיות הטכנולוגיות במדד ממשיך להתעצם.
* שורה תחתונה למחר: כל העיניים יופנו להתפתחויות במפרץ הפרסי ולשאלה אם גל המתקפות האמריקאי יתרחב או יתפוגג, שכן זה הגורם שיכתיב את כיוון הנפט ואת תיאבון הסיכון. משקיע יעקוב אחר שלושה צירים: האם הרוטציה מהטכנולוגיה אל האנרגיה והדפנסיביים נמשכת, האם הנפט מתייצב מעל הרמות הנוכחיות, והאם התנודתיות, שכבר טיפסה, ממשיכה לעלות. בסביבה כזו עוצמת התגובה עלולה להתעצם דווקא בשעת המסחר האחרונה.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-08. Never mention in the review that these came from tweets/posts:

@gurgavin [Tue Jul 07 23:28:39 +0000 2026]: ALL 1 YEAR SPACEX PRICE TARGETS ARE HERE AS THE QUIET PERIOD ENDED TODAY $SPCX RAYMOND JAMES $800 MORGAN STANLEY $300 DEUTSCHE BANK $255 OPPENHEIMER $250 CANTOR FITZGERALD $246 BERNSTEIN $239 BANK OF AMERICA $235 WELLS FARGO $230 RBC $225 JP MORGAN $225 UBS $210 GOLDMAN SACHS $205 NEEDHAM $200 CURRENT PRICE $150

@wallstengine [Tue Jul 07 20:10:53 +0000 2026]: $PENG | Penguin Solutions Q3 FY26 Earnings Highlights 🔷 Revenue: $478.7M vs $421.4M Est. 🟢 🔷 Adj EPS: $0.84 vs $0.56 Est. 🟢 🔷 Record quarterly net sales, up 48% YoY. FY26 Outlook Raised: 🔷 Non-GAAP EPS: $2.60 ±$0.05 vs $2.28 Est. 🟢 🔷 Net sales growth now seen at 22% ±2%, up from 12% ±5% 🔷 Non-GAAP gross margin: 28.5% ±0.5% Segment Revenue: 🔷 Advanced Computing: $137.6M, up 4% YoY 🔷 Integrated Memory: $275.1M, up 111% YoY 🔷 Optimized LED: $66.1M, up 7% YoY Business Highlights: 🔷 Integrated Memory net sales more than doubled YoY 🔷 AI Infrastructure added 4 new customer logos in Q3 🔷 Became an NVIDIA AI Factory Specialized Partner 🔷 Expanded ClusterWareAI with an AI Factory Operations Agent

@KobeissiLetter [Tue Jul 07 23:29:59 +0000 2026]: Emerging markets are seeing historic investment demand: Assets under management (AUM) in the MSCI emerging markets ETF, $IEMG, are up to a record $160 billion. And, the assets of the FTSE emerging markets ETF, $VWO, are up to a record $120 billion. Over the last 12 months, $IEMG assets have nearly doubled while $VWO assets have risen nearly +50%. This comes as $IEMG has rallied +39% over this period while $VWO has returned +23%. Furthermore, $IEMG attracted +$22 billion in inflows over the last 12 months, more than double the inflows into $VWO. The difference between the two funds comes down to South Korea, which is classified as "emerging" by MSCI and "developed" by FTSE Russell. South Korea's AI boom is reshaping emerging market investing.

@gurgavin [Mon Jul 06 19:52:14 +0000 2026]: SPACEX WILL BE ADDED TO THE NASDAQ 100 INDEX TOMORROW THIS IS THE QUICKEST TIME EVER FOR A COMPANY TO BE ADDED TO THE NASDAQ 100 INDEX $SPCX

@StockMKTNewz [Tue Jul 07 23:05:51 +0000 2026]: Exxon Mobil $XOM said its Q2 revenue increased by almost $4 billion as the Iran conflict boosted oil prices - Bloomberg https://t.co/zVBzz4R6s5

@gurgavin [Fri Jul 03 21:26:04 +0000 2026]: IMAGINE SHORTING MICRON WHEN TRUMP IS TRYNA PUMP IT EVERY SINGLE DAY $MU

@AIStockSavvy [Tue Jul 07 19:06:43 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Perplexity Adopts $NVDA NVIDIA Vera CPUs for AI Infrastructure 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐏𝐞𝐫𝐩𝐥𝐞𝐱𝐢𝐭𝐲 will deploy NVIDIA's new 𝐕𝐞𝐫𝐚 𝐂𝐏𝐔𝐬 for AI workloads. ➤ NVIDIA expects 𝐕𝐞𝐫𝐚 𝐂𝐏𝐔 sales to reach 𝐨𝐯𝐞𝐫 $𝟐𝟎 𝐛𝐢𝐥𝐥𝐢𝐨𝐧 this fiscal year. ➤ Vera expands NVIDIA into the 𝐂𝐏𝐔 market dominated by Intel and AMD. ➤ NVIDIA is broadening beyond AI GPUs into 𝐠𝐞𝐧𝐞𝐫𝐚𝐥-𝐩𝐮𝐫𝐩𝐨𝐬𝐞 computing processors. ➤ Perplexity said Vera delivers about 𝟏.𝟓𝐱 faster AI agent coding performance. ➤ Perplexity did not disclose the number of 𝐕𝐞𝐫𝐚 𝐂𝐏𝐔𝐬 it plans to purchase. ➤ OpenAI, Anthropic, and Oracle have also committed to using NVIDIA Vera CPUs. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ NVIDIA is challenging 𝐈𝐧𝐭𝐞𝐥 and 𝐀𝐌𝐃 in the multibillion-dollar CPU market. ➤ Rising AI agent workloads are driving demand for 𝐀𝐈-𝐨𝐩𝐭𝐢𝐦𝐢𝐳𝐞𝐝 CPUs. ➤ Additional customer wins strengthen NVIDIA's 𝐞𝐧𝐭𝐞𝐫𝐩𝐫𝐢𝐬𝐞 AI infrastructure strategy. 👉 𝐄𝐱𝐩𝐞𝐫𝐭 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭: ➤ "NVIDIA's CPU performs AI agent coding tasks about 1.5 times faster than traditional CPUs." — 𝐍𝐚𝐭𝐞 𝐊𝐮𝐩𝐩, Vice President for Computer Enterprise and Infrastructure at Perplexity.

@gurgavin [Wed Jul 08 00:06:20 +0000 2026]: RAYMOND JAMES SAYS SPACEX SHOULD BE WORTH $800 1 YEAR FROM NOW THAT VALUES SPACEX AT $10 TRILLION DOLLARS WHAT ARE THEY ON ??? $SPCX

@KobeissiLetter [Tue Jul 07 19:20:54 +0000 2026]: BREAKING: Brent crude oil prices surge above $76/barrel after the US revokes Iran's general license to export oil in response to Iran striking three commercial vessels in the Strait of Hormuz. https://t.co/zTH55IWNw4

@KobeissiLetter [Tue Jul 07 18:53:26 +0000 2026]: BREAKING: The US is revoking Iran's newly issued general license to export oil after Iran struck three commercial vessels in the Strait of Hormuz. The US called Iran's latest actions in the Strait of Hormuz "wholly unacceptable" and said they will be "met with consequences."

@KobeissiLetter [Tue Jul 07 16:52:21 +0000 2026]: AI is the hottest topic on global earnings calls: Mentions of AI disruptions during H1 2026 earnings calls jumped to a record ~780. This marks a +310% increase from ~190 mentions in H2 2025. In the first half alone, there were more mentions of AI disruptions than in the previous 3 years combined. Meanwhile, a record 337 executives at S&P 500 firms mentioned AI during Q1 2026 earnings calls held between March 15th and June 11th, according to FactSet. This is more than double the 5-year average of 164 and more than triple the 10-year average of 103. AI is transforming corporate strategy and financial markets.

@AIStockSavvy [Wed Jul 08 00:52:58 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $NVDA Nvidia and AI Chip Startup D-Matrix Are Combining Hardware in a New System to Power AI Models - The Information

@AIStockSavvy [Tue Jul 07 22:10:17 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $FIGR Figure Reports Record Q2 Marketplace Volume Above Guidance 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ Figure said preliminary 𝐐𝟐 𝟐𝟎𝟐𝟔 results exceeded the top end of prior guidance. ➤ Consumer Loan Marketplace Volume reached 𝐚 𝐫𝐞𝐜𝐨𝐫𝐝 $𝟒.𝟐𝟓𝟗 𝐛𝐢𝐥𝐥𝐢𝐨𝐧 in Q2, up 𝟒𝟕% QoQ and 𝟏𝟑𝟐% YoY. ➤ June Consumer Loan Marketplace Volume rose to $𝟏.𝟓𝟏𝟗 𝐛𝐢𝐥𝐥𝐢𝐨𝐧, up 𝟖% MoM and 𝟏𝟓𝟓% YoY. ➤ $𝐘𝐋𝐃𝐒 in circulation totaled $𝟓𝟓𝟔 𝐦𝐢𝐥𝐥𝐢𝐨𝐧 at June-end, roughly flat MoM. ➤ Democratized Prime 𝐌𝐚𝐭𝐜𝐡𝐞𝐝 𝐎𝐟𝐟𝐞𝐫𝐬 reached $𝟑𝟗𝟐 𝐦𝐢𝐥𝐥𝐢𝐨𝐧, up 𝟐% MoM and 𝟔% QoQ. ➤ 𝐁𝐨𝐫𝐫𝐨𝐰𝐞𝐫 𝐃𝐞𝐦𝐚𝐧𝐝 increased to $𝟒𝟏𝟒 𝐦𝐢𝐥𝐥𝐢𝐨𝐧, while 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐋𝐞𝐧𝐝𝐞𝐫 𝐒𝐮𝐩𝐩𝐥𝐲 rose to $𝟓𝟐𝟐 𝐦𝐢𝐥𝐥𝐢𝐨𝐧. ➤ Figure will transition from 𝐦𝐨𝐧𝐭𝐡𝐥𝐲 disclosures to a weekly performance dashboard. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ Marketplace volume growth signals 𝐬𝐭𝐫𝐨𝐧𝐠 consumer lending demand and platform adoption. ➤ Results above guidance may reinforce confidence in Figure's 𝟐𝟎𝟐𝟔 growth outlook. ➤ Weekly reporting could provide investors with more 𝐟𝐫𝐞𝐪𝐮𝐞𝐧𝐭 operating performance updates.

@StockMKTNewz [Wed Jul 08 00:34:05 +0000 2026]: Cathie Wood and Ark Invest bought 44,196 shares of SpaceX $SPCX today

@StockMKTNewz [Tue Jul 07 18:36:08 +0000 2026]: Meta Platforms $META just announced that it's rolling out Muse Image, its first image-generation model from ​Meta Superintelligence Labs - Reuters https://t.co/wwrOFL35K0

@KobeissiLetter [Tue Jul 07 21:32:59 +0000 2026]: BREAKING: The US Military announces it has begun launching a series of powerful strikes against Iran. The US says these strikes are in response to Iranian attacks on three vessels that were transiting the Strait of Hormuz.

@KobeissiLetter [Tue Jul 07 15:17:43 +0000 2026]: BREAKING: US officials say Iran has struck a third commercial ship in the Strait of Hormuz, per Axios. This follows attacks on two commercial vessels yesterday and comes after a one-week agreement between the US and Iran on halting attacks in the Strait of Hormuz has expired.

@KobeissiLetter [Tue Jul 07 14:04:46 +0000 2026]: BREAKING: The Nasdaq 100 extends losses to over -1% on the day as chip stocks pull back. https://t.co/1XPmJ5WBEs

@wallstengine [Tue Jul 07 19:12:12 +0000 2026]: $USO +4.5% https://t.co/7yutwsKREf

@AIStockSavvy [Tue Jul 07 22:04:56 +0000 2026]: Iran says US strike seriously violates Iran-US Islamabad memorandum - $QQQ $SPY $USO State broadcaster IRIB reported early on the 8th that Iran’s government said the US strike on Iran seriously violates the Iran‑US Islamabad memorandum of understanding.

@AIStockSavvy [Tue Jul 07 21:51:11 +0000 2026]: U.S. officials said the strike on Iran was a "punitive action, not a proportional response," and that the operation "will not end in the short term." - CNN - $QQQ $SPY $USO

@AIStockSavvy [Tue Jul 07 21:42:08 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: US Military Says It’s Launching New Wave of Strikes Against Iran - Bloomberg - $QQQ $SPY $USO

@AIStockSavvy [Tue Jul 07 20:57:26 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $SPCX SpaceXAI plans to release as early as Wednesday a new AI model developed in partnership with Cursor - The Information

@wallstengine [Tue Jul 07 22:36:01 +0000 2026]: $SHMD received a repeat order worth over €37M from a Chinese customer for HDI-ML and mSAP production equipment. The equipment will support capacity expansion for AI server boards and optical module applications. Including this order, SCHMID’s 2026 order intake now stands at €81.7M, up from €44.3M before the deal.

@KobeissiLetter [Tue Jul 07 15:10:45 +0000 2026]: The market's rally is broadening: The equal-weighted S&P 500 index has recorded 31 all-time highs so far this year, the 2nd-highest total since 2021. This comes as the index has rallied +12.2% over the period, outperforming the S&P 500's +10.1% gain. By comparison, the S&P 500 has seen 24 all-time highs year-to-date. At this pace, the equal-weighted index is on track to record 60 new all-time highs in 2026, the 2nd-highest annual total on record. This would rank only behind the 68 all-time highs posted in 2013. Market leadership is expanding.

@KobeissiLetter [Wed Jul 08 01:51:24 +0000 2026]: BREAKING: Interest expense on US public debt as a % of GDP is up to ~3.2%, the highest since at least the 1970s. This figure has nearly TRIPLED over the last 5 years. Over the same period, national defense spending as a % of GDP has fallen to ~3.0%, the lowest since the early 2000s. As a result, interest expense has exceeded national defense spending for 3 consecutive years, the longest streak in at least 46 years. Meanwhile, nominal interest payments have risen +$711 billion since 2020, or +140%, to a record annualized rate of $1.22 trillion. Over the same period, defense spending has increased +$237 billion, or +35%, to a record annualized rate of $923 billion. America's debt burden is in uncharted territory.

@AIStockSavvy [Tue Jul 07 21:31:12 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Netflix, Disney and YouTube Interested in Fifa World Cup U.S. Rights, Package Could Reach $2 Billion - CNBC - $NFLX $GOOGL $DIS

@AIStockSavvy [Tue Jul 07 20:07:49 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $FCEL FuelCell Energy launches $200M common stock offering

@AIStockSavvy [Tue Jul 07 20:05:48 +0000 2026]: $PENG | Penguin Solutions, Inc., Q3-2026 Earning Report https://t.co/GMZdwr5gxy

@StockMKTNewz [Tue Jul 07 20:31:21 +0000 2026]: Anthropic has now overtaken OpenAI in paid business adoption of AI https://t.co/f28z62qIk7

@wallstengine [Wed Jul 08 00:17:56 +0000 2026]: RT @wallstengine: Wall Street is officially out with its first wave of price targets on SpaceX $SPCX. Based on the 18 analyst targets shown…

@KobeissiLetter [Tue Jul 07 20:19:03 +0000 2026]: China is now dominating the global auto market: China's vehicle exports jumped +68.7% YoY in May, to ~930,000. This is almost +1,100% above levels seen in May 2019. This comes as new EV exports surged +112.6% YoY, to 424,000, accounting for ~46% of the total. As a result, China exported a record 8.6 million vehicles in the 12 months ending May. By comparison, Japan exported just 4.2 million, or -51% fewer, during the same period. To put this into perspective, China exported just 1.0 million vehicles in 2019, while Japan exported 4.8 million, or +380% more. China is now the undisputed leader of the global car market.

@gurgavin [Mon Jul 06 16:11:32 +0000 2026]: TRUMP SAYS “COUPLE OF GUYS WENT SHORT ( THE STOCK ) MARKET POOR BASTARDS ARE IN BIG TROUBLE THEY'RE GETTING WIPED OUT”

@wallstengine [Tue Jul 07 18:52:51 +0000 2026]: The U.S. is revoking a general license that allowed Iranian oil sales after calling Iran’s actions in the Strait of Hormuz “wholly unacceptable.” The move follows tanker attacks near the strait, which carries about a fifth of global oil consumption. https://t.co/TSYpZf59Sx

@StockMKTNewz [Tue Jul 07 23:48:40 +0000 2026]: Samsung has begun mass production of its most advanced data center storage drive, which is set for use inside Nvidia’s upcoming Vera Rubin platform - Bloomberg https://t.co/qFRPg4Nmpd

@wallstengine [Tue Jul 07 20:55:38 +0000 2026]: SPACEXAI PLANS TO LAUNCH NEW MODEL WITH CURSOR AS SOON AS WEDNESDAY

@gurgavin [Mon Jul 06 19:45:40 +0000 2026]: KIND OF CRAZY AMERICA WAS EXPECTED TO LOSE TODAY AFTER ITS BEST PLAYER GOT A RED CARD LAST GAME AND WASN’T ALLOWED TO PLAY TODAY BUT TRUMP CALLED FIFA AND MADE THEM OVERTURN THE DECISION NOW AMERICA IS EXPECTED TO WIN

@gurgavin [Sat Jul 04 18:37:40 +0000 2026]: HAPPY INDEPENDENCE DAY TO MY AMERICAN FOLLOWERS 🇺🇸🇺🇸🇺🇸🇺🇸 “IT’S NEVER PAID TO BET AGAINST AMERICA. WE COME THROUGH THINGS, BUT IT’S NOT ALWAYS A SMOOTH RIDE. NEVER BET AGAINST AMERICA.” - WARREN BUFFETT -

@StockMKTNewz [Tue Jul 07 23:12:36 +0000 2026]: A total of 42 Million Americans 🇺🇸 watched the men's USA vs Belgium, the most viewed soccer game in the US of all time - Bloomberg A record number of people saw us play so bad https://t.co/Dbo6PulR8l

@StockMKTNewz [Tue Jul 07 19:29:42 +0000 2026]: SK Hynix is expected to bring in $231 Billion of revenue this year up from $67B last year https://t.co/xCuDbe4fm9

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.