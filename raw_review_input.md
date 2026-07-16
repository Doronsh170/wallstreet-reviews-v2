אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are a senior Wall Street investment advisor writing your signature END-OF-DAY review in Hebrew for
2026-07-15 (יום רביעי). PAST TENSE.

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
  "title": "סיכום יום המסחר בוול סטריט 🇺🇸 – יום רביעי, 15.7.2026",
  "date": "2026-07-15",
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
  S&P 500 (SPY ETF): $754.81 (daily: +0.40%), prev close: $751.83
  Nasdaq 100 (QQQ ETF): $717.74 (daily: -0.27%), prev close: $719.69
  Dow Jones (DIA ETF): $525.95 (daily: +0.24%), prev close: $524.69
  Russell 2000 (IWM ETF): $295.77 (daily: +0.43%), prev close: $294.51
  Energy Sector (XLE ETF): $56.50 (daily: -0.79%), prev close: $56.95
  Technology Sector (XLK ETF): $181.58 (daily: -1.11%), prev close: $183.62
  Financials Sector (XLF ETF): $56.56 (daily: +0.68%), prev close: $56.18
  Consumer Discretionary Sector (XLY ETF): $117.00 (daily: +0.95%), prev close: $115.90
  Healthcare Sector (XLV ETF): $158.29 (daily: +0.00%), prev close: $158.29
  Industrials Sector (XLI ETF): $180.06 (daily: -0.22%), prev close: $180.45
  Consumer Staples Sector (XLP ETF): $83.47 (daily: +0.06%), prev close: $83.42
  Utilities Sector (XLU ETF): $45.22 (daily: -1.03%), prev close: $45.69
  WTI Crude Oil (USO ETF): $121.38 (daily: +1.01%), prev close: $120.17
  Brent Crude Oil (BNO ETF): $47.59 (daily: +0.63%), prev close: $47.29
  Gold (GLD ETF): $372.35 (daily: +0.05%), prev close: $372.15
  Silver (SLV ETF): $52.21 (daily: -1.81%), prev close: $53.17
  Bitcoin (IBIT ETF): $36.81 (daily: +0.63%), prev close: $36.58
  US 20Y+ Bonds (TLT ETF): $84.24 (daily: +0.19%), prev close: $84.08
  US Dollar (UUP ETF): $28.25 (daily: -0.49%), prev close: $28.39
  VIX Volatility (VIXY ETF): $20.06 (daily: -2.90%), prev close: $20.66

INDIVIDUAL STOCKS mentioned in the source tweets (verified quotes):
  $NVDA: $212.50 (daily: +0.33%), prev close: $211.80
  $MU: $904.28 (daily: -8.02%), prev close: $983.12
  $EOSE: $4.37 (daily: +1.86%), prev close: $4.29
  $AMZN: $254.96 (daily: +3.02%), prev close: $247.49
  $GOOGL: $370.92 (daily: +3.17%), prev close: $359.51
  $META: $681.31 (daily: +3.07%), prev close: $661.04
  $SPCX: $135.27 (daily: -0.60%), prev close: $136.08
  $LLY: $1156.63 (daily: +0.35%), prev close: $1152.54
  $ASTS: $66.31 (daily: -3.65%), prev close: $68.82
  $AAPL: $327.50 (daily: +4.01%), prev close: $314.86
  $AMD: $529.14 (daily: -3.46%), prev close: $548.13
  $AVGO: $394.28 (daily: +1.33%), prev close: $389.11

DIRECTIONAL FACTS — Hebrew direction words (עולה/יורד/צונח/מזנק) MUST match these:
  נפט (WTI/ברנט): עולה (USO: +1.01%, BNO: +0.63%)
  זהב: יציב/כמעט ללא שינוי (GLD: +0.05%)
  ביטקוין: עולה (IBIT: +0.63%)
  דולר: יורד (UUP: -0.49%)
  תנודתיות / VIX: יורד (VIXY: -2.90%)
  אג"ח ארוכות / TLT: עולה (TLT: +0.19%)

The % changes above are ACCURATE — use them for direction and magnitude.
The ETF tickers above (SPY/QQQ/DIA/USO/GLD/...) are measurement instruments for YOUR verification only — NEVER name them, Finnhub, or the word 'proxy' in the visible Hebrew text.
For exact index LEVELS (points), gold/oil absolute prices, VIX level, Bitcoin price, 10Y yield: verify via web search. Do NOT estimate them from ETF prices.
For sector performance (XLE/XLK/...): USE ONLY the Finnhub numbers above — never invent sector percentages.
If ANY percentage you write contradicts the data above, you are WRONG. Fix it.
══════════════════════════════════════════════════════════════════════════════

