אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are a senior Wall Street investment advisor writing your signature END-OF-DAY review in Hebrew for
2026-07-13 (יום שני). PAST TENSE.

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

This is a professional MARKET REVIEW — NOT a data dump. Explain the day — don't copy the data.
6-9 points TOTAL, opening with the day's picture and closing with the bottom line:
* FIRST point — the day's story in one narrative (headline that captures the day, e.g. "יום תנודתי שהסתיים בירוק"):
  what the major indices did (direction + rounded %, from the verified data) woven into ONE story of the
  session — how it opened, what moved it, how it closed — not a list of numbers.
* MIDDLE points — ONE point per real story. Pick the STRONGEST stories of the day from the menu below —
  do NOT force every category, and never pad to reach a count:
  - הסיפור של היום: WHY the market moved — the main driver, with clear cause-and-effect and the transmission
    mechanism explained simply.
  - Macro data released today: actual vs forecast vs previous AND the market implication (repricing of rate
    expectations, yields, sector rotation).
  - Leading and lagging sectors (sector percentages ONLY from the verified data) and what drove them.
  - 1-3 notable stock stories with the REASON for each move. Each significant story gets its own point.
  - Commodities, dollar and yields — direction and meaning, not a list of prices.
  - After-hours earnings, or geopolitics that moved markets today — when truly material.
* LAST point — "שורה תחתונה למחר: ..." — what investors should watch in the next session and why.
Every direction word MUST match the DIRECTIONAL FACTS block.

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
- NEVER use an em dash / double hyphen ("—" or "--") as a clause separator. Use a comma, a colon, or start a new sentence instead.
- Never write "נתון בפועל עדיין לא קיים". If a figure has not been released yet, give only the forecast (צפי) and the previous reading (נתון קודם).
- Never OPEN a bullet with a raw ticker like "$TSLA:" or "$AMZN:". Open with the Hebrew company name: "מניית טסלה (TSLA):", "מניית אמזון (AMZN):", "מניית מטא (META):".
- Finnhub and the measurement ETFs (SPY/QQQ/DIA/USO/BNO/GLD/UUP/VIXY/TLT...) are a hidden verification layer ONLY. NEVER mention Finnhub, "proxy", "דרך USO", "האינדיקציה מ-", or any technical data-source wording in the visible text — describe the asset itself (נפט, זהב, דולר, תשואות) directly.
- SIGN-FLIP: if the verified data shows a stock DOWN, do NOT describe it positively (עלתה/התחזקה/הובילה/בלטה לחיוב). If the news is positive but the stock fell, write: "למרות החדשות, המניה ירדה".

CRITICAL — OUTPUT FORMAT (MANDATORY):
- Return ONLY a JSON object, no backticks, no explanations, in EXACTLY this structure:
{
  "title": "סיכום יום המסחר בוול סטריט 🇺🇸 – יום שני, 13.7.2026",
  "date": "2026-07-13",
  "summary": ["כותרת הנקודה: תמצית אמיתית של הנקודה במשפט קצר אחד", "כותרת שנייה: ...", "..."],
  "sections": [
    {
      "heading": "סיכום המסחר",
      "content": "* כותרת קצרה וספציפית: שניים עד ארבעה משפטים של פרוזה אנליטית עם המספרים המרכזיים, ההקשר והמשמעות.\n* כותרת נוספת: ..."
    }
  ]
}
- EXACTLY 1 section. Heading EXACTLY "סיכום המסחר". Title EXACTLY as given above.
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

