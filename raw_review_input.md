אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are a senior Wall Street investment advisor writing your signature PRE-MARKET briefing in Hebrew.
Script run date: 2026-07-09 (יום חמישי). Briefing target date: 2026-07-09 (יום חמישי).
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
  "title": "נקודות חשובות לקראת פתיחת המסחר בוול סטריט 🇺🇸 – יום חמישי, 9.7.2026",
  "date": "2026-07-09",
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
  $MU: $948.80 (daily: +1.11%), prev close: $938.38
  $SNDK: $1727.18 (daily: +6.77%), prev close: $1617.70
  $FIX: $1684.94 (daily: +0.09%), prev close: $1683.44
  $AMD: $517.40 (daily: +0.25%), prev close: $516.11
  $MSFT: $383.34 (daily: -1.41%), prev close: $388.84
  $FDX: $309.76 (daily: -1.00%), prev close: $312.88

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

══ SCHEDULED DATA CHECK ══
Use web search to find what US economic data is scheduled for release on 2026-07-09.
Include the release time in Israel time and the market consensus/forecast.
══════════════════════════════════

══ CONTEXT: YESTERDAY'S DAILY SUMMARY — DO NOT REPEAT THIS CONTENT ══
Already published. Your briefing is FORWARD-LOOKING. Mention an item below ONLY if there is a genuinely NEW overnight development about it.

