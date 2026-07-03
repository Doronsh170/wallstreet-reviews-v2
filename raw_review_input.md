אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are a senior Wall Street market analyst writing a PRE-MARKET briefing in Hebrew.
Script run date: 2026-07-03 (יום שישי). Briefing target date: 2026-07-06 (יום שני).
This runs on 2026-07-03 but the briefing is for the NEXT trading day: 2026-07-06 (יום שני). Do NOT use 'היום'/'הבוקר' — use 'ביום שני'. Do NOT describe futures/pre-market as live — they are not available yet.

FORWARD-LOOKING ONLY: no yesterday's index performance, no closing levels, zero backward-looking data,
and nothing that already appears in the prior-context block. 7-12 bullets covering: scheduled economic data
(Israel times + consensus), expected earnings, NEW overnight geopolitical developments (always with the market
transmission mechanism: event → oil → inflation → rates → equities), NEW overnight company news and analyst moves,
commodity/currency signals. Futures: direction only unless a specific futures percentage appears in the sources —
never copy an ETF percentage as a futures percentage.

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

CRITICAL — OUTPUT FORMAT (MANDATORY):
- Return ONLY a JSON object, no backticks, no explanations, in EXACTLY this structure:
{
  "title": "נקודות חשובות לקראת פתיחת המסחר בוול סטריט 🇺🇸 – יום שני 2026-07-06",
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
  $TSLA: $393.45 (daily: -7.49%), prev close: $425.30
  $MU: $975.56 (daily: -5.49%), prev close: $1032.28
  $SPCX: $162.00 (daily: +2.83%), prev close: $157.54
  $HOOD: $112.73 (daily: +3.76%), prev close: $108.65
  $AAPL: $308.63 (daily: +4.84%), prev close: $294.38
  $AAL: $17.92 (daily: -1.27%), prev close: $18.15
  $ABBV: $261.07 (daily: +3.99%), prev close: $251.06
  $AHR: $55.04 (daily: +2.59%), prev close: $53.65
  $APGE: $132.91 (daily: +0.11%), prev close: $132.77
  $ASB: $30.64 (daily: -1.86%), prev close: $31.22
  $BCS: $27.77 (daily: +1.83%), prev close: $27.27

DIRECTIONAL FACTS — Hebrew direction words (עולה/יורד/צונח/מזנק) MUST match these:
  נפט (WTI/Brent proxies): עולה (USO: +0.69%, BNO: +0.66%)
  זהב: עולה (GLD: +2.03%)
  ביטקוין: עולה (IBIT: +2.56%)
  דולר: יורד (UUP: -0.53%)
  תנודתיות / VIX: יורד (VIXY: -1.35%)
  אג"ח ארוכות / TLT: יציב/כמעט ללא שינוי (TLT: -0.01%)

The % changes above are ACCURATE — use them for direction and magnitude.
For exact index LEVELS (points), gold/oil absolute prices, VIX level, Bitcoin price, 10Y yield: verify via web search. Do NOT estimate them from ETF prices.
For sector performance (XLE/XLK/...): USE ONLY the Finnhub numbers above — never invent sector percentages.
If ANY percentage you write contradicts the data above, you are WRONG. Fix it.
══════════════════════════════════════════════════════════════════════════════

══ SCHEDULED DATA CHECK ══
Use web search to find what US economic data is scheduled for release on 2026-07-03.
Include the release time in Israel time and the market consensus/forecast.
══════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-03. Never mention in the review that these came from tweets/posts:

@gurgavin [Thu Jul 02 19:10:49 +0000 2026]: TESLA CAPS EMPLOYEE AI SPEND AT $200 PER WEEK PER THE INFORMATION $TSLA

@gurgavin [Tue Jun 30 20:38:47 +0000 2026]: MICHAEL BURRY IS REPORTEDLY SHORT TESLA NOW HE NEVER LEARNS , NO ONE MAKES MONEY BETTING AGAINST ELON $TSLA https://t.co/wsBIQluMTg

@wallstengine [Thu Jul 02 19:14:20 +0000 2026]: $TSLA reportedly told employees it will cap AI spending at $200 per week starting July 6, per The Information. Some Tesla software engineers were reportedly using thousands of dollars worth of AI tokens per week. Employees will need approval to exceed the cap, though beta versions of xAI products are reportedly excluded.

@KobeissiLetter [Thu Jul 02 13:35:17 +0000 2026]: BREAKING: President Trump says Micron stock, $MU, went up “9 points” after the company announced a $250 million contribution to Trump Accounts. https://t.co/444Y3BIl9T

@gurgavin [Wed Jul 01 18:02:23 +0000 2026]: SPACEX HAS BEEN SHOWING OFF A PROTOTYPE OF A NEW “AI DEVICE” WHICH IS SIMILAR THAN AS IPHONE PER WSJ THE DEVICE RUNS ON CUSTOM SOFTWARE AND USED XAI’S TECH $SPCX

@wallstengine [Thu Jul 02 18:56:37 +0000 2026]: $META CEO Mark Zuckerberg told employees in an internal town hall that AI agent development over the last four months has not “accelerated in the way we expected.” - Reuters https://t.co/tT20xKh2bm

@StockMKTNewz [Fri Jul 03 00:07:45 +0000 2026]: Cathie Wood and Ark Invest bought 96,935 shares of Tesla $TSLA today https://t.co/iUfRbH6TQ5

@StockMKTNewz [Thu Jul 02 20:10:05 +0000 2026]: Meta Platforms $META CEO Mark Zuckerberg reportedly told employees at an internal town hall meeting that HE EXPECTS META TO FEEL MORE OF THE BENEFITS FROM ITS AI INVESTMENT IN THE NEXT 3-6 MONTHS https://t.co/e2o9qInLmL

@StockMKTNewz [Thu Jul 02 20:07:28 +0000 2026]: Robinhood $HOOD just confirmed it will be reporting earnings after the markets close on Wednesday, July 29th The earnings call will be live streamed directly to X

@StockMKTNewz [Thu Jul 02 19:57:05 +0000 2026]: Apple $AAPL stock is now up by 5% today 👀 🍏🍏🍏🍏🍏 https://t.co/ZdV5m4wyHx

@StockMKTNewz [Thu Jul 02 19:53:48 +0000 2026]: All these stocks hit new 52 WEEK HIGHS at some point today American Airlines $AAL Crowdstrike $CRWD Unitedhealth $UNH Visa $V Monster $MNST GE Aerospace $GE Moderna $MRNA Banco Santander $SAN CSX $CSX Oscar Health $OSCR Barclays Plc $BCS Super Group $SGHC Valley National Bancorp $VLY Johnson & Johnson $JNJ Delta Air Lines $DAL Healthpeak $DOC Abbvie $ABBV U.S. Bancorp $USB Siriusxm $SIRI Citizens Financial $CFG ING $ING Webster Financial $WBS F.N.B. $FNB American Healthcare $AHR Old National Bncp $ONB Jfrog $FROG Okta Cl A $OKTA Franklin Resources $BEN Apogee Therapeutics $APGE Illumina $ILMN Columbia Banking Sys $COLB Centene $CNC Iridium $IRDM Royalty Pharma $RPRX Incyte $INCY Edwards Lifesciences $EW Ventas $VTR Sharkninja $SN Welltower $WELL Alliant Energy $LNT Brightspring Health $BTSG US Foods Holding $USFD UBS Group $UBS Exelixis $EXEL Associated Banc-Corp $ASB Eastern Bankshares $EBC Union Pacific $UNP Linde $LIN Valero Energy $VLO

@wallstengine [Thu Jul 02 20:07:36 +0000 2026]: $META CEO MARK ZUCKERBERG SAYS IN INTERNAL TOWN HALL HE EXPECTS COMPANY TO FEEL MORE BENEFITS OF AI INVESTMENT IN NEXT 3-6 MONTHS

@gurgavin [Thu Jul 02 18:04:16 +0000 2026]: AN AUTOGRAPHED JACKET OF NVIDIA CEO JENSEN HUANG IS UP FOR AUCTION ON SOTHEBYS IT'S SIGNED BY HIM AND HE ACTUALLY WORE THIS EXACT JACKET IN THE PAST IT'S ESTIMATED TO SELL FOR $40,000–$60,000 $NVDA https://t.co/jedGiznXYO

@KobeissiLetter [Thu Jul 02 22:00:02 +0000 2026]: Levered ETFs have become one of the most powerful forces in US equity markets: Daily rebalancing activity in US equity leveraged ETFs is up to a record $50 billion. Leveraged ETFs must rebalance daily to stay at their target leverage, adding more exposure after markets rise and reducing it after markets fall. This figure has more than QUADRUPLED since the start of 2026. Rebalancing activity now accounts for a record 1.60% of S&P 500 futures volume, exceeding the 2020-2024 peaks by 200%. To put it simply, leveraged ETFs have grown large enough that their daily rebalancing can now amplify market moves in both directions. Leveraged ETFs are amplifying market volatility like never before.

@KobeissiLetter [Thu Jul 02 12:31:26 +0000 2026]: BREAKING: The US economy adds 57,000 jobs in June, well below expectations of 114,000. The unemployment rate fell to 4.2%, below expectations of 4.3%. May's jobs number was also revised down by -43,000 jobs. The labor market remains in a volatile situation.

@AIStockSavvy [Thu Jul 02 19:21:31 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $TSLA Tesla Caps Employee AI Spend At $200 A Week - Information

@AIStockSavvy [Thu Jul 02 17:36:55 +0000 2026]: $RIVN | Canaccord reiterates 𝐁𝐮𝐲 on 𝐑𝐢𝐯𝐢𝐚𝐧, maintains 𝐏𝐓 𝐚𝐭 $𝟐𝟐 Analyst sees a unique opportunity for Rivian to become the #2 EV alternative to Tesla in the US as other OEMs retreat from EV commitments. https://t.co/9DwLSWnAUp

@KobeissiLetter [Thu Jul 02 17:11:59 +0000 2026]: BREAKING: The Strategic Petroleum Reserve (SPR) fell -5.5 million barrels last week, to 326 million barrels, the lowest since May 1983. This marks the 13th consecutive weekly decline, the longest streak since the 2021-2023 period, per Zerohedge. Over this time period, US oil reserves in the SPR have fallen -89 million barrels. This represents 51.7% of the planned 172 million barrels to be released under a relief program coordinated by the IEA to lower energy costs. By comparison, the US added +69 million barrels of oil to the SPR between July 2023 and March 2026. US oil reserves are being depleted at a historic pace.

@KobeissiLetter [Thu Jul 02 16:15:56 +0000 2026]: Retail dip-buying is reaching historic extremes: Average daily equity purchases by retail investors during S&P 500 down days are running at nearly 3.5 times the daily average seen since 2020, the highest on record. This is +56% higher than during the meme stock mania in 2021. Year-to-date, retail purchases on down days are 2.3 times larger than on up days. Even during S&P 500 up days, retail investors purchased nearly 1.5 times the daily average seen since 2020, so far this year, and double the figure posted in 2025. Individual investors have consistently purchased more equities on down days than on up days in each of the last 7 years. Retail investors are eager to buy dips.

@KobeissiLetter [Thu Jul 02 14:51:00 +0000 2026]: History points to a strong July for US stocks: Since 2005, the S&P 500 has recorded an average gain of +2.5% in July, more than 4 times the average increase seen in the other 11 months of the year. The index has not declined in July for 11 consecutive years, the longest positive streak of any month over this period. Meanwhile, the S&P 500 has posted 24 all-time highs so far in 2026. This ranks among the top 20 strongest starts to a year for the index since World War II.. Historically, when the index has seen such a streak, it has rallied another +6% over the following 6 months, on average. Seasonal patterns suggest continued bullish momentum this month.

@KobeissiLetter [Thu Jul 02 13:47:10 +0000 2026]: US-hiring plans remain historically depressed: US-based employers announced plans to add 10,933 jobs in June, marking a -44% decline from 19,536 in May. Year-to-date, US hiring plans rose +10% YoY, to 91,405 workers. This comes as technology sector hiring plans surged +167% YoY, to 14,761 workers. However, excluding technology, hiring plans are down -1% YoY, to 76,644 workers. The decline has been driven by entertainment and leisure hiring plans, which are down -57% YoY to 12,096 workers so far in 2026. This also follows 5 consecutive years of declining hiring intentions, which fell -84% since 2020, to 508,000 for the full year 2025. Hiring continues to weaken beneath the surface.

@gurgavin [Thu Jul 02 04:05:46 +0000 2026]: JUST IN : OPEN AI TO HANDOVER 5% OF IT’S ENTIRE COMPANY TO THE US GOVT PER FT

@wallstengine [Fri Jul 03 01:40:28 +0000 2026]: $MSTR -73% in one year 🩸 https://t.co/nJYIksFwN7

@wallstengine [Thu Jul 02 19:38:45 +0000 2026]: BlueCrest Capital Management and Michael Platt reported beneficial ownership of 2,354,233 Class A shares of $CCXI Churchill Capital Corp XI, equal to 5.6%. https://t.co/EYRuQhlutE

@wallstengine [Thu Jul 02 18:39:03 +0000 2026]: $FIG +12% https://t.co/PwPeROBfkc

@AIStockSavvy [Thu Jul 02 23:58:18 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: Data center startup Crusoe in talks to raise $3 bln; valuation could double to $30 bln - $META $ORCL Crusoe, a data-center startup supplying AI compute to Meta Platforms and Oracle, is in talks to raise roughly $3 bln, people familiar with the matter said, a deal that could roughly double its valuation to about $30 bln. The company is still negotiating the round and no final valuation has been set; investors expect a post-money valuation near $30 bln including the new capital. Crusoe was valued at about $10 bln in October last year.

@AIStockSavvy [Thu Jul 02 19:52:37 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $PLTR Palantir CEO said some U.S. government clients have shifted to open-source AI. - The Information

@AIStockSavvy [Thu Jul 02 19:09:25 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $META Meta CEO Mark Zuckerberg Says In Internal Town Hall That Ai Agent Development Over The Last Four Months Hasn't 'accelerated In The Way We Expected' - Reuters

@AIStockSavvy [Thu Jul 02 17:37:31 +0000 2026]: $TSLA | Truist Securities 𝐫𝐚𝐢𝐬𝐞𝐬 𝐏𝐓 on 𝐓𝐞𝐬𝐥𝐚 to $𝟒𝟑𝟎 from $𝟒𝟎𝟎, maintains 𝐇𝐨𝐥𝐝 https://t.co/BNs7VbHHBG

@AIStockSavvy [Thu Jul 02 17:35:33 +0000 2026]: $TSLA | Freedom Broker reiterates 𝐇𝐨𝐥𝐝 on 𝐓𝐞𝐬𝐥𝐚, 𝐫𝐚𝐢𝐬𝐞𝐬 𝐏𝐓 𝐭𝐨 $𝟒𝟐𝟎 𝐟𝐫𝐨𝐦 $𝟒𝟎𝟎 Analyst raises PT on strong Q2 deliveries that beat expectations, but maintains a Hold rating. https://t.co/rcWFRmAlT1

@wallstengine [Thu Jul 02 19:17:29 +0000 2026]: $META’s Zuckerberg reportedly told employees in an internal town hall that the bets behind the company’s reorganization “haven’t come to fruition yet.” He still believes long-term trends remain aligned with the basic shape of the reorg.

@KobeissiLetter [Thu Jul 02 20:05:00 +0000 2026]: BREAKING: The Dow surges nearly +600 points and closes at its highest level on record. https://t.co/YYa1kGCaYD

@KobeissiLetter [Thu Jul 02 19:01:56 +0000 2026]: BREAKING: Global stock market cap is up to a record $166 trillion. This marks a +$32 trillion YoY increase, or +23.6%, far above the long-term average. Global markets have surged +$94 trillion, or +131%, since the 2020 pandemic low. By comparison, the global equity market value has grown at a +7.0% compound annual growth rate (CAGR) over the last 20 years. Meanwhile, as a % of global GDP, the global equity market cap is up to a record ~134%. Global equities are in the midst of one of the most powerful rallies in history.

@KobeissiLetter [Thu Jul 02 12:13:46 +0000 2026]: BREAKING: President Trump says the US spends more money on NATO than any other country "without getting any benefit from doing so." https://t.co/FL76gyluyJ

@gurgavin [Tue Jun 30 20:52:21 +0000 2026]: JUST IN: TRUMP MADE $635 MILLION DOLLARS IN ROYALTIES LINKED TO HIS MEME COIN https://t.co/X3oXvQ7wPc

@AIStockSavvy [Thu Jul 02 20:20:17 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Jane Street Group Discloses Passive Stake of 5% in $HTZ Hertz Global as of June 26 - Filing

@AIStockSavvy [Thu Jul 02 17:40:09 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $MSFT Microsoft is planning to merge its consumer and enterprise Copilot chatbots in August - The Information

@AIStockSavvy [Thu Jul 02 17:35:04 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: $AMZN Amazon to Begin Internet Service This Year After Latest Launch - Bloomberg

@wallstengine [Thu Jul 02 20:07:43 +0000 2026]: $META CTO ANDREW BOSWORTH SAYS IN INTERNAL TOWN HALL THAT MOUSE TRACKING SOFTWARE WENT THROUGH PRIVACY, LEGAL AND OTHER REVIEWS BEFORE IT LAUNCHED

@wallstengine [Thu Jul 02 19:04:19 +0000 2026]: $META CEO Mark Zuckerberg told employees in an internal town hall that the company’s 2026 reorganization “wasn’t as clean as it could have been.”

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.