══ VERIFIED MARKET DATA (from Finnhub API — these are FACTS, do NOT override with guesses) ══
DAILY PERFORMANCE:
  S&P 500 (SPY ETF): $749.17 (daily: -0.77%), prev close: $754.95
  Nasdaq 100 (QQQ ETF): $711.74 (daily: -1.90%), prev close: $725.51
  Dow Jones (DIA ETF): $524.47 (daily: -0.25%), prev close: $525.78
  Russell 2000 (IWM ETF): $293.48 (daily: -0.85%), prev close: $295.99
  Energy Sector (XLE ETF): $56.74 (daily: +3.01%), prev close: $55.08
  Technology Sector (XLK ETF): $181.28 (daily: -2.42%), prev close: $185.78
  Financials Sector (XLF ETF): $56.07 (daily: +0.65%), prev close: $55.71
  Consumer Discretionary Sector (XLY ETF): $116.04 (daily: -1.02%), prev close: $117.24
  Healthcare Sector (XLV ETF): $161.41 (daily: +0.35%), prev close: $160.84
  Industrials Sector (XLI ETF): $180.37 (daily: -0.85%), prev close: $181.92
  Consumer Staples Sector (XLP ETF): $84.59 (daily: +0.56%), prev close: $84.12
  Utilities Sector (XLU ETF): $45.72 (daily: +0.68%), prev close: $45.41
  WTI Crude Oil (USO ETF): $117.79 (daily: +8.36%), prev close: $108.70
  Brent Crude Oil (BNO ETF): $46.00 (daily: +9.13%), prev close: $42.15
  Gold (GLD ETF): $367.13 (daily: -2.62%), prev close: $377.01
  Silver (SLV ETF): $52.16 (daily: -3.32%), prev close: $53.95
  Bitcoin (IBIT ETF): $35.22 (daily: -2.79%), prev close: $36.23
  US 20Y+ Bonds (TLT ETF): $83.97 (daily: -0.59%), prev close: $84.47
  US Dollar (UUP ETF): $28.50 (daily: +0.39%), prev close: $28.39
  VIX Volatility (VIXY ETF): $21.02 (daily: +3.34%), prev close: $20.34

INDIVIDUAL STOCKS mentioned in the source tweets (verified quotes):
  $QQQ: $711.74 (daily: -1.90%), prev close: $725.51
  $SPY: $749.17 (daily: -0.77%), prev close: $754.95
  $USO: $117.79 (daily: +8.36%), prev close: $108.70
  $AAPL: $317.31 (daily: +0.63%), prev close: $315.32
  $SPCX: $139.14 (daily: -4.24%), prev close: $145.30
  $HOOD: $109.86 (daily: -1.88%), prev close: $111.97
  $CRWV: $83.31 (daily: -6.27%), prev close: $88.88
  $GOOGL: $352.51 (daily: -1.31%), prev close: $357.18

DIRECTIONAL FACTS — Hebrew direction words (עולה/יורד/צונח/מזנק) MUST match these:
  נפט (WTI/ברנט): עולה (USO: +8.36%, BNO: +9.13%)
  זהב: יורד (GLD: -2.62%)
  ביטקוין: יורד (IBIT: -2.79%)
  דולר: עולה (UUP: +0.39%)
  תנודתיות / VIX: עולה (VIXY: +3.34%)
  אג"ח ארוכות / TLT: יורד (TLT: -0.59%)

The % changes above are ACCURATE — use them for direction and magnitude.
The ETF tickers above (SPY/QQQ/DIA/USO/GLD/...) are measurement instruments for YOUR verification only — NEVER name them, Finnhub, or the word 'proxy' in the visible Hebrew text.
For exact index LEVELS (points), gold/oil absolute prices, VIX level, Bitcoin price, 10Y yield: verify via web search. Do NOT estimate them from ETF prices.
For sector performance (XLE/XLK/...): USE ONLY the Finnhub numbers above — never invent sector percentages.
If ANY percentage you write contradicts the data above, you are WRONG. Fix it.
══════════════════════════════════════════════════════════════════════════════

══ MANDATORY MACRO DATA CHECK ══
Use web search to check if ANY of these were released on 2026-07-13: CPI (headline AND core),
PPI (headline AND core), NFP, Jobless Claims, Consumer Sentiment (Michigan), ISM PMI, GDP,
Retail Sales, FOMC decision/minutes. If released — include with actual, forecast, previous,
AND the market implication. If none — skip, but you MUST check first.
══════════════════════════════════

══ CONTEXT: THIS MORNING'S PRE-MARKET BRIEFING ══
Published before the session. Use it to resolve scheduled items (expected → actual), do NOT quote it verbatim.

