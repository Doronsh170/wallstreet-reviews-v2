אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are a senior Wall Street market analyst writing an end-of-day market review in Hebrew for
2026-07-02 (יום חמישי). PAST TENSE. This is a professional, readable MARKET REVIEW —
NOT a data dump. EXACTLY 5 bullets, in this order:
* המדדים: what the major indices did (direction + rounded %), one flowing analytical sentence or two.
* הסיפור של היום: WHY the market moved — the main driver(s), with clear cause-and-effect.
* סקטורים ומניות בולטות: the 1-3 most notable sector/stock stories with the reason. Stock items open with "מניית <שם בעברית> (TICKER)".
* סחורות, דולר ותשואות: oil, gold, dollar and yields in brief — direction and meaning, not a list of prices.
* שורה תחתונה למחר: what investors should watch in the next session.
Each bullet: 2-4 short sentences. Do NOT list ETF prices, do NOT dump long series of percentages or price levels,
do NOT mention Finnhub or any ETF proxy in the text. Explain the day — don't copy the data.
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
- Never write "נתון בפועל עדיין לא קיים". If a figure has not been released yet, give only the forecast (צפי) and the previous reading (נתון קודם).
- Never OPEN a bullet with a raw ticker like "$TSLA:" or "$AMZN:". Open with the Hebrew company name: "מניית טסלה (TSLA):", "מניית אמזון (AMZN):", "מניית מטא (META):".
- Finnhub and the measurement ETFs (SPY/QQQ/DIA/USO/BNO/GLD/UUP/VIXY/TLT...) are a hidden verification layer ONLY. NEVER mention Finnhub, "proxy", "דרך USO", "האינדיקציה מ-", or any technical data-source wording in the visible text — describe the asset itself (נפט, זהב, דולר, תשואות) directly.
- SIGN-FLIP: if the verified data shows a stock DOWN, do NOT describe it positively (עלתה/התחזקה/הובילה/בלטה לחיוב). If the news is positive but the stock fell, write: "למרות החדשות, המניה ירדה".

CRITICAL — OUTPUT FORMAT (MANDATORY):
- Return ONLY a JSON object, no backticks, no explanations, in EXACTLY this structure:
{
  "title": "סיכום יום המסחר בוול סטריט 🇺🇸 – יום חמישי, 2.7.2026",
  "date": "2026-07-02",
  "sections": [
    {
      "heading": "סיכום המסחר",
      "content": "* נושא ראשון: משפט אנליטי תמציתי עם מספרים.\n* נושא שני: ...\n* נושא שלישי: ..."
    }
  ]
}
- EXACTLY 1 section. Heading EXACTLY "סיכום המסחר". Title EXACTLY as given above.
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
  $TSLA: $393.45 (daily: -7.49%), prev close: $425.30
  $META: $582.90 (daily: -4.90%), prev close: $612.91
  $MU: $975.56 (daily: -5.49%), prev close: $1032.28
  $NVDA: $194.83 (daily: -1.39%), prev close: $197.58
  $SNDK: $1745.00 (daily: -14.13%), prev close: $2032.22
  $SPCX: $162.00 (daily: +2.83%), prev close: $157.54
  $RIVN: $18.63 (daily: +8.44%), prev close: $17.18
  $MSTR: $100.77 (daily: +7.90%), prev close: $93.39
  $CCXI: $19.10 (daily: +11.96%), prev close: $17.06
  $ORCL: $140.27 (daily: -1.56%), prev close: $142.50
  $PLTR: $129.30 (daily: +2.84%), prev close: $125.73
  $HTZ: $2.12 (daily: -3.64%), prev close: $2.20

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

══ MANDATORY MACRO DATA CHECK ══
Use web search to check if ANY of these were released on 2026-07-03: CPI (headline AND core),
PPI (headline AND core), NFP, Jobless Claims, Consumer Sentiment (Michigan), ISM PMI, GDP,
Retail Sales, FOMC decision/minutes. If released — include with actual, forecast, previous,
AND the market implication. If none — skip, but you MUST check first.
══════════════════════════════════

══ CONTEXT: THIS MORNING'S PRE-MARKET BRIEFING ══
Published before the session. Use it to resolve scheduled items (expected → actual), do NOT quote it verbatim.

