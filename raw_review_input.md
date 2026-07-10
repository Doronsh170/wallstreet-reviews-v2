אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are a senior Wall Street investment advisor writing your signature END-OF-DAY review in Hebrew for
2026-07-10 (יום שישי). PAST TENSE.

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
  "title": "סיכום יום המסחר בוול סטריט 🇺🇸 – יום שישי, 10.7.2026",
  "date": "2026-07-10",
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
  S&P 500 (SPY ETF): $754.95 (daily: +0.43%), prev close: $751.71
  Nasdaq 100 (QQQ ETF): $725.51 (daily: +0.31%), prev close: $723.28
  Dow Jones (DIA ETF): $525.78 (daily: +0.30%), prev close: $524.19
  Russell 2000 (IWM ETF): $295.99 (daily: -0.42%), prev close: $297.24
  Energy Sector (XLE ETF): $55.08 (daily: +0.47%), prev close: $54.82
  Technology Sector (XLK ETF): $185.78 (daily: +0.23%), prev close: $185.35
  Financials Sector (XLF ETF): $55.71 (daily: +0.31%), prev close: $55.54
  Consumer Discretionary Sector (XLY ETF): $117.24 (daily: +0.33%), prev close: $116.85
  Healthcare Sector (XLV ETF): $160.84 (daily: -0.82%), prev close: $162.17
  Industrials Sector (XLI ETF): $181.92 (daily: +0.45%), prev close: $181.11
  Consumer Staples Sector (XLP ETF): $84.12 (daily: +1.11%), prev close: $83.20
  Utilities Sector (XLU ETF): $45.41 (daily: +0.62%), prev close: $45.13
  WTI Crude Oil (USO ETF): $108.70 (daily: -0.28%), prev close: $109.01
  Brent Crude Oil (BNO ETF): $42.15 (daily: -0.05%), prev close: $42.17
  Gold (GLD ETF): $377.01 (daily: -0.31%), prev close: $378.18
  Silver (SLV ETF): $53.95 (daily: -0.35%), prev close: $54.14
  Bitcoin (IBIT ETF): $36.23 (daily: +1.17%), prev close: $35.81
  US 20Y+ Bonds (TLT ETF): $84.47 (daily: -0.02%), prev close: $84.49
  US Dollar (UUP ETF): $28.39 (daily: +0.11%), prev close: $28.36
  VIX Volatility (VIXY ETF): $20.34 (daily: -2.26%), prev close: $20.81

INDIVIDUAL STOCKS mentioned in the source tweets (verified quotes):
  $AAPL: $315.32 (daily: -0.28%), prev close: $316.22
  $MU: $979.30 (daily: -1.24%), prev close: $991.64
  $SNDK: $1915.92 (daily: +3.10%), prev close: $1858.27
  $META: $669.21 (daily: +5.97%), prev close: $631.48
  $QQQ: $725.51 (daily: +0.31%), prev close: $723.28
  $SPY: $754.95 (daily: +0.43%), prev close: $751.71
  $USO: $108.70 (daily: -0.28%), prev close: $109.01
  $CRCL: $66.14 (daily: +4.97%), prev close: $63.01

DIRECTIONAL FACTS — Hebrew direction words (עולה/יורד/צונח/מזנק) MUST match these:
  נפט (WTI/ברנט): מעורב — להשתמש בניסוח ניטרלי בלבד (USO: -0.28%, BNO: -0.05%)
  זהב: יורד (GLD: -0.31%)
  ביטקוין: עולה (IBIT: +1.17%)
  דולר: יציב/כמעט ללא שינוי (UUP: +0.11%)
  תנודתיות / VIX: יורד (VIXY: -2.26%)
  אג"ח ארוכות / TLT: יציב/כמעט ללא שינוי (TLT: -0.02%)

The % changes above are ACCURATE — use them for direction and magnitude.
The ETF tickers above (SPY/QQQ/DIA/USO/GLD/...) are measurement instruments for YOUR verification only — NEVER name them, Finnhub, or the word 'proxy' in the visible Hebrew text.
For exact index LEVELS (points), gold/oil absolute prices, VIX level, Bitcoin price, 10Y yield: verify via web search. Do NOT estimate them from ETF prices.
For sector performance (XLE/XLK/...): USE ONLY the Finnhub numbers above — never invent sector percentages.
If ANY percentage you write contradicts the data above, you are WRONG. Fix it.
══════════════════════════════════════════════════════════════════════════════

