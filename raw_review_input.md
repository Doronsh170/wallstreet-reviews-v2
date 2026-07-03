אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are a senior Wall Street market analyst writing a PRE-MARKET briefing in Hebrew.
Script run date: 2026-07-03 (יום שישי). Briefing target date: 2026-07-06 (יום שני).
This runs on 2026-07-03 but the briefing is for the NEXT trading day: 2026-07-06 (יום שני). Do NOT use 'היום'/'הבוקר' — use 'ביום שני'. Do NOT describe futures/pre-market as live — they are not available yet.

This is a professional, readable BRIEFING — NOT a data dump. FORWARD-LOOKING ONLY: no yesterday's index
performance, no closing levels, and nothing that already appears in the prior-context block.
EXACTLY 5 bullets, in this order:
* תמונת פתיחה: the mood and backdrop heading into the session — the single most important theme, and futures
  direction ONLY (no percentage unless a specific futures figure appears in the sources; never copy an ETF
  percentage as a futures percentage).
* הסיפור המרכזי: the main driver investors will watch and why it matters, with the transmission mechanism
  explained simply (event → oil → inflation → rates → equities) only when it is genuinely relevant.
* מאקרו ואירועים: the economic releases and Fed events scheduled for the day — Israel time, consensus and the
  previous reading, plus one sentence on why the number matters. If nothing is scheduled, say so in one short
  sentence and point to the next key date.
* דוחות ומניות במוקד: expected earnings and the 1-3 most important NEW overnight stock stories (company news,
  analyst moves). Stock items open with "מניית <שם בעברית> (TICKER)". Positive news about a falling stock →
  "למרות החדשות, המניה ירדה".
* שורה תחתונה: what will decide the direction of the session, in 1-2 sentences.
Each bullet: 2-4 short sentences of flowing Hebrew prose — not a list of figures. After the Hebrew label,
continue in Hebrew words — never open with a ticker, a price or an English term. Do NOT stack prices, price
targets and percentages: pick only the few figures that carry the story. No ETF proxies, no Finnhub, no ISO dates.

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
  "title": "נקודות חשובות לקראת פתיחת המסחר בוול סטריט 🇺🇸 – יום שני, 6.7.2026",
  "date": "2026-07-06",
  "sections": [
    {
      "heading": "נקודות מרכזיות",
      "content": "* נושא ראשון: משפט אנליטי תמציתי עם מספרים.\n* נושא שני: ...\n* נושא שלישי: ..."
    }
  ]
}
- EXACTLY 1 section. Heading EXACTLY "נקודות מרכזיות". Title EXACTLY as given above.
- content = one string, bullets separated by \n, each bullet starts with "* ".
- No "שורה תחתונה"/summary section — merge any concluding insight as a regular bullet.
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
  S&P 500 (SPY ETF): $744.82 (daily: -0.13%), prev close: $745.76
  Nasdaq 100 (QQQ ETF): $712.64 (daily: -1.73%), prev close: $725.17
  Dow Jones (DIA ETF): $527.92 (daily: +1.06%), prev close: $522.40
  Russell 2000 (IWM ETF): $297.62 (daily: -0.57%), prev close: $299.32
  Energy Sector (XLE ETF): $53.24 (daily: +0.81%), prev close: $52.81
  Technology Sector (XLK ETF): $180.62 (daily: -2.69%), prev close: $185.62
  Financials Sector (XLF ETF): $55.64 (daily: +1.57%), prev close: $54.78
  Consumer Discretionary Sector (XLY ETF): $117.15 (daily: -0.80%), prev close: $118.09
  Healthcare Sector (XLV ETF): $163.77 (daily: +2.65%), prev close: $159.54
  Industrials Sector (XLI ETF): $183.94 (daily: +0.32%), prev close: $183.36
  Consumer Staples Sector (XLP ETF): $85.01 (daily: +2.05%), prev close: $83.30
  Utilities Sector (XLU ETF): $45.77 (daily: +2.23%), prev close: $44.77
  WTI Crude Oil (USO ETF): $104.01 (daily: +0.72%), prev close: $103.27
  Brent Crude Oil (BNO ETF): $39.68 (daily: +0.69%), prev close: $39.41
  Gold (GLD ETF): $378.17 (daily: +2.04%), prev close: $370.60
  Silver (SLV ETF): $55.04 (daily: +2.72%), prev close: $53.58
  Bitcoin (IBIT ETF): $34.89 (daily: +2.62%), prev close: $34.00
  US 20Y+ Bonds (TLT ETF): $85.53 (daily: +0.01%), prev close: $85.52
  US Dollar (UUP ETF): $28.33 (daily: -0.56%), prev close: $28.49
  VIX Volatility (VIXY ETF): $21.24 (daily: -1.30%), prev close: $21.52