══ MANDATORY MACRO DATA CHECK ══
Use web search to check if ANY of these were released on 2026-07-16: CPI (headline AND core),
PPI (headline AND core), NFP, Jobless Claims, Consumer Sentiment (Michigan), ISM PMI, GDP,
Retail Sales, FOMC decision/minutes. If released — include with actual, forecast, previous,
AND the market implication. If none — skip, but you MUST check first.
══════════════════════════════════

══ CONTEXT: THIS MORNING'S PRE-MARKET BRIEFING ══
Published before the session. Use it to resolve scheduled items (expected → actual), do NOT quote it verbatim.

[נקודות מרכזיות]
* אופטימיות זהירה לקראת הפתיחה: החוזים העתידיים מצביעים על פתיחה חיובית מתונה, החוזים על S&P 500 עולים כ-0.1% ואלו של נאסד"ק 100 מוסיפים כ-0.4%, בהובלת מניות השבבים ובראשן איי.אס.אם.אל (ASML) שמוסיפה כ-3% לאחר שהעלתה את תחזית המכירות שלה זו הפעם השנייה השנה. הרוח הגבית המרכזית היא מדד המחירים לצרכן שפורסם אתמול והפתיע לטובה: המדד הכללי ירד ביוני 0.4%, הירידה החודשית החדה ביותר מאז אפריל 2020, והקצב השנתי התמתן ל-3.5% לעומת צפי של 3.8% ו-4.2% במאי, כאשר אינפלציית הליבה נותרה יציבה בחודש והתמתנה ל-2.6% בקצב שנתי. בתגובה נסוגה תשואת האג"ח לעשר שנים לאזור 4.57%, והמשקיעים מגיעים לפתיחה עם תיאבון סיכון מחודש.
* מדד המחירים ליצרן במוקד היום: אחרי ההקלה במדד המחירים לצרכן, המבחן הבא של נרטיב הדיסאינפלציה יגיע היום ב-15:30 שעון ישראל עם מדד המחירים ליצרן (PPI) ליוני. התחזיות מדברות על ירידה קלה של כ-0.1% במדד הכללי לאחר זינוק של 1.1% במאי, על התמתנות הקצב השנתי ל-6.2% מ-6.5%, ועל עלייה של 0.4% במדד הליבה, כך שקריאה חמה בצד היצרנים עלולה לקרר את האופטימיות. במקביל יעיד היום יו"ר הפדרל ריזרב קווין וורש בפני ועדת הבנקאות של הסנאט ב-17:00 שעון ישראל, לאחר שאתמול הבהיר בבית הנבחרים כי השיפור באינפלציה אינו בגדר "משימה שהושלמה", ובערב (21:00 שעון ישראל) יתפרסם הספר הבז' של הפד עם תמונת מצב אזורית של הכלכלה.
* ההסלמה מול איראן מלהיטה את הנפט: הלילה דווח על סבב תקיפות אמריקאי נוסף נגד מטרות באיראן ועל השבת הסגר הימי על נמלי הנפט שלה, והנשיא טראמפ מאיים כי אם טהרן לא תשוב לשולחן המשא ומתן, התקיפות יורחבו בשבוע הבא גם לתחנות כוח ולגשרים. מחיר הנפט ממשיך לטפס הבוקר בכ-1%, כאשר הגולמי האמריקאי נסחר סביב 80.1 דולר לחבית והברנט סביב 85.8 דולר. במקביל, מרווחי הזיקוק כמעט שילשו את עצמם מתחילת השנה והגיעו לרמת שיא של 59 דולר לחבית, כאשר כ-10% מכושר הזיקוק העולמי מושבת בשל המלחמה, כך שמחירי הדלקים נשארים גבוהים גם כשהנפט הגולמי רחוק כ-40 דולר משיא חודש מרץ. עבור המשקיעים זהו תהליך שמזין את האינפלציה בדלת האחורית ומקשה על הפדרל ריזרב להכריז על ניצחון.
* מניית מורגן סטנלי (MS): הבנק פתח את בוקר הדוחות עם תוצאות חזקות במיוחד לרבעון השני, רווח של 3.46 דולר למניה מול צפי של 2.93 דולר והכנסות שיא של 21.35 מיליארד דולר, גידול של 27% לעומת הרבעון המקביל. ההכנסות ממסחר במניות הגיעו לשיא רבעוני של 6.3 מיליארד דולר, גידול של 69%, חטיבת ניהול העושר גייסה סכום שיא של 148 מיליארד דולר בנכסים חדשים, לפי Bloomberg יותר ממחציתו קשורה לגל ההנפקות החדש, והבנק אישר תוכנית רכישה עצמית של עד 20 מיליארד דולר לצד העלאת הדיבידנד הרבעוני. גם בנק אוף ניו יורק מלון (BNY) ופי.אן.סי (PNC) היכו הבוקר את תחזיות הרווח וההכנסות, פתיחה שמחזקת את ההערכה שהבנקים יהיו עוגן חיובי בעונת הדוחות הנוכחית.
* מניית ג'ונסון אנד ג'ונסון (JNJ): ענקית הבריאות היכתה את התחזיות עם מכירות של 25.31 מיליארד דולר ברבעון, גידול של 6.6%, ורווח מתואם של 2.90 דולר למניה, והעלתה את תחזית המכירות השנתית לטווח של 100.8 עד 101.4 מיליארד דולר. משמעות התחזית המעודכנת היא חציית רף 100 מיליארד הדולר בהכנסות שנתיות לראשונה בהיסטוריה בת 140 השנים של החברה, בתמיכת הצמיחה בתרופות האונקולוגיה ושורת אישורי FDA טריים. הדוח מספק נקודת אור למגזר הבריאות, שבלט אתמול לשלילה בירידה של קרוב ל-2%, והוא איתות מעודד לקראת דוחות שאר ענקיות הפארמה בהמשך העונה.
* מניית אי.בי.אם (IBM): טלטלה בענקית הטכנולוגיה הוותיקה, שצנחה אתמול כ-25%, הירידה היומית החדה ביותר שלה מאז 1968. החברה, שעוד בתחילת יוני הציגה עלייה של 13% מתחילת השנה, איבדה מאז 35% משווייה, יותר מ-100 מיליארד דולר, בתוך 42 ימים בלבד. הקריסה ממחישה את התנודתיות חסרת התקדים במגזר הטכנולוגיה השנה: תעודות הסל של השבבים והתוכנה רשמו כבר 34 ימי מסחר עם תנועה חדה של 4% ומעלה מתחילת השנה, כמעט פי ארבעה מהשיא השנתי הקודם מ-2024 ויותר מסך שבע השנים הקודמות יחד. המסר למשקיעים חד: בעידן הבינה המלאכותית גם ענקיות ותיקות נבחנות מחדש בכל רבעון.
* מניית פייפאל (PYPL): לפי הוול סטריט ג'ורנל, ענקית התשלומים הפרטית סטרייפ וקרן ההשקעות אדוונט הגישו הצעה לרכישת פייפאל לפי 60.50 דולר למניה, עסקה בשווי מוערך של כ-53 מיליארד דולר. המשקיע מייקל ביורי, שמחזיק במניה בתיק שלו, ממהר לסמן את ההצעה כנמוכה מדי: לדבריו זו רק הצעת פתיחה, המשקפת פי 1.21 בלבד ממדד הערך הפנימי שהוא מחשב למניה, והוא אינו מתכוון למכור. סאגת הרכישה מציפה מחדש את הדיון על התמחור הזול של ענקיות הפינטק הוותיקות, וכעת השאלה היא אם סטרייפ תשפר את הצעתה או שמתחרים נוספים ייכנסו לתמונה.
* מניית אלפבית (GOOGL) בתמיכת באפט: וורן באפט חשף כי הוא שיזם את השקעת ברקשייר האת'וויי (BRK.B) באלפבית, והודה כי שגה שלא רכש את המניה מוקדם יותר, כך לפי CNBC. מדובר בחותמת אמון נדירה מהמשקיע הנודע במניית טכנולוגיה שהפכה לאחת הנהנות המרכזיות ממהפכת הבינה המלאכותית, והמניה סיימה את יום המסחר של אתמול בעלייה של כ-2%.
* שורה תחתונה: את כיוון המסחר היום יכתיבו מדד המחירים ליצרן ליוני, שיתפרסם היום, יום רביעי, ב-15:30 שעון ישראל עם צפי לירידה קלה של 0.1% במדד הכללי ולעלייה של 0.4% במדד הליבה, ועדות היו"ר וורש בסנאט ב-17:00 שעון ישראל. קריאה מתונה תבסס את מגמת ההקלה של מדד המחירים לצרכן ותתמוך בהמשך הראלי, בעוד הפתעה כלפי מעלה, בשעה שהנפט שב מעל 80 דולר לחבית, עלולה להחזיר במהירות את חששות הריבית. שכבת ביטחון נוספת מגיעה מדוחות הבנקים החזקים, שנותנים לשוק עוגן בסיסי חיובי לקראת הפתיחה.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-16. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Wed Jul 15 17:30:07 +0000 2026]: Semiconductor stocks are the new leaders of the market: Micron, $MU, has contributed ~1.4 percentage points to the S&P 500's +8% gain over the last 6 months, the largest contribution of any index constituent. This comes as the stock rallied +188% over this period. AMD, $AMD, ranks 2nd with a ~0.9 percentage point contribution after surging +158%. Apple, $AAPL, and Intel, $INTC, follow with ~0.8 percentage point contributions as their stocks gained +20% and +205%, respectively. Broadcom, $AVGO, Nvidia, $NVDA, and Sandisk, $SNDK, each added ~0.4 percentage points with returns of +9%, +5%, and +395%, respectively. A handful of chip stocks are powering the broader market.

