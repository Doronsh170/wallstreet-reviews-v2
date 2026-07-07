אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are a senior Wall Street investment advisor writing your signature WEEKLY review in Hebrew for the
trading week 29/06–03/07/2026. The review does BOTH: sums up the week that ended AND prepares the reader for
the coming week. PAST TENSE for the summary points. ONLY events and moves from THIS specific week in the
summary points. Use the WEEKLY PERFORMANCE numbers for weekly index changes — NOT the daily numbers, and
never confuse Friday's daily change with the weekly change.

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

6-9 points TOTAL in three blocks, in this order:
* OPENING point — "השבוע שהיה: ..." — 3-5 sentences telling the ARC of the week as one story: how it opened,
  what flipped the sentiment, how it closed, with the weekly index numbers woven into the narrative.
* SUMMARY points (3-5) — ONE thematic point per major story of the week, each with its own specific headline.
  Pick the STRONGEST stories — do NOT force every category:
  - Fed policy signals and rate expectations, with the probabilities when they appear in the sources.
  - The week's key macro data with FULL numbers (actual vs forecast vs previous) and the market implication —
    merge related releases into one point.
  - The week's defining sector/technology story, with the transmission mechanism.
  - Notable company news: earnings, M&A, milestones — merged where related.
  - Commodities and the dollar with weekly context, or geopolitics with market impact.
* PREPARATION points (1-2) — the COMING week (verify the schedule via web search):
  - "השבוע הקרוב במאקרו: ..." — the scheduled releases and Fed events with dates, Israel times and consensus.
  - "דוחות בשבוע הקרוב: ..." — the key earnings reports scheduled and what the market will look for in them
    (merge into the macro point when the earnings slate is thin).
* CLOSING point — "בשורה התחתונה: ..." — 2-4 sentences of synthesis: what the week taught us, the fragilities
  and the opportunities, and the frame for the coming week. Seasonal/historical context is welcome when verified.

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
  "title": "סיכום שבועי והכנה לשבוע הבא בוול סטריט 🇺🇸 – 29/06–03/07/2026",
  "date": "2026-07-03",
  "sections": [
    {
      "heading": "סיכום השבוע",
      "content": "* כותרת קצרה וספציפית: שניים עד ארבעה משפטים של פרוזה אנליטית עם המספרים המרכזיים, ההקשר והמשמעות.\n* כותרת נוספת: ..."
    }
  ]
}
- EXACTLY 1 section. Heading EXACTLY "סיכום השבוע". Title EXACTLY as given above.
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
  $USO: $108.92 (daily: +4.38%), prev close: $104.35
  $SPCX: $149.47 (daily: -6.83%), prev close: $160.42
  $QQQ: $709.43 (daily: -1.85%), prev close: $722.82
  $SPY: $747.71 (daily: -0.48%), prev close: $751.28
  $PENG: $62.71 (daily: -7.38%), prev close: $67.71
  $NVDA: $196.93 (daily: +0.71%), prev close: $195.55
  $GOOGL: $367.03 (daily: +0.16%), prev close: $366.46
  $TSLA: $402.90 (daily: -4.02%), prev close: $419.77
  $MU: $938.38 (daily: -4.71%), prev close: $984.75
  $MSFT: $388.84 (daily: +0.54%), prev close: $386.74
  $FIGR: $31.05 (daily: -9.78%), prev close: $34.41

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

══ MANDATORY MACRO DATA CHECK ══
Use web search to find ALL major US economic data released during the week of 29/06–03/07/2026:
CPI (headline+core, monthly+annual), PPI, NFP/employment, Jobless Claims, Consumer Sentiment,
ISM PMI, FOMC, GDP, Retail Sales. For EVERY data point: actual, forecast, previous, market implication.
Do NOT skip Core CPI if headline CPI was released. Do NOT write 'expected' about data already released.
IN ADDITION — for the preparation points, use web search to verify the COMING week's schedule:
economic releases and Fed events (with dates, Israel times and consensus where available) and the key
earnings reports scheduled, and what the market will look for in each.
══════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-08. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Tue Jul 07 12:13:16 +0000 2026]: BREAKING: SpaceX, $SPCX, is being added to the Nasdaq 100 today. This marks the fastest inclusion into the Nasdaq 100 in the index’s history.