[נקודות מרכזיות]
* מאקרו: ל־2026-07-03 לא מתוכננים נתוני מאקרו אמריקאיים בגלל חופשת 4 ביולי; ביום שני ב־17:00 שעון ישראל יתפרסם ISM Services PMI ליוני, נתון בפועל עדיין לא קיים, קונצנזוס 54.5 מול 54.5 קודם.
* Fed: ביום רביעי ב־21:00 שעון ישראל יתפרסם פרוטוקול ישיבת ה־FOMC של יוני; המוקד לשוק ביום שני יהיה ניסוח סביב יעד אינפלציה של 2% והאם חולשת התעסוקה מקטינה לחץ להעלאת ריבית.
* דוחות: ביום שני 2026-07-06 אין דוחות אמריקאיים מהותיים בלוח המרכזי; ביום שלישי 2026-07-07 אחרי הנעילה $PENG צפויה לדווח עם תחזית EPS של $0.54 והכנסות של $407.5M, ובהמשך השבוע $DAL במוקד עם תחזית EPS של $1.53 והכנסות של $17.5B.
* גיאופוליטיקה ונפט: לפי Reuters, מאמצי השלום בין ארה״ב לאיראן עדיין מחזיקים חלקית, Brent סביב $71.87 ו־WTI סביב $68.63; מנגנון השוק ליום שני הוא הסכם יציב יותר → נפט רגוע יותר → פחות לחץ אינפלציוני → פחות לחץ ריבית → תמיכה במניות, אך פגיעה מחודשת בשיט דרך הורמוז תהפוך את השרשרת.
* סחורות ומטבעות: האינדיקציה מ־Finnhub מצביעה על נפט נעים בתנודתיות דרך USO +0.69% ו־BNO +0.66%, זהב נעים בתנודתיות דרך GLD +2.03%, ביטקוין נעים בתנודתיות דרך IBIT +2.56%, דולר נעים בתנודתיות דרך UUP -0.53%, אג״ח ארוכות כמעט ללא שינוי דרך TLT -0.01%, ותנודתיות נעים בתנודתיותת דרך VIXY -1.35%.
* $TSLA: ביום שני 2026-07-06 תיכנס לתוקף תקרת שימוש פנימית של $200 בשבוע לעובד עבור כלי בינה מלאכותית, Truist העלתה יעד ל־$430 מ־$400 ו־Freedom Broker העלתה יעד ל־$420 מ־$400, כאשר שתי ההמלצות נשארו ברמת החזק.
* $META: לפי Reuters, מארק צוקרברג אמר לעובדים שפיתוח סוכני בינה מלאכותית לא הואץ כמצופה ב־4 החודשים האחרונים, אך החברה מצפה להרגיש יותר תועלת מההשקעות בבינה מלאכותית בטווח של 3–6 חודשים.
* $AMZN: לפי Reuters, Amazon Leo צפויה להתחיל שירות אינטרנט לווייני ראשוני ב־2026 לאחר שיגור נוסף של 29 לוויינים, עם 394 מתוך 398 לוויינים ששוגרו במסלול ותוכנית ארוכת טווח של יותר מ־3,200 לוויינים.
* $HOOD: החברה אישרה שתפרסם את דוחות Q2 2026 ביום רביעי 2026-07-29 אחרי נעילת המסחר, עם שיחת הנהלה ב־5:00 PM ET; קונצנזוס EPS חיצוני עומד על $0.41.
* בינה מלאכותית ומדיניות: לפי Reuters וה־FT, OpenAI דנה בהענקת נתח של 5% לממשלת ארה״ב לפני IPO, בעוד סנאטור ברני סנדרס הציע מודל של 50%; ביום שני זה עשוי להחזיר למוקד את $MSFT, $GOOGL ו־$META סביב סיכון רגולטורי במודלי בינה מלאכותית.
* מבנה שוק: פעילות האיזון היומית של תעודות סל ממונפות במניות ארה״ב הגיעה לשיא של $50B ומהווה 1.60% מנפח החוזים על S&P 500, יותר מפי 4 מתחילת 2026; המשמעות ליום שני היא רגישות גבוהה יותר לתנועה כיוונית במדדים בשעה האחרונה של המסחר.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-03. Never mention in the review that these came from tweets/posts:

@gurgavin [Thu Jul 02 19:10:49 +0000 2026]: TESLA CAPS EMPLOYEE AI SPEND AT $200 PER WEEK PER THE INFORMATION $TSLA

@gurgavin [Tue Jun 30 20:38:47 +0000 2026]: MICHAEL BURRY IS REPORTEDLY SHORT TESLA NOW HE NEVER LEARNS , NO ONE MAKES MONEY BETTING AGAINST ELON $TSLA https://t.co/wsBIQluMTg

@wallstengine [Thu Jul 02 19:14:20 +0000 2026]: $TSLA reportedly told employees it will cap AI spending at $200 per week starting July 6, per The Information. Some Tesla software engineers were reportedly using thousands of dollars worth of AI tokens per week. Employees will need approval to exceed the cap, though beta versions of xAI products are reportedly excluded.