@wallstengine [Wed Jul 15 21:07:07 +0000 2026]: $EOSE won a multi-million-dollar Golden Dome defense contract to supply zinc-based long-duration energy storage for U.S. defense infrastructure. Initial deployment will use Eos’ Z3 system as a prototype at a critical military installation. The Z3 is built at Eos’ Pittsburgh facility and contains about 91% domestic content.

@KobeissiLetter [Thu Jul 16 01:37:00 +0000 2026]: Investors are demanding more protection against Big Tech credit risk: 5-year credit default swap (CDS) spreads on Oracle, $ORCL, Amazon, $AMZN, Google, $GOOGL, and Microsoft, $MSFT, are up to ~75 basis points, near the highest in at least 7 years. CDS spreads on the same group excluding $ORCL are up to ~49 basis points, the highest since at least 2018. Both metrics have more than doubled since the start of 2025 and are now significantly above their 2022 bear market peaks. This comes as Big Tech has issued debt at an unprecedented pace to finance AI infrastructure, prompting investors to hedge against rising credit risk. $AMZN, $GOOGL, $NVDA, $META, $ORCL, and SpaceX, $SPCX, have issued a record $182 billion in investment-grade bonds so far in 2026, up +1,300% YoY, accounting for ~15% of total US corporate bond issuance year-to-date. The AI revolution is reshaping credit markets.