══ MANDATORY MACRO DATA CHECK ══
Use web search to check if ANY of these were released on 2026-07-11: CPI (headline AND core),
PPI (headline AND core), NFP, Jobless Claims, Consumer Sentiment (Michigan), ISM PMI, GDP,
Retail Sales, FOMC decision/minutes. If released — include with actual, forecast, previous,
AND the market implication. If none — skip, but you MUST check first.
══════════════════════════════════

══ CONTEXT: THIS MORNING'S PRE-MARKET BRIEFING ══
Published before the session. Use it to resolve scheduled items (expected → actual), do NOT quote it verbatim.

[נקודות מרכזיות]
* מומנטום השבבים מול זהירות לפני הפתיחה: וול סטריט נכנסת ליום המסחר האחרון של השבוע כשהשאלה המרכזית היא אם ראלי הטכנולוגיה והזיכרון ישמור על הקצב, על רקע נסיגה במחירי הנפט שממתנת את חששות האינפלציה ומול מתיחות גיאופוליטית מתחדשת מול איראן. היומן הכלכלי דל היום ונטול נתוני מאקרו כבדים, ולכן הזרקורים יופנו לסיפורי המניות, לפתיחת המסחר במניית SK Hynix ולתגובת השוק להתפתחויות סביב טהרן. הסנטימנט נותר תומך אך זהיר, כשהמשקיעים בוחנים אם הריכוזיות הגבוהה בענקיות הטכנולוגיה תמשיך להוביל את המדדים.
* יומן מאקרו דל ודלתא פותחת את הדוחות: הלוח הכלכלי היום דליל, כשתשומת הלב מופנית לדוח הנפט החודשי של סוכנות האנרגיה הבינלאומית (IEA) שיתפרסם סביב 11:00 שעון ישראל ולנתוני מספר אסדות הקידוח של בייקר יוז ב-20:00. בחזית הדוחות, חברת התעופה דלתא (DAL) תדווח לפני הפתיחה בסביבות 13:30 שעון ישראל ותספק אינדיקציה ראשונה לבריאות הצריכה והתעופה לקראת עונת הדוחות. בהיעדר זרז מאקרו, כיוון המסחר יוכתב בעיקר מהמומנטום הסקטוריאלי ומחדשות החברות.
* הנפקת SK Hynix יוצאת לדרך: מניית יצרנית הזיכרון הקוריאנית SK Hynix צפויה להתחיל להיסחר היום תחת הטיקר הזמני SKHYV, לפני מעבר לטיקר הקבוע SKHY בתחילת השבוע הבא, בהנפקת ADR שמשכה ביקושים אדירים של קרוב ל-200 מיליארד דולר ומעל 500 משקיעים. החברה עדכנה כי תגייס כ-40 טריליון וון (כ-26.5 מיליארד דולר), מעט פחות מיעד קודם של 43 טריליון וון. עבור המשקיעים זהו מבחן חי לתיאבון סביב מחזור הזיכרון, שממשיך להזין את מניות מיקרון (MU) וסאנדיסק (SNDK) ואת מגזר השבבים כולו.
* מניית מטא (META): דיווח של פייננשל טיימס חושף כי טנסנט מנהלת מגעים להפוך לבעלת המניות הגדולה בחברת מאנוס (Manus), בעוד משקיעים ממהרים לפרק את הרכישה של מאנוס בידי מטא בשווי כ-2 מיליארד דולר. במקביל, קרן ARK של קאתי ווד הוסיפה כ-34 אלף מניות מטא, המשך להתעניינות הגוברת בחברה על רקע מרוץ ה-AI וההשקעות שלה בתשתיות המחשוב. המשקיעים יבחנו אם הסיבוב סביב מאנוס מסמן שינוי באסטרטגיית הרכישות של החברה.
* גל קניות שיא של בכירי הטכנולוגיה: לפי נתוני SentimenTrader, 28 מנהלים בכירים בחברות מגזר הטכנולוגיה רכשו בחצי השנה האחרונה מניות של החברות שלהם עצמם בשוק הפתוח, המספר הגבוה ביותר שנרשם אי פעם ויותר מכפול לעומת תחילת 2026. הנתון עוקף את השיא הקודם של 25 מנהלים שנקבע ב-2011, בעוד בתחילת 2025 נמנו חמישה קונים בלבד. קניות מסיביות של מקורבים נחשבות לרוב לאות אמון פנימי בהמשך העליות, והן מספקות רוח גבית סנטימנטלית למגזר שמוביל את השוק.
* מתיחות מול איראן וזרקור על הנפט: על פי דיווח ב-וול סטריט ג'ורנל, ישראל העבירה לארה"ב מודיעין חדש לפיו איראן עשויה לשקול מזימה לפגוע בנשיא טראמפ, התפתחות שמחדדת את סיכון הזנב הגיאופוליטי אחרי שהנפט כבר נסוג בחדות מרמות השיא של תחילת השבוע. במקביל, יצוא מוצרי הנפט של ארה"ב ירד לשיא של כ-8.7 מיליון חביות ביום, עדות לביקוש עולמי חזק לדלק אמריקאי. השילוב בין הרגעת מחירים לבין סיכון גיאופוליטי חי הופך את דוח ה-IEA ואת ההתפתחויות סביב טהרן לגורם מפתח בכיוון האנרגיה היום.
* גל המלצות קנייה בטכנולוגיה: בית ההשקעות Stifel המשיך לתדלק את הסנטימנט החיובי עם שדרוג של מניית טוויליו (TWLO) להמלצת קנייה והעלאת מחיר היעד ל-260 דולר מ-175 דולר, בטענה שהחברה ממוצבת היטב לגל ה-AI הסוכני (agentic) דרך פלטפורמת התקשורת שלה. באותה נשימה שדרג הבית גם את מניית שופיפיי (SHOP) להמלצת קנייה עם יעד של 150 דולר, בהצביעו על נתיב ריאלי לצמיחת הכנסות של מעל 30% ב-2026. ההמלצות מצטרפות לזרם החיובי סביב מניות הצמיחה ומחזקות את נרטיב ה-AI כמנוע המרכזי של השוק.
* שורה תחתונה: את כיוון יום המסחר האחרון של השבוע יכריעו בעיקר המשך המומנטום במניות השבבים והזיכרון, ובראשם קבלת הפנים להנפקת SK Hynix, לצד תגובת השוק להתפתחויות הגיאופוליטיות מול איראן והשפעתן על הנפט. בהיעדר נתוני מאקרו כבדים, דוח דלתא וזרם ההמלצות בטכנולוגיה יספקו את הטון, כשהריכוזיות הגבוהה בענקיות ממשיכה להפוך כל תפנית בהן לקריטית עבור המדדים כולם.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-11. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Fri Jul 10 20:29:12 +0000 2026]: BREAKING: Apple, $AAPL, has sued OpenAI, alleging "misappropriation of trade secrets," according to newly filed court records.