INDIVIDUAL STOCKS mentioned in the source tweets (verified quotes):
  $META: $582.94 (daily: -4.89%), prev close: $612.91
  $TSLA: $393.49 (daily: -7.48%), prev close: $425.30
  $NVDA: $194.86 (daily: -1.38%), prev close: $197.58
  $MU: $975.60 (daily: -5.49%), prev close: $1032.28
  $SNDK: $1745.04 (daily: -14.13%), prev close: $2032.22
  $PLTR: $129.33 (daily: +2.86%), prev close: $125.73
  $INTC: $120.38 (daily: -5.23%), prev close: $127.02
  $MSFT: $390.53 (daily: +1.63%), prev close: $384.28
  $SPCX: $162.03 (daily: +2.85%), prev close: $157.54
  $AMD: $517.86 (daily: -4.26%), prev close: $540.88
  $AVGO: $360.49 (daily: -2.40%), prev close: $369.34
  $GOOGL: $359.95 (daily: -0.35%), prev close: $361.21

DIRECTIONAL FACTS — Hebrew direction words (עולה/יורד/צונח/מזנק) MUST match these:
  נפט (WTI/ברנט): עולה (USO: +0.72%, BNO: +0.69%)
  זהב: עולה (GLD: +2.04%)
  ביטקוין: עולה (IBIT: +2.62%)
  דולר: יורד (UUP: -0.56%)
  תנודתיות / VIX: יורד (VIXY: -1.30%)
  אג"ח ארוכות / TLT: יציב/כמעט ללא שינוי (TLT: +0.01%)

The % changes above are ACCURATE — use them for direction and magnitude.
The ETF tickers above (SPY/QQQ/DIA/USO/GLD/...) are measurement instruments for YOUR verification only — NEVER name them, Finnhub, or the word 'proxy' in the visible Hebrew text.
For exact index LEVELS (points), gold/oil absolute prices, VIX level, Bitcoin price, 10Y yield: verify via web search. Do NOT estimate them from ETF prices.
For sector performance (XLE/XLK/...): USE ONLY the Finnhub numbers above — never invent sector percentages.
If ANY percentage you write contradicts the data above, you are WRONG. Fix it.
══════════════════════════════════════════════════════════════════════════════

══ SCHEDULED DATA CHECK ══
Use web search to find what US economic data is scheduled for release on 2026-07-03.
Include the release time in Israel time and the market consensus/forecast.
══════════════════════════════════

══ CONTEXT: YESTERDAY'S DAILY SUMMARY — DO NOT REPEAT THIS CONTENT ══
Already published. Your briefing is FORWARD-LOOKING. Mention an item below ONLY if there is a genuinely NEW overnight development about it.

