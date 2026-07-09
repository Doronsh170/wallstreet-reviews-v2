אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are a senior Wall Street investment advisor writing your signature END-OF-DAY review in Hebrew for
2026-07-08 (יום רביעי). PAST TENSE.

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
- Never write "נתון בפועל עדיין לא קיים". If a figure has not been released yet, give only the forecast (צפי) and the previous reading (נתון קודם).
- Never OPEN a bullet with a raw ticker like "$TSLA:" or "$AMZN:". Open with the Hebrew company name: "מניית טסלה (TSLA):", "מניית אמזון (AMZN):", "מניית מטא (META):".
- Finnhub and the measurement ETFs (SPY/QQQ/DIA/USO/BNO/GLD/UUP/VIXY/TLT...) are a hidden verification layer ONLY. NEVER mention Finnhub, "proxy", "דרך USO", "האינדיקציה מ-", or any technical data-source wording in the visible text — describe the asset itself (נפט, זהב, דולר, תשואות) directly.
- SIGN-FLIP: if the verified data shows a stock DOWN, do NOT describe it positively (עלתה/התחזקה/הובילה/בלטה לחיוב). If the news is positive but the stock fell, write: "למרות החדשות, המניה ירדה".

CRITICAL — OUTPUT FORMAT (MANDATORY):
- Return ONLY a JSON object, no backticks, no explanations, in EXACTLY this structure:
{
  "title": "סיכום יום המסחר בוול סטריט 🇺🇸 – יום רביעי, 8.7.2026",
  "date": "2026-07-08",
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

US-ISRAEL TIME OFFSET TODAY: +7 hours (add 7 hours to US Eastern Time)
Key times in Israel time today:
- US economic data releases (CPI, NFP, PPI, GDP, Jobless Claims): 15:30 שעון ישראל
- ISM PMI, JOLTS, Consumer Confidence: 17:00 שעון ישראל
- FOMC rate decision / minutes: 21:00 שעון ישראל | Fed Chair press conference: 21:30 שעון ישראל
- US market open: 16:30 שעון ישראל | US market close: 23:00 שעון ישראל
USE ONLY THESE TIMES. Do NOT calculate your own offset.

══ VERIFIED MARKET DATA (from Finnhub API — these are FACTS, do NOT override with guesses) ══
DAILY PERFORMANCE:
  S&P 500 (SPY ETF): $745.40 (daily: -0.31%), prev close: $747.71
  Nasdaq 100 (QQQ ETF): $711.44 (daily: +0.28%), prev close: $709.43
  Dow Jones (DIA ETF): $522.77 (daily: -1.07%), prev close: $528.45
  Russell 2000 (IWM ETF): $293.48 (daily: -0.92%), prev close: $296.19
  Energy Sector (XLE ETF): $55.60 (daily: +1.76%), prev close: $54.64
  Technology Sector (XLK ETF): $181.40 (daily: +1.24%), prev close: $179.18
  Financials Sector (XLF ETF): $54.97 (daily: -1.93%), prev close: $56.05
  Consumer Discretionary Sector (XLY ETF): $115.30 (daily: -1.78%), prev close: $117.39
  Healthcare Sector (XLV ETF): $162.30 (daily: -1.30%), prev close: $164.44
  Industrials Sector (XLI ETF): $180.42 (daily: -1.07%), prev close: $182.38
  Consumer Staples Sector (XLP ETF): $84.39 (daily: -0.55%), prev close: $84.86
  Utilities Sector (XLU ETF): $45.36 (daily: -0.74%), prev close: $45.70
  WTI Crude Oil (USO ETF): $112.21 (daily: +3.02%), prev close: $108.92
  Brent Crude Oil (BNO ETF): $43.57 (daily: +3.91%), prev close: $41.93
  Gold (GLD ETF): $374.45 (daily: -0.81%), prev close: $377.49
  Silver (SLV ETF): $52.83 (daily: -2.99%), prev close: $54.46
  Bitcoin (IBIT ETF): $35.23 (daily: -2.54%), prev close: $36.15
  US 20Y+ Bonds (TLT ETF): $84.36 (daily: -0.22%), prev close: $84.55
  US Dollar (UUP ETF): $28.36 (daily: -0.14%), prev close: $28.40
  VIX Volatility (VIXY ETF): $21.23 (daily: +1.73%), prev close: $20.87

INDIVIDUAL STOCKS mentioned in the source tweets (verified quotes):
  $META: $603.12 (daily: -2.02%), prev close: $615.58
  $SPCX: $148.30 (daily: -0.78%), prev close: $149.47
  $QQQ: $711.44 (daily: +0.28%), prev close: $709.43
  $SPY: $745.40 (daily: -0.31%), prev close: $747.71
  $USO: $112.21 (daily: +3.02%), prev close: $108.92
  $COST: $953.13 (daily: +0.59%), prev close: $947.50
  $AMD: $517.40 (daily: +0.25%), prev close: $516.11
  $MSFT: $383.34 (daily: -1.41%), prev close: $388.84
  $FDX: $309.76 (daily: -1.00%), prev close: $312.88
  $AMZN: $243.62 (daily: -0.96%), prev close: $245.98

DIRECTIONAL FACTS — Hebrew direction words (עולה/יורד/צונח/מזנק) MUST match these:
  נפט (WTI/ברנט): עולה (USO: +3.02%, BNO: +3.91%)
  זהב: יורד (GLD: -0.81%)
  ביטקוין: יורד (IBIT: -2.54%)
  דולר: יציב/כמעט ללא שינוי (UUP: -0.14%)
  תנודתיות / VIX: עולה (VIXY: +1.73%)
  אג"ח ארוכות / TLT: יורד (TLT: -0.22%)

The % changes above are ACCURATE — use them for direction and magnitude.
The ETF tickers above (SPY/QQQ/DIA/USO/GLD/...) are measurement instruments for YOUR verification only — NEVER name them, Finnhub, or the word 'proxy' in the visible Hebrew text.
For exact index LEVELS (points), gold/oil absolute prices, VIX level, Bitcoin price, 10Y yield: verify via web search. Do NOT estimate them from ETF prices.
For sector performance (XLE/XLK/...): USE ONLY the Finnhub numbers above — never invent sector percentages.
If ANY percentage you write contradicts the data above, you are WRONG. Fix it.
══════════════════════════════════════════════════════════════════════════════

══ MANDATORY MACRO DATA CHECK ══
Use web search to check if ANY of these were released on 2026-07-09: CPI (headline AND core),
PPI (headline AND core), NFP, Jobless Claims, Consumer Sentiment (Michigan), ISM PMI, GDP,
Retail Sales, FOMC decision/minutes. If released — include with actual, forecast, previous,
AND the market implication. If none — skip, but you MUST check first.
══════════════════════════════════

══ CONTEXT: THIS MORNING'S PRE-MARKET BRIEFING ══
Published before the session. Use it to resolve scheduled items (expected → actual), do NOT quote it verbatim.

[נקודות מרכזיות]
* סנטימנט זהיר ומוטה סיכון בפתיחה: וול סטריט צפויה להיפתח תחת ענן גיאופוליטי כבד אחרי שהצבא האמריקאי פתח בלילה בגל מתקפות נגד יעדים באיראן, ואיראן הגיבה בהאשמה שהמהלך מפר את מזכר ההבנות בין המדינות. הזרם אל נכסי המקלט ואל סחורות האנרגיה מכתיב את מצב הרוח, והמשקיעים יעקבו אחר השאלה אם ההסלמה תתרחב לפני פרסום פרוטוקול ה-Fed בהמשך היום. בסביבה כזו הרוטציה מהצמיחה אל הסקטורים הדפנסיביים עלולה להימשך גם היום.
* פרוטוקול ה-Fed במוקד היום: בשעה 21:00 שעון ישראל יפורסם פרוטוקול ישיבת הריבית האחרונה של הפדרל ריזרב, והוא צפוי להיות אירוע המאקרו המרכזי של המסחר בהיעדר נתון כלכלי כבד אחר בלוח. המשקיעים יחפשו בו רמזים לקצב הורדות הריבית ולמידת חילוקי הדעות בין חברי הוועדה. על רקע קפיצת מחירי הנפט והחשש מאינפלציית אנרגיה מתחדשת, כל נימה נצית בפרוטוקול עלולה להכביד על מניות הצמיחה שכבר נמצאות בלחץ.
* ההסלמה מול איראן דוחפת את הנפט: מחירי הנפט ממשיכים לטפס בחדות על רקע המשבר במפרץ הפרסי, כשה-WTI מוסיף כ-4.4% והברנט מזנק כ-5% אל מעל 76 דולר לחבית, לאחר שארה"ב ביטלה את רישיון הייצוא של איראן והחלה בתקיפות. מיצר הורמוז מעביר כחמישית מצריכת הנפט העולמית, ולכן כל החרפה נוספת בשיט בו מתורגמת מיידית לפרמיית סיכון על האנרגיה ולבריחה מנכסי צמיחה. השאלה המרכזית להיום היא אם גל התקיפות האמריקאי יתרחב או יתפוגג, שכן זה הגורם שיכתיב את כיוון הנפט ואת תיאבון הסיכון.
* שרשרת האספקה של ה-AI ממשיכה לרכז עניין: סביב מניות השבבים נמשכת זרימת חדשות חיובית שמנוגדת לחולשת המחירים בימים האחרונים. סמסונג החלה בייצור המוני של כונן האחסון המתקדם שלה שישולב בפלטפורמת Vera Rubin הקרובה של אנבידיה, אנבידיה מדווחת כי היא משלבת חומרה עם הסטארטאפ D-Matrix במערכת חדשה להרצת מודלים, ו-SK Hynix צפויה להכנסות של כ-231 מיליארד דולר השנה לעומת 67 מיליארד אשתקד. מניית אנבידיה (NVDA) עלתה במתינות של 0.71%, אך עוצמת הביקושים לתשתית ה-AI נותרת הסיפור המבני שמזין את המגזר.
* מניית ספייס-אקס (SPCX): עם תום תקופת השקט שלאחר ההנפקה פרסמה וול סטריט את גל יעדי המחיר הראשון שלה למניה, וטווח ההערכות חושף פערים דרמטיים בין האנליסטים. ריימונד ג'יימס הציב יעד של 800 דולר, שגלום בו שווי של כ-10 טריליון דולר, בעוד יתר היעדים נעים סביב 200 עד 300 דולר, זאת מול מחיר נוכחי של כ-150 דולר. למרות ההתלהבות והדיווח שקאתי ווד וקרן ARK רכשו כ-44 אלף מניות, המניה עצמה ירדה 6.83% ונסחפה עם החולשה הרוחבית במניות הצמיחה.
* מניית פינגווין סולושנס (PENG): החברה פרסמה דוחות רבעון שלישי חזקים במיוחד, עם הכנסות שיא של 478.7 מיליון דולר מול צפי של 421.4 מיליון, רווח מתואם למניה של 0.84 דולר מול צפי של 0.56 דולר, והעלאת תחזית הרווח השנתית ל-2.60 דולר למניה. הצמיחה הובלה על ידי זינוק של 111% בהכנסות הזיכרון המשולב על רקע ביקושי ה-AI. למרות התוצאות המרשימות המניה ירדה 7.38%, עדות לרף הציפיות הגבוה שהשוק מציב כעת בפני מניות ה-AI.
* מניית מטא (META): החברה משיקה את Muse Image, מודל יצירת התמונות הראשון שלה ממעבדות Meta Superintelligence Labs, במהלך שממצב אותה בחזית מרוץ ה-AI הגנרטיבי מול OpenAI וגוגל. המניה בלטה לחיוב עם עלייה של 2.55% והייתה מהבודדות בקבוצת המגה-קאפ הטכנולוגית שהתנתקו מהסנטימנט השלילי שרבץ על המגזר. עבור המשקיעים זהו אות נוסף לכך שמטא ממירה את השקעות ה-AI הכבדות שלה למוצרים ממשיים.
* שורה תחתונה: כיוון המסחר היום ייקבע בצומת של שני כוחות, ההתפתחויות במפרץ הפרסי שיכתיבו את מחיר הנפט ואת מפלס החשש, ופרוטוקול ה-Fed ב-21:00 שעון ישראל שיאותת על נתיב הריבית. כל עוד ההסלמה נמשכת והנפט מזנק, הלחץ על מניות הצמיחה והטכנולוגיה עלול להימשך, בעוד סקטור האנרגיה והנכסים הדפנסיביים ממשיכים ליהנות מהבריחה מסיכון.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-09. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Thu Jul 09 00:02:35 +0000 2026]: Tech stocks are experiencing one of their most volatile periods in history: The ratio of the Nasdaq 100 volatility index, $VXN, to the S&P 500 volatility index, $VIX, is up to 1.7 points, the highest in 23 years. This marks the first time since 2018 that the ratio has surpassed 1.5 points. By comparison, during the 2008 Financial Crisis, this metric peaked at ~1.6 points. This comes as $VXN stands at 28 points while the $VIX is at 16 points, or 43% lower. $VXN has now been above 20 points for 5 consecutive months, the longest streak since the 2022 bear market. The market is pricing-in severe volatility in tech.