[סיכום המסחר]
* מסחר מפוצל שהסתיים מעורב: וול סטריט חתמה יום תנודתי במיוחד עם תמונה מפוצלת בין המדדים, כשמדד ה-S&P 500 נסוג ב-0.31% ומדד הדאו ג'ונס איבד 1.07%, בעוד מדד הנאסד"ק 100 הצליח להתאושש ולסגור בעלייה קלה של 0.28%. המסחר נפתח בירידות חדות, כשחוזי המדדים איתתו על פתיחה שלילית של עד 1.6% בנאסד"ק על רקע ההסלמה מול איראן, אך התאוששות הדרגתית לאורך היום צמצמה את ההפסדים לאחר שנשמעו רמזים לרצון איראני בהסכם. סקטור הפיננסים בלט לרעה עם צניחה של 1.93% והכביד על המדדים הרחבים.
* איראן מכתיבה את מצב הרוח: הסיפור המרכזי של היום היה ההסלמה הצבאית במפרץ הפרסי, לאחר שפיקוד המרכז האמריקאי (CENTCOM) הודיע על סבב תקיפות נוסף באיראן שנועד לצמצם את יכולתה לאיים על חופש השיט במיצר הורמוז. איראן הגיבה בשיגור טילים ומזל"טים לעבר מדינות המפרץ, מהלך שהזרים ביקוש אל נכסי המקלט ואל האנרגיה והכביד על מניות הצמיחה. לקראת סגירת המסחר נרשם היפוך כשהנשיא טראמפ מסר כי איראן פנתה אליו ומעוניינת מאוד בהסכם, אמירה ששלחה את חוזי הנאסד"ק בחזרה אל הטריטוריה החיובית.
* הנפט ממשיך לטפס בחדות: מחירי הנפט זינקו על רקע פרמיית הסיכון סביב מיצר הורמוז, כשה-WTI הוסיף 3.02% והברנט קפץ ב-3.91% ורשם את אחת העליות החדות בשוק. סקטור האנרגיה היה המוביל הבולט של היום עם עלייה של 1.76%, וכמעט הסקטור היחיד שנצבע בירוק לצד הטכנולוגיה שהוסיפה 1.24%. מיצר הורמוז מעביר כחמישית מצריכת הנפט העולמית, ולכן כל חשש להפרעה בשיט בו מתומחר מיידית כפרמיית סיכון על מחירי האנרגיה.
* פרוטוקול ה-Fed בנימה נצית: פרוטוקול ישיבת הריבית האחרונה של הפדרל ריזרב שפורסם היום חשף עמדה נצית מהצפוי, כשכל חברי הוועדה תמכו בהותרת הריבית ללא שינוי אך אחדים אף ראו הצדקה להעלאת ריבית. הצוות הכלכלי של ה-Fed העלה את תחזיות האינפלציה לשנים 2026–2027, הוריד את תחזיות צמיחת התוצר, וציין סיכונים כלפי מעלה ליציבות המחירים. על רקע קפיצת מחירי הנפט, השילוב של אינפלציה גבוהה יותר וצמיחה איטית יותר הכביד על ציפיות הריבית ועל מניות הצמיחה.
* מניית מטא (META): החברה המשיכה להזרים חדשות עסקיות חיוביות סביב שאיפות ה-AI שלה, ובהן תוכנית להשקיע כ-10 מיליארד דולר בהקמת מרכז הנתונים הראשון שלה בקנדה במחוז אלברטה ודיווחים על פיתוח משקפי AI חכמים בעלי יכולת חישה מתמדת. אולם למרות זרם הבשורות המניה ירדה ב-2.02% ונסחפה עם הסנטימנט השלילי שרבץ על המגה-קאפ הטכנולוגית ביום מוטה סיכון. עבור המשקיעים זו תזכורת שאפילו חדשות חיוביות אינן חסינות מפני לחצי מאקרו רוחביים.
* מניית ספייס-אקס (SPCX): עם תום תקופת השקט שלאחר ההנפקה פרסמו בתי ההשקעות את גל יעדי המחיר הראשון למניה, וטווח ההערכות חשף פערים דרמטיים בין האנליסטים. ריימונד ג'יימס בלטה עם יעד של 800 דולר הגלום בשווי של כ-10 טריליון דולר, בעוד מרבית הבנקים מתמקמים בטווח של כ-200 עד 300 דולר, זאת מול מחיר נוכחי של כ-150 דולר. קאתי ווד וקרן ARK ניצלו את התנודתיות ורכשו כ-182 אלף מניות, אך המניה עצמה נסוגה ב-0.78% ביום החלש למניות הצמיחה.
* מניית קוסטקו (COST): הקמעונאית דיווחה על מכירות יוני חזקות שהגיעו ל-29.24 מיליארד דולר, זינוק של 10.6% בהשוואה לשנה שעברה, כשגם המכירות בארה"ב קפצו ב-10.6%. הנתון החזק, לצד גידול של יותר מ-20% במכירות המקוונות, ביסס את קוסטקו כאחת הנקודות היציבות ביום סוער, והמניה נסגרה בעלייה קלה של 0.59%. בסביבה מוטת סיכון המשקיעים חזרו אל הקמעונאות הדפנסיבית עם ביקושי צריכה יציבים.
* שורה תחתונה למחר: תשומת הלב תופנה בראש ובראשונה להתפתחויות במפרץ הפרסי, והשאלה אם קו הפיוס שאותת טראמפ יחזיק או שההסלמה תתחדש, שכן זה יכתיב את כיוון הנפט ואת תיאבון הסיכון. במקביל, הנימה הנצית בפרוטוקול ה-Fed והחשש מאינפלציית אנרגיה מתחדשת עלולים להמשיך להעיב על מניות הצמיחה, בעוד התנודתיות במניות הטכנולוגיה טיפסה לרמות הגבוהות ביותר מזה שנים. משקיע נבון יעקוב אחר מחיר הנפט ואחר סקטור הפיננסים שהוביל את הירידות.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-09. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Thu Jul 09 00:02:35 +0000 2026]: Tech stocks are experiencing one of their most volatile periods in history: The ratio of the Nasdaq 100 volatility index, $VXN, to the S&P 500 volatility index, $VIX, is up to 1.7 points, the highest in 23 years. This marks the first time since 2018 that the ratio has surpassed 1.5 points. By comparison, during the 2008 Financial Crisis, this metric peaked at ~1.6 points. This comes as $VXN stands at 28 points while the $VIX is at 16 points, or 43% lower. $VXN has now been above 20 points for 5 consecutive months, the longest streak since the 2022 bear market. The market is pricing-in severe volatility in tech.

@gurgavin [Wed Jul 08 19:47:47 +0000 2026]: META TO INVEST $10 BILLION IN CANADA META IS LOOKING TO BUILD ITS FIRST DATA CENTER IN CANADA TO SUPPORT ITS AI AMBITIONS THE DATA CENTER WILL BE IN ALBERTA AND CREATE OVER 3,000 LOCAL CONSTRUCTION JOBS 🇨🇦🇨🇦🇨🇦 🇨🇦 $META