[נקודות מרכזיות]
* זהירות לקראת פתיחת המסחר: החוזים על S&P 500 יורדים בכ־0.3%, החוזים על Nasdaq 100 נחלשים בכ־1.0% והחוזים על הדאו נעים סביב 0.0%. השוק צפוי להיפתח תחת לחץ ממוקד בטכנולוגיה, כאשר ברנט נסחר סביב 78.86 דולר ו־WTI סביב 74.36 דולר בעקבות ההסלמה במפרץ.
* מצר הורמוז מחזיר את הנפט למוקד: איראן טוענת כי המצר נסגר, אך פיקוד המרכז האמריקאי דיווח שכ־20 כלי שיט עברו בו במהלך 24 השעות האחרונות. ברנט סביב 78.86 דולר ו־WTI סביב 74.36 דולר משקפים תמחור של סיכון לאספקה, אך עדיין לא הפסקה מלאה של התנועה. הישארות ברנט מעל 78 דולר עלולה להזין מחדש את שרשרת הנפט, האינפלציה, הריבית ולחץ המכפילים במניות הצמיחה.
* לוח מאקרו דל אך לא שקט: נגיד הפדרל ריזרב כריסטופר וולר ינאם ב־19:30 שעון ישראל, והמשקיעים יעקבו אחר עמדתו לגבי רמת הריבית המרסנת. ב־21:00 יתפרסם מאזן התקציב הפדרלי ליוני, כאשר משרד התקציב של הקונגרס צופה גירעון של 126 מיליארד דולר, לעומת גירעון של 293 מיליארד דולר במאי.
* השבבים באסיה תחת לחץ: מדד KOSPI בדרום קוריאה יורד בכ־7.6% ומניית SK Hynix מאבדת כ־9.3%, כאשר החשש מתמחור גבוה ומהיקף השקעות ה-AI פוגע במגזר. הלחץ באסיה עובר לחוזי Nasdaq 100, שיורדים ביותר מ־1.0%, ומאותת כי מניות השבבים האמריקאיות עשויות לרכז תנודתיות גבוהה כבר בפתיחה.
* פער התזרים של מהפכת ה-AI: אנבידיה (NVDA), מיקרון (MU), ברודקום (AVGO) ואפלייד מטיריאלס (AMAT) צפויות לייצר יחד שיא של כ־430 מיליארד דולר בתזרים מזומנים חופשי (FCF) ב־12 החודשים הקרובים, יותר מפי 3 לעומת לפני שנתיים. מנגד, התזרים המצטבר של אמזון (AMZN), אלפבית (GOOGL), מטא (META), מיקרוסופט (MSFT) ואורקל (ORCL) צפוי להפוך לשלילי, לאחר שיא של 260 מיליארד דולר ב־2024, על רקע השקעות הון של כ־1.8 טריליון דולר בשנים 2026 ו־2027. הפער ממחיש כי בשלב הנוכחי של מחזור הבינה המלאכותית (AI), חלק גדול מהערך הכספי עובר מספקיות הענן אל יצרניות השבבים והציוד.
* מניית מטא (META) מגדילה הימור: החברה מרחיבה את מרכז הנתונים בלואיזיאנה לקיבולת של 5 גיגה-וואט ומעלה את ההשקעה המוצהרת למעל 50 מיליארד דולר, לעומת תוכנית מקורית של 10 מיליארד דולר. מטא תקצה גם יותר ממיליארד דולר לכבישים, מים ותשתיות מקומיות, מה שממחיש כי השקעות AI הופכות מפרויקט מחשוב להשקעת תשתית בקנה מידה אזורי. עבור משקיעי META, המהלך מגדיל את פוטנציאל הקיבולת העתידית, אך גם מעמיק את הלחץ על התזרים וההחזר הנדרש מהשקעה של 50 מיליארד דולר.
* האג״ח וה-VIX משדרים פער: תשואת אג״ח ארה״ב ל־10 שנים נמצאת סביב 4.57%, רמה שממשיכה להציב רף היוון גבוה למניות צמיחה. במקביל, מדד VIX עומד על 15.03 ונותר מתחת לרמת 20, כך ששוק האופציות עדיין אינו מתמחר פאניקה רחבה למרות ירידה של כ־1.0% בחוזי Nasdaq 100. השילוב בין תשואה של 4.57% ל־VIX של 15.03 מצביע על לחץ מאקרו וריבית, אך לא על מעבר מלא למצב של בריחה מסיכון.
* שורה תחתונה: כיוון המסחר ייקבע לפי היכולת של ברנט להתייצב סביב 78 דולר ולפי השאלה אם חוזי Nasdaq 100 יצמצמו את הירידה של כ־1.0% עד הפתיחה ב־16:30. בהמשך, דברי וולר ב־19:30 יקבעו אם זעזוע האנרגיה יתורגם גם להקשחת ציפיות הריבית.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-13. Never mention in the review that these came from tweets/posts:

