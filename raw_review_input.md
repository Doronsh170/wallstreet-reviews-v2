אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are a senior Wall Street market analyst writing a PRE-MARKET briefing in Hebrew.
Script run date: 2026-07-06 (יום שני). Briefing target date: 2026-07-06 (יום שני).
The briefing is for TODAY. The US cash market has NOT opened yet — never describe it as open, trading, or having reacted. Use 'השוק צפוי להיפתח', 'המשקיעים יעקבו אחר'. Futures may be described in present tense; the cash market may not.

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
  $AMZN: $242.67 (daily: +0.40%), prev close: $241.70
  $MU: $975.56 (daily: -5.49%), prev close: $1032.28
  $INTC: $120.35 (daily: -5.25%), prev close: $127.02
  $SNDK: $1745.00 (daily: -14.13%), prev close: $2032.22
  $MSFT: $390.49 (daily: +1.62%), prev close: $384.28
  $GOOGL: $359.91 (daily: -0.36%), prev close: $361.21
  $ORCL: $140.27 (daily: -1.56%), prev close: $142.50
  $NVDA: $194.83 (daily: -1.39%), prev close: $197.58
  $DDOG: $260.36 (daily: -1.56%), prev close: $264.48
  $AMD: $517.82 (daily: -4.26%), prev close: $540.88
  $AMAT: $603.04 (daily: -7.35%), prev close: $650.91

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
Use web search to find what US economic data is scheduled for release on 2026-07-06.
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

Source tweets/posts from X (Twitter) — gathered 2026-07-06. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Sun Jul 05 00:21:40 +0000 2026]: The AI infrastructure buildout is entering a new phase: US tech companies are committing to spend a record $850 billion on data center leases over the next several years. This marks a +$570 billion YoY increase, or +204%, and +$200 billion QoQ increase, or +31%. Meta, $META, added the most in Q1 2026, committing +$79 billion in new leases, a +76% QoQ increase, bringing its total to ~$183 billion. At the same time, Microsoft, $MSFT, added +$41 billion, a +26% QoQ increase, bringing its total to ~$197 billion. Oracle leads with the largest total commitments at ~$250 billion, having already secured many of the key sites needed to fulfill its contract with OpenAI. Tech companies are doubling down on AI.

@gurgavin [Thu Jul 02 19:10:49 +0000 2026]: TESLA CAPS EMPLOYEE AI SPEND AT $200 PER WEEK PER THE INFORMATION $TSLA

@KobeissiLetter [Sun Jul 05 14:33:00 +0000 2026]: The AI spending boom is redefining the US economy: AI CapEx across Alphabet, $GOOGL, Amazon, $AMZN, Meta, $META, Microsoft, $MSFT, and Oracle, $ORCL, is projected to rise to ~3.2% of US GDP in 2027. If that materializes, annual CapEx will surpass national defense spending for the first time in history, which is projected at ~2.7% of GDP next year. For this year alone, AI CapEx is set to increase to ~2.5% of GDP, from 1.5% in 2025, close to the estimated defense spending of ~2.7%. This comes as AI CapEx of these 5 companies is projected to surpass $800 billion in 2026. Subsequently, in 2027, this is expected to rise further, to a record $1.1 trillion. Truly mind-blowing numbers.

@gurgavin [Wed Jul 01 18:02:23 +0000 2026]: SPACEX HAS BEEN SHOWING OFF A PROTOTYPE OF A NEW “AI DEVICE” WHICH IS SIMILAR THAN AS IPHONE PER WSJ THE DEVICE RUNS ON CUSTOM SOFTWARE AND USED XAI’S TECH $SPCX

@KobeissiLetter [Sun Jul 05 13:32:15 +0000 2026]: Key Events This Week: 1. June S&P Global Services PMI data - Monday 2. ADP Employment Change data - Tuesday 3. Fed Meeting Minutes - Wednesday 4. Initial Jobless Claims data - Thursday 5. June Existing Home Sales data - Thursday 6. IEA Monthly Report - Friday We are one week out from earnings season.