@KobeissiLetter [Fri Jul 03 12:57:12 +0000 2026]: Leverage in South Korean stocks is out of control: Assets under management (AUM) in South Korea's leveraged ETFs are up to a record ~$45 billion. AUM has surged +800% since the start of 2026. As a result, leveraged exposure as a % of free float market capitalization, the portion of shares actually available for public trading, is up to a record ~2.9%, more than TRIPLING since January. Meanwhile, the Hong Kong-listed 2x leveraged long SK Hynix ETF rose to ~$15 billion in assets at its peak, the largest single-stock leveraged product in the world. By comparison, four leading 2x leveraged long ETFs tracking Micron, $MU, Nvidia, $NVDA, Sandisk, $SNDK, and Tesla, $TSLA, have each never exceeded $10 billion in assets. Leverage in Korea is at extreme levels.

@wallstengine [Thu Jul 02 18:56:37 +0000 2026]: $META CEO Mark Zuckerberg told employees in an internal town hall that AI agent development over the last four months has not “accelerated in the way we expected.” - Reuters https://t.co/tT20xKh2bm

@KobeissiLetter [Thu Jul 02 13:35:17 +0000 2026]: BREAKING: President Trump says Micron stock, $MU, went up “9 points” after the company announced a $250 million contribution to Trump Accounts. https://t.co/444Y3BIl9T

@gurgavin [Wed Jul 01 18:02:23 +0000 2026]: SPACEX HAS BEEN SHOWING OFF A PROTOTYPE OF A NEW “AI DEVICE” WHICH IS SIMILAR THAN AS IPHONE PER WSJ THE DEVICE RUNS ON CUSTOM SOFTWARE AND USED XAI’S TECH $SPCX

@StockMKTNewz [Fri Jul 03 00:07:45 +0000 2026]: Cathie Wood and Ark Invest bought 96,935 shares of Tesla $TSLA today https://t.co/iUfRbH6TQ5

@StockMKTNewz [Thu Jul 02 20:10:05 +0000 2026]: Meta Platforms $META CEO Mark Zuckerberg reportedly told employees at an internal town hall meeting that HE EXPECTS META TO FEEL MORE OF THE BENEFITS FROM ITS AI INVESTMENT IN THE NEXT 3-6 MONTHS https://t.co/e2o9qInLmL

@wallstengine [Thu Jul 02 20:07:36 +0000 2026]: $META CEO MARK ZUCKERBERG SAYS IN INTERNAL TOWN HALL HE EXPECTS COMPANY TO FEEL MORE BENEFITS OF AI INVESTMENT IN NEXT 3-6 MONTHS

@gurgavin [Thu Jul 02 18:04:16 +0000 2026]: AN AUTOGRAPHED JACKET OF NVIDIA CEO JENSEN HUANG IS UP FOR AUCTION ON SOTHEBYS IT'S SIGNED BY HIM AND HE ACTUALLY WORE THIS EXACT JACKET IN THE PAST IT'S ESTIMATED TO SELL FOR $40,000–$60,000 $NVDA https://t.co/jedGiznXYO

@KobeissiLetter [Thu Jul 02 22:00:02 +0000 2026]: Levered ETFs have become one of the most powerful forces in US equity markets: Daily rebalancing activity in US equity leveraged ETFs is up to a record $50 billion. Leveraged ETFs must rebalance daily to stay at their target leverage, adding more exposure after markets rise and reducing it after markets fall. This figure has more than QUADRUPLED since the start of 2026. Rebalancing activity now accounts for a record 1.60% of S&P 500 futures volume, exceeding the 2020-2024 peaks by 200%. To put it simply, leveraged ETFs have grown large enough that their daily rebalancing can now amplify market moves in both directions. Leveraged ETFs are amplifying market volatility like never before.

@KobeissiLetter [Thu Jul 02 12:31:26 +0000 2026]: BREAKING: The US economy adds 57,000 jobs in June, well below expectations of 114,000. The unemployment rate fell to 4.2%, below expectations of 4.3%. May's jobs number was also revised down by -43,000 jobs. The labor market remains in a volatile situation.