@gurgavin [Tue Jul 07 23:28:39 +0000 2026]: ALL 1 YEAR SPACEX PRICE TARGETS ARE HERE AS THE QUIET PERIOD ENDED TODAY $SPCX RAYMOND JAMES $800 MORGAN STANLEY $300 DEUTSCHE BANK $255 OPPENHEIMER $250 CANTOR FITZGERALD $246 BERNSTEIN $239 BANK OF AMERICA $235 WELLS FARGO $230 RBC $225 JP MORGAN $225 UBS $210 GOLDMAN SACHS $205 NEEDHAM $200 CURRENT PRICE $150

@gurgavin [Mon Jul 06 19:52:14 +0000 2026]: SPACEX WILL BE ADDED TO THE NASDAQ 100 INDEX TOMORROW THIS IS THE QUICKEST TIME EVER FOR A COMPANY TO BE ADDED TO THE NASDAQ 100 INDEX $SPCX

@wallstengine [Thu Jul 09 09:20:46 +0000 2026]: Goldman Sachs Initiates Coverage on $FIX with Buy Rating, PT $2,159 Analyst comments: "Comfort Systems USA is a leading mechanical and electrical contractor with significant leverage to the AI infrastructure build-out, with data centers and semiconductors representing 56% of sales. We forecast a 23% organic growth CAGR from 2025–2028E, as leading indicators point to strong data center demand growth in the medium term, with FIX’s overweight exposure to Texas positioning it to outgrow the market. Our work suggests data center projects carry meaningfully higher margins, and we expect continued margin expansion, driven by rising data center mix. While we think data center capex will eventually moderate, the timing of any such moderation remains uncertain, and in the interim there is visibility into another year of double-digit hyperscaler capex growth in 2027. To date, FIX's stock has acted as a relatively pure-play beneficiary of rising hyperscaler data center capex. Our EBITDA estimates are 9% above FactSet consensus for 2026/2027, driven by our higher revenue estimates. While we see limited scope for further multiple expansion, we expect valuation to remain elevated near current levels so long as FIX's medium-term organic growth outlook remains robust and margins continue to expand." Analyst: Adam Bubes

@gurgavin [Wed Jul 08 00:06:20 +0000 2026]: RAYMOND JAMES SAYS SPACEX SHOULD BE WORTH $800 1 YEAR FROM NOW THAT VALUES SPACEX AT $10 TRILLION DOLLARS WHAT ARE THEY ON ??? $SPCX

@StockMKTNewz [Wed Jul 08 20:16:04 +0000 2026]: $AMD just confirmed it will be reporting earnings after the markets close on Tuesday, August 4th https://t.co/LABHmTHU0p

@StockMKTNewz [Wed Jul 08 20:07:26 +0000 2026]: Microsoft $MSFT just confirmed it will be reporting earnings after the stock markets close on Wednesday, July 29th https://t.co/rBef0bhPKw

@StockMKTNewz [Wed Jul 08 19:34:30 +0000 2026]: Mark Zuckerberg and Meta Platforms $META just announced plans to invest $10 Billion to build its first data center in Canada 🇨🇦 https://t.co/wCDSVLnVHj

@StockMKTNewz [Wed Jul 08 23:57:16 +0000 2026]: Jim Cramer just said today he thinks the selling in FedEx $FDX stock has created a buying opportunity https://t.co/bOwP8HZHvV

@wallstengine [Thu Jul 09 09:53:29 +0000 2026]: Mizuho Upgrades $FIVE to Outperform from Neutral, PT $220 Analyst comments: "We now see a more favorable risk/reward profile for a business with sustained momentum and a merchandising team fully dialed in. Comparable sales will decelerate from here following a squishy-induced +22.7% gain in Q1; however, we do not view this as an impediment to owning the shares. Our positive view contemplates: (1) upside to second-half Street estimates as new customers are being retained extremely well; (2) paid Instagram and TikTok influencers are amplifying trends and expanding the company’s reach across core customer demographics; and (3) EBIT margin should expand further as average store volumes build closer to $3 million per unit versus the historical $2 million+ per store. At current levels, we believe the pendulum has swung too far on valuation. Our $220 price target implies upside potential of more than 20%." Analyst: David Bellinger