@gurgavin [Fri Jul 10 20:34:28 +0000 2026]: JUST IN : APPLE HAS JUST SUED OPENAI IN FEDERAL COURT FOR ALLEGED TRADE SECRET THEFT $AAPL

@gurgavin [Fri Jul 10 20:12:35 +0000 2026]: ARITZIA REPORTED EARNINGS YESTERDAY REVENUE UP 43% 📈 COMP SALES UP 35%📈 DIGITAL REVENUE UP 56%📈 US REVENUE UP 55%📈 PROFIT PER SHARE UP 96%📈 ONE OF THE BEST GROWTH STORIES IN CANADA CURRENTLY 🇨🇦🇨🇦🇨🇦🇨🇦 $ATZ https://t.co/pqgJGuNjTK

@gurgavin [Thu Jul 09 16:52:48 +0000 2026]: SOMEONE JUST FILED FOR A S&amp;P 500 &amp; NASDAQ 100 ETF THAT EXCLUDES ONLY ELON MUSK’S COMPANIES THE FUNDS ARE CALLED EX-ELON ENTERPRISES ETF THE FUND EXCLUDES ANY COMPANY “FOUNDED, CONTROLLED, OR LED” BY MUSK CITING GOVERNANCE CONCERNS &amp; POLITICAL RISK $SPNE $QQNE

@gurgavin [Fri Jul 10 17:36:14 +0000 2026]: *SK HYNIX CEO SAYS MEMORY CHIP SHORTAGE MAY PERSIST PAST 2030 $SKHYV

@StockMKTNewz [Mon Jul 13 16:19:45 +0000 2026]: Apple $AAPL has agreed to acquire certain assets and hire employees from SigScalr - MacRumors