@gurgavin [Fri Jul 10 20:34:28 +0000 2026]: JUST IN : APPLE HAS JUST SUED OPENAI IN FEDERAL COURT FOR ALLEGED TRADE SECRET THEFT $AAPL

@gurgavin [Wed Jul 08 19:47:47 +0000 2026]: META TO INVEST $10 BILLION IN CANADA META IS LOOKING TO BUILD ITS FIRST DATA CENTER IN CANADA TO SUPPORT ITS AI AMBITIONS THE DATA CENTER WILL BE IN ALBERTA AND CREATE OVER 3,000 LOCAL CONSTRUCTION JOBS 🇨🇦🇨🇦🇨🇦 🇨🇦 $META

@StockMKTNewz [Fri Jul 10 20:33:45 +0000 2026]: Apple $AAPL just filed a lawsuit against OpenAI in federal court alleging trade secret theft Apple says OpenAI took the iPhone maker’s intellectual property in order to develop its own consumer hardware. “This much is clear, however: at every level, from members of its Technical Staff to its Chief Hardware Officer, and in coordination with business partners, OpenAI has been stealing Apple’s trade secrets and confidential information,” Apple said in a legal filing - CNBC

@KobeissiLetter [Fri Jul 10 13:21:22 +0000 2026]: BREAKING: Circle stock, $CRCL, surges over +15% after the U.S. Office of the Comptroller of the Currency grants the company approval to operate as a bank. https://t.co/aDUYWZx0HP