[סיכום המסחר]
* המדדים: וול סטריט נסגרה במגמה מעורבת, כאשר S&P 500 ירד ב-0.13%, Nasdaq 100 ירד ב-1.73%, Dow Jones עלה ב-1.05% ו-Russell 2000 ירד ב-0.58%. הפער בין Dow Jones החזק לבין Nasdaq 100 החלש שיקף מעבר חד ממניות צמיחה וטכנולוגיה למניות ערך וסקטורים דפנסיביים.
* הסיפור של היום: שוק העבודה היה המנוע המרכזי של המסחר, לאחר שנוספו ביוני 57 אלף משרות בלבד מול צפי של 110 אלף, כאשר מאי תוקן מטה ל-129 אלף מ-172 אלף. שיעור האבטלה ירד ל-4.2% מול צפי של 4.3%, אך הירידה הגיעה לצד יציאה של כ-720 אלף איש מכוח העבודה, ולכן השוק פירש את הנתון כחולשה תעסוקתית שמפחיתה לחץ להעלאת ריבית.
* סקטורים ומניות בולטות: סקטור הטכנולוגיה ירד ב-2.71%, בזמן שסקטור הבריאות עלה ב-2.63%, שירותים ציבוריים עלו ב-2.21% וצריכה בסיסית עלתה ב-2.03%. מניית טסלה (TSLA) ירדה ב-7.49% למרות העלאות יעדים ל-420 ו-430 דולר, על רקע דיווח על תקרת שימוש פנימית של 200 דולר בשבוע לכלי בינה מלאכותית. מניית מטא (META) ירדה ב-4.90% לאחר שמארק צוקרברג אמר כי פיתוח סוכני AI בארבעת החודשים האחרונים לא האיץ בקצב שהחברה ציפתה לו.
* סחורות, דולר ותשואות: הנפט נעים בתנודתיות בכ-0.7%, הזהב נעים בתנודתיות ב-2.03% והביטקוין נעים בתנודתיות ב-2.56%, שילוב שמתאים ליום שבו הדולר נעים בתנודתיות ב-0.53%. אג״ח ארוכות היו כמעט ללא שינוי עם ירידה של 0.01%, והתנודתיות ירדה ב-1.35%, כלומר השוק לא תימחר אירוע לחץ רחב למרות הירידה החדה בטכנולוגיה.
* שורה תחתונה למחר: ביום שישי, 3.7.2026, לא פורסמו נתוני מאקרו מרכזיים בארה״ב בגלל חופשת 4 ביולי, ולכן המוקד עבר ליום שני, 6.7.2026. המשקיעים עקבו בעיקר אחרי ISM Services PMI ליוני בשעה 17:00 שעון ישראל, עם צפי של 54.5 מול 54.5 קודם, ואחרי השאלה אם חולשת התעסוקה תמשיך לתמוך בדולר חלש ובמעבר מסקטור הטכנולוגיה לסקטורים דפנסיביים.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-03. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Fri Jul 03 12:57:12 +0000 2026]: Leverage in South Korean stocks is out of control: Assets under management (AUM) in South Korea's leveraged ETFs are up to a record ~$45 billion. AUM has surged +800% since the start of 2026. As a result, leveraged exposure as a % of free float market capitalization, the portion of shares actually available for public trading, is up to a record ~2.9%, more than TRIPLING since January. Meanwhile, the Hong Kong-listed 2x leveraged long SK Hynix ETF rose to ~$15 billion in assets at its peak, the largest single-stock leveraged product in the world. By comparison, four leading 2x leveraged long ETFs tracking Micron, $MU, Nvidia, $NVDA, Sandisk, $SNDK, and Tesla, $TSLA, have each never exceeded $10 billion in assets. Leverage in Korea is at extreme levels.

@gurgavin [Thu Jul 02 19:10:49 +0000 2026]: TESLA CAPS EMPLOYEE AI SPEND AT $200 PER WEEK PER THE INFORMATION $TSLA

@gurgavin [Tue Jun 30 20:38:47 +0000 2026]: MICHAEL BURRY IS REPORTEDLY SHORT TESLA NOW HE NEVER LEARNS , NO ONE MAKES MONEY BETTING AGAINST ELON $TSLA https://t.co/wsBIQluMTg