@gurgavin [Wed Jul 08 19:47:47 +0000 2026]: META TO INVEST $10 BILLION IN CANADA META IS LOOKING TO BUILD ITS FIRST DATA CENTER IN CANADA TO SUPPORT ITS AI AMBITIONS THE DATA CENTER WILL BE IN ALBERTA AND CREATE OVER 3,000 LOCAL CONSTRUCTION JOBS 🇨🇦🇨🇦🇨🇦 🇨🇦 $META

@gurgavin [Tue Jul 07 23:28:39 +0000 2026]: ALL 1 YEAR SPACEX PRICE TARGETS ARE HERE AS THE QUIET PERIOD ENDED TODAY $SPCX RAYMOND JAMES $800 MORGAN STANLEY $300 DEUTSCHE BANK $255 OPPENHEIMER $250 CANTOR FITZGERALD $246 BERNSTEIN $239 BANK OF AMERICA $235 WELLS FARGO $230 RBC $225 JP MORGAN $225 UBS $210 GOLDMAN SACHS $205 NEEDHAM $200 CURRENT PRICE $150

@gurgavin [Mon Jul 06 19:52:14 +0000 2026]: SPACEX WILL BE ADDED TO THE NASDAQ 100 INDEX TOMORROW THIS IS THE QUICKEST TIME EVER FOR A COMPANY TO BE ADDED TO THE NASDAQ 100 INDEX $SPCX