@wallstengine [Mon Jul 06 08:24:32 +0000 2026]: Bernstein SocGen Group Downgrades $DDOG to Market Perform from Outperform, Raises PT to $226 from $180 Analyst comments: "Our model post-Q1 implied future “Born-in-AI” growth, outside their largest customer, after this year would slow to effectively ~40% YoY growth. But with the newest AI Lab customers added in Q4 and Q1, this seems much too low. While there probably isn’t a 1:1 relationship with AI Lab revenue and Datadog, for example, pricing increases drive AI Labs while Datadog tends to discount more with scale, we anticipate price is at most ~half the labs’ growth. Based on the labs’ expectation of 100%+ revenue CAGR over the next few years, we raise Datadog’s participation. We will need to refine this over time as we learn more, but this feels like a fairer expectation. Downgrade on Q3+ earnings caution versus more exuberant investor expectations: demand signals are slowing in both enterprise and some AI Labs. Not only do we start lapping tough comps in Q4, but as we’ve discussed in several other notes, we are seeing demand signals flatlining ex-AI (~85% of revenue), which causes ex-AI growth to peak in Q3 and potentially regress 100-200bps in Q4. We also re-highlight signals that AI Labs are seeing growth plateau — our QoQ into Q3 “Born-in-AI” expectations are low relative to recent growth trends. Altogether, Q4 could see a 500bps growth rate regression, falling to ~29% YoY. This would be a disappointment versus recent investor conversations, where some expect high-30% to 40%+ peak growth and 30%+ growth into next year." Analyst: Peter Weed

@gurgavin [Thu Jul 02 18:04:16 +0000 2026]: AN AUTOGRAPHED JACKET OF NVIDIA CEO JENSEN HUANG IS UP FOR AUCTION ON SOTHEBYS IT'S SIGNED BY HIM AND HE ACTUALLY WORE THIS EXACT JACKET IN THE PAST IT'S ESTIMATED TO SELL FOR $40,000–$60,000 $NVDA https://t.co/jedGiznXYO

@gurgavin [Fri Jul 03 21:26:04 +0000 2026]: IMAGINE SHORTING MICRON WHEN TRUMP IS TRYNA PUMP IT EVERY SINGLE DAY $MU

@wallstengine [Sat Jul 04 11:35:41 +0000 2026]: Intel $INTC reportedly fixed 18A wafer-to-wafer yield variability, with Oregon + Arizona output reaching ~30K wafers/month, per BlueFin. https://t.co/1GyQwUsEbU

@KobeissiLetter [Sun Jul 05 22:07:05 +0000 2026]: BREAKING: Nasdaq 100 futures surge over +1% as markets reopen after the Fourth of July weekend. https://t.co/SR4uYkiBLZ

@KobeissiLetter [Sat Jul 04 22:10:50 +0000 2026]: BREAKING: The US goods trade deficit widened by -$22.8 billion, or -27%, in May, to -$105.8 billion, the largest since March 2025. This marks the largest monthly increase since November 2025. US goods exports fell -$11.8 billion, or -5%, to $207.7 billion, the lowest since February, driven by a sharp decline in industrial supplies, particularly energy shipments. Meanwhile, imports rose +$10.9 billion, or +4%, to $313.4 billion, the highest since March 2025. The increase was driven by continued imports of data center equipment, including computers, semiconductors, and telecom equipment. The trade deficit is widening again.