@AIStockSavvy [Thu Jul 02 19:21:31 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $TSLA Tesla Caps Employee AI Spend At $200 A Week - Information

@AIStockSavvy [Thu Jul 02 17:36:55 +0000 2026]: $RIVN | Canaccord reiterates 𝐁𝐮𝐲 on 𝐑𝐢𝐯𝐢𝐚𝐧, maintains 𝐏𝐓 𝐚𝐭 $𝟐𝟐 Analyst sees a unique opportunity for Rivian to become the #2 EV alternative to Tesla in the US as other OEMs retreat from EV commitments. https://t.co/9DwLSWnAUp

@StockMKTNewz [Fri Jul 03 11:40:34 +0000 2026]: Michael Burry is now reportedly short Micron $MU stock - MarketWatch https://t.co/pKrkOSp87L

@KobeissiLetter [Thu Jul 02 17:11:59 +0000 2026]: BREAKING: The Strategic Petroleum Reserve (SPR) fell -5.5 million barrels last week, to 326 million barrels, the lowest since May 1983. This marks the 13th consecutive weekly decline, the longest streak since the 2021-2023 period, per Zerohedge. Over this time period, US oil reserves in the SPR have fallen -89 million barrels. This represents 51.7% of the planned 172 million barrels to be released under a relief program coordinated by the IEA to lower energy costs. By comparison, the US added +69 million barrels of oil to the SPR between July 2023 and March 2026. US oil reserves are being depleted at a historic pace.

@KobeissiLetter [Thu Jul 02 16:15:56 +0000 2026]: Retail dip-buying is reaching historic extremes: Average daily equity purchases by retail investors during S&P 500 down days are running at nearly 3.5 times the daily average seen since 2020, the highest on record. This is +56% higher than during the meme stock mania in 2021. Year-to-date, retail purchases on down days are 2.3 times larger than on up days. Even during S&P 500 up days, retail investors purchased nearly 1.5 times the daily average seen since 2020, so far this year, and double the figure posted in 2025. Individual investors have consistently purchased more equities on down days than on up days in each of the last 7 years. Retail investors are eager to buy dips.

@KobeissiLetter [Thu Jul 02 14:51:00 +0000 2026]: History points to a strong July for US stocks: Since 2005, the S&P 500 has recorded an average gain of +2.5% in July, more than 4 times the average increase seen in the other 11 months of the year. The index has not declined in July for 11 consecutive years, the longest positive streak of any month over this period. Meanwhile, the S&P 500 has posted 24 all-time highs so far in 2026. This ranks among the top 20 strongest starts to a year for the index since World War II.. Historically, when the index has seen such a streak, it has rallied another +6% over the following 6 months, on average. Seasonal patterns suggest continued bullish momentum this month.

@KobeissiLetter [Thu Jul 02 13:47:10 +0000 2026]: US-hiring plans remain historically depressed: US-based employers announced plans to add 10,933 jobs in June, marking a -44% decline from 19,536 in May. Year-to-date, US hiring plans rose +10% YoY, to 91,405 workers. This comes as technology sector hiring plans surged +167% YoY, to 14,761 workers. However, excluding technology, hiring plans are down -1% YoY, to 76,644 workers. The decline has been driven by entertainment and leisure hiring plans, which are down -57% YoY to 12,096 workers so far in 2026. This also follows 5 consecutive years of declining hiring intentions, which fell -84% since 2020, to 508,000 for the full year 2025. Hiring continues to weaken beneath the surface.

@gurgavin [Thu Jul 02 04:05:46 +0000 2026]: JUST IN : OPEN AI TO HANDOVER 5% OF IT’S ENTIRE COMPANY TO THE US GOVT PER FT

@wallstengine [Fri Jul 03 01:40:28 +0000 2026]: $MSTR -73% in one year 🩸 https://t.co/nJYIksFwN7

@wallstengine [Thu Jul 02 20:07:43 +0000 2026]: $META CTO ANDREW BOSWORTH SAYS IN INTERNAL TOWN HALL THAT MOUSE TRACKING SOFTWARE WENT THROUGH PRIVACY, LEGAL AND OTHER REVIEWS BEFORE IT LAUNCHED

@wallstengine [Thu Jul 02 19:38:45 +0000 2026]: BlueCrest Capital Management and Michael Platt reported beneficial ownership of 2,354,233 Class A shares of $CCXI Churchill Capital Corp XI, equal to 5.6%. https://t.co/EYRuQhlutE

@AIStockSavvy [Thu Jul 02 23:58:18 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: Data center startup Crusoe in talks to raise $3 bln; valuation could double to $30 bln - $META $ORCL Crusoe, a data-center startup supplying AI compute to Meta Platforms and Oracle, is in talks to raise roughly $3 bln, people familiar with the matter said, a deal that could roughly double its valuation to about $30 bln. The company is still negotiating the round and no final valuation has been set; investors expect a post-money valuation near $30 bln including the new capital. Crusoe was valued at about $10 bln in October last year.

@AIStockSavvy [Thu Jul 02 19:52:37 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $PLTR Palantir CEO said some U.S. government clients have shifted to open-source AI. - The Information

@AIStockSavvy [Thu Jul 02 19:09:25 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $META Meta CEO Mark Zuckerberg Says In Internal Town Hall That Ai Agent Development Over The Last Four Months Hasn't 'accelerated In The Way We Expected' - Reuters

@AIStockSavvy [Thu Jul 02 17:37:31 +0000 2026]: $TSLA | Truist Securities 𝐫𝐚𝐢𝐬𝐞𝐬 𝐏𝐓 on 𝐓𝐞𝐬𝐥𝐚 to $𝟒𝟑𝟎 from $𝟒𝟎𝟎, maintains 𝐇𝐨𝐥𝐝 https://t.co/BNs7VbHHBG

@AIStockSavvy [Thu Jul 02 17:35:33 +0000 2026]: $TSLA | Freedom Broker reiterates 𝐇𝐨𝐥𝐝 on 𝐓𝐞𝐬𝐥𝐚, 𝐫𝐚𝐢𝐬𝐞𝐬 𝐏𝐓 𝐭𝐨 $𝟒𝟐𝟎 𝐟𝐫𝐨𝐦 $𝟒𝟎𝟎 Analyst raises PT on strong Q2 deliveries that beat expectations, but maintains a Hold rating. https://t.co/rcWFRmAlT1

@wallstengine [Thu Jul 02 19:17:29 +0000 2026]: $META’s Zuckerberg reportedly told employees in an internal town hall that the bets behind the company’s reorganization “haven’t come to fruition yet.” He still believes long-term trends remain aligned with the basic shape of the reorg.

@KobeissiLetter [Thu Jul 02 20:05:00 +0000 2026]: BREAKING: The Dow surges nearly +600 points and closes at its highest level on record. https://t.co/YYa1kGCaYD

@KobeissiLetter [Thu Jul 02 19:01:56 +0000 2026]: BREAKING: Global stock market cap is up to a record $166 trillion. This marks a +$32 trillion YoY increase, or +23.6%, far above the long-term average. Global markets have surged +$94 trillion, or +131%, since the 2020 pandemic low. By comparison, the global equity market value has grown at a +7.0% compound annual growth rate (CAGR) over the last 20 years. Meanwhile, as a % of global GDP, the global equity market cap is up to a record ~134%. Global equities are in the midst of one of the most powerful rallies in history.

@gurgavin [Tue Jun 30 20:52:21 +0000 2026]: JUST IN: TRUMP MADE $635 MILLION DOLLARS IN ROYALTIES LINKED TO HIS MEME COIN https://t.co/X3oXvQ7wPc

@AIStockSavvy [Thu Jul 02 20:20:17 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Jane Street Group Discloses Passive Stake of 5% in $HTZ Hertz Global as of June 26 - Filing

@AIStockSavvy [Thu Jul 02 17:40:09 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $MSFT Microsoft is planning to merge its consumer and enterprise Copilot chatbots in August - The Information

@AIStockSavvy [Thu Jul 02 17:35:04 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: $AMZN Amazon to Begin Internet Service This Year After Latest Launch - Bloomberg

@wallstengine [Thu Jul 02 19:04:19 +0000 2026]: $META CEO Mark Zuckerberg told employees in an internal town hall that the company’s 2026 reorganization “wasn’t as clean as it could have been.”

@StockMKTNewz [Thu Jul 02 22:07:49 +0000 2026]: 🇺🇸 President Trump just said he - Didn't know about his Crypto Earnings, that his kids run his business, and he is "not involved"

@StockMKTNewz [Thu Jul 02 21:58:47 +0000 2026]: 🇺🇸 PRESIDENT TRUMP JUST SAID - I THINK AI IS BIGGER THAN THE INTERNET

@StockMKTNewz [Fri Jul 03 12:03:28 +0000 2026]: SK HYNIX MADE MORE PROFIT IN Q1 OF THIS YEAR THAN REVENUE IT BROUGHT IN ALL OF 2023 Here is what SK Hynix's numbers have looked like over the last couple of years - 2023: Revenue $21.24B, Profit/(loss) -$5.92B - 2024: Revenue $42.91B, Profit $12.83B - 2025: Revenue $62.98B, Profit $27.84B - Q1 2026: Revenue $34.08B, Profit $26.15B SK Hynix is on pace to bring in more than $100 Billion of PROFIT in 2026 which would be almost 4x more than 2025 SK Hynix will be listing its shares on the Nasdaq next week Shoutout to my partners over at Leverage Shares for making the graphic

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.