@gurgavin [Thu Jul 09 16:52:48 +0000 2026]: SOMEONE JUST FILED FOR A S&amp;P 500 &amp; NASDAQ 100 ETF THAT EXCLUDES ONLY ELON MUSK’S COMPANIES THE FUNDS ARE CALLED EX-ELON ENTERPRISES ETF THE FUND EXCLUDES ANY COMPANY “FOUNDED, CONTROLLED, OR LED” BY MUSK CITING GOVERNANCE CONCERNS &amp; POLITICAL RISK $SPNE $QQNE

@KobeissiLetter [Fri Jul 10 01:05:23 +0000 2026]: Corporate insiders are buying tech stocks at a record pace: 28 executives at companies within the US technology sector ETF, $XLK, have purchased their own stock on the open market over the last 6 months, the highest count on record, according to SentimenTrader. This figure has DOUBLED since the start of 2026. This also surpasses the previous record of 25 insiders set in 2011. By comparison, in early 2025, just 5 executives were buyers. US executives are rushing to buy tech stocks.

@StockMKTNewz [Fri Jul 10 20:26:56 +0000 2026]: APPLE $AAPL SUES OPENAI ALLEGING MISAPPROPRIATION OF TRADE SECRETS - COURT RECORDS

@StockMKTNewz [Fri Jul 10 20:18:20 +0000 2026]: The 🇺🇸 loosened export controls on the United Arab Emirates 🇦🇪, making it easier to export Nvidia $NVDA AI chips, military equipment, commercial satellites and spacecraft https://t.co/FM7gPWruQD

@wallstengine [Fri Jul 10 15:18:12 +0000 2026]: Important SK hynix listing note for today: The ADR debut will trade under $SKHYV today, not $SKHY, because today is when-issued trading. Regular-way trading in $SKHY starts Monday. Leverage Shares’ $SKHX and $SKHZ also begin Monday, so they won’t be available to trade today. https://t.co/6qYzBjZCCB

@gurgavin [Fri Jul 10 20:12:35 +0000 2026]: ARITZIA REPORTED EARNINGS YESTERDAY REVENUE UP 43% 📈 COMP SALES UP 35%📈 DIGITAL REVENUE UP 56%📈 US REVENUE UP 55%📈 PROFIT PER SHARE UP 96%📈 ONE OF THE BEST GROWTH STORIES IN CANADA CURRENTLY 🇨🇦🇨🇦🇨🇦🇨🇦 $ATZ https://t.co/pqgJGuNjTK

@gurgavin [Fri Jul 10 17:36:14 +0000 2026]: *SK HYNIX CEO SAYS MEMORY CHIP SHORTAGE MAY PERSIST PAST 2030 $SKHYV

@KobeissiLetter [Fri Jul 10 15:50:01 +0000 2026]: BREAKING: SK Hynix stock, South Korea’s second most valuable company, officially debuts on the Nasdaq and surges +14% at the open, now worth over $1 trillion. The company’s ADRs were priced at $149/share, raising $26.5 billion. https://t.co/BDUARtVkTi

@gurgavin [Wed Jul 08 18:08:57 +0000 2026]: FOMC MEETING MINUTES ARE OUT *ALL FOMC PARTICIPANTS SUPPORTED KEEPING INTEREST RATES UNCHANGED, THOUGH A FEW SAW A CASE FOR A RATE HIKE *FED STAFF RAISED THEIR 2026–2027 INFLATION FORECASTS, LOWERED GDP GROWTH PROJECTIONS, AND SAW UPSIDE RISKS TO PRICE STABILITY

@wallstengine [Fri Jul 10 15:36:44 +0000 2026]: SK HYNIX OPENS UP 14% AT $170, IPO AT $149 $SKHYV $SKHY