@AIStockSavvy [Sun Jul 05 18:35:33 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: $MU Micron Breaks Ground on ¥1.5 Trillion($9.3 billion) AI Memory Chip Expansion in Japan 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐌𝐢𝐜𝐫𝐨𝐧 began construction on a ¥𝟏.𝟓 𝐭𝐫𝐢𝐥𝐥𝐢𝐨𝐧 AI memory chip expansion in Hiroshima. ➤ The new facility will produce 𝐡𝐢𝐠𝐡-𝐛𝐚𝐧𝐝𝐰𝐢𝐝𝐭𝐡 𝐦𝐞𝐦𝐨𝐫𝐲 (HBM) for AI processors. ➤ HBM shipments are expected to begin around 𝐬𝐮𝐦𝐦𝐞𝐫 𝟐𝟎𝟐𝟖. ➤ Japan's government will provide up to ¥𝟓𝟎𝟎 𝐛𝐢𝐥𝐥𝐢𝐨𝐧 toward the project cost. ➤ Total Japanese support for Micron has reached about ¥𝟕𝟕𝟓 𝐛𝐢𝐥𝐥𝐢𝐨𝐧, including R&D funding. ➤ The expansion aims to improve 𝐩𝐨𝐰𝐞𝐫 𝐞𝐟𝐟𝐢𝐜𝐢𝐞𝐧𝐜𝐲 and data transmission for AI memory. ➤ Micron said about 𝟖𝟎% of materials used at the Hiroshima facility are sourced from Japan. ➤ The project expands Micron's global AI memory manufacturing alongside new U.S. fabs. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ Rising 𝐀𝐈 demand is driving massive global investment in advanced memory production. ➤ The expansion strengthens Micron's position in the competitive 𝐇𝐁𝐌 market. ➤ Japan continues investing heavily to rebuild its 𝐬𝐞𝐦𝐢𝐜𝐨𝐧𝐝𝐮𝐜𝐭𝐨𝐫 manufacturing ecosystem. 👉 𝐄𝐱𝐩𝐞𝐫𝐭 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭: ➤ "Micron's very first HBM production wafer — for the memory technology at the heart of AI — was made right here in Hiroshima. When American boldness meets Japanese craftsmanship, you do not get a compromise. You get the best in the world." — 𝐒𝐚𝐧𝐣𝐚𝐲 𝐌𝐞𝐡𝐫𝐨𝐭𝐫𝐚, CEO of Micron Technology. ➤ "Japan's support for Micron, now the only maker of DRAM within the country's borders, has invaluable worth." — 𝐑𝐲𝐨𝐬𝐞𝐢 𝐀𝐤𝐚𝐳𝐚𝐰𝐚, Japan's Minister of Economy, Trade and Industry. ➤ "The Hiroshima factory's strength lies in its ability to quickly deliver cutting-edge and high-performance products to customers. Creating next-generation chips here is directly tied to Micron's strategy." — 𝐊𝐨𝐭𝐚 𝐍𝐨𝐬𝐚𝐤𝐚, Representative Director of Micron Japan.

@AIStockSavvy [Fri Jul 03 14:48:48 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: $META Meta Is Reportedly Considering a Partnership With Samsung to Produce a ₩100 Trillion Custom AI Chip. - $GOOGL $AVGO $NVDA $AMD $INTC Meta is considering a collaboration with Samsung Electronics to produce a custom artificial intelligence chip worth about 100 trillion South Korean won. If the collaboration is successful, it will become one of Samsung's important AI orders for its semiconductor foundry business. The two parties have not officially announced the collaboration yet.

@AIStockSavvy [Fri Jul 03 14:17:57 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: Kioxia, $SNDK Sandisk Begin Production of 10th-Gen 3D NAND Flash at K2 Fab 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐊𝐢𝐨𝐱𝐢𝐚 and 𝐒𝐚𝐧𝐝𝐢𝐬𝐤 began production of 𝐭𝐡-𝐠𝐞𝐧 𝟑𝐃 𝐍𝐀𝐍𝐃 at Japan's K2 Fab. ➤ K2 previously produced 𝐞𝐢𝐠𝐡𝐭𝐡-𝐠𝐞𝐧 𝟑𝐃 𝐍𝐀𝐍𝐃 and will now scale 10th-gen output. ➤ Both generations use 𝐂𝐁𝐀 technology for higher performance, capacity, and lower power. ➤ K2 features 𝐞𝐚𝐫𝐭𝐡𝐪𝐮𝐚𝐤𝐞-𝐫𝐞𝐬𝐢𝐬𝐭𝐚𝐧𝐭 design, AI-driven production, and energy-efficient equipment. ➤ Companies extended their 𝐣𝐨𝐢𝐧𝐭 𝐯𝐞𝐧𝐭𝐮𝐫𝐞 through 𝐃𝐞𝐜𝐞𝐦𝐛𝐞𝐫 𝟐𝟎𝟑𝟒. ➤ Continued investments aim to support 𝐦𝐮𝐥𝐭𝐢-𝐲𝐞𝐚𝐫 NAND bit growth and manufacturing expansion. ➤ Partnership has collaborated on 𝐍𝐀𝐍𝐃 𝐟𝐥𝐚𝐬𝐡 innovation for more than 𝟐𝟓 years. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ Expands manufacturing capacity to meet rising 𝐀𝐈 and data storage demand. ➤ Strengthens long-term 𝐍𝐀𝐍𝐃 𝐟𝐥𝐚𝐬𝐡 supply and technology leadership. ➤ Reinforces the strategic 𝐔.𝐒.-𝐉𝐚𝐩𝐚𝐧 semiconductor manufacturing partnership. 👉 𝐄𝐱𝐩𝐞𝐫𝐭 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭: ➤ "We are pleased to begin production of our advanced 10th-generation flash memory here in Kitakami. The eighth and further generation flash memory products produced at the Fab2 will deliver new value to the rapidly growing AI market. Leveraging the partnership and scale advantages, Kioxia will continue to manufacture leading-edge flash memory products and achieve sustainable corporate growth. Kioxia will continue to contribute to the advancement of the semiconductor industry and the development of local and domestic economies." — 𝐊𝐨𝐢𝐜𝐡𝐢𝐫𝐨 𝐒𝐡𝐢𝐛𝐚𝐲𝐚𝐦𝐚, President and CEO of Kioxia Iwate Corporation. ➤ "Beginning production of our 10th-generation 3D flash memory at our Kitakami facility marks an important milestone for the two companies as demand for high-performance flash technologies continues to increase. Through our K2 facility we will continue to support our customers with the world's leading NAND technology, while providing new economic opportunities for the communities we operate in and serving as an example of strong U.S.-Japan economic relations." — 𝐀𝐥𝐩𝐞𝐫 𝐈𝐥𝐤𝐛𝐚𝐡𝐚𝐫, Chief Technology Officer of Sandisk Corporation.

@wallstengine [Mon Jul 06 08:31:43 +0000 2026]: Raymond James Downgrades $JBLU to Underperform from Market Perform Analyst comments: "We believe Frontier and JetBlue are the biggest beneficiaries of Spirit's recent demise, with Frontier positioned to realize the greater near-term benefit through stronger fares and margin expansion, while JetBlue has the opportunity to create a more valuable long-term strategic asset, as discussed in our mid-May Airline Strategy Call. Although we see limited upside in both JBLU and ULCC following the recent rally, JetBlue shares are further constrained by the ~$6.12 conversion price of its convertible debt. Moreover, while we do not anticipate any liquidity concerns at JetBlue in 2026, assuming no further macro shocks, we believe the more prudent course of action, unattractive for current equity holders, would be to address the capital structure via a Chapter 11 restructuring, particularly given the compelling actions taken by management over the last few years, including the recent build-out of Ft. Lauderdale (FLL) as a first true hub. Thus, we are downgrading JBLU from Market Perform to Underperform." Analyst: Savanthi Syth

@StockMKTNewz [Sun Jul 05 20:04:13 +0000 2026]: Citi just released this list of its most and least preferred tech & communication stocks for the rest of 2026 Most Preferred tickers $AMZN $GOOGL $SNDK $AMD $MSFT $EQIX $SBAC $AMT $DASH $LITE $CIEN $APP $TTWO $NXST $TXN $AMAT $MDB $SNOW $BOX $NAVN $APPN $DDOG $RBRK Least Preferred Tickers: $OPTU $UNTI $CCOI $HPQ $XRX $AMC $SIRI $QRVO $SWKS $OLED $GTM $ADBE $CXM $OTEX $DBX $PAYC $RPB $FSLY (Source @SeekingAlpha)

@KobeissiLetter [Sun Jul 05 17:16:00 +0000 2026]: Retail risk appetite is at record levels: 0DTE options contracts now account for a record 48% of total retail options volume. This percentage has more than TRIPLED over the last 5 years. Furthermore, 0DTE options reflected a record 30% of total US options volume in May. By comparison, the 2022 high was ~18% while the average over the last 5 years is ~21%. As a result, the average options contract now expires in under 3 days. Retail demand for short-term options has never been higher.

@gurgavin [Thu Jul 02 04:05:46 +0000 2026]: JUST IN : OPEN AI TO HANDOVER 5% OF IT’S ENTIRE COMPANY TO THE US GOVT PER FT

@StockMKTNewz [Sun Jul 05 18:19:51 +0000 2026]: Minions &amp; Monsters, the 7th film in the animated franchise was the highest-grossing movie over the July 4th holiday weekend The movie brought in $61.4 million in US and Canadian box office sales - Bloomberg The franchise is owned by Comcast's $CMCSA Universal Pictures https://t.co/4N5ibc1KKf

@StockMKTNewz [Sun Jul 05 17:52:31 +0000 2026]: Happy 32nd Birthday to Amazon $AMZN

@AIStockSavvy [Fri Jul 03 14:33:24 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: Report Says $BABA Alibaba Bans Claude Code Over Security Concerns 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐀𝐥𝐢𝐛𝐚𝐛𝐚 reportedly banned employees from using 𝐂𝐥𝐚𝐮𝐝𝐞 𝐂𝐨𝐝𝐞 for work. ➤ Internal notice reportedly labels Claude Code as 𝐡𝐢𝐠𝐡-𝐫𝐢𝐬𝐤 software with security vulnerabilities. ➤ Workplace ban is scheduled to take effect on 𝐉𝐮𝐥𝐲 𝟏𝟎. ➤ Report cites concerns over hidden code allegedly tracking 𝐂𝐡𝐢𝐧𝐞𝐬𝐞 users. ➤ Anthropic engineer said the tracking mechanism was an 𝐞𝐱𝐩𝐞𝐫𝐢𝐦𝐞𝐧𝐭 introduced in March. ➤ Anthropic said the feature targeted 𝐚𝐜𝐜𝐨𝐮𝐧𝐭 𝐚𝐛𝐮𝐬𝐞 and model distillation concerns. ➤ The company said the tracking system would be 𝐫𝐨𝐥𝐥𝐞𝐝 𝐛𝐚𝐜𝐤. ➤ Alibaba reportedly recommended employees use its 𝐐𝐨𝐝𝐞𝐫 coding platform instead. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ Highlights growing 𝐔.𝐒.-𝐂𝐡𝐢𝐧𝐚 AI security and technology tensions. ➤ May accelerate adoption of 𝐝𝐨𝐦𝐞𝐬𝐭𝐢𝐜 AI development tools in China. ➤ Underscores increasing focus on 𝐞𝐧𝐭𝐞𝐫𝐩𝐫𝐢𝐬𝐞 AI security and data governance. 👉 𝐄𝐱𝐩𝐞𝐫𝐭 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭: ➤ "It was an experiment... designed to prevent account abuse from unauthorised resellers and protect against distillation." — 𝐓𝐡𝐚𝐫𝐢𝐪 𝐒𝐡𝐢𝐡𝐢𝐩𝐚𝐫, Anthropic Engineer. ➤ "If a US AI coding tool can detect Chinese usage or proxy access, then it's not surprising for major Chinese tech companies to not want employees using it internally." — 𝐋𝐢𝐳𝐳𝐢 𝐋𝐞𝐞, Fellow at the Asia Society Policy Institute's Centre for China Analysis.

@AIStockSavvy [Thu Jul 02 23:58:18 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: Data center startup Crusoe in talks to raise $3 bln; valuation could double to $30 bln - $META $ORCL Crusoe, a data-center startup supplying AI compute to Meta Platforms and Oracle, is in talks to raise roughly $3 bln, people familiar with the matter said, a deal that could roughly double its valuation to about $30 bln. The company is still negotiating the round and no final valuation has been set; investors expect a post-money valuation near $30 bln including the new capital. Crusoe was valued at about $10 bln in October last year.

@wallstengine [Mon Jul 06 10:05:53 +0000 2026]: $ATAI says AtaiBeckley dosed the last patient in its Phase 2b Elumina trial of VLS-01 for treatment-resistant depression. Topline data expected in Q4 2026. Trial details: 156 patients Randomized 1:1 vs placebo Primary endpoint: MADRS change at Day 29 VLS-01 is an oral transmucosal DMT formulation If Phase 2b data are supportive, AtaiBeckley plans to move VLS-01 into Phase 3 for major depressive disorder, with generalized anxiety disorder as a potential follow-on indication.

@wallstengine [Mon Jul 06 09:49:49 +0000 2026]: B. Riley says $AMZN’s RNG and OpenAI’s MRC are becoming “structural headwinds for transceiver TAM.” The firm says the 2025 optical bull case assumed AI clusters would keep moving to deeper 3-tier and 4-tier networks, driving more transceivers per unit of compute. Now, B. Riley says that thesis is hitting a “structural wall” as hyperscalers move toward network flattening. Key impact: > MRC helps training clusters bypass physical network bottlenecks > RNG helps $AMZN flatten scale-out inference, data ingestion, and RAG networks > RNG replaces active aggregation switches with passive optical ShuffleBoxes > Active networking equipment could fall by over 60% > Structural transceiver counts could fall 40% to 50% B. Riley says $AAOI is especially exposed because $AMZN and $ORCL are expected anchor customers for the 800G/1.6T transceivers driving its growth outlook.

@wallstengine [Mon Jul 06 09:13:14 +0000 2026]: Jefferies says the absence of $NVDA Kyber/backplane PCB in 2027 is becoming “highly likely,” meaning Rubin Ultra would stick with the Oberon/NVL72 structure. Estimated impact vs prior forecasts: AI PCB TAM: $25B → $24B in 2027, $41B → $36B in 2028 AI CCL TAM: $12B → $11B in 2027, $21B → $17B in 2028 Negative for the PCB/CCL supply chain, but Jefferies says upstream materials may still outperform on price hikes, while the delay is positive for copper cable makers.

@KobeissiLetter [Sun Jul 05 20:47:00 +0000 2026]: The US stock market has never been more dominant: US stock market capitalization is up to a record ~$81 trillion, now accounting for ~48% of global market cap. This exceeds the world's 2nd largest stock market, China, at $17 trillion, by 375%. The US stock market is now twice as large as that of China, Japan, Hong Kong, and Taiwan combined. It is also larger than the next 18 stock markets combined. The Magnificent 7 stocks alone are now larger than China's market value. The current scale of the US stock market is unprecedented.

@KobeissiLetter [Sun Jul 05 19:37:00 +0000 2026]: BREAKING: US technology funds attracted +$14.3 billion in inflows in the week ending July 1st, the 2nd biggest weekly inflow on record. This follows -$9.3 billion in outflows the prior week and a record +$19.2 billion in inflows two weeks earlier. This brings the 4-week average of weekly inflows to a record +$9.0 billion. Tech funds are now on pace to attract +$152 billion in inflows in 2026, an all-time high. Meanwhile, US equity funds recorded -$17.2 billion in outflows in the week ending July 1st, the largest weekly withdrawal since March. Investors are aggressively rotating into technology.

@AIStockSavvy [Mon Jul 06 03:05:55 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $LMT Lockheed Martin Leading Race for $3.5 Billion Purchase of Naval Defense Firm Ultra Maritime - CNBC

@AIStockSavvy [Mon Jul 06 02:42:31 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $INTC Intel confirms price hikes on select consumer and server CPUs citing supply costs and demand — select Xeon processors now over $1,000 more expensive - Tom's Hardware

@AIStockSavvy [Mon Jul 06 00:05:58 +0000 2026]: 📊 Overnight Movers $SNDK $MU $IREN $MSTR $BMNR $WDC $CRCL $NBIS $CLSK $ALAB $MRVL $ARM $CRWV https://t.co/eIGsx8jphJ

@AIStockSavvy [Fri Jul 03 14:28:57 +0000 2026]: 🏆 TOP 10 WEEKLY ANALYST RATINGS: $MU $FCEL $INTC $BE $ALAB $SNDK $AMAT $ABSI $MRVL $HIMS https://t.co/Icw8ePDvvr

@AIStockSavvy [Thu Jul 02 20:20:17 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Jane Street Group Discloses Passive Stake of 5% in $HTZ Hertz Global as of June 26 - Filing

@StockMKTNewz [Sun Jul 05 22:13:19 +0000 2026]: Stock futures are back … we’re getting closer to the market being open again 🟢🟢🟢🟢 https://t.co/hD8qqQuVkI

@StockMKTNewz [Sun Jul 05 19:16:19 +0000 2026]: Nvidia and Apple supplier Foxconn just announced a 40% jump in quarterly sales More than 50% of Foxconn's revenue came from Cloud and Networking ... ~3 years ago it was 25% of their business - Bloomberg https://t.co/fTiC2ah3Us

@KobeissiLetter [Sun Jul 05 15:51:00 +0000 2026]: Shocking stat of the day: The US labor force participation rate among 25 to 54-year-olds dropped -0.6 percentage points in June, the 2nd-largest monthly decline on record in data going back to the 1940s. This metric measures the proportion of Americans in prime age either working or actively looking for work. The decline matches those seen in January 1968, March 1960, May 1953, October 1952, and June 1951. The only larger monthly drop was recorded in April 2020, during the pandemic, when nearly the entire economy shut down. As a result, the prime-age labor force participation rate fell to 83.3%, the lowest since December 2023. Meanwhile, the total labor force participation rate has declined for 7 consecutive months, to 61.5%, the lowest since February 2021. The US job market is rapidly deteriorating under the surface.

@StockMKTNewz [Sun Jul 05 23:08:22 +0000 2026]: Hyundai's Boston Dynamics humanoid robot unit showed off one of its robots at the 2026 FIFA World Cup https://t.co/3gzWE9JlA3

@wallstengine [Sat Jul 04 11:26:16 +0000 2026]: U.S. tech postings hit 575,000 in April, a 3-year high, while listings requiring AI skills more than doubled YoY. https://t.co/HCqULeeRMU

@KobeissiLetter [Sun Jul 05 18:30:00 +0000 2026]: The Kobeissi Letter for the week of July 6th has been published and may be viewed through the link below: https://t.co/9c65UCffkW The Chart of the Week for the week of July 6th has been published. View or sign up for FREE through the link below: https://t.co/lFT7Stiwzt

@gurgavin [Sat Jul 04 18:37:40 +0000 2026]: HAPPY INDEPENDENCE DAY TO MY AMERICAN FOLLOWERS 🇺🇸🇺🇸🇺🇸🇺🇸 “IT’S NEVER PAID TO BET AGAINST AMERICA. WE COME THROUGH THINGS, BUT IT’S NOT ALWAYS A SMOOTH RIDE. NEVER BET AGAINST AMERICA.” - WARREN BUFFETT -

@StockMKTNewz [Sun Jul 05 17:00:38 +0000 2026]: Watch out for this Allen &amp; Company Sun Valley conference this week All of these major CEOs will be there: Mark Zuckerberg Jeff Bezos Tim Cook Sundar Pichai Sam Altman and more https://t.co/YWR1pvUpjI

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.