@wallstengine [Thu Jul 09 09:18:37 +0000 2026]: B. Riley Raises $BAND PT to $85 from $55 - Buy Analyst comments: "We are also slightly increasing our FY27 estimates to reflect higher growth fueled by advances in AI voice technology that we believe will accelerate demand for Bandwidth. Since we first highlighted advances in AI voice technology by frontier model developers OpenAI and Google, we believe each of them has continued to advance their AI voice capabilities, and xAI has announced advances in its AI voice capabilities as well. Furthermore, developments at Microsoft suggest the company is also aggressively developing AI voice technologies for its AI models and for AI agents in Microsoft’s productivity applications. We believe the focus on AI voice technology by frontier model developers and large-scale enterprise software developers reaffirms our thesis that AI voice will become a primary mode of communication with AI software. Our previous note discussed advances that make AI voice sound more natural, whereas some of the more recent advances make voice agents work reliably in production. We believe that as AI voice expands the market for carrier-grade voice connectivity, Bandwidth's specialization in digital voice services positions the company as a primary infrastructure beneficiary." Analyst: Erik Suppiger

@StockMKTNewz [Wed Jul 08 19:44:11 +0000 2026]: Amazon Web Services $AMZN just announced plans to invest $5 Billion in the Philippines 🇵🇭 over the next 15 years https://t.co/ZkorfkIplp