@wallstengine [Thu Jul 02 19:14:20 +0000 2026]: $TSLA reportedly told employees it will cap AI spending at $200 per week starting July 6, per The Information. Some Tesla software engineers were reportedly using thousands of dollars worth of AI tokens per week. Employees will need approval to exceed the cap, though beta versions of xAI products are reportedly excluded.

@wallstengine [Thu Jul 02 18:56:37 +0000 2026]: $META CEO Mark Zuckerberg told employees in an internal town hall that AI agent development over the last four months has not “accelerated in the way we expected.” - Reuters https://t.co/tT20xKh2bm

@gurgavin [Wed Jul 01 18:02:23 +0000 2026]: SPACEX HAS BEEN SHOWING OFF A PROTOTYPE OF A NEW “AI DEVICE” WHICH IS SIMILAR THAN AS IPHONE PER WSJ THE DEVICE RUNS ON CUSTOM SOFTWARE AND USED XAI’S TECH $SPCX

@StockMKTNewz [Fri Jul 03 15:38:27 +0000 2026]: Palantir $PLTR CEO Alex Karp said that some 🇺🇸 government customers have switched from proprietary AI models to Nvidia’s $NVDA open-source Nemotron models - The Information https://t.co/D3chr9tdsv

@wallstengine [Thu Jul 02 20:07:36 +0000 2026]: $META CEO MARK ZUCKERBERG SAYS IN INTERNAL TOWN HALL HE EXPECTS COMPANY TO FEEL MORE BENEFITS OF AI INVESTMENT IN NEXT 3-6 MONTHS

@gurgavin [Thu Jul 02 18:04:16 +0000 2026]: AN AUTOGRAPHED JACKET OF NVIDIA CEO JENSEN HUANG IS UP FOR AUCTION ON SOTHEBYS IT'S SIGNED BY HIM AND HE ACTUALLY WORE THIS EXACT JACKET IN THE PAST IT'S ESTIMATED TO SELL FOR $40,000–$60,000 $NVDA https://t.co/jedGiznXYO

@KobeissiLetter [Fri Jul 03 16:23:00 +0000 2026]: BREAKING: Since the start of 2025, US jobs numbers have now been revised down in 14 out of 17 months by a total of -710,000 jobs. May and April jobs numbers were revised down by a total of -74,000, the largest 2-month downward revision since December. April jobs were revised down by -31,000, to +148,000, while May jobs were revised down by -43,000, to +129,000. This means -41,765 jobs have been revised out of previously reported data, on average, in each month of this period. If we apply this average to the +57,000 June nonfarm payrolls, it would imply just ~15,000 jobs were added last month. Job market revisions are concerning.

@KobeissiLetter [Thu Jul 02 22:00:02 +0000 2026]: Levered ETFs have become one of the most powerful forces in US equity markets: Daily rebalancing activity in US equity leveraged ETFs is up to a record $50 billion. Leveraged ETFs must rebalance daily to stay at their target leverage, adding more exposure after markets rise and reducing it after markets fall. This figure has more than QUADRUPLED since the start of 2026. Rebalancing activity now accounts for a record 1.60% of S&P 500 futures volume, exceeding the 2020-2024 peaks by 200%. To put it simply, leveraged ETFs have grown large enough that their daily rebalancing can now amplify market moves in both directions. Leveraged ETFs are amplifying market volatility like never before.

@wallstengine [Thu Jul 02 19:17:29 +0000 2026]: $META’s Zuckerberg reportedly told employees in an internal town hall that the bets behind the company’s reorganization “haven’t come to fruition yet.” He still believes long-term trends remain aligned with the basic shape of the reorg.

@StockMKTNewz [Fri Jul 03 16:06:30 +0000 2026]: Tesla $TSLA just said its Robotaxi service is now available in Miami https://t.co/BWJPgQ2raa

