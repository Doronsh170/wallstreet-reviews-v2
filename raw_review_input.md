אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are a senior Wall Street market analyst writing a PRE-MARKET briefing in Hebrew.
Script run date: 2026-07-05 (יום ראשון). Briefing target date: 2026-07-06 (יום שני).
This runs on 2026-07-05 but the briefing is for the NEXT trading day: 2026-07-06 (יום שני). Do NOT use 'היום'/'הבוקר' — use 'ביום שני'. Do NOT describe futures/pre-market as live — they are not available yet.

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
  S&P 500 (SPY ETF): $744.78 (daily: -0.13%), prev close: $745.76
  Nasdaq 100 (QQQ ETF): $712.60 (daily: -1.73%), prev close: $725.17
  Dow Jones (DIA ETF): $527.88 (daily: +1.05%), prev close: $522.40
  Russell 2000 (IWM ETF): $297.58 (daily: -0.58%), prev close: $299.32
  Energy Sector (XLE ETF): $53.22 (daily: +0.78%), prev close: $52.81
  Technology Sector (XLK ETF): $180.59 (daily: -2.71%), prev close: $185.62
  Financials Sector (XLF ETF): $55.62 (daily: +1.53%), prev close: $54.78
  Consumer Discretionary Sector (XLY ETF): $117.12 (daily: -0.82%), prev close: $118.09
  Healthcare Sector (XLV ETF): $163.74 (daily: +2.63%), prev close: $159.54
  Industrials Sector (XLI ETF): $183.91 (daily: +0.30%), prev close: $183.36
  Consumer Staples Sector (XLP ETF): $84.99 (daily: +2.03%), prev close: $83.30
  Utilities Sector (XLU ETF): $45.76 (daily: +2.21%), prev close: $44.77
  WTI Crude Oil (USO ETF): $103.98 (daily: +0.69%), prev close: $103.27
  Brent Crude Oil (BNO ETF): $39.67 (daily: +0.66%), prev close: $39.41
  Gold (GLD ETF): $378.13 (daily: +2.03%), prev close: $370.60
  Silver (SLV ETF): $55.02 (daily: +2.69%), prev close: $53.58
  Bitcoin (IBIT ETF): $34.87 (daily: +2.56%), prev close: $34.00
  US 20Y+ Bonds (TLT ETF): $85.51 (daily: -0.01%), prev close: $85.52
  US Dollar (UUP ETF): $28.34 (daily: -0.53%), prev close: $28.49
  VIX Volatility (VIXY ETF): $21.23 (daily: -1.35%), prev close: $21.52

INDIVIDUAL STOCKS mentioned in the source tweets (verified quotes):
  $META: $582.90 (daily: -4.90%), prev close: $612.91
  $MU: $975.56 (daily: -5.49%), prev close: $1032.28
  $NVDA: $194.83 (daily: -1.39%), prev close: $197.58
  $TSLA: $393.45 (daily: -7.49%), prev close: $425.30
  $MSFT: $390.49 (daily: +1.62%), prev close: $384.28
  $INTC: $120.35 (daily: -5.25%), prev close: $127.02
  $AMZN: $242.67 (daily: +0.40%), prev close: $241.70
  $AVGO: $360.45 (daily: -2.41%), prev close: $369.34
  $SNDK: $1745.00 (daily: -14.13%), prev close: $2032.22
  $SPCX: $162.00 (daily: +2.83%), prev close: $157.54
  $AAPL: $308.63 (daily: +4.84%), prev close: $294.38
  $GOOGL: $359.91 (daily: -0.36%), prev close: $361.21

DIRECTIONAL FACTS — Hebrew direction words (עולה/יורד/צונח/מזנק) MUST match these:
  נפט (WTI/ברנט): עולה (USO: +0.69%, BNO: +0.66%)
  זהב: עולה (GLD: +2.03%)
  ביטקוין: עולה (IBIT: +2.56%)
  דולר: יורד (UUP: -0.53%)
  תנודתיות / VIX: יורד (VIXY: -1.35%)
  אג"ח ארוכות / TLT: יציב/כמעט ללא שינוי (TLT: -0.01%)

The % changes above are ACCURATE — use them for direction and magnitude.
The ETF tickers above (SPY/QQQ/DIA/USO/GLD/...) are measurement instruments for YOUR verification only — NEVER name them, Finnhub, or the word 'proxy' in the visible Hebrew text.
For exact index LEVELS (points), gold/oil absolute prices, VIX level, Bitcoin price, 10Y yield: verify via web search. Do NOT estimate them from ETF prices.
For sector performance (XLE/XLK/...): USE ONLY the Finnhub numbers above — never invent sector percentages.
If ANY percentage you write contradicts the data above, you are WRONG. Fix it.
══════════════════════════════════════════════════════════════════════════════