@gurgavin [Thu Jul 02 19:10:49 +0000 2026]: TESLA CAPS EMPLOYEE AI SPEND AT $200 PER WEEK PER THE INFORMATION $TSLA

@wallstengine [Tue Jul 07 20:10:53 +0000 2026]: $PENG | Penguin Solutions Q3 FY26 Earnings Highlights 🔷 Revenue: $478.7M vs $421.4M Est. 🟢 🔷 Adj EPS: $0.84 vs $0.56 Est. 🟢 🔷 Record quarterly net sales, up 48% YoY. FY26 Outlook Raised: 🔷 Non-GAAP EPS: $2.60 ±$0.05 vs $2.28 Est. 🟢 🔷 Net sales growth now seen at 22% ±2%, up from 12% ±5% 🔷 Non-GAAP gross margin: 28.5% ±0.5% Segment Revenue: 🔷 Advanced Computing: $137.6M, up 4% YoY 🔷 Integrated Memory: $275.1M, up 111% YoY 🔷 Optimized LED: $66.1M, up 7% YoY Business Highlights: 🔷 Integrated Memory net sales more than doubled YoY 🔷 AI Infrastructure added 4 new customer logos in Q3 🔷 Became an NVIDIA AI Factory Specialized Partner 🔷 Expanded ClusterWareAI with an AI Factory Operations Agent

@gurgavin [Mon Jul 06 19:52:14 +0000 2026]: SPACEX WILL BE ADDED TO THE NASDAQ 100 INDEX TOMORROW THIS IS THE QUICKEST TIME EVER FOR A COMPANY TO BE ADDED TO THE NASDAQ 100 INDEX $SPCX

@gurgavin [Thu Jul 02 18:04:16 +0000 2026]: AN AUTOGRAPHED JACKET OF NVIDIA CEO JENSEN HUANG IS UP FOR AUCTION ON SOTHEBYS IT'S SIGNED BY HIM AND HE ACTUALLY WORE THIS EXACT JACKET IN THE PAST IT'S ESTIMATED TO SELL FOR $40,000–$60,000 $NVDA https://t.co/jedGiznXYO

@gurgavin [Fri Jul 03 21:26:04 +0000 2026]: IMAGINE SHORTING MICRON WHEN TRUMP IS TRYNA PUMP IT EVERY SINGLE DAY $MU

@StockMKTNewz [Tue Jul 07 16:40:21 +0000 2026]: The first NASDAQ 100 ETF not by Invesco is about to launch Blackrock will be launching its Nasdaq 100 ETF $IQQ this week after getting the license from Nasdaq IMO this matters for you for just 1 reason Expect the fees on ETFs tracking the Nasdaq 100 to drop ... closer to S&P 500 ETF levels?? 👀

@StockMKTNewz [Tue Jul 07 16:09:58 +0000 2026]: ChatGPT just sold some of its Google $GOOGL shares in the Rallies AI Arena