@AIStockSavvy [Fri Jul 10 20:27:00 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $AAPL Apple Sues OpenAI Alleging Misappropriation of Trade Secrets, Court Records Show

@wallstengine [Fri Jul 10 15:50:47 +0000 2026]: Nearly 50 million shares have already traded. $SKHYV $SKHY https://t.co/csb25BvepG

@KobeissiLetter [Fri Jul 10 20:03:56 +0000 2026]: BREAKING: The S&amp;P 500 closes rises for a second straight week and closes just 0.6% away from a fresh record high. https://t.co/Opa1ioRHkj

@KobeissiLetter [Fri Jul 10 14:39:30 +0000 2026]: BREAKING: President Trump says Iran has asked the US to continue "talks" and he has "agreed to do so, but the US has stated to them, in no uncertain terms, that the cease fire is over." https://t.co/Wt16VxOFbL

@KobeissiLetter [Thu Jul 09 22:22:49 +0000 2026]: BREAKING: Total US oil product exports surged to a record 8.7 million barrels per day last week. The increase was led by propane, followed by diesel, gasoline, and jet fuel cargoes. Most US diesel exports are headed to Brazil and the rest of South America, while ~14% is bound for Europe. Since March, US oil product exports have risen +2.0 million barrels per day, or +30%. By comparison, in early 2022, refined product shipments briefly fell below 4.0 million barrels per day. This comes despite weekly crude oil exports declining -3.1 million barrels per day from their April peak, to 3.3 million barrels per day, close to the average levels seen over the last 2 years. Global demand for American fuel is skyrocketing.

@KobeissiLetter [Thu Jul 09 20:34:59 +0000 2026]: BREAKING: US consumer credit fell -$182 million in May, the first monthly decline since November 2024. This was significantly below expectations of a +$17.5 billion increase and followed a +$20.8 billion increase in April. The decline was driven by revolving credit, which includes credit cards, plunging -$5.3 billion, the 2nd-largest monthly drop since November 2020. This comes after a +$11.5 billion and +$10.7 billion increase in April and March. At the same time, non-revolving credit, which includes auto and student loans, jumped +$5.1 billion, the smallest monthly increase since February. Meanwhile, the average interest rate on credit cards rose to 22.15%, near the highest on record. Is consumer borrowing reaching a tipping point?

@gurgavin [Wed Jul 08 09:16:40 +0000 2026]: FUTURES UPDATE S&amp;P 500 DOWN 1.1% 📉 DOW JONES DOWN 1.4% 📉 NASDAQ 100 DOWN 1.6% 📉

@AIStockSavvy [Fri Jul 10 18:28:32 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: U.S. issues new Iran-related sanctions - Treasury website - $QQQ $SPY $USO

@AIStockSavvy [Fri Jul 10 15:13:05 +0000 2026]: SK Chairman: Memory Demand Won't Normalize Until AI Reaches General Artificial Intelligence - $SKHY $MU $SNDK

@AIStockSavvy [Fri Jul 10 15:12:09 +0000 2026]: SK Chairman Chey: Memory as a Service Model Is Another Area We Could Focus on in the Future - Bloomberg - $SKHY $MU $SNDK

@AIStockSavvy [Fri Jul 10 13:56:29 +0000 2026]: 📢 Companies Reporting Earnings Next Week $JPM $GS $BAC $WFC $C $FAST $AEHR $BNY $ELV $PNC $FHN $JNJ $MS $CTAS $CAG $ASML $BLK $JBHT $UAL $KARO $UNH $ABT $AAL $USB $PLD $TSM $GE $ISRG $NFLX $AA $TRV https://t.co/9ls0lI5sE0

@KobeissiLetter [Fri Jul 10 19:42:15 +0000 2026]: BREAKING: The Bank of Japan's total assets dropped -$146 billion in Q2 2026, to $3.97 trillion, the lowest since Q1 2020. This also marks the largest quarterly decline since the Quantitative Tightening (QT) program began in August 2024. Since the Q1 2024 peak, the BoJ has reduced its balance sheet by -$726 billion, or -15.6%. Japanese government bond holdings fell -$78 billion in Q2, to $3.22 trillion, the lowest since Q3 2020. Since the 2023 peak, JGB holdings have dropped -$459 billion, or -12.5%. The BoJ also sold -$74 million in equity ETFs and J-REITs last quarter, bringing its holdings down by -1.0%, to $234 billion, the lowest since 2022. Japan’s bond market is poised for more volatility.

@KobeissiLetter [Fri Jul 10 18:00:21 +0000 2026]: Retail investors are slowing their stock purchases: Retail investors have bought a net +$13.0 billion in US equities over the last month, the least since 2020, according to VandaTrack. Retail net monthly purchases have declined -$18.0 billion, or -58%, since early 2026. At the same time, net purchases of single stocks have fallen -$8.0 billion, or -71%, to $3.2 billion, the lowest since Q1 2020. Despite this, total retail turnover is up to a record $500 billion, doubling since mid-2024. This comes as retail investors are now selling stocks almost as aggressively as they are buying, compressing net purchases. Retail activity in the market is cooling down.

@AIStockSavvy [Fri Jul 10 17:45:52 +0000 2026]: SK Hynix CEO: memory chip shortage may persist beyond 2030 - $MU $SKHY $SNDK

@AIStockSavvy [Fri Jul 10 15:34:40 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: U.S. and Iran are expected to hold a new round of talks next week, possibly in Switzerland. - Axios - $QQQ $SPY $USO

@AIStockSavvy [Fri Jul 10 14:09:55 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $NU Nubank Mexico receives final approval to operate as a full bank

@AIStockSavvy [Fri Jul 10 14:01:28 +0000 2026]: $SKHY | SK Hynix ADR indicative opening price may be $180; issue price $149.

@gurgavin [Thu Jul 09 16:37:14 +0000 2026]: *ANTHROPIC ADDS 2008 CRISIS-ERA FED CHAIR BERNANKE TO GOVERNANCE BOARD

@wallstengine [Fri Jul 10 18:25:26 +0000 2026]: RT @wallstengine: BofA says $META's 2026 buildout math may be far better than expected: 6.5 GW of added capacity on $145B of capex implies…

@gurgavin [Wed Jul 08 19:42:59 +0000 2026]: LIKE IT OR NOT RATES HIKES ARE COMING SOON 56% WE SEE A HIKE BEFORE THIS YEAR ENDS AND A 75% CHANCE WE SEE HIKE'S GOING INTO NEXT YEAR ACCORDING TO KALSHI https://t.co/Y1T4xKIibi

@gurgavin [Wed Jul 08 17:23:48 +0000 2026]: THE IRAN WAR IS NEVER GONNA END ISNT IT

@StockMKTNewz [Fri Jul 10 19:27:36 +0000 2026]: The new Nasdaq 100 https://t.co/WeDJzKhxYR

@StockMKTNewz [Fri Jul 10 15:20:53 +0000 2026]: THE SK HYNIX US IPO IS HERE I am co hosting the live stream below on the WOLF page ... JOIN UP ⬇️ We have a HUGE panel of guests joining us throughout the day https://t.co/BBRLKlLn4I

@AIStockSavvy [Fri Jul 10 15:48:39 +0000 2026]: SK Hynix opens at $170 in U.S. debut; IPO price $149 SK Hynix opened at $170 per American depositary receipt (ADR) in its U.S. debut, up 14% from the $149 IPO price; shares climbed to $174 within minutes. Trading under temporary ticker SKHYV, the ADR offering raised $26.51 billion, the largest equity issuance ever by a non-U.S. company, underscoring investor appetite for firms positioned to benefit from the AI boom.

@wallstengine [Fri Jul 10 18:42:59 +0000 2026]: OpenAI and Google are reportedly selling advanced AI model access to Singapore-based subsidiaries of Alibaba, Baidu, and Tencent, per FT. Those Chinese companies are on the Pentagon’s 1260H list, but the sales are currently legal because U.S. AI controls do not broadly block model access by foreign subsidiaries. OpenAI said it suspended Alibaba-affiliated API users this month over concerns about illicit use and suspected distillation. Google said its AI services are available in Singapore and Hong Kong under usage policies.

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.