══ SCHEDULED DATA CHECK ══
Use web search to find what US economic data is scheduled for release on 2026-07-05.
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

Source tweets/posts from X (Twitter) — gathered 2026-07-05. Never mention in the review that these came from tweets/posts:

@StockMKTNewz [Fri Jul 03 20:33:07 +0000 2026]: This is how the largest stocks in the world have performed over the last decade Nvidia $NVDA +16,602%🟢 Apple $AAPL +1,187%🟢 Google $GOOGL +919%🟢 Microsoft $MSFT +663%🟢 Amazon $AMZN +569%🟢 Taiwan Semi $TSM +1,536%🟢 Broadcom $AVGO +2,237%🟢 Meta Platforms $META +410%🟢 Tesla $TSLA +2,626%🟢 Eli Lilly $LLY +1,438%🟢 Micron $MU +7,705%🟢

@StockMKTNewz [Sat Jul 04 14:09:53 +0000 2026]: Here are the top 50 largest American 🇺🇸 companies Nvidia $NVDA $4.718T Apple $AAPL $4.532T Google $GOOG $4.346T Microsoft $MSFT $2.900T Amazon $AMZN $2.610T SpaceX $SPCX $2.134T Broadcom $AVGO $1.714T Meta Platforms $META $1.479T Tesla $TSLA $1.477T Micron Technology $MU $1.101T Berkshire Hathaway $BRK.B $1.095T Eli Lilly $LLY $1.082T JPMorgan $JPM $896.21B Walmart $WMT $890.03B AMD $AMD $844.35B Visa $V $688.67B Johnson & Johnson $JNJ $633.19B Intel $INTC $604.87B Exxon Mobil $XOM $568.23B Applied Materials $AMAT $478.78B Mastercard $MA $476.59B AbbVie $ABBV $461.25B Cisco $CSCO $444.16B Caterpillar $CAT $443.79B Lam Research $LRCX $439.46B Costco $COST $422.04B Bank of America $BAC $416.78B Oracle $ORCL $404.04B General Electric $GE $394.44B UnitedHealth $UNH $386.28B Coca-Cola $KO $362.01B Home Depot $HD $356.86B Procter & Gamble $PG $352.57B Morgan Stanley $MS $337.42B Chevron $CVX $336.97B Netflix $NFLX $326.96B Merck $MRK $319.99B Palantir $PLTR $309.97B KLA $KLAC $307.69B Goldman Sachs $GS $301.20B GE Vernova $GEV $299.11B Philip Morris $PM $284.07B Palo Alto Networks $PANW $283.66B IBM $IBM $272.11B RTX $RTX $268.32B Texas Instruments $TXN $266.72B Wells Fargo $WFC $261.67B Sandisk $SNDK $258.41B Dell $DELL $254.78B American Express $AXP $240.15B

@KobeissiLetter [Sat Jul 04 19:55:21 +0000 2026]: Leverage in South Korean chip stocks is out of control: Single-stock leveraged and inverse ETFs tracking SK Hynix now hold ~$19 billion in total assets, more than 4 times the stock's average daily trading volume this year of ~$4.5 billion. At the same time, Samsung has ~$12.4 billion in leveraged ETF assets, +176% above its ~$4.5 billion in average daily turnover. Furthermore, the Hong Kong-listed 2x leveraged long SK Hynix ETF, which holds ~$13 billion in assets, is worth about twice the value of SK Hynix shares traded on an average day, the widest gap of any major stock with a leveraged ETF tracking it. By comparison, Micron, $MU, has ~$9.9 billion in leveraged ETF assets, well below its ~$27.5 billion in average daily trading volume. All while Tesla, $TSLA, and Nvidia, $NVDA, have leveraged ETF assets of ~$6.0 billion and ~$5.6 billion, both far smaller than their daily trading volumes of ~$23.6 billion and ~$28.8 billion, respectively. Leverage concentration in Korean chip stocks is through the roof.