@AIStockSavvy [Tue Jul 07 19:06:43 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Perplexity Adopts $NVDA NVIDIA Vera CPUs for AI Infrastructure 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐏𝐞𝐫𝐩𝐥𝐞𝐱𝐢𝐭𝐲 will deploy NVIDIA's new 𝐕𝐞𝐫𝐚 𝐂𝐏𝐔𝐬 for AI workloads. ➤ NVIDIA expects 𝐕𝐞𝐫𝐚 𝐂𝐏𝐔 sales to reach 𝐨𝐯𝐞𝐫 $𝟐𝟎 𝐛𝐢𝐥𝐥𝐢𝐨𝐧 this fiscal year. ➤ Vera expands NVIDIA into the 𝐂𝐏𝐔 market dominated by Intel and AMD. ➤ NVIDIA is broadening beyond AI GPUs into 𝐠𝐞𝐧𝐞𝐫𝐚𝐥-𝐩𝐮𝐫𝐩𝐨𝐬𝐞 computing processors. ➤ Perplexity said Vera delivers about 𝟏.𝟓𝐱 faster AI agent coding performance. ➤ Perplexity did not disclose the number of 𝐕𝐞𝐫𝐚 𝐂𝐏𝐔𝐬 it plans to purchase. ➤ OpenAI, Anthropic, and Oracle have also committed to using NVIDIA Vera CPUs. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ NVIDIA is challenging 𝐈𝐧𝐭𝐞𝐥 and 𝐀𝐌𝐃 in the multibillion-dollar CPU market. ➤ Rising AI agent workloads are driving demand for 𝐀𝐈-𝐨𝐩𝐭𝐢𝐦𝐢𝐳𝐞𝐝 CPUs. ➤ Additional customer wins strengthen NVIDIA's 𝐞𝐧𝐭𝐞𝐫𝐩𝐫𝐢𝐬𝐞 AI infrastructure strategy. 👉 𝐄𝐱𝐩𝐞𝐫𝐭 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭: ➤ "NVIDIA's CPU performs AI agent coding tasks about 1.5 times faster than traditional CPUs." — 𝐍𝐚𝐭𝐞 𝐊𝐮𝐩𝐩, Vice President for Computer Enterprise and Infrastructure at Perplexity.

@StockMKTNewz [Tue Jul 07 17:28:40 +0000 2026]: Microsoft $MSFT is looking to reduce AI costs, is starting to replace OpenAI and Anthropic with its own models in software products like Excel and Outlook - Bloomberg https://t.co/PmDskUtpjd

@KobeissiLetter [Tue Jul 07 19:20:54 +0000 2026]: BREAKING: Brent crude oil prices surge above $76/barrel after the US revokes Iran's general license to export oil in response to Iran striking three commercial vessels in the Strait of Hormuz. https://t.co/zTH55IWNw4

@KobeissiLetter [Tue Jul 07 18:53:26 +0000 2026]: BREAKING: The US is revoking Iran's newly issued general license to export oil after Iran struck three commercial vessels in the Strait of Hormuz. The US called Iran's latest actions in the Strait of Hormuz "wholly unacceptable" and said they will be "met with consequences."

@KobeissiLetter [Tue Jul 07 13:44:18 +0000 2026]: Global financial institutions are set to reduce exposure to the US Dollar: 4% of financial institutions plan to reduce their US Dollar exposure in their portfolios over the next 12-24 months, the first such reading in 3 years, according to an OMFIF survey of 74 central banks and 16 public pension and sovereign wealth funds managing over $10 trillion in reserve assets. The US Dollar is the only major currency expected to see a lower exposure among survey respondents. Furthermore, 8% expect to reduce the US Dollar in their reserves over the next 10 years. Nevertheless, the US Dollar is still the most held currency across financial institutions, at 58%, slightly down from 60% in 2025. Meanwhile, 82% of central banks surveyed now hold physical gold, up from 71% last year. 51% of respondents cite protection against geopolitical risk as a motivation for holding gold, up from 40% in 2024. Central banks are diversifying from the US Dollar into gold.

@AIStockSavvy [Tue Jul 07 22:10:17 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $FIGR Figure Reports Record Q2 Marketplace Volume Above Guidance 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ Figure said preliminary 𝐐𝟐 𝟐𝟎𝟐𝟔 results exceeded the top end of prior guidance. ➤ Consumer Loan Marketplace Volume reached 𝐚 𝐫𝐞𝐜𝐨𝐫𝐝 $𝟒.𝟐𝟓𝟗 𝐛𝐢𝐥𝐥𝐢𝐨𝐧 in Q2, up 𝟒𝟕% QoQ and 𝟏𝟑𝟐% YoY. ➤ June Consumer Loan Marketplace Volume rose to $𝟏.𝟓𝟏𝟗 𝐛𝐢𝐥𝐥𝐢𝐨𝐧, up 𝟖% MoM and 𝟏𝟓𝟓% YoY. ➤ $𝐘𝐋𝐃𝐒 in circulation totaled $𝟓𝟓𝟔 𝐦𝐢𝐥𝐥𝐢𝐨𝐧 at June-end, roughly flat MoM. ➤ Democratized Prime 𝐌𝐚𝐭𝐜𝐡𝐞𝐝 𝐎𝐟𝐟𝐞𝐫𝐬 reached $𝟑𝟗𝟐 𝐦𝐢𝐥𝐥𝐢𝐨𝐧, up 𝟐% MoM and 𝟔% QoQ. ➤ 𝐁𝐨𝐫𝐫𝐨𝐰𝐞𝐫 𝐃𝐞𝐦𝐚𝐧𝐝 increased to $𝟒𝟏𝟒 𝐦𝐢𝐥𝐥𝐢𝐨𝐧, while 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐋𝐞𝐧𝐝𝐞𝐫 𝐒𝐮𝐩𝐩𝐥𝐲 rose to $𝟓𝟐𝟐 𝐦𝐢𝐥𝐥𝐢𝐨𝐧. ➤ Figure will transition from 𝐦𝐨𝐧𝐭𝐡𝐥𝐲 disclosures to a weekly performance dashboard. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ Marketplace volume growth signals 𝐬𝐭𝐫𝐨𝐧𝐠 consumer lending demand and platform adoption. ➤ Results above guidance may reinforce confidence in Figure's 𝟐𝟎𝟐𝟔 growth outlook. ➤ Weekly reporting could provide investors with more 𝐟𝐫𝐞𝐪𝐮𝐞𝐧𝐭 operating performance updates.

@StockMKTNewz [Tue Jul 07 18:36:08 +0000 2026]: Meta Platforms $META just announced that it's rolling out Muse Image, its first image-generation model from ​Meta Superintelligence Labs - Reuters https://t.co/wwrOFL35K0

@KobeissiLetter [Tue Jul 07 16:52:21 +0000 2026]: AI is the hottest topic on global earnings calls: Mentions of AI disruptions during H1 2026 earnings calls jumped to a record ~780. This marks a +310% increase from ~190 mentions in H2 2025. In the first half alone, there were more mentions of AI disruptions than in the previous 3 years combined. Meanwhile, a record 337 executives at S&P 500 firms mentioned AI during Q1 2026 earnings calls held between March 15th and June 11th, according to FactSet. This is more than double the 5-year average of 164 and more than triple the 10-year average of 103. AI is transforming corporate strategy and financial markets.

@KobeissiLetter [Tue Jul 07 21:32:59 +0000 2026]: BREAKING: The US Military announces it has begun launching a series of powerful strikes against Iran. The US says these strikes are in response to Iranian attacks on three vessels that were transiting the Strait of Hormuz.

@KobeissiLetter [Tue Jul 07 15:17:43 +0000 2026]: BREAKING: US officials say Iran has struck a third commercial ship in the Strait of Hormuz, per Axios. This follows attacks on two commercial vessels yesterday and comes after a one-week agreement between the US and Iran on halting attacks in the Strait of Hormuz has expired.

@KobeissiLetter [Tue Jul 07 14:04:46 +0000 2026]: BREAKING: The Nasdaq 100 extends losses to over -1% on the day as chip stocks pull back. https://t.co/1XPmJ5WBEs

@AIStockSavvy [Tue Jul 07 22:04:56 +0000 2026]: Iran says US strike seriously violates Iran-US Islamabad memorandum - $QQQ $SPY $USO State broadcaster IRIB reported early on the 8th that Iran’s government said the US strike on Iran seriously violates the Iran‑US Islamabad memorandum of understanding.

@AIStockSavvy [Tue Jul 07 21:51:11 +0000 2026]: U.S. officials said the strike on Iran was a "punitive action, not a proportional response," and that the operation "will not end in the short term." - CNN - $QQQ $SPY $USO

@AIStockSavvy [Tue Jul 07 21:42:08 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: US Military Says It’s Launching New Wave of Strikes Against Iran - Bloomberg - $QQQ $SPY $USO

@AIStockSavvy [Tue Jul 07 20:57:26 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $SPCX SpaceXAI plans to release as early as Wednesday a new AI model developed in partnership with Cursor - The Information

@AIStockSavvy [Tue Jul 07 18:02:30 +0000 2026]: $COIN | US Tiger Securities 𝐮𝐩𝐠𝐫𝐚𝐝𝐞𝐬 𝐂𝐨𝐢𝐧𝐛𝐚𝐬𝐞 to 𝐁𝐮𝐲, sets 𝐏𝐓 𝐚𝐭 $𝟐𝟎𝟎 Analyst upgrades on a more constructive view of the Bitcoin cycle, believing the largest part of de-risking is complete and upside is ahead. https://t.co/qBUgsPsPGX

@wallstengine [Tue Jul 07 22:36:01 +0000 2026]: $SHMD received a repeat order worth over €37M from a Chinese customer for HDI-ML and mSAP production equipment. The equipment will support capacity expansion for AI server boards and optical module applications. Including this order, SCHMID’s 2026 order intake now stands at €81.7M, up from €44.3M before the deal.

@KobeissiLetter [Tue Jul 07 15:10:45 +0000 2026]: The market's rally is broadening: The equal-weighted S&P 500 index has recorded 31 all-time highs so far this year, the 2nd-highest total since 2021. This comes as the index has rallied +12.2% over the period, outperforming the S&P 500's +10.1% gain. By comparison, the S&P 500 has seen 24 all-time highs year-to-date. At this pace, the equal-weighted index is on track to record 60 new all-time highs in 2026, the 2nd-highest annual total on record. This would rank only behind the 68 all-time highs posted in 2013. Market leadership is expanding.

@AIStockSavvy [Tue Jul 07 21:31:12 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Netflix, Disney and YouTube Interested in Fifa World Cup U.S. Rights, Package Could Reach $2 Billion - CNBC - $NFLX $GOOGL $DIS

@AIStockSavvy [Tue Jul 07 20:07:49 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $FCEL FuelCell Energy launches $200M common stock offering

@AIStockSavvy [Tue Jul 07 20:05:48 +0000 2026]: $PENG | Penguin Solutions, Inc., Q3-2026 Earning Report https://t.co/GMZdwr5gxy

@wallstengine [Tue Jul 07 19:12:12 +0000 2026]: $USO +4.5% https://t.co/7yutwsKREf

@StockMKTNewz [Tue Jul 07 16:23:58 +0000 2026]: The United States 🇺🇸, Japan 🇯🇵, and South Korea 🇰🇷 just signed a new pact around working together to accelerate Small Modular Nuclear Reactor Development https://t.co/UfN0BUGzcX

@KobeissiLetter [Tue Jul 07 20:19:03 +0000 2026]: China is now dominating the global auto market: China's vehicle exports jumped +68.7% YoY in May, to ~930,000. This is almost +1,100% above levels seen in May 2019. This comes as new EV exports surged +112.6% YoY, to 424,000, accounting for ~46% of the total. As a result, China exported a record 8.6 million vehicles in the 12 months ending May. By comparison, Japan exported just 4.2 million, or -51% fewer, during the same period. To put this into perspective, China exported just 1.0 million vehicles in 2019, while Japan exported 4.8 million, or +380% more. China is now the undisputed leader of the global car market.

@gurgavin [Mon Jul 06 16:11:32 +0000 2026]: TRUMP SAYS “COUPLE OF GUYS WENT SHORT ( THE STOCK ) MARKET POOR BASTARDS ARE IN BIG TROUBLE THEY'RE GETTING WIPED OUT”

@wallstengine [Tue Jul 07 18:52:51 +0000 2026]: The U.S. is revoking a general license that allowed Iranian oil sales after calling Iran’s actions in the Strait of Hormuz “wholly unacceptable.” The move follows tanker attacks near the strait, which carries about a fifth of global oil consumption. https://t.co/TSYpZf59Sx

@StockMKTNewz [Tue Jul 07 20:31:21 +0000 2026]: Anthropic has now overtaken OpenAI in paid business adoption of AI https://t.co/f28z62qIk7

@gurgavin [Mon Jul 06 19:45:40 +0000 2026]: KIND OF CRAZY AMERICA WAS EXPECTED TO LOSE TODAY AFTER ITS BEST PLAYER GOT A RED CARD LAST GAME AND WASN’T ALLOWED TO PLAY TODAY BUT TRUMP CALLED FIFA AND MADE THEM OVERTURN THE DECISION NOW AMERICA IS EXPECTED TO WIN

@gurgavin [Sat Jul 04 18:37:40 +0000 2026]: HAPPY INDEPENDENCE DAY TO MY AMERICAN FOLLOWERS 🇺🇸🇺🇸🇺🇸🇺🇸 “IT’S NEVER PAID TO BET AGAINST AMERICA. WE COME THROUGH THINGS, BUT IT’S NOT ALWAYS A SMOOTH RIDE. NEVER BET AGAINST AMERICA.” - WARREN BUFFETT -

@gurgavin [Tue Jul 07 17:57:39 +0000 2026]: THIS MIGHT BE THE CRAZIEST GAME I HAVE EVER WATCHED

@StockMKTNewz [Tue Jul 07 20:06:13 +0000 2026]: The 🇺🇸 stock market just closed the day Red 🔴🔴🔴🔴 https://t.co/siYr5U7NBP

@StockMKTNewz [Tue Jul 07 19:29:42 +0000 2026]: SK Hynix is expected to bring in $231 Billion of revenue this year up from $67B last year https://t.co/xCuDbe4fm9

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.