@AIStockSavvy [Mon Jul 13 17:18:20 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: $GOOGL Google Expands TPU Push Into AI Cloud Market Dominated by Nvidia - Seeking Alpha - $NBIS $CRWV $NVDA 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐆𝐨𝐨𝐠𝐥𝐞 is marketing 𝐓𝐏𝐔𝐬 to emerging AI neocloud providers. ➤ 𝐍𝐯𝐢𝐝𝐢𝐚 continues to dominate the neocloud GPU market. ➤ Google reportedly approached 𝐍𝐬𝐜𝐚𝐥𝐞 to adopt TPU infrastructure. ➤ Nscale said current deployments remain focused on 𝐍𝐯𝐢𝐝𝐢𝐚 𝐆𝐏𝐔 capacity. ➤ Smaller neoclouds could become potential 𝐆𝐨𝐨𝐠𝐥𝐞 𝐓𝐏𝐔 customers. ➤ Google already supplies TPUs to 𝐀𝐧𝐭𝐡𝐫𝐨𝐩𝐢𝐜, 𝐌𝐞𝐭𝐚, and 𝐀𝐩𝐩𝐥𝐞. ➤ Google and 𝐁𝐥𝐚𝐜𝐤𝐬𝐭𝐨𝐧𝐞 are building a TPU-powered neocloud. ➤ Venture plans to rent TPUs to AI labs and enterprise customers next year. ➤ Google is also partnering with AI cloud provider 𝐅𝐥𝐮𝐢𝐝𝐬𝐭𝐚𝐜𝐤. 👉 𝐄𝐱𝐩𝐞𝐫𝐭 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭: 𝐓𝐡𝐨𝐦𝐚𝐬 𝐊𝐮𝐫𝐢𝐚𝐧, Google Cloud CEO: "This joint venture with Blackstone helps meet growing demand for TPUs, which are optimized specifically for efficiency and performance in the AI era. Together, we're accelerating AI transformation and providing more options for organizations to access accelerated compute capability."

@wallstengine [Mon Jul 13 17:33:25 +0000 2026]: Sunrun $RUN is piloting a program to turn rooftop solar and battery systems into distributed AI compute capacity, per Bloomberg. Customers could host a small filing-cabinet-sized computer and earn “a couple hundred dollars to more than that” per month, CEO Mary Powell said. Sunrun says the “mini data-center capabilities” would be aggregated and sold to tech companies looking for AI compute. No buyers or full economics disclosed yet. Separately, Sunrun, Tesla and Renew Home plan to aggregate 16GW+ of flexible home energy capacity for hyperscalers and utilities.

@gurgavin [Mon Jul 13 14:17:52 +0000 2026]: NEW DAY NEW ALL TIME LOWS FOR SPACEX SHARES $SPCX https://t.co/iKT9uNDcqM

@KobeissiLetter [Mon Jul 13 17:57:35 +0000 2026]: BREAKING: US oil prices surge +9% after President Trump announces the US is reimposing its blockade of the Strait of Hormuz, with ships now required to pay a fee equal to 20% of their cargo’s value to transit the waterway. https://t.co/34sNm9ID2Z

@KobeissiLetter [Mon Jul 13 12:18:20 +0000 2026]: BREAKING: President Trump says the United States is "taking over" the Strait of Hormuz. Brent crude oil prices extend gains to rise above $79/barrel.

@StockMKTNewz [Mon Jul 13 20:11:20 +0000 2026]: Cipotle $CMG just said that its first Chipotle restaurant in Mexico 🇲🇽 will open on Thursday in San Pedro Garza García, Nuevo León https://t.co/8jEz514BEy

@AIStockSavvy [Mon Jul 13 16:40:33 +0000 2026]: Federal Reserve Governor Waller said he expects consumer spending to remain strong and AI-related investment to stay robust. - $QQQ $SPY $SPX

@AIStockSavvy [Mon Jul 13 16:31:05 +0000 2026]: Waller said if core inflation prints high again this week, the Fed will need to consider near-term rate hikes. - $QQQ $SPY $SPX

@AIStockSavvy [Mon Jul 13 14:55:24 +0000 2026]: $ISRG | TD Cowen maintains 𝐁𝐮𝐲 on 𝐈𝐧𝐭𝐮𝐢𝐭𝐢𝐯𝐞 𝐒𝐮𝐫𝐠𝐢𝐜𝐚𝐥, 𝐜𝐮𝐭𝐬 𝐏𝐓 𝐭𝐨 $𝟓𝟐𝟎 from $585 Analyst sees a potential floor for underperforming shares in Q2, suggesting guidance may have an upward bias despite ongoing concerns. https://t.co/1UaSaUT4Qc

@StockMKTNewz [Mon Jul 13 19:19:59 +0000 2026]: Oracle $ORCL stock hit new 52 WEEK LOWS today https://t.co/bTA60ha7oF

@KobeissiLetter [Mon Jul 13 18:55:57 +0000 2026]: BREAKING: Iran’s Foreign Minister Araghchi responds to President Trump announcing a 20% fee to transit the Strait of Hormuz: “POTUS is absolutely right. Whoever provides secure and safe passage of commercial vessels through the Strait of Hormuz should be compensated for this service. Iran has always been the guardian of the Strait and will remain so forever. 20% is of course too much. We will be fair,” he says.

@KobeissiLetter [Mon Jul 13 17:19:09 +0000 2026]: BREAKING: Total US federal debt is now up to a record $39.4 trillion, rising +$3.2 trillion over the last 12 months. Since 2020, US federal debt is now up a massive +$16.3 trillion. This marks a +$2.5 trillion average annual increase, or +$209 billion per month. At this pace, total US debt will surge to $50.0 trillion before 2030. The US debt crisis has no end in sight.

@KobeissiLetter [Mon Jul 13 15:31:16 +0000 2026]: Hedge funds are piling into US semiconductor stocks: Last week, hedge funds purchased the most US semiconductor stocks in at least 3.5 years. This follows the 2 largest consecutive weekly sales since June 2024. As a result, semiconductor stocks now account for 10% of total hedge fund exposure. This percentage is twice as high as during the same period last year. However, this remains below the peak of 14% recorded in May. Hedge funds are betting the semiconductor selloff is already over.

@KobeissiLetter [Mon Jul 13 14:22:45 +0000 2026]: BREAKING: President Trump says the US is reinstating its blockade of the Strait of Hormuz for Iranian ships and customers. Trump says the US will now be known as "The Guardian of the Strait of Hormuz" and will be "reimbursed" at a rate of 20% on all cargo shipped. It appears the US is now imposing a blockade and fees to transit the Strait of Hormuz.

@KobeissiLetter [Mon Jul 13 13:47:53 +0000 2026]: BREAKING: The UAE is planning to build a new port and container terminal on the country's east cost to bypass the Strait of Hormuz, per FT. Details include: 1. Dubai's DP World is in talks to develop a new multipurpose port in the coastal area of Fujairah 2. The new project would allow containers to enter and leave the country without having to pass through the Strait of Hormuz 3. Shipments would then be moved on trucks overland to Dubai, Abu Dhabi, and neighboring Gulf countries The Iran War continues to reshape global trade.

@StockMKTNewz [Mon Jul 13 20:06:44 +0000 2026]: Palantir $PLTR just confirmed it will be reporting earnings after the markets close on Monday, August 3rd

@StockMKTNewz [Mon Jul 13 19:32:59 +0000 2026]: Robinhood $HOOD is reportedly gauging investor interest in a bond backed by bills for its branded consumer credit cards, in what would be the firm’s first offering of its kind The company is looking to sell at least $400 million of asset backed securities in four parts, Initial price talk on the deal’s highest-rated portion is a premium of about 0.8% over the benchmark This is a rumor from Bloomberg, we're still waiting for confirmation from the company

@AIStockSavvy [Mon Jul 13 15:02:49 +0000 2026]: Iran Security Official: $QQQ $SPY $USO ➤ Says control of the Strait of Hormuz is determined by Iran's will, not by Trump's posts ➤ Says Trump's claim that the United States has protected the Strait of Hormuz for 50 years is purely an illusion ➤ Says Trump had forgotten the Strait of Hormuz had belonged to Iran for thousands of years, long before the United States existed

@AIStockSavvy [Mon Jul 13 14:18:18 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: U.S. President Trump says he will restore a blockade against Iran. - $QQQ $SPY $USO

@AIStockSavvy [Mon Jul 13 13:57:46 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Dubai plans new port to bypass Strait of Hormuz - FT - $USO

@wallstengine [Mon Jul 13 18:44:01 +0000 2026]: Bank earnings kick off Q2 earnings season tomorrow. Here’s a preview using @PPLXfinance: JPMorgan: Revenue: $51.1B; +12% YoY Adj. EPS: $5.59; +29% YoY Implied move: ~3.6% $JPM should have a solid quarter. 🧵 (1/8) https://t.co/pitlMHxYUY

@KobeissiLetter [Mon Jul 13 19:49:23 +0000 2026]: BREAKING: President Trump’s Thursday speech is reportedly to address “newly declassified intelligence reports related to foreign interference in the 2020 election,” per MS NOW.

@KobeissiLetter [Mon Jul 13 19:41:41 +0000 2026]: BREAKING: President Trump says he will be addressing the nation on Thursday at 9 PM ET. https://t.co/WmN61ODtYj

@gurgavin [Sun Jul 12 22:08:29 +0000 2026]: STOCK MARKET FUTURES JUST OPENED S&amp;P 500 DOWN 0.3% 📉 DOW JONES DOWN 0.3% 📉 NASDAQ 100 DOWN 0.5% 📉 https://t.co/XJT17hqZLv

@gurgavin [Sun Jul 12 19:04:45 +0000 2026]: TRUMP IS PROBABLY GONNA ANNOUNCE CEASEFIRE NUNBER 528239 RIGH BEFORE FUTURES OPEN FOR THE 3RD WEEK IN A ROW

@gurgavin [Sat Jul 11 23:30:27 +0000 2026]: *IRAN STRIKES VESSEL, CLOSES STRAIT OF HORMUZ INDEFINITELY HERE WE GO AGIN

@StockMKTNewz [Mon Jul 13 19:47:30 +0000 2026]: Berkshire Hathaway $BRK.B is back to having a larger market cap than Micron $MU https://t.co/5jbe5859Ui

@AIStockSavvy [Mon Jul 13 19:15:25 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $HOOD Robinhood Plans First Asset-Backed Bond Tied to Credit Card Receivables 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐑𝐨𝐛𝐢𝐧𝐡𝐨𝐨𝐝 is gauging demand for its first 𝐚𝐬𝐬𝐞𝐭-𝐛𝐚𝐜𝐤𝐞𝐝 𝐛𝐨𝐧𝐝. ➤ Offering is backed by 𝐜𝐨𝐧𝐬𝐮𝐦𝐞𝐫 𝐜𝐫𝐞𝐝𝐢𝐭 𝐜𝐚𝐫𝐝 receivables. ➤ Initial deal size targets at least 𝐒𝟒𝟎𝟎 𝐦𝐢𝐥𝐥𝐢𝐨𝐧. ➤ Total issuance could increase to 𝐒𝟓𝟎𝟎 𝐦𝐢𝐥𝐥𝐢𝐨𝐧. ➤ Securities will be split into 𝐟𝐨𝐮𝐫 𝐭𝐫𝐚𝐧𝐜𝐡𝐞𝐬. ➤ Top-rated tranche is priced at about 𝐨.𝟖 𝐩𝐞𝐫𝐜𝐞𝐧𝐭𝐚𝐠𝐞 𝐩𝐨𝐢𝐧𝐭 over benchmark. ➤ Deal supports Robinhood's expansion into the 𝐜𝐫𝐞𝐝𝐢𝐭 𝐜𝐚𝐫𝐝 market. ➤ Robinhood introduced a 𝐒𝟔𝟗𝟓 𝐩𝐥𝐚𝐭𝐢𝐧𝐮𝐦 credit card in March. ➤ 𝐖𝐞𝐥𝐥𝐬 𝐅𝐚𝐫𝐠𝐨 and 𝐁𝐚𝐫𝐜𝐥𝐚𝐲𝐬 are managing the offering. ➤ 𝐂𝐨𝐚𝐬𝐭𝐚𝐥 𝐂𝐨𝐦𝐦𝐮𝐧𝐢𝐭𝐲 𝐁𝐚𝐧𝐤 owns Robinhood's branded credit card accounts.

@AIStockSavvy [Mon Jul 13 14:54:01 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: States Set To Sue Monday To Block Paramount-warner Bros. Deal - Bloomberg - $PARA $PSKY $WBD

@gurgavin [Sun Jul 12 18:51:40 +0000 2026]: NEW ALL TIME HIGHS COMING

@KobeissiLetter [Mon Jul 13 20:13:40 +0000 2026]: Crypto funds are showing their first signs of a recovery: Crypto ETFs attracted +$281.8 million in inflows last week, the first weekly inflow since the 2nd week of May. Bitcoin funds posted +$197.4 million in inflows, while Ethereum funds attracted +$84.4 million. This also marks the end of an 8-week streak of outflows, totaling more than -$7 billion. As a result, trailing 12-month inflows are down to +$1 billion, from +$10 billion in late April. By comparison, inflows peaked at +$12 billion in October 2025. Buyers are beginning to return to the crypto market.

@StockMKTNewz [Mon Jul 13 17:06:27 +0000 2026]: LIVE STREAM GOING ON RIGHT NOW @ChrisCamillo and @amitisinvesting are live on the WOLF Channel talking about using AI for the stock market

@wallstengine [Mon Jul 13 19:10:40 +0000 2026]: RT @wallstengine: Bernstein: We see China as the lead competitor for $SPCX Analyst comments: “On July 10, China 🇨🇳 successfully landed the…

@StockMKTNewz [Mon Jul 13 19:46:13 +0000 2026]: 🇺🇸 President Trump said he will be making an address to the nation at 9PM ET on Thursday

@AIStockSavvy [Mon Jul 13 15:18:38 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: U.S. Federal Communications Commission (FCC) will accelerate approval of satellite applications.

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.