@KobeissiLetter [Sun Jul 05 00:21:40 +0000 2026]: The AI infrastructure buildout is entering a new phase: US tech companies are committing to spend a record $850 billion on data center leases over the next several years. This marks a +$570 billion YoY increase, or +204%, and +$200 billion QoQ increase, or +31%. Meta, $META, added the most in Q1 2026, committing +$79 billion in new leases, a +76% QoQ increase, bringing its total to ~$183 billion. At the same time, Microsoft, $MSFT, added +$41 billion, a +26% QoQ increase, bringing its total to ~$197 billion. Oracle leads with the largest total commitments at ~$250 billion, having already secured many of the key sites needed to fulfill its contract with OpenAI. Tech companies are doubling down on AI.

@gurgavin [Thu Jul 02 19:10:49 +0000 2026]: TESLA CAPS EMPLOYEE AI SPEND AT $200 PER WEEK PER THE INFORMATION $TSLA

@gurgavin [Wed Jul 01 18:02:23 +0000 2026]: SPACEX HAS BEEN SHOWING OFF A PROTOTYPE OF A NEW “AI DEVICE” WHICH IS SIMILAR THAN AS IPHONE PER WSJ THE DEVICE RUNS ON CUSTOM SOFTWARE AND USED XAI’S TECH $SPCX

@gurgavin [Thu Jul 02 18:04:16 +0000 2026]: AN AUTOGRAPHED JACKET OF NVIDIA CEO JENSEN HUANG IS UP FOR AUCTION ON SOTHEBYS IT'S SIGNED BY HIM AND HE ACTUALLY WORE THIS EXACT JACKET IN THE PAST IT'S ESTIMATED TO SELL FOR $40,000–$60,000 $NVDA https://t.co/jedGiznXYO

@gurgavin [Fri Jul 03 21:26:04 +0000 2026]: IMAGINE SHORTING MICRON WHEN TRUMP IS TRYNA PUMP IT EVERY SINGLE DAY $MU

@StockMKTNewz [Sun Jul 05 11:43:27 +0000 2026]: SpaceX $SPCX will be added to the NASDAQ 100 $QQQ ETF this week https://t.co/Elk2WI3TM7

@wallstengine [Sat Jul 04 11:35:41 +0000 2026]: Intel $INTC reportedly fixed 18A wafer-to-wafer yield variability, with Oregon + Arizona output reaching ~30K wafers/month, per BlueFin. https://t.co/1GyQwUsEbU

@StockMKTNewz [Sat Jul 04 16:00:35 +0000 2026]: Amazon $AMZN is the largest American 🇺🇸 company ranked by REVENUE https://t.co/JYqwEXoibK

@KobeissiLetter [Sun Jul 05 13:32:15 +0000 2026]: Key Events This Week: 1. June S&P Global Services PMI data - Monday 2. ADP Employment Change data - Tuesday 3. Fed Meeting Minutes - Wednesday 4. Initial Jobless Claims data - Thursday 5. June Existing Home Sales data - Thursday 6. IEA Monthly Report - Friday We are one week out from earnings season.

@KobeissiLetter [Sat Jul 04 22:10:50 +0000 2026]: BREAKING: The US goods trade deficit widened by -$22.8 billion, or -27%, in May, to -$105.8 billion, the largest since March 2025. This marks the largest monthly increase since November 2025. US goods exports fell -$11.8 billion, or -5%, to $207.7 billion, the lowest since February, driven by a sharp decline in industrial supplies, particularly energy shipments. Meanwhile, imports rose +$10.9 billion, or +4%, to $313.4 billion, the highest since March 2025. The increase was driven by continued imports of data center equipment, including computers, semiconductors, and telecom equipment. The trade deficit is widening again.

@KobeissiLetter [Sat Jul 04 18:26:56 +0000 2026]: BREAKING: Bitcoin officially reclaims $63,000. https://t.co/Q9Rlg2b85Z