@AIStockSavvy [Fri Jul 03 14:48:48 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: $META Meta Is Reportedly Considering a Partnership With Samsung to Produce a ₩100 Trillion Custom AI Chip. - $GOOGL $AVGO $NVDA $AMD $INTC Meta is considering a collaboration with Samsung Electronics to produce a custom artificial intelligence chip worth about 100 trillion South Korean won. If the collaboration is successful, it will become one of Samsung's important AI orders for its semiconductor foundry business. The two parties have not officially announced the collaboration yet.

@AIStockSavvy [Fri Jul 03 14:17:57 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: Kioxia, $SNDK Sandisk Begin Production of 10th-Gen 3D NAND Flash at K2 Fab 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐊𝐢𝐨𝐱𝐢𝐚 and 𝐒𝐚𝐧𝐝𝐢𝐬𝐤 began production of 𝐭𝐡-𝐠𝐞𝐧 𝟑𝐃 𝐍𝐀𝐍𝐃 at Japan's K2 Fab. ➤ K2 previously produced 𝐞𝐢𝐠𝐡𝐭𝐡-𝐠𝐞𝐧 𝟑𝐃 𝐍𝐀𝐍𝐃 and will now scale 10th-gen output. ➤ Both generations use 𝐂𝐁𝐀 technology for higher performance, capacity, and lower power. ➤ K2 features 𝐞𝐚𝐫𝐭𝐡𝐪𝐮𝐚𝐤𝐞-𝐫𝐞𝐬𝐢𝐬𝐭𝐚𝐧𝐭 design, AI-driven production, and energy-efficient equipment. ➤ Companies extended their 𝐣𝐨𝐢𝐧𝐭 𝐯𝐞𝐧𝐭𝐮𝐫𝐞 through 𝐃𝐞𝐜𝐞𝐦𝐛𝐞𝐫 𝟐𝟎𝟑𝟒. ➤ Continued investments aim to support 𝐦𝐮𝐥𝐭𝐢-𝐲𝐞𝐚𝐫 NAND bit growth and manufacturing expansion. ➤ Partnership has collaborated on 𝐍𝐀𝐍𝐃 𝐟𝐥𝐚𝐬𝐡 innovation for more than 𝟐𝟓 years. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ Expands manufacturing capacity to meet rising 𝐀𝐈 and data storage demand. ➤ Strengthens long-term 𝐍𝐀𝐍𝐃 𝐟𝐥𝐚𝐬𝐡 supply and technology leadership. ➤ Reinforces the strategic 𝐔.𝐒.-𝐉𝐚𝐩𝐚𝐧 semiconductor manufacturing partnership. 👉 𝐄𝐱𝐩𝐞𝐫𝐭 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭: ➤ "We are pleased to begin production of our advanced 10th-generation flash memory here in Kitakami. The eighth and further generation flash memory products produced at the Fab2 will deliver new value to the rapidly growing AI market. Leveraging the partnership and scale advantages, Kioxia will continue to manufacture leading-edge flash memory products and achieve sustainable corporate growth. Kioxia will continue to contribute to the advancement of the semiconductor industry and the development of local and domestic economies." — 𝐊𝐨𝐢𝐜𝐡𝐢𝐫𝐨 𝐒𝐡𝐢𝐛𝐚𝐲𝐚𝐦𝐚, President and CEO of Kioxia Iwate Corporation. ➤ "Beginning production of our 10th-generation 3D flash memory at our Kitakami facility marks an important milestone for the two companies as demand for high-performance flash technologies continues to increase. Through our K2 facility we will continue to support our customers with the world's leading NAND technology, while providing new economic opportunities for the communities we operate in and serving as an example of strong U.S.-Japan economic relations." — 𝐀𝐥𝐩𝐞𝐫 𝐈𝐥𝐤𝐛𝐚𝐡𝐚𝐫, Chief Technology Officer of Sandisk Corporation.

@AIStockSavvy [Thu Jul 02 19:21:31 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $TSLA Tesla Caps Employee AI Spend At $200 A Week - Information

@StockMKTNewz [Fri Jul 03 15:11:13 +0000 2026]: Here is Microsoft's $MSFT market cap every July since going public 1986: $790 MILLION 1987: $2.7 BILLION 1988: $3.5B 1989: $3B 1990: $8B 1991: $11B 1992: $19B 1993: $25B 1994: $28B 1995: $55B 1996: $70B 1997: $160B 1998: $270B 1999: $470B 2000: $420B - Steve Ballmer replaces Bill Gates as CEO 2001: $380B 2002: $290B 2003: $280B 2004: $310B 2005: $265B 2006: $235B 2007: $280B 2008: $240B 2009: $210B 2010: $200B 2011: $220B 2012: $255B 2013: $280B 2014: $345B - Satya Nadella replaces Steve Ballmer as CEO 2015: $355B 2016: $400B 2017: $530B 2018: $765B 2019: $1 TRILLION 2020: $1.5T 2021: $2T 2022: $1.9T 2023: $2.5T 2024: $3.4T 2025: $3.8T 2026: $2.9T

@StockMKTNewz [Fri Jul 03 11:40:34 +0000 2026]: Michael Burry is now reportedly short Micron $MU stock - MarketWatch https://t.co/pKrkOSp87L

@KobeissiLetter [Fri Jul 03 14:05:24 +0000 2026]: What is happening with the US labor market? The difference between nonfarm payrolls and the household survey was a massive 564,000 jobs in June. This comes as Thursday’s job report showed +57,000 non-farm payrolls were added last month. At the same time, -507,000 Americans lost their job, the 3rd-largest drop since January 2024, according to the household survey. The household survey is a closely followed metric because it counts each worker only once, even if they hold multiple jobs. Year-to-date, total employment in the household survey has declined -1.7 million, to 162.26 million, the lowest since December 2024. Over the same period, total nonfarm employment has risen +552,000, to a record 158.98 million. Something does not add up here.

@KobeissiLetter [Thu Jul 02 17:11:59 +0000 2026]: BREAKING: The Strategic Petroleum Reserve (SPR) fell -5.5 million barrels last week, to 326 million barrels, the lowest since May 1983. This marks the 13th consecutive weekly decline, the longest streak since the 2021-2023 period, per Zerohedge. Over this time period, US oil reserves in the SPR have fallen -89 million barrels. This represents 51.7% of the planned 172 million barrels to be released under a relief program coordinated by the IEA to lower energy costs. By comparison, the US added +69 million barrels of oil to the SPR between July 2023 and March 2026. US oil reserves are being depleted at a historic pace.

@KobeissiLetter [Thu Jul 02 16:15:56 +0000 2026]: Retail dip-buying is reaching historic extremes: Average daily equity purchases by retail investors during S&P 500 down days are running at nearly 3.5 times the daily average seen since 2020, the highest on record. This is +56% higher than during the meme stock mania in 2021. Year-to-date, retail purchases on down days are 2.3 times larger than on up days. Even during S&P 500 up days, retail investors purchased nearly 1.5 times the daily average seen since 2020, so far this year, and double the figure posted in 2025. Individual investors have consistently purchased more equities on down days than on up days in each of the last 7 years. Retail investors are eager to buy dips.

@KobeissiLetter [Thu Jul 02 14:51:00 +0000 2026]: History points to a strong July for US stocks: Since 2005, the S&P 500 has recorded an average gain of +2.5% in July, more than 4 times the average increase seen in the other 11 months of the year. The index has not declined in July for 11 consecutive years, the longest positive streak of any month over this period. Meanwhile, the S&P 500 has posted 24 all-time highs so far in 2026. This ranks among the top 20 strongest starts to a year for the index since World War II.. Historically, when the index has seen such a streak, it has rallied another +6% over the following 6 months, on average. Seasonal patterns suggest continued bullish momentum this month.

@gurgavin [Thu Jul 02 04:05:46 +0000 2026]: JUST IN : OPEN AI TO HANDOVER 5% OF IT’S ENTIRE COMPANY TO THE US GOVT PER FT

@wallstengine [Fri Jul 03 01:40:28 +0000 2026]: $MSTR -73% in one year 🩸 https://t.co/nJYIksFwN7

@wallstengine [Thu Jul 02 20:07:43 +0000 2026]: $META CTO ANDREW BOSWORTH SAYS IN INTERNAL TOWN HALL THAT MOUSE TRACKING SOFTWARE WENT THROUGH PRIVACY, LEGAL AND OTHER REVIEWS BEFORE IT LAUNCHED

@wallstengine [Thu Jul 02 19:38:45 +0000 2026]: BlueCrest Capital Management and Michael Platt reported beneficial ownership of 2,354,233 Class A shares of $CCXI Churchill Capital Corp XI, equal to 5.6%. https://t.co/EYRuQhlutE

@wallstengine [Thu Jul 02 19:04:19 +0000 2026]: $META CEO Mark Zuckerberg told employees in an internal town hall that the company’s 2026 reorganization “wasn’t as clean as it could have been.”

@StockMKTNewz [Fri Jul 03 16:14:26 +0000 2026]: Tesla $TSLA posted this earlier in the week: “Engineering tests of the first production Cybercab have begun in Austin” https://t.co/iYPkaKMMIM

@AIStockSavvy [Fri Jul 03 14:33:24 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: Report Says $BABA Alibaba Bans Claude Code Over Security Concerns 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐀𝐥𝐢𝐛𝐚𝐛𝐚 reportedly banned employees from using 𝐂𝐥𝐚𝐮𝐝𝐞 𝐂𝐨𝐝𝐞 for work. ➤ Internal notice reportedly labels Claude Code as 𝐡𝐢𝐠𝐡-𝐫𝐢𝐬𝐤 software with security vulnerabilities. ➤ Workplace ban is scheduled to take effect on 𝐉𝐮𝐥𝐲 𝟏𝟎. ➤ Report cites concerns over hidden code allegedly tracking 𝐂𝐡𝐢𝐧𝐞𝐬𝐞 users. ➤ Anthropic engineer said the tracking mechanism was an 𝐞𝐱𝐩𝐞𝐫𝐢𝐦𝐞𝐧𝐭 introduced in March. ➤ Anthropic said the feature targeted 𝐚𝐜𝐜𝐨𝐮𝐧𝐭 𝐚𝐛𝐮𝐬𝐞 and model distillation concerns. ➤ The company said the tracking system would be 𝐫𝐨𝐥𝐥𝐞𝐝 𝐛𝐚𝐜𝐤. ➤ Alibaba reportedly recommended employees use its 𝐐𝐨𝐝𝐞𝐫 coding platform instead. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ Highlights growing 𝐔.𝐒.-𝐂𝐡𝐢𝐧𝐚 AI security and technology tensions. ➤ May accelerate adoption of 𝐝𝐨𝐦𝐞𝐬𝐭𝐢𝐜 AI development tools in China. ➤ Underscores increasing focus on 𝐞𝐧𝐭𝐞𝐫𝐩𝐫𝐢𝐬𝐞 AI security and data governance. 👉 𝐄𝐱𝐩𝐞𝐫𝐭 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭: ➤ "It was an experiment... designed to prevent account abuse from unauthorised resellers and protect against distillation." — 𝐓𝐡𝐚𝐫𝐢𝐪 𝐒𝐡𝐢𝐡𝐢𝐩𝐚𝐫, Anthropic Engineer. ➤ "If a US AI coding tool can detect Chinese usage or proxy access, then it's not surprising for major Chinese tech companies to not want employees using it internally." — 𝐋𝐢𝐳𝐳𝐢 𝐋𝐞𝐞, Fellow at the Asia Society Policy Institute's Centre for China Analysis.

@AIStockSavvy [Thu Jul 02 23:58:18 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: Data center startup Crusoe in talks to raise $3 bln; valuation could double to $30 bln - $META $ORCL Crusoe, a data-center startup supplying AI compute to Meta Platforms and Oracle, is in talks to raise roughly $3 bln, people familiar with the matter said, a deal that could roughly double its valuation to about $30 bln. The company is still negotiating the round and no final valuation has been set; investors expect a post-money valuation near $30 bln including the new capital. Crusoe was valued at about $10 bln in October last year.

@AIStockSavvy [Thu Jul 02 19:52:37 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $PLTR Palantir CEO said some U.S. government clients have shifted to open-source AI. - The Information

@AIStockSavvy [Thu Jul 02 19:09:25 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $META Meta CEO Mark Zuckerberg Says In Internal Town Hall That Ai Agent Development Over The Last Four Months Hasn't 'accelerated In The Way We Expected' - Reuters

@KobeissiLetter [Thu Jul 02 20:05:00 +0000 2026]: BREAKING: The Dow surges nearly +600 points and closes at its highest level on record. https://t.co/YYa1kGCaYD

@KobeissiLetter [Thu Jul 02 19:01:56 +0000 2026]: BREAKING: Global stock market cap is up to a record $166 trillion. This marks a +$32 trillion YoY increase, or +23.6%, far above the long-term average. Global markets have surged +$94 trillion, or +131%, since the 2020 pandemic low. By comparison, the global equity market value has grown at a +7.0% compound annual growth rate (CAGR) over the last 20 years. Meanwhile, as a % of global GDP, the global equity market cap is up to a record ~134%. Global equities are in the midst of one of the most powerful rallies in history.

@gurgavin [Tue Jun 30 20:52:21 +0000 2026]: JUST IN: TRUMP MADE $635 MILLION DOLLARS IN ROYALTIES LINKED TO HIS MEME COIN https://t.co/X3oXvQ7wPc

@AIStockSavvy [Fri Jul 03 14:28:57 +0000 2026]: 🏆 TOP 10 WEEKLY ANALYST RATINGS: $MU $FCEL $INTC $BE $ALAB $SNDK $AMAT $ABSI $MRVL $HIMS https://t.co/Icw8ePDvvr

@AIStockSavvy [Thu Jul 02 20:20:17 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Jane Street Group Discloses Passive Stake of 5% in $HTZ Hertz Global as of June 26 - Filing

@AIStockSavvy [Thu Jul 02 17:40:09 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $MSFT Microsoft is planning to merge its consumer and enterprise Copilot chatbots in August - The Information

@StockMKTNewz [Fri Jul 03 12:03:28 +0000 2026]: SK HYNIX MADE MORE PROFIT IN Q1 OF THIS YEAR THAN REVENUE IT BROUGHT IN ALL OF 2023 Here is what SK Hynix's numbers have looked like over the last couple of years - 2023: Revenue $21.24B, Profit/(loss) -$5.92B - 2024: Revenue $42.91B, Profit $12.83B - 2025: Revenue $62.98B, Profit $27.84B - Q1 2026: Revenue $34.08B, Profit $26.15B SK Hynix is on pace to bring in more than $100 Billion of PROFIT in 2026 which would be almost 4x more than 2025 SK Hynix will be listing its shares on the Nasdaq next week Shoutout to my partners over at Leverage Shares for making the graphic

@KobeissiLetter [Fri Jul 03 15:14:00 +0000 2026]: Foreign investors are piling into US equities at a record pace: Cumulative year-to-date inflows from global investment funds into US equities are up to ~2.5% of their total assets under management. This percentage has more than DOUBLED since May alone. This is also significantly above the 2002-2025 average of -0.3% in outflows for this point in the year. By comparison, excluding the top 10% with the largest inflows and the bottom 10% with the largest outflows of the 2002-2025 period, global fund inflows averaged just ~1.5% by this point in the year. The YTD pace has already exceeded the full-year total recorded in the middle 50% of years since 2002. Current demand for US equities is unprecedented.

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.