@AIStockSavvy [Wed Jul 08 22:39:31 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: President Trump said Iran phoned moments ago and said it wants to reach a deal. - CNN - $QQQ $SPY $USO

@KobeissiLetter [Wed Jul 08 18:40:17 +0000 2026]: BREAKING: Nasdaq 100 futures erase all losses and turn green on the day after President Trump says the Iran ceasefire is “over.” https://t.co/YFNFSoNc9X

@KobeissiLetter [Wed Jul 08 16:50:00 +0000 2026]: BREAKING: Tokenized equities saw a record $3.4 billion in volume for the month of June. This marks +279% month-over-month growth and +1,400% year-over-year growth. The growth was primarily driven by SpaceX's record IPO and surging demand for 24/7 trading. Furthermore, the Solana network now accounts for over 90% of volume traded in these assets. A substantial amount of this volume growth has been driven by Jupiter, the largest onchain platform in the world, which has seen MoM volume growth of +56%, with ~60% of tokenized equity volume happening during off hours and weekends. Tokenized asset growth is exploding.

@gurgavin [Wed Jul 08 18:08:57 +0000 2026]: FOMC MEETING MINUTES ARE OUT *ALL FOMC PARTICIPANTS SUPPORTED KEEPING INTEREST RATES UNCHANGED, THOUGH A FEW SAW A CASE FOR A RATE HIKE *FED STAFF RAISED THEIR 2026–2027 INFLATION FORECASTS, LOWERED GDP GROWTH PROJECTIONS, AND SAW UPSIDE RISKS TO PRICE STABILITY

@AIStockSavvy [Thu Jul 09 10:20:23 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: $CBRS Cerebras Expands European AI Infrastructure, Targets 200 MW by 2027 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐂𝐞𝐫𝐞𝐛𝐫𝐚𝐬 will launch its first 𝐄𝐮𝐫𝐨𝐩𝐞𝐚𝐧 data center capacity by the end of 2026. ➤ Company plans rapid expansion across 𝐅𝐫𝐚𝐧𝐜𝐞, 𝐍𝐨𝐫𝐰𝐚𝐲, and 𝐅𝐢𝐧𝐥𝐚𝐧𝐝. ➤ Total AI infrastructure capacity is targeted to reach 𝟐𝟎𝟎 𝐌𝐖 by the end of 2027. ➤ A portion of the new capacity is expected to support 𝐎𝐩𝐞𝐧𝐀𝐈 workloads. ➤ Expansion aims to deliver 𝐟𝐚𝐬𝐭𝐞𝐫 𝐀𝐈 𝐢𝐧𝐟𝐞𝐫𝐞𝐧𝐜𝐞 and lower latency for European users. ➤ Infrastructure is designed to meet rising demand from 𝐞𝐧𝐭𝐞𝐫𝐩𝐫𝐢𝐬𝐞𝐬, researchers, and governments. ➤ Cerebras said its 𝐰𝐚𝐟𝐞𝐫-𝐬𝐜𝐚𝐥𝐞 architecture enables industry-leading AI inference and training. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ European expansion strengthens regional access to 𝐥𝐨𝐜𝐚𝐥 𝐀𝐈 𝐜𝐨𝐦𝐩𝐮𝐭𝐞. ➤ Additional capacity could support growing demand for 𝐥𝐨𝐰-𝐥𝐚𝐭𝐞𝐧𝐜𝐲 AI services. ➤ Expansion deepens Cerebras' presence in the competitive 𝐀𝐈 𝐢𝐧𝐟𝐫𝐚𝐬𝐭𝐫𝐮𝐜𝐭𝐮𝐫𝐞 market. 👉 𝐄𝐱𝐩𝐞𝐫𝐭 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭: ➤ "We are contracting significant capacity for 2027, with data centers slated for Norway and Finland as we actively build across Europe. These deployments will enable us to move decisively on what our customers have been asking for: fast, high-performance AI compute located in Europe." — 𝐀𝐧𝐝𝐫𝐞𝐰 𝐅𝐞𝐥𝐝𝐦𝐚𝐧, CEO of Cerebras. ➤ "Our customers don't just want AI compute. They want it close to home, powered responsibly, and available fast. This expansion and capacity plan reflects our confidence in Europe as a long-term growth market for Cerebras." — 𝐀𝐧𝐝𝐫𝐞𝐰 𝐅𝐞𝐥𝐝𝐦𝐚𝐧, CEO of Cerebras.

@AIStockSavvy [Thu Jul 09 10:18:33 +0000 2026]: 📊 𝐈𝐍𝐕𝐄𝐒𝐓𝐎𝐑 𝐍𝐎𝐓𝐄: UBS, Bernstein See Memory Prices Rising as AI Demand Accelerates - $MU $SNDK $WDC $STX $SKHY 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ Global memory sales reached a record 𝐔𝐒$𝟕𝟒.𝟔 𝐛𝐢𝐥𝐥𝐢𝐨𝐧, up 𝟑𝟏.𝟕% MoM. ➤ 𝐃𝐑𝐀𝐌 sales hit a record 𝐔𝐒$𝟒𝟖.𝟎 𝐛𝐢𝐥𝐥𝐢𝐨𝐧, rising 𝟐𝟕.𝟕% MoM. ➤ 𝐍𝐀𝐍𝐃 sales surged to a record 𝐔𝐒$𝟐𝟓.𝟖 𝐛𝐢𝐥𝐥𝐢𝐨𝐧, up 𝟒𝟎.𝟕% MoM. ➤ UBS forecasts 𝐃𝐃𝐑 contract prices to rise 𝟑𝟐% in Q3 and 𝟏𝟖% in Q4 2026. ➤ UBS expects 𝐍𝐀𝐍𝐃 contract prices to increase 𝟑𝟎% in Q3 and 𝟏𝟐% in Q4. ➤ UBS projects 𝐇𝐁𝐌 demand to grow 𝟗𝟎% in 2026 and 𝟕𝟕% in 2027. ➤ UBS sees the 𝐃𝐑𝐀𝐌 market remaining structurally undersupplied through at least Q2 2028. ➤ Bernstein expects memory price gains to 𝐬𝐥𝐨𝐰 in Q3 2026 despite near-term strength. ➤ Major beneficiaries include 𝐌𝐢𝐜𝐫𝐨𝐧, 𝐒𝐚𝐦𝐬𝐮𝐧𝐠, 𝐒𝐊 𝐇𝐲𝐧𝐢𝐱, and 𝐒𝐚𝐧𝐃𝐢𝐬𝐤. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ Higher memory prices could boost 𝐫𝐞𝐯𝐞𝐧𝐮𝐞 and margins for leading chipmakers. ➤ Sustained 𝐀𝐈 infrastructure spending is driving the current memory upcycle. ➤ Upcoming 𝐋𝐓𝐀 negotiations may determine the strength and duration of price gains. 👉 𝐄𝐱𝐩𝐞𝐫𝐭 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭: ➤ "Our July Memory Monthly suggests that the memory upcycle is strengthening further amid accelerating AI-driven demand and ongoing LTA negotiations." — 𝐔𝐁𝐒. ➤ "We still believe demand destruction in consumer segment will eventually happen and the pace of the price increase should narrow notably into 3QCY26." — 𝐁𝐞𝐫𝐧𝐬𝐭𝐞𝐢𝐧. ➤ "LTAs can reduce the impact of a correction, and we expect more clarity on these LTAs as more are signed." — 𝐁𝐞𝐫𝐧𝐬𝐭𝐞𝐢𝐧. ➤ "Customer affordability and sustainability of AI-related capital expenditure are still the key risks to this unprecedented upcycle." — 𝐔𝐁𝐒.

@AIStockSavvy [Wed Jul 08 22:39:04 +0000 2026]: $ONDS | Stifel reiterates 𝐁𝐮𝐲 on 𝐎𝐧𝐝𝐚𝐬 𝐇𝐨𝐥𝐝𝐢𝐧𝐠𝐬, maintains 𝐏𝐓 𝐚𝐭 $𝟏𝟖 Analyst sees the DZYNE acquisition as a strategic expansion of ONDS's defense tech portfolio, validating their positive thesis despite integration risks. https://t.co/PS5ePw8Mcp

@wallstengine [Thu Jul 09 10:10:17 +0000 2026]: PEPSICO $PEP Q2’26 EARNINGS HIGHLIGHTS 🔹 Revenue: $24.181B (Est. $23.96B) 🟢; +6.4% YoY 🔹 Adj. EPS: $2.20 (Est. $2.19) 🟢; +4% YoY 🔹 Operating Profit: $4.02B (Est. $4.06B) 🔴 🔹 Foods North America: $6.37B (Est. $6.48B) 🔴 🔹 EMEA Revenue: $4.98B (Est. $4.89B) 🟢 FY Guide: 🔹 Affirms fiscal 2026 guidance 🔹 Organic Revenue Growth: +2%-+4% 🔹 Core Constant Currency EPS Growth: +4%-+6% Other Metrics: 🔹 Organic Revenue Growth: +2.4% 🔹 International Beverages Franchise Revenue: $1.52B; +11% YoY Comments: 🔹 "Our North America business was softer than we anticipated in the second quarter, and we now expect a more gradual improvement in performance trends for the balance of this year"

@StockMKTNewz [Thu Jul 09 00:19:39 +0000 2026]: Cathie Wood and Ark Invest bought 181,847 shares of SpaceX $SPCX today https://t.co/sw9jUX3adQ

@StockMKTNewz [Wed Jul 08 20:17:52 +0000 2026]: Costco $COST just reported June sales of $29.24 Billion up 10.6% YoY https://t.co/19U4ng4QvY

@KobeissiLetter [Thu Jul 09 02:16:09 +0000 2026]: BREAKING: President Trump says Iran called him and “they want to make a deal so badly.” US stock market futures turn green on the news. https://t.co/1MkYnxxkCK

@KobeissiLetter [Thu Jul 09 01:19:34 +0000 2026]: BREAKING: The Index of US Financial Conditions is up to ~1.2 points, the easiest since February 2026. This is also near the highest level in at least 11 years. Since 2015, similar readings have only been recorded in early 2025 and during 2021, before the Fed started hiking rates. The Financial Conditions Index has risen over +1.0 points since the March low. Most of this surge has come from rising equity markets and falling corporate bond spreads. Financial conditions are easing despite the recent increase in inflation.

@KobeissiLetter [Wed Jul 08 21:47:14 +0000 2026]: BREAKING: President Trump says “it will get much worse” if Iran attacks ships in the Strait of Hormuz again. https://t.co/kn8xRu6mA7

@KobeissiLetter [Wed Jul 08 20:19:47 +0000 2026]: BREAKING: US CENTCOM announces that the US has begun conducting additional strikes in Iran. These strikes are intended to "further degrade Iran's ability to threaten freedom of navigation in the Strait of Hormuz," CENTCOM says.

@KobeissiLetter [Wed Jul 08 17:50:01 +0000 2026]: Gold is entering a historically favorable period of the year: Gold prices have gained +1.5% in July on average over the last 20 years, making it the 2nd-strongest month of the year. Gold prices have also recorded positive returns in 65% of July months, the 2nd-best win rate of any month. The strongest July over this period was in 2020, when gold returned +10.7%. The only better month historically has been August, with an average gain of +1.6% since 2005. August also posted a 55% win rate, with its strongest year coming in 2011, when gold returned +12.1%. By comparison, June has historically been the weakest month, with an average decline of -0.4% and just 40% positive readings since 2005. Seasonality is turning in favor of gold bulls.

@gurgavin [Wed Jul 08 09:16:40 +0000 2026]: FUTURES UPDATE S&amp;P 500 DOWN 1.1% 📉 DOW JONES DOWN 1.4% 📉 NASDAQ 100 DOWN 1.6% 📉

@AIStockSavvy [Thu Jul 09 10:16:09 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: $NOK Nokia Defense and NestAI Advance AI Battlefield Technology Partnership 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐍𝐨𝐤𝐢𝐚 𝐃𝐞𝐟𝐞𝐧𝐬𝐞 and NestAI advanced their strategic defense technology partnership. ➤ Partnership follows Nokia's and Tesi's 𝐄𝐔𝐑 𝟏𝟎𝟎 𝐦𝐢𝐥𝐥𝐢𝐨𝐧 joint investment announced in November 2025. ➤ Companies are developing 𝐭𝐡𝐫𝐞𝐞 integrated battlefield capabilities for European defense forces. ➤ Nokia's deployable 𝟓𝐆 networks will integrate with 𝐍𝐞𝐬𝐭𝐎𝐒 for command, control, and autonomous operations. ➤ NestOS will incorporate Nokia's 𝐫𝐚𝐝𝐢𝐨-𝐧𝐞𝐭𝐰𝐨𝐫𝐤 planning models for mission connectivity. ➤ Companies will combine 𝐞𝐚𝐫𝐥𝐲-𝐝𝐞𝐭𝐞𝐜𝐭𝐢𝐨𝐧 and multi-sensor tracking for threat awareness. ➤ Technologies are designed for 𝐝𝐞𝐧𝐢𝐞𝐝 𝐜𝐨𝐦𝐦𝐮𝐧𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬, electronic attacks, and drone threats. ➤ Systems are built to 𝐍𝐀𝐓𝐎 operational requirements using European-developed technology. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ Expands Europe's 𝐬𝐨𝐯𝐞𝐫𝐞𝐢𝐠𝐧 𝐝𝐞𝐟𝐞𝐧𝐬𝐞 𝐀𝐈 and secure communications capabilities. ➤ Combines AI, sensing, and 𝟓𝐆 to support next-generation battlefield operations. ➤ Strengthens Nokia's presence in the growing 𝐝𝐞𝐟𝐞𝐧𝐬𝐞 𝐭𝐞𝐜𝐡𝐧𝐨𝐥𝐨𝐠𝐲 market. 👉 𝐄𝐱𝐩𝐞𝐫𝐭 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭: ➤ "Defense is moving quickly to adopt AI-enabled capabilities, from mission planning to unmanned operations. But AI only works in the field when it has secure, resilient connectivity behind it." — 𝐌𝐢𝐤𝐤𝐨 𝐇𝐚𝐮𝐭𝐚𝐥𝐚, Chief Geopolitical & Government Relations Officer and Chairman, Nokia Defense. ➤ "The partnership addresses the real conditions European forces face, from the network underneath to the threats at the edge, on technology that Europe develops and controls." — 𝐏𝐞𝐭𝐞𝐫 𝐒𝐚𝐫𝐥𝐢𝐧, Founder and Executive Chairman of NestAI.

@AIStockSavvy [Thu Jul 09 01:54:52 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: After earlier US airstrikes, Iran again launched missiles and drones at Gulf states. - Fox News - $QQQ $SPY $USO

@AIStockSavvy [Thu Jul 09 01:43:21 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: $META Meta Reportedly Developing Always-On AI Smart Glasses - The Verge 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ Meta is reportedly developing 𝐚𝐥𝐰𝐚𝐲𝐬-𝐨𝐧 "𝐬𝐮𝐩𝐞𝐫 𝐬𝐞𝐧𝐬𝐢𝐧𝐠" AI smart glasses. ➤ Prototype glasses could 𝐜𝐨𝐧𝐭𝐢𝐧𝐮𝐨𝐮𝐬𝐥𝐲 record audio and capture photos every few seconds. ➤ Meta AI would use captured data to answer 𝐜𝐨𝐧𝐭𝐞𝐱𝐭-𝐚𝐰𝐚𝐫𝐞 user queries. ➤ Report says 𝐫𝐚𝐰 𝐚𝐮𝐝𝐢𝐨 and images may not be stored or accessible. ➤ Instead, extracted 𝐦𝐞𝐭𝐚𝐝𝐚𝐭𝐚 could be uploaded for AI processing. ➤ Report says the recording 𝐋𝐄𝐃 𝐢𝐧𝐝𝐢𝐜𝐚𝐭𝐨𝐫 may remain off in "super sensing" mode. ➤ Meta is also discussing using captured data to 𝐭𝐫𝐚𝐢𝐧 𝐀𝐈 models. ➤ The feature could reportedly arrive on 𝐞𝐱𝐢𝐬𝐭𝐢𝐧𝐠 Ray-Ban Meta smart glasses. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ Always-on sensing could significantly expand 𝐀𝐈 𝐰𝐞𝐚𝐫𝐚𝐛𝐥𝐞 capabilities. ➤ The reported design may intensify 𝐩𝐫𝐢𝐯𝐚𝐜𝐲 and surveillance concerns. ➤ The move could strengthen Meta's competition in the 𝐀𝐈 𝐰𝐞𝐚𝐫𝐚𝐛𝐥𝐞 market. 👉 𝐄𝐱𝐩𝐞𝐫𝐭 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭: ➤ "While we don't comment on internal prototypes, we're committed to getting our glasses right because they need to be loved by both people wearing them and those around them." — 𝐃𝐚𝐯𝐞 𝐀𝐫𝐧𝐨𝐥𝐝, Meta Spokesperson. ➤ "Our approach has been to develop new technologies that will help people throughout their day, with privacy built in from the ground up." — 𝐃𝐚𝐯𝐞 𝐀𝐫𝐧𝐨𝐥𝐝, Meta Spokesperson.

@AIStockSavvy [Wed Jul 08 22:42:03 +0000 2026]: $AMAT | Mizuho Securities 𝐫𝐚𝐢𝐬𝐞𝐬 𝐏𝐓 on 𝐀𝐩𝐩𝐥𝐢𝐞𝐝 𝐌𝐚𝐭𝐞𝐫𝐢𝐚𝐥𝐬 𝐈𝐧𝐜. to $𝟔𝟓𝟎 from $𝟓𝟒𝟎, maintains 𝐁𝐮𝐲 https://t.co/JFk9wqXV8y

@AIStockSavvy [Wed Jul 08 22:35:25 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: SK Hynix's US IPO was more than seven times oversubscribed. - Bloomberg - $MU $SNDK

@wallstengine [Thu Jul 09 08:58:09 +0000 2026]: $ALNY shares are moving higher after the $IONS/$AZN CARDIO-TTRansform Phase 3 trial in ATTR-CM missed its primary endpoint. Wainua/eplontersen did not significantly reduce CV mortality and recurrent CV events vs placebo through Week 140. Ionis said most patients were on stabilizers, with 57% on them at baseline and another 24% starting during the trial The monotherapy subgroup showed a nominally significant benefit, but patients already on stabilizers saw no treatment effect

@wallstengine [Thu Jul 09 08:47:07 +0000 2026]: $META is reportedly working on “super sensing” smart glasses that could continuously record audio and take photos every few seconds. Users could then ask Meta AI questions based on what the glasses captured. Meta is reportedly considering a setup where raw audio and images are not directly stored or shown to users, but metadata is uploaded for AI queries. The recording LED may stay off during “super sensing” mode, since Meta currently reserves the indicator for active photo or video capture.

@KobeissiLetter [Wed Jul 08 23:29:48 +0000 2026]: Agentic AI continues to see rapid growth. Over the last 12 months, the focus has rapidly shifted toward the software layer that allows AI to connect with enterprise data and applications. Instead of simply answering questions, these systems can access company databases, analyze documents, execute multi-step tasks, and automate entire business processes with minimal human input. In other words, AI is evolving from a chatbot into a digital employee. As a result, the enterprise AI market is now expected to exceed $155 billion by 2030. This is why virtually every major technology company is racing to build AI agents. The next phase of the AI Revolution has arrived.

@gurgavin [Wed Jul 08 08:19:57 +0000 2026]: *TRUMP SAYS IRAN CEASE FIRE IS OVER HERE WE GO AGAIN

@AIStockSavvy [Wed Jul 08 22:37:52 +0000 2026]: $SRPT | Wolfe Research 𝐮𝐩𝐠𝐫𝐚𝐝𝐞𝐬 𝐒𝐚𝐫𝐞𝐩𝐭𝐚 𝐭𝐨 𝐎𝐮𝐭𝐩𝐞𝐫𝐟𝐨𝐫𝐦, sets 𝐏𝐓 𝐚𝐭 $𝟐𝟕 Analyst sees a shift in stock performance driven by a new market regime, upcoming MAD data in H2, and increased investor focus on DM1/FSHD. https://t.co/5zz0CVRn5v

@wallstengine [Thu Jul 09 09:24:01 +0000 2026]: $META ADDED TO BOFA US 1 LIST

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.