@AIStockSavvy [Fri Jul 03 14:48:48 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: $META Meta Is Reportedly Considering a Partnership With Samsung to Produce a ₩100 Trillion Custom AI Chip. - $GOOGL $AVGO $NVDA $AMD $INTC Meta is considering a collaboration with Samsung Electronics to produce a custom artificial intelligence chip worth about 100 trillion South Korean won. If the collaboration is successful, it will become one of Samsung's important AI orders for its semiconductor foundry business. The two parties have not officially announced the collaboration yet.

@AIStockSavvy [Fri Jul 03 14:17:57 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: Kioxia, $SNDK Sandisk Begin Production of 10th-Gen 3D NAND Flash at K2 Fab 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐊𝐢𝐨𝐱𝐢𝐚 and 𝐒𝐚𝐧𝐝𝐢𝐬𝐤 began production of 𝐭𝐡-𝐠𝐞𝐧 𝟑𝐃 𝐍𝐀𝐍𝐃 at Japan's K2 Fab. ➤ K2 previously produced 𝐞𝐢𝐠𝐡𝐭𝐡-𝐠𝐞𝐧 𝟑𝐃 𝐍𝐀𝐍𝐃 and will now scale 10th-gen output. ➤ Both generations use 𝐂𝐁𝐀 technology for higher performance, capacity, and lower power. ➤ K2 features 𝐞𝐚𝐫𝐭𝐡𝐪𝐮𝐚𝐤𝐞-𝐫𝐞𝐬𝐢𝐬𝐭𝐚𝐧𝐭 design, AI-driven production, and energy-efficient equipment. ➤ Companies extended their 𝐣𝐨𝐢𝐧𝐭 𝐯𝐞𝐧𝐭𝐮𝐫𝐞 through 𝐃𝐞𝐜𝐞𝐦𝐛𝐞𝐫 𝟐𝟎𝟑𝟒. ➤ Continued investments aim to support 𝐦𝐮𝐥𝐭𝐢-𝐲𝐞𝐚𝐫 NAND bit growth and manufacturing expansion. ➤ Partnership has collaborated on 𝐍𝐀𝐍𝐃 𝐟𝐥𝐚𝐬𝐡 innovation for more than 𝟐𝟓 years. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ Expands manufacturing capacity to meet rising 𝐀𝐈 and data storage demand. ➤ Strengthens long-term 𝐍𝐀𝐍𝐃 𝐟𝐥𝐚𝐬𝐡 supply and technology leadership. ➤ Reinforces the strategic 𝐔.𝐒.-𝐉𝐚𝐩𝐚𝐧 semiconductor manufacturing partnership. 👉 𝐄𝐱𝐩𝐞𝐫𝐭 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭: ➤ "We are pleased to begin production of our advanced 10th-generation flash memory here in Kitakami. The eighth and further generation flash memory products produced at the Fab2 will deliver new value to the rapidly growing AI market. Leveraging the partnership and scale advantages, Kioxia will continue to manufacture leading-edge flash memory products and achieve sustainable corporate growth. Kioxia will continue to contribute to the advancement of the semiconductor industry and the development of local and domestic economies." — 𝐊𝐨𝐢𝐜𝐡𝐢𝐫𝐨 𝐒𝐡𝐢𝐛𝐚𝐲𝐚𝐦𝐚, President and CEO of Kioxia Iwate Corporation. ➤ "Beginning production of our 10th-generation 3D flash memory at our Kitakami facility marks an important milestone for the two companies as demand for high-performance flash technologies continues to increase. Through our K2 facility we will continue to support our customers with the world's leading NAND technology, while providing new economic opportunities for the communities we operate in and serving as an example of strong U.S.-Japan economic relations." — 𝐀𝐥𝐩𝐞𝐫 𝐈𝐥𝐤𝐛𝐚𝐡𝐚𝐫, Chief Technology Officer of Sandisk Corporation.

@AIStockSavvy [Thu Jul 02 19:21:31 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $TSLA Tesla Caps Employee AI Spend At $200 A Week - Information

@wallstengine [Sat Jul 04 10:57:13 +0000 2026]: Analog devices $ADI is asking customers to place orders “at least six months in advance” through preferred channel partners to secure supply.

@wallstengine [Fri Jul 03 01:40:28 +0000 2026]: $MSTR -73% in one year 🩸 https://t.co/nJYIksFwN7

@KobeissiLetter [Sat Jul 04 17:56:00 +0000 2026]: BREAKING: World central banks purchased +41 tonnes of gold in May, the largest monthly addition since November 2025. This follows +17 tonnes acquired in April, and marks the 3rd monthly purchase this year. Poland led for the 2nd consecutive month at +18 tonnes, bringing its year-to-date total to +64 tonnes, with gold reserves now at a record 614 tonnes. China added +10 tonnes, the biggest monthly addition since December 2024, increasing its official gold reserves to a record 2,331 tonnes, also accounting for 9% of total FX reserves, near an all-time high. This also marks the 20th consecutive monthly purchase by the Chinese central bank. At the same time, Uzbekistan and Kazakhstan acquired +9 tonnes and +7 tonnes, respectively. Central bank demand for gold is back.

@KobeissiLetter [Sat Jul 04 16:56:00 +0000 2026]: What is happening in Hong Kong? Chinese semiconductor exports to Hong Kong rose to a record $15 billion in May. This figure has soared over +200% since early 2025. At the same time, Chinese chip exports to the world surged to a record $35 billion, tripling over the same period. As a result, Hong Kong accounted for 43% of China’s semiconductor exports in May. Over the first 5 months of 2026, China exported $239 billion of chips globally, with Hong Kong absorbing over 50% of this total, a record proportion and up from ~33% a decade ago. Hong Kong has become a dominant logistics hub for China’s chip trade.

@KobeissiLetter [Sat Jul 04 14:36:32 +0000 2026]: Japanese individual investors are buying the dip at a record pace: Retail investors purchased +$5.9 billion of Japanese equities in the week ended June 26th, the largest weekly total on record. At the same time, foreign funds sold -$7.7 billion, the largest weekly outflow since March. This follows -$6.0 billion in sales by retail in the prior 2 weeks. Stocks linked to AI and semiconductors were hit hardest last week, with SoftBank, Kioxia, and Furukawa Electric each falling at least -12% during the week. Despite the pullback, the Nikkei 225 surged +37% in Q2 2026, its best quarterly performance on record, fueled by AI-related names. Retail dip buying has become a global trend.

@gurgavin [Thu Jul 02 04:05:46 +0000 2026]: JUST IN : OPEN AI TO HANDOVER 5% OF IT’S ENTIRE COMPANY TO THE US GOVT PER FT

@AIStockSavvy [Fri Jul 03 14:33:24 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: Report Says $BABA Alibaba Bans Claude Code Over Security Concerns 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐀𝐥𝐢𝐛𝐚𝐛𝐚 reportedly banned employees from using 𝐂𝐥𝐚𝐮𝐝𝐞 𝐂𝐨𝐝𝐞 for work. ➤ Internal notice reportedly labels Claude Code as 𝐡𝐢𝐠𝐡-𝐫𝐢𝐬𝐤 software with security vulnerabilities. ➤ Workplace ban is scheduled to take effect on 𝐉𝐮𝐥𝐲 𝟏𝟎. ➤ Report cites concerns over hidden code allegedly tracking 𝐂𝐡𝐢𝐧𝐞𝐬𝐞 users. ➤ Anthropic engineer said the tracking mechanism was an 𝐞𝐱𝐩𝐞𝐫𝐢𝐦𝐞𝐧𝐭 introduced in March. ➤ Anthropic said the feature targeted 𝐚𝐜𝐜𝐨𝐮𝐧𝐭 𝐚𝐛𝐮𝐬𝐞 and model distillation concerns. ➤ The company said the tracking system would be 𝐫𝐨𝐥𝐥𝐞𝐝 𝐛𝐚𝐜𝐤. ➤ Alibaba reportedly recommended employees use its 𝐐𝐨𝐝𝐞𝐫 coding platform instead. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ Highlights growing 𝐔.𝐒.-𝐂𝐡𝐢𝐧𝐚 AI security and technology tensions. ➤ May accelerate adoption of 𝐝𝐨𝐦𝐞𝐬𝐭𝐢𝐜 AI development tools in China. ➤ Underscores increasing focus on 𝐞𝐧𝐭𝐞𝐫𝐩𝐫𝐢𝐬𝐞 AI security and data governance. 👉 𝐄𝐱𝐩𝐞𝐫𝐭 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭: ➤ "It was an experiment... designed to prevent account abuse from unauthorised resellers and protect against distillation." — 𝐓𝐡𝐚𝐫𝐢𝐪 𝐒𝐡𝐢𝐡𝐢𝐩𝐚𝐫, Anthropic Engineer. ➤ "If a US AI coding tool can detect Chinese usage or proxy access, then it's not surprising for major Chinese tech companies to not want employees using it internally." — 𝐋𝐢𝐳𝐳𝐢 𝐋𝐞𝐞, Fellow at the Asia Society Policy Institute's Centre for China Analysis.

@AIStockSavvy [Thu Jul 02 23:58:18 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: Data center startup Crusoe in talks to raise $3 bln; valuation could double to $30 bln - $META $ORCL Crusoe, a data-center startup supplying AI compute to Meta Platforms and Oracle, is in talks to raise roughly $3 bln, people familiar with the matter said, a deal that could roughly double its valuation to about $30 bln. The company is still negotiating the round and no final valuation has been set; investors expect a post-money valuation near $30 bln including the new capital. Crusoe was valued at about $10 bln in October last year.

@AIStockSavvy [Thu Jul 02 19:52:37 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $PLTR Palantir CEO said some U.S. government clients have shifted to open-source AI. - The Information

@AIStockSavvy [Thu Jul 02 19:09:25 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $META Meta CEO Mark Zuckerberg Says In Internal Town Hall That Ai Agent Development Over The Last Four Months Hasn't 'accelerated In The Way We Expected' - Reuters

@KobeissiLetter [Sat Jul 04 15:37:00 +0000 2026]: Full-time jobs in the US are falling at a concerning rate: Full-time employment dropped -514,000 in June, to 133.66 million, the lowest since December 2024. This marks the 3rd consecutive monthly decline, totaling -1.01 million. Since January 2025, full-time employment has now fallen -2.24 million This also brings full-time employment back to levels seen in Q1 2023. Meanwhile, the full-time employment-to-population ratio, which measures the proportion of the population working full-time, is down to 48.5%, from 50.5% in 2022, the lowest since mid-2021. The weakness in the US labor market is accelerating.

@AIStockSavvy [Fri Jul 03 14:28:57 +0000 2026]: 🏆 TOP 10 WEEKLY ANALYST RATINGS: $MU $FCEL $INTC $BE $ALAB $SNDK $AMAT $ABSI $MRVL $HIMS https://t.co/Icw8ePDvvr

@AIStockSavvy [Thu Jul 02 20:20:17 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Jane Street Group Discloses Passive Stake of 5% in $HTZ Hertz Global as of June 26 - Filing

@AIStockSavvy [Thu Jul 02 17:40:09 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $MSFT Microsoft is planning to merge its consumer and enterprise Copilot chatbots in August - The Information

@StockMKTNewz [Fri Jul 03 21:11:36 +0000 2026]: This is what my actual portfolio looks like when you combine all my investments What do you think? https://t.co/CnWRPhdKiA

@KobeissiLetter [Sat Jul 04 01:48:39 +0000 2026]: What is happening with the US construction sector? The hiring rate in US construction fell -0.3 percentage points in May, to 3.5%, the lowest since data began in 2000. Since January, this figure has declined -1.1 percentage points, extending its 4-year downtrend. By comparison, the 2008 Financial Crisis and 2020 pandemic lows were 4.5% and 3.7%, respectively. This comes as 295,000 new workers were hired in the construction sector in May, the 3rd-lowest monthly total since the 2020 pandemic. Excluding 2020, this is the 3rd-lowest reading in 10 years. US construction hiring is historically weak.

@StockMKTNewz [Sun Jul 05 11:31:00 +0000 2026]: Stock market bear Michael Burry said he thinks the end of what he says is a "AI bubble" is getting close "The end is nigh. Dancing with the devil in the pale moon light."

@wallstengine [Sat Jul 04 11:26:16 +0000 2026]: U.S. tech postings hit 575,000 in April, a 3-year high, while listings requiring AI skills more than doubled YoY. https://t.co/HCqULeeRMU

@wallstengine [Sat Jul 04 01:18:18 +0000 2026]: Trump says the U.S. Treasury will accept philanthropic contributions of readily tradable publicly traded stock to help fund Trump Accounts for eligible American children. https://t.co/QZC0IepZiq

@wallstengine [Fri Jul 03 19:15:22 +0000 2026]: Trump’s outgoing AI adviser Sriram Krishnan told FT the administration will not create a formal AI licensing regime. “There will not be an FDA for AI,” he said. Krishnan said requiring companies to go through lawyers before releasing a model would put “sand in the gears” of AI development and is “never, never going to happen under President Trump.” He also blamed part of the AI backlash on the industry’s own messaging, saying AI companies focused too much on dystopian risks and “have done a terrible job” explaining real benefits like medical diagnosis.

@gurgavin [Sat Jul 04 18:37:40 +0000 2026]: HAPPY INDEPENDENCE DAY TO MY AMERICAN FOLLOWERS 🇺🇸🇺🇸🇺🇸🇺🇸 “IT’S NEVER PAID TO BET AGAINST AMERICA. WE COME THROUGH THINGS, BUT IT’S NOT ALWAYS A SMOOTH RIDE. NEVER BET AGAINST AMERICA.” - WARREN BUFFETT -

@wallstengine [Fri Jul 03 11:29:22 +0000 2026]: 👀 https://t.co/wsNfoQ7t2B

@gurgavin [Thu Jul 02 20:30:28 +0000 2026]: *DOW JONES HIT A NEW ALL TIME HIGH

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.