@wallstengine [Wed Jul 08 19:35:09 +0000 2026]: $META will invest about $10B to build its first data center in Canada, a 1GW facility in Sturgeon County, Alberta, largely powered by natural gas. The project is expected to need 3,000 construction workers and create 300 full-time jobs. https://t.co/8jZ7JSeFuq

@gurgavin [Wed Jul 08 00:06:20 +0000 2026]: RAYMOND JAMES SAYS SPACEX SHOULD BE WORTH $800 1 YEAR FROM NOW THAT VALUES SPACEX AT $10 TRILLION DOLLARS WHAT ARE THEY ON ??? $SPCX

@StockMKTNewz [Wed Jul 08 20:16:04 +0000 2026]: $AMD just confirmed it will be reporting earnings after the markets close on Tuesday, August 4th https://t.co/LABHmTHU0p

@StockMKTNewz [Wed Jul 08 20:07:26 +0000 2026]: Microsoft $MSFT just confirmed it will be reporting earnings after the stock markets close on Wednesday, July 29th https://t.co/rBef0bhPKw

@StockMKTNewz [Wed Jul 08 19:34:30 +0000 2026]: Mark Zuckerberg and Meta Platforms $META just announced plans to invest $10 Billion to build its first data center in Canada 🇨🇦 https://t.co/wCDSVLnVHj

@wallstengine [Wed Jul 08 22:33:19 +0000 2026]: SK HYNIX’S $SKHY U.S. LISTING IS NOW MORE THAN 7 TIMES OVERSUBSCRIBED, WITH PRICING SET FOR THURSDAY.

@StockMKTNewz [Wed Jul 08 23:57:16 +0000 2026]: Jim Cramer just said today he thinks the selling in FedEx $FDX stock has created a buying opportunity https://t.co/bOwP8HZHvV

@StockMKTNewz [Wed Jul 08 19:44:11 +0000 2026]: Amazon Web Services $AMZN just announced plans to invest $5 Billion in the Philippines 🇵🇭 over the next 15 years https://t.co/ZkorfkIplp

@AIStockSavvy [Wed Jul 08 22:39:31 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: President Trump said Iran phoned moments ago and said it wants to reach a deal. - CNN - $QQQ $SPY $USO

@KobeissiLetter [Wed Jul 08 18:40:17 +0000 2026]: BREAKING: Nasdaq 100 futures erase all losses and turn green on the day after President Trump says the Iran ceasefire is “over.” https://t.co/YFNFSoNc9X

@KobeissiLetter [Wed Jul 08 16:50:00 +0000 2026]: BREAKING: Tokenized equities saw a record $3.4 billion in volume for the month of June. This marks +279% month-over-month growth and +1,400% year-over-year growth. The growth was primarily driven by SpaceX's record IPO and surging demand for 24/7 trading. Furthermore, the Solana network now accounts for over 90% of volume traded in these assets. A substantial amount of this volume growth has been driven by Jupiter, the largest onchain platform in the world, which has seen MoM volume growth of +56%, with ~60% of tokenized equity volume happening during off hours and weekends. Tokenized asset growth is exploding.

@gurgavin [Wed Jul 08 18:08:57 +0000 2026]: FOMC MEETING MINUTES ARE OUT *ALL FOMC PARTICIPANTS SUPPORTED KEEPING INTEREST RATES UNCHANGED, THOUGH A FEW SAW A CASE FOR A RATE HIKE *FED STAFF RAISED THEIR 2026–2027 INFLATION FORECASTS, LOWERED GDP GROWTH PROJECTIONS, AND SAW UPSIDE RISKS TO PRICE STABILITY

@AIStockSavvy [Wed Jul 08 22:39:04 +0000 2026]: $ONDS | Stifel reiterates 𝐁𝐮𝐲 on 𝐎𝐧𝐝𝐚𝐬 𝐇𝐨𝐥𝐝𝐢𝐧𝐠𝐬, maintains 𝐏𝐓 𝐚𝐭 $𝟏𝟖 Analyst sees the DZYNE acquisition as a strategic expansion of ONDS's defense tech portfolio, validating their positive thesis despite integration risks. https://t.co/PS5ePw8Mcp

@wallstengine [Wed Jul 08 20:16:09 +0000 2026]: $LEVI Q2’26 EARNINGS HIGHLIGHTS 🔹 Net Revenue: $1.562B (Est. $1.52B) 🟡; +8% 🔹 Adj. EPS: $0.28 (Est. $0.24) 🟢; +27% YoY 🔹 Gross Margin: 62.7%; +10 bps 🔹 Adj. EBIT Margin: 9.0%; +70 bps 🔹 DTC Revenue: +11% reported; 51% of total revenue FY Guide: 🔹 Adj. EPS: $1.46-$1.52 (Est. $1.51) 🟡 🔹 Reported Net Revenue Growth: Raised to 7.0%-7.5% 🔹 Organic Net Revenue Growth: Raised to 5.5%-6.0% Segment Revenue: 🔹 Americas: $815M; +9% reported, +7% organic 🔹 Europe: $420M; +4% reported, -1% organic 🔹 Asia: $284M; +10% reported, +12% organic 🔹 Beyond Yoga: $43M; +16% reported and organic Other Metrics: 🔹 E-commerce: +19% reported, +17% organic 🔹 DTC Comparable Sales Growth: +6% 🔹 Inventories: Down 7% YoY Capital Return: 🔹 Dividend: Increased to $0.16/share, +14% YoY

@wallstengine [Wed Jul 08 20:09:14 +0000 2026]: Honeywell Technologies $HON revised 2026 adjusted EPS guidance to $7.90-$8.30 from $3.95-$4.15 after a 1-for-2 reverse stock split cut shares to 317M. Sales guidance stays at $19.9B-$20.2B and full-year free cash flow remains about $2B.

@StockMKTNewz [Thu Jul 09 00:19:39 +0000 2026]: Cathie Wood and Ark Invest bought 181,847 shares of SpaceX $SPCX today https://t.co/sw9jUX3adQ

@StockMKTNewz [Wed Jul 08 20:17:52 +0000 2026]: Costco $COST just reported June sales of $29.24 Billion up 10.6% YoY https://t.co/19U4ng4QvY

@KobeissiLetter [Thu Jul 09 02:16:09 +0000 2026]: BREAKING: President Trump says Iran called him and “they want to make a deal so badly.” US stock market futures turn green on the news. https://t.co/1MkYnxxkCK

@KobeissiLetter [Wed Jul 08 21:47:14 +0000 2026]: BREAKING: President Trump says “it will get much worse” if Iran attacks ships in the Strait of Hormuz again. https://t.co/kn8xRu6mA7

@KobeissiLetter [Wed Jul 08 20:19:47 +0000 2026]: BREAKING: US CENTCOM announces that the US has begun conducting additional strikes in Iran. These strikes are intended to "further degrade Iran's ability to threaten freedom of navigation in the Strait of Hormuz," CENTCOM says.

@KobeissiLetter [Wed Jul 08 17:50:01 +0000 2026]: Gold is entering a historically favorable period of the year: Gold prices have gained +1.5% in July on average over the last 20 years, making it the 2nd-strongest month of the year. Gold prices have also recorded positive returns in 65% of July months, the 2nd-best win rate of any month. The strongest July over this period was in 2020, when gold returned +10.7%. The only better month historically has been August, with an average gain of +1.6% since 2005. August also posted a 55% win rate, with its strongest year coming in 2011, when gold returned +12.1%. By comparison, June has historically been the weakest month, with an average decline of -0.4% and just 40% positive readings since 2005. Seasonality is turning in favor of gold bulls.

@gurgavin [Wed Jul 08 09:16:40 +0000 2026]: FUTURES UPDATE S&amp;P 500 DOWN 1.1% 📉 DOW JONES DOWN 1.4% 📉 NASDAQ 100 DOWN 1.6% 📉

@AIStockSavvy [Thu Jul 09 01:54:52 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: After earlier US airstrikes, Iran again launched missiles and drones at Gulf states. - Fox News - $QQQ $SPY $USO

@AIStockSavvy [Thu Jul 09 01:43:21 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: $META Meta Reportedly Developing Always-On AI Smart Glasses - The Verge 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ Meta is reportedly developing 𝐚𝐥𝐰𝐚𝐲𝐬-𝐨𝐧 "𝐬𝐮𝐩𝐞𝐫 𝐬𝐞𝐧𝐬𝐢𝐧𝐠" AI smart glasses. ➤ Prototype glasses could 𝐜𝐨𝐧𝐭𝐢𝐧𝐮𝐨𝐮𝐬𝐥𝐲 record audio and capture photos every few seconds. ➤ Meta AI would use captured data to answer 𝐜𝐨𝐧𝐭𝐞𝐱𝐭-𝐚𝐰𝐚𝐫𝐞 user queries. ➤ Report says 𝐫𝐚𝐰 𝐚𝐮𝐝𝐢𝐨 and images may not be stored or accessible. ➤ Instead, extracted 𝐦𝐞𝐭𝐚𝐝𝐚𝐭𝐚 could be uploaded for AI processing. ➤ Report says the recording 𝐋𝐄𝐃 𝐢𝐧𝐝𝐢𝐜𝐚𝐭𝐨𝐫 may remain off in "super sensing" mode. ➤ Meta is also discussing using captured data to 𝐭𝐫𝐚𝐢𝐧 𝐀𝐈 models. ➤ The feature could reportedly arrive on 𝐞𝐱𝐢𝐬𝐭𝐢𝐧𝐠 Ray-Ban Meta smart glasses. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ Always-on sensing could significantly expand 𝐀𝐈 𝐰𝐞𝐚𝐫𝐚𝐛𝐥𝐞 capabilities. ➤ The reported design may intensify 𝐩𝐫𝐢𝐯𝐚𝐜𝐲 and surveillance concerns. ➤ The move could strengthen Meta's competition in the 𝐀𝐈 𝐰𝐞𝐚𝐫𝐚𝐛𝐥𝐞 market. 👉 𝐄𝐱𝐩𝐞𝐫𝐭 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭: ➤ "While we don't comment on internal prototypes, we're committed to getting our glasses right because they need to be loved by both people wearing them and those around them." — 𝐃𝐚𝐯𝐞 𝐀𝐫𝐧𝐨𝐥𝐝, Meta Spokesperson. ➤ "Our approach has been to develop new technologies that will help people throughout their day, with privacy built in from the ground up." — 𝐃𝐚𝐯𝐞 𝐀𝐫𝐧𝐨𝐥𝐝, Meta Spokesperson.

@AIStockSavvy [Wed Jul 08 22:42:03 +0000 2026]: $AMAT | Mizuho Securities 𝐫𝐚𝐢𝐬𝐞𝐬 𝐏𝐓 on 𝐀𝐩𝐩𝐥𝐢𝐞𝐝 𝐌𝐚𝐭𝐞𝐫𝐢𝐚𝐥𝐬 𝐈𝐧𝐜. to $𝟔𝟓𝟎 from $𝟓𝟒𝟎, maintains 𝐁𝐮𝐲 https://t.co/JFk9wqXV8y

@AIStockSavvy [Wed Jul 08 22:35:25 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: SK Hynix's US IPO was more than seven times oversubscribed. - Bloomberg - $MU $SNDK

@AIStockSavvy [Wed Jul 08 22:34:50 +0000 2026]: $NOW | 𝐆𝐨𝐥𝐝𝐦𝐚𝐧 𝐒𝐚𝐜𝐡𝐬 maintains 𝐁𝐮𝐲 on 𝐒𝐞𝐫𝐯𝐢𝐜𝐞𝐍𝐨𝐰, 𝐜𝐮𝐭𝐬 𝐏𝐓 𝐭𝐨 $𝟏𝟒𝟓 https://t.co/V9aySjvEO9

@wallstengine [Wed Jul 08 20:20:56 +0000 2026]: $AZZ Q1’27 EARNINGS HIGHLIGHTS 🔹 Revenue: $448.5M (Est. $434.53M) 🟢 🔹 EPS: $1.85 (Est. $1.69) 🟢 FY Guide: 🔹 Revenue: $1.8B-$1.85B (Est. $1.75B) 🟢 🔹 EPS: $6.75-$7.15 (Est. $6.83) 🟡 https://t.co/WVs1Wq82GJ

@KobeissiLetter [Thu Jul 09 01:19:34 +0000 2026]: BREAKING: The Index of US Financial Conditions is up to ~1.2 points, the easiest since February 2026. This is also near the highest level in at least 11 years. Since 2015, similar readings have only been recorded in early 2025 and during 2021, before the Fed started hiking rates. The Financial Conditions Index has risen over +1.0 points since the March low. Most of this surge has come from rising equity markets and falling corporate bond spreads. Financial conditions are easing despite the recent increase in inflation.

@KobeissiLetter [Wed Jul 08 23:29:48 +0000 2026]: Agentic AI continues to see rapid growth. Over the last 12 months, the focus has rapidly shifted toward the software layer that allows AI to connect with enterprise data and applications. Instead of simply answering questions, these systems can access company databases, analyze documents, execute multi-step tasks, and automate entire business processes with minimal human input. In other words, AI is evolving from a chatbot into a digital employee. As a result, the enterprise AI market is now expected to exceed $155 billion by 2030. This is why virtually every major technology company is racing to build AI agents. The next phase of the AI Revolution has arrived.

@gurgavin [Wed Jul 08 08:19:57 +0000 2026]: *TRUMP SAYS IRAN CEASE FIRE IS OVER HERE WE GO AGAIN

@AIStockSavvy [Wed Jul 08 22:37:52 +0000 2026]: $SRPT | Wolfe Research 𝐮𝐩𝐠𝐫𝐚𝐝𝐞𝐬 𝐒𝐚𝐫𝐞𝐩𝐭𝐚 𝐭𝐨 𝐎𝐮𝐭𝐩𝐞𝐫𝐟𝐨𝐫𝐦, sets 𝐏𝐓 𝐚𝐭 $𝟐𝟕 Analyst sees a shift in stock performance driven by a new market regime, upcoming MAD data in H2, and increased investor focus on DM1/FSHD. https://t.co/5zz0CVRn5v

@AIStockSavvy [Wed Jul 08 20:35:38 +0000 2026]: Iranian armed forces to launch 'massive' attack on U.S. army bases in the region shortly - Iran's Nournews - $QQQ $SPY $USO

@AIStockSavvy [Wed Jul 08 20:30:22 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: $COST Costco Reports 10.6% Jump in July Net Sales 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐂𝐨𝐬𝐭𝐜𝐨 reported 𝐉𝐮𝐥𝐲 net sales of 𝟐𝟗.𝟐𝟒 𝐛𝐢𝐥𝐥𝐢𝐨𝐧, up 𝟏𝟎.𝟔% year over year. ➤ Fiscal year-to-date net sales reached 𝟐𝟓𝟎.𝟒𝟑 𝐛𝐢𝐥𝐥𝐢𝐨𝐧, increasing 𝟏𝟎.𝟏%. ➤ Five-week 𝐜𝐨𝐦𝐩𝐚𝐫𝐚𝐛𝐥𝐞 𝐬𝐚𝐥𝐞𝐬 rose 𝟖.𝟖% companywide. ➤ U.S. comparable sales increased 𝟏𝟎.𝟔%, while Canada rose 𝟑.𝟕%. ➤ Other international comparable sales advanced 𝟒.𝟕% during the five-week period. ➤ 𝐃𝐢𝐠𝐢𝐭𝐚𝐥𝐥𝐲-𝐞𝐧𝐚𝐛𝐥𝐞𝐝 sales surged 𝟐𝟎.𝟗% for the five-week period. ➤ Adjusted comparable sales rose 𝟕.𝟎%, excluding fuel price and foreign exchange impacts. ➤ Fiscal year-to-date digitally-enabled sales increased 𝟐𝟏.𝟓%.

@wallstengine [Wed Jul 08 20:17:18 +0000 2026]: $COST JUNE TOTAL COMP SALES +8.8%, EST. +9.8% COSTCO JUNE US COMP SALES EX-GAS, FX +7.6%, EST. +7.8%

@StockMKTNewz [Wed Jul 08 22:32:17 +0000 2026]: SK Hynix's IPO is reportedly more than 7x oversubscribed

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.