@KobeissiLetter [Wed Jul 15 16:16:21 +0000 2026]: BREAKING: Micron, $MU, extends losses to -10% on the day as the selloff in memory stocks gains momentum. The stock has now erased $110 billion in market cap today. https://t.co/EdaFY2pp2k

@AIStockSavvy [Wed Jul 15 21:02:55 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $EOSE Eos Wins Golden Dome Energy Storage Contract With U.S. Department of War 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐄𝐨𝐬 awarded a 𝐆𝐨𝐥𝐝𝐞𝐧 𝐃𝐨𝐦𝐞 contract by the Department of War. ➤ Contract supports resilient 𝐥𝐨𝐧𝐠-𝐝𝐮𝐫𝐚𝐭𝐢𝐨𝐧 𝐞𝐧𝐞𝐫𝐠𝐲 𝐬𝐭𝐨𝐫𝐚𝐠𝐞 for defense infrastructure. ➤ Initial deployment will use 𝐄𝐨𝐬' 𝐙𝟑 zinc-based energy storage system. ➤ Prototype will be installed at a 𝐜𝐫𝐢𝐭𝐢𝐜𝐚𝐥 defense installation. ➤ Eos technology features approximately 𝐨𝐯𝐞𝐫 𝟗𝟎% 𝐝𝐨𝐦𝐞𝐬𝐭𝐢𝐜 content. ➤ System is 𝐍𝐃𝐀𝐀 𝐒𝐞𝐜𝐭𝐢𝐨𝐧 𝟖𝟒𝟐 and 𝐅𝐄𝐎𝐂 compliant. ➤ Thorn Hill facility is expanding production toward 𝐚𝐧𝐧𝐮𝐚𝐥 𝟖 𝐆𝐖𝐡 capacity. ➤ Eos plans to create 𝐚𝐩𝐩𝐫𝐨𝐱𝐢𝐦𝐚𝐭𝐞𝐥𝐲 𝟏,𝟎𝟎𝟎 jobs across the Pittsburgh region. ➤ Program is designed to 𝐬𝐜𝐚𝐥𝐞 with evolving national defense requirements. 👉 𝐄𝐱𝐩𝐞𝐫𝐭 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭𝐬: 𝐏𝐫𝐞𝐬𝐢𝐝𝐞𝐧𝐭 𝐃𝐨𝐧𝐚𝐥𝐝 𝐉. 𝐓𝐫𝐮𝐦𝐩: “Eos in Pittsburgh just agreed to a multi-million-dollar partnership with the Department of War to build energy storage technology in support of our Golden Dome missile defense. Yeah we're building a golden dome over our country and its going to be a very effective one.” 𝐉𝐨𝐞 𝐌𝐚𝐬𝐭𝐫𝐚𝐧𝐠𝐞𝐥𝐨, Eos Chief Executive Officer: “This award validates the strategy we’ve built around American technology innovation, manufacturing and supply chains. Today, we’re proving that America can still manufacture advanced technology at scale and deliver for our nation’s most critical missions.” 𝐌𝐢𝐜𝐡𝐞𝐥𝐥𝐞 𝐁𝐮𝐜𝐳𝐤𝐨𝐰𝐬𝐤𝐢, Eos Chief Administration Officer: “We spent the last year building the relationships, compliance foundation and technical proof points the Department of War requires. This award reflects that work. Eos is ready to deliver for the Department's mission at scale.” 𝐒𝐞𝐧𝐚𝐭𝐨𝐫 𝐃𝐚𝐯𝐞 𝐌𝐜𝐂𝐨𝐫𝐦𝐢𝐜𝐤: “The Golden Dome should be built on American technology. Eos' technology will help secure the power infrastructure our military depends on, while creating good jobs right here in Pennsylvania.”

@gurgavin [Wed Jul 15 16:08:32 +0000 2026]: SPACEX SHARES ARE NOW TRADING BELOW THE IPO PRICE OF $135 EVERY SINGLE PERSON WHO BOUGHT SPACEX SHARES IS NOW IN THE RED $SPCX

@gurgavin [Tue Jul 14 21:22:03 +0000 2026]: YESTERDAY JIM CRAMER TOLD HIS VIEWERS TO BUY $IBM SHARES TODAY IBM SHARES FELL 25% THE BIGGEST 1 DAY DROP IN THE COMPANY’S ENTIRE 100 YEAR HISTORY INVERSE CRAMER NEVER FAILS https://t.co/4d3LPm20KD

@StockMKTNewz [Wed Jul 15 23:15:11 +0000 2026]: NVIDIA $NVDA JUST SHRUNK THE SIZE OF ITS ROBOTICS CHIP IN HALF WITHOUT LOSING PERFORMANCE NVIDIA introduced two new modules, the T3000 and T2000, built on its Thor architecture for humanoid robots and edge AI, aimed at moving robotics from research labs into mass-market deployment. Per NVIDIA, migrating to the smaller chip also helps cut costs "amid high memory prices" The T2000 is an entry-level option for autonomous mobile robots and industrial manipulators. Companies already building on the platform include 1X, Boston Dynamics, Amazon Robotics, FANUC, and Medtronic. NVIDIA also released new "agent skills" that reportedly let developers cut memory usage without new hardware. T3000 and T2000 are set to ship in Q1 2027.

@StockMKTNewz [Wed Jul 15 23:07:05 +0000 2026]: NVIDIA $NVDA x JAPAN 🇯🇵 Nvidia just announced that a bunch of Japan's largest companies, startups, and research institutions are building industry-specific AI using its open Nemotron models, aimed at Japan's language, industries, and aging workforce. - SoftBank's Intuitions trained its own Sarashina models on Nemotron, one of which was selected by Japan's Digital Agency. SoftBank also built a large telco model for autonomous network operations. - Institute of Science Tokyo used Nemotron to build its Swallow models, now used for financial-document translation and asset-management reporting. - ENEOS Holdings is using Nemotron for agentic AI workflows in energy and materials R&D. Hitachi is combining it with its own IT/OT domain knowledge for physical AI. NTT DATA used it to improve its proprietary tsuzumi 2 model. Sakana AI is folding it into its Fugu model-routing platform.

@wallstengine [Wed Jul 15 23:39:10 +0000 2026]: $NVDA JUST CUT ITS THOR ROBOTICS COMPUTER TO HALF THE SIZE AND POWER The new T3000 module is roughly half the size and power of NVIDIA’s T5000, while delivering similar inference performance on multimodal AI workloads. Inside: → 865 FP4 teraflops → 32GB of LPDDR5X memory → 273GB/s memory bandwidth → 25GbE connectivity NVIDIA also introduced the T2000, a lower-cost option with 400 FP4 teraflops and 16GB of memory for mobile robots, industrial manipulators, and other edge AI systems. NVIDIA’s new Jetson agent skills optimize memory usage without requiring new hardware. UBTech, Agile Robots, and Connect Tech reportedly reduced memory usage by as much as 15GB, enough to move from a 64GB Jetson module to a 32GB version. That means lower hardware costs and more capable models running on smaller systems. Companies including 1X, Amazon Robotics, Boston Dynamics, FANUC, and Agile Robots are already building on the Thor platform. The T3000 and T2000 are scheduled to ship in Q1 2027.

@StockMKTNewz [Wed Jul 15 23:00:42 +0000 2026]: Eli Lilly $LLY is reportedly in talks to acquire medical psychedelic company AtaiBeckley - Bloomberg https://t.co/MK4AmES9Ic

@StockMKTNewz [Wed Jul 15 20:02:55 +0000 2026]: AST SPACEMOBILE $ASTS ANNOUNCES PROPOSED PRIVATE OFFERING OF $1.0 BILLION OF CONVERTIBLE SENIOR NOTES DUE 2034

@StockMKTNewz [Wed Jul 15 19:50:41 +0000 2026]: 🇺🇸 President Trump just said: “They just gave me the award for being the salesman of the year. I have sold more Boeing $BA planes and no one comes close. You know what I got for that? Nothing. If I was in the private sector, I would say I want a piece of the company.” https://t.co/8crSXjBk29

@wallstengine [Thu Jul 16 00:00:31 +0000 2026]: Eli Lilly $LLY is reportedly in talks to acquire psychedelic drugmaker AtaiBeckley $ATAI, per Bloomberg. A deal could be announced as soon as this week. AtaiBeckley has a market value of about $2B, and Lilly is reportedly negotiating at a premium. The key asset is BPL-003, a fast-acting nasal spray for treatment-resistant depression that has FDA Breakthrough Therapy designation. Bloomberg Intelligence estimates the psychedelic treatment market could reach $7B in sales by 2032.

@gurgavin [Wed Jul 15 19:18:13 +0000 2026]: PAYPAL SHARES ARE UP TODAY ON A POTENTIAL $53 BILLION TAKEOVER OFFER FROM STRIPE PAYPAL -> MAKING $5 BILLION+ A YEAR AND GROWING -> BUYING BACK 7% OF THE COMPANY EVERY YEAR -> TRADING AT JUST 9X EARNINGS BEFORE THE NEWS AND JUST 11X THE BUYOUT OFFER THERE IS NO WAY THE BOARD AGREES TO SELL AT JUST $60.50 I THINK $75 SHOULD BE THE BARE MINIMUM I THINK THIS STARTS A BIDDING WAR 69% CHANCE PAYPAL GETS ACQUIRED THIS YEAR ON KALSHI RIGHT NOW $PYPL

@wallstengine [Thu Jul 16 00:25:24 +0000 2026]: $NVDA is expanding its Toyota partnership beyond autonomous driving, supplying AI hardware and software for smart cities, traffic systems and factories. Toyota will use Nvidia tech in Woven City, plus Omniverse for assembly-line digital twins, Isaac robotics and Nemotron LLMs. https://t.co/ffhsFcgl8i

@KobeissiLetter [Wed Jul 15 20:14:59 +0000 2026]: BREAKING: President Trump says he just "received a call" from Iran and they "want to meet" with him. "They want to settle so badly," Trump says. US oil prices extend gains to above $80/barrel.

@StockMKTNewz [Wed Jul 15 20:12:20 +0000 2026]: United Airlines $UAL said it expects to spend $6 Billion more on fuel than it had originally expected https://t.co/hEYXzsOOKK

@AIStockSavvy [Wed Jul 15 23:03:54 +0000 2026]: Japan’s Enterprises and Startups Build Industry-Specialized AI With Nvidia Nemotron Open Models - $NVDA

@AIStockSavvy [Wed Jul 15 23:03:14 +0000 2026]: $NVDA | Nvidia Says Introduces New Jetson Thor Computers to Advance Mainstream Robotics and Edge AI

@AIStockSavvy [Wed Jul 15 23:02:40 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Nvidia Says Expands Partnership With Toyota to Advance Physical AI Across Automotive, Robotics and Cities - $NVDA $TM

@wallstengine [Wed Jul 15 23:33:06 +0000 2026]: Guggenheim Upgrades $NXT to Buy from Neutral, Sets PT at $125 Analyst comments: "We are upgrading Nextracker to Buy establishing a $125 PT, which would value the company at approximately 18x our calendar 2027 estimated EBITDA. NXT’s business execution and strategy have always been strong, in our view, but we also believe investors have historically tended to overpay for the stock, which is why we regard the recent decline as an attractive buying opportunity. Since reaching a peak of $156 on May 29, NXT has declined 33%, compared with flat performance for the S&P 500 over the same period. The resulting valuation of approximately 15x calendar 2027 estimated EBITDA is attractive, in our opinion. Our estimate revisions reflect the inclusion of Prevalon, as well as some adjustments to our outlook for the core tracker business." Analyst: Joseph Osha I actually bought $NXT in a GameStock tournament and shared the trade on Discord a couple of weeks ago.GameStock is a stock competition app where users build portfolios and compete in tournaments: https://t.co/DfgoZJ3FSb

@wallstengine [Wed Jul 15 20:11:25 +0000 2026]: J.B. HUNT $JBHT Q2’26 EARNINGS HIGHLIGHTS 🔹 Revenue: $3.50B (Est. $3.17B) 🟢; +19% YoY 🔹 EPS: $1.91 (Est. $1.71) 🟢; +45% YoY 🔹 Intermodal Revenue: $1.75B (Est. $1.49B) 🟢; +22% YoY FY26 Guide: 🔹 Annual Effective Tax Rate: 24.0% to 24.5% Segment Net Revenue: 🔹 Intermodal: $1.75B; +22% YoY 🔹 Dedicated: $921M; +9% YoY 🔹 ICS: $388M; +49% YoY 🔹 FMS: $198M; -6% YoY 🔹 Truckload: $240M; +35% YoY Other Q2 Metrics: 🔹 Intermodal Loads: 578,072 (Est. 537,462) 🟢; +10% YoY 🔹 Operating Income: $259.5M; +32% YoY Comments: 🔸 “Our second quarter results reflect the strength of executing our strategy, as we leveraged our investments in our people, technology, and capacity to drive growth and improve profitability.” 🔸 “As market conditions continue to evolve, we remain focused on creating long-term value for our shareholders, delivering valuable solutions to our customers while maintaining discipline around returns on our capital.”

@KobeissiLetter [Thu Jul 16 00:36:00 +0000 2026]: BREAKING: China’s crude oil imports dropped -41% YoY in June, to 29 million tons or 7 million barrels per day, the lowest in 10 years. MoM, oil imports fell by -4 million tons, or -12%, to the weakest level in 8 years. Import volumes have now declined -26 million tons, or -47%, since the late-2025 peak. By comparison, the average between 2020 and 2025 was ~45 million tons per month. Meanwhile, China's seaborne crude imports stood at around 6 ⁠million barrels per day in June, with imports from the Middle East falling to their lowest in 10 years. At the same time, Iranian oil imports fell -40% MoM, to below 800,000 barrels per day. The Iran War has created a historic supply shock.

@KobeissiLetter [Wed Jul 15 23:30:13 +0000 2026]: BREAKING: President Trump says Iran has allowed an American citizen who was detailed in 2024 to leave the country "in good condition." President Trump also thanks Iran for the "gesture of goodwill." https://t.co/W1lJIiPDhb

@KobeissiLetter [Wed Jul 15 15:10:25 +0000 2026]: Institutional investors are rushing into US stocks: Global managers’ cash allocation has declined -0.5 percentage points month-over-month, to 3.6%, near the lowest in 13 years, according to a BofA survey of 181 participants with $484 billion in assets. At the same time, 24% of managers are now net overweight US equities, the highest since December 2024. This is also the 2nd-highest reading since late-2021. Furthermore, 82% of respondents said "long global semiconductor stocks" is the most crowded trade, the 3rd consecutive month semiconductors have topped the list. All while allocation to global equities is up +4 percentage points this month, to 42% overweight, the 4th-highest since January 2022. The appetite for risk is surging globally.

@KobeissiLetter [Wed Jul 15 18:33:18 +0000 2026]: Market selloffs are becoming increasingly selective: Over the last 20 S&P 500 down days, an average of 239 stocks finished positive, the highest reading on record. This is TRIPLE the levels seen during the 2022 bear market and nearly double the 20-year average of 133 stocks. Since June 1st, 9 of the last 14 down days in the S&P 500 saw ~64% of index names closing higher. By comparison, only ~32% of down days over the past year saw more stocks closing positive than negative. This suggests market weakness is being increasingly driven by a smaller group of stocks, with investors rotating rather than exiting equities. Market breadth is showing unusual strength during periods of weakness.

@gurgavin [Tue Jul 14 22:22:21 +0000 2026]: THE MARKET NOW EXPECTS 1 RATE CUT IN 2026 FOLLOWING TODAYS CPI PRINT ON KALSHI BEFORE THE CPI PRINT MARKET ONLY EXPECTED 0.3 RATE CUTS THIS YEAR https://t.co/myyWS2hZFd

@AIStockSavvy [Wed Jul 15 23:07:36 +0000 2026]: Jim Cramer on $APLD Applied Digital Corporation : “I like Applied Digital. It has come down...and this one is one of those that can be owned ... Start it small, don’t start it big because it is losing money.”

@AIStockSavvy [Wed Jul 15 23:06:09 +0000 2026]: Jim Cramer on $BE Bloom Energy: “You want to buy Bloom Energy. It’s come down a great deal and it’s a non-combustible way to be able to power data centers"

@AIStockSavvy [Wed Jul 15 20:57:29 +0000 2026]: Wedbush analyst Ygal Arounian assumes coverage on $RDDT $UBER $GOOGL $AMZN $DUOL $META https://t.co/iQeSLMFA2m

@AIStockSavvy [Wed Jul 15 20:21:50 +0000 2026]: $RKLB | Piper Sandler 𝐢𝐧𝐢𝐭𝐢𝐚𝐭𝐞𝐬 𝐜𝐨𝐯𝐞𝐫𝐚𝐠𝐞 on 𝐑𝐨𝐜𝐤𝐞𝐭 𝐋𝐚𝐛 𝐔𝐒𝐀 with 𝐍𝐞𝐮𝐭𝐫𝐚𝐥, 𝐏𝐓 𝐚𝐭 $𝟖𝟑 https://t.co/RvtTVk44dM

@AIStockSavvy [Wed Jul 15 20:20:42 +0000 2026]: $ASTS | Piper Sandler 𝐢𝐧𝐢𝐭𝐢𝐚𝐭𝐞𝐬 𝐂𝐨𝐯𝐞𝐫𝐚𝐠𝐞 on 𝐀𝐒𝐓 𝐒𝐩𝐚𝐜𝐞𝐦𝐨𝐛𝐢𝐥𝐞 with 𝐎𝐯𝐞𝐫𝐰𝐞𝐢𝐠𝐡𝐭, 𝐏𝐓 𝐚𝐭 $𝟏𝟎𝟎 https://t.co/OWnbdYManG

@wallstengine [Wed Jul 15 21:43:00 +0000 2026]: SK Hynix $SKHY posted another record-volume day, trading 75M shares. The new Leverage Shares ETFs also saw record activity: $SKHX, 2x long SK Hynix: 6M shares traded $SKHZ, 1x short SK Hynix: nearly 2M shares traded https://t.co/V3v5X2Wh2L

@wallstengine [Wed Jul 15 20:12:57 +0000 2026]: JABIL $JBL AUTHORIZED A NEW $1.5B SHARE REPURCHASE PROGRAM.

@gurgavin [Tue Jul 14 18:18:52 +0000 2026]: A SOUTH KOREAN FINANCIAL YOUTUBER WAS JUST STABBED MULTIPLE TIMES BY ONE OF HIS SUBSCRIBERS THE SUBSCRIBER LOST MONEY FOLLOWING HIS STOCK PICKS 😭😭😭😭

@StockMKTNewz [Thu Jul 16 01:31:51 +0000 2026]: South Korea's 🇰🇷 central bank just raised interest rates for the first time in more than 3 years - Bloomberg https://t.co/VcPT8HmxVw

@KobeissiLetter [Wed Jul 15 22:02:14 +0000 2026]: US Leveraged ETF growth is exploding: The number of US-listed leveraged ETFs is up to a record 700, now more than double the number seen at the end of 2024. More than 400 of these funds are leveraged single-stock ETFs. This comes as ~210 new leveraged funds have been launched year-to-date, already surpassing the ~205 seen in the full year 2025. In the first half of 2026, leveraged and inverse ETFs made up 31% of all US-listed ETF launches, up from 22% in all of 2025. In June alone, 117 such funds had their debut, nearly half of the total 239 ETFs launched in the US market. Leverage has never been more popular.

@gurgavin [Wed Jul 15 21:10:44 +0000 2026]: ARGENTINA WILL PLAY SPAIN IN THE FINAL NOW 60% CHANCE SPAIN WINS AND ARGENTINA 40% CAN MESSI WIN IT BACK TO BACK ??? https://t.co/t2gWJyPg47

@gurgavin [Wed Jul 15 20:54:15 +0000 2026]: HOLY WHAT A COMEBACK BY ARGENTINA

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.