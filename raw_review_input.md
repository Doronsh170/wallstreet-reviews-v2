אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are a senior Wall Street market analyst writing an on-demand INTRADAY UPDATE in Hebrew,
covering ONLY the last two hours: 21:12–23:12 שעון ישראל, on 2026-07-03 (יום שישי).
Market state right now: השוק סגור (לילה / סוף שבוע / חג). Frame ALL market descriptions accordingly — if the cash market is not
open, NEVER describe it as trading or reacting. Futures / pre-market / after-hours moves may be described,
but always labeled as such (בחוזים העתידיים, בטרום מסחר, במסחר המאוחר).

STRICT RECENCY RULE — this is the whole point of this update:
- Include ONLY news, data releases, headlines and price moves from INSIDE the two-hour window above.
  An older story may get HALF A SENTENCE of context, and only if it directly explains a move inside the window.
- Use web search to verify WHEN each item happened. If you cannot confirm it happened inside the window — OMIT it.
- Do NOT recycle content from the prior-review context block below. If the last two hours were genuinely quiet,
  say so honestly in the first bullet ("שעתיים רגועות יחסית, ללא אירועים מהותיים") — never pad with old news.

TIMEFRAME OF NUMBERS — critical:
- The verified Finnhub percentages above are DAILY changes (vs. the previous close), NOT two-hour changes.
  When you use them, label them explicitly: "מתחילת היום". NEVER present a daily number as a two-hour move.
- A two-hour figure ("בשעתיים האחרונות עלתה ב-...") may appear ONLY if a source tweet or your web search
  states that intraday figure explicitly. NEVER derive a two-hour change from the daily numbers.
- Direction words must still match the DIRECTIONAL FACTS block (daily direction), framed as "מתחילת היום".

EXACTLY 4 bullets, in this order:
* מה קרה בשעתיים האחרונות: the single most important development inside the window and the market's
  immediate reaction (or the futures / pre-market reaction if the cash market is closed).
* הסיפור המרכזי: WHY the market moved — the main driver with clear cause-and-effect, and the transmission
  mechanism explained simply only when genuinely relevant.
* מניות ונכסים בתנועה: the 1-3 most notable movers WITHIN the window, each with its trigger.
  Stock items open with "מניית <שם בעברית> (TICKER)".
* מה הלאה: what to watch in the COMING hours (scheduled data, Fed speakers, earnings after the close) —
  Israel time, with the consensus where known.
Each bullet: 2-3 short sentences of flowing Hebrew prose — not a list of figures. After the Hebrew label,
continue in Hebrew words — never open with a ticker, a price or an English term. No ETF proxies, no Finnhub,
no ISO dates.

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
  "title": "עדכון ביניים מוול סטריט 🇺🇸 – יום שישי, 3.7.2026, 23:12",
  "date": "2026-07-03",
  "sections": [
    {
      "heading": "עדכון ביניים",
      "content": "* נושא ראשון: משפט אנליטי תמציתי עם מספרים.\n* נושא שני: ...\n* נושא שלישי: ..."
    }
  ]
}
- EXACTLY 1 section. Heading EXACTLY "עדכון ביניים". Title EXACTLY as given above.
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
Use web search to check if ANY US economic data (CPI, PPI, NFP, Jobless Claims, ISM PMI, GDP, Retail Sales,
Consumer Sentiment), an FOMC decision/minutes, or a Fed official's speech happened between 21:12–23:12 Israel time
on 2026-07-03. If yes — include actual vs forecast vs previous AND the immediate market reaction.
If none — skip, but you MUST check first. Do NOT include data released earlier today, outside the window.
══════════════════════════════════

══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══
Already published on the site. Your update covers ONLY the last two hours. Mention an item below ONLY if there is a genuinely NEW development about it inside the two-hour window.

[נקודות מרכזיות]
* תמונת פתיחה: המסחר יחזור ביום שני, 6.7.2026, אחרי סוף שבוע ארוך של חג העצמאות האמריקאי, כשברקע רוטציה חדה ממניות הטכנולוגיה והצמיחה אל סקטורים דפנסיביים ומניות ערך. שני גורמים תומכים ברקע: עונתיות חיובית של יולי, החודש החזק בשנה עם עלייה ממוצעת של 2.5% ב-S&P 500 מאז 2005 ו-11 שנים רצופות ללא ירידה בחודש זה, וזרימות שיא של קרנות השקעה זרות למניות אמריקאיות, כ-2.5% מסך הנכסים המנוהלים מתחילת השנה.
* הסיפור המרכזי: שוק העבודה יישאר הציר שסביבו נע השוק גם בשבוע הקרוב. הרוויזיות מטה בנתוני התעסוקה נמשכות, 14 מתוך 17 החודשים האחרונים תוקנו כלפי מטה בסך כולל של 710 אלף משרות, ואפריל ומאי תוקנו יחד ב-74 אלף נוספים. תמונה תעסוקתית רכה יותר מקטינה את הלחץ על הפדרל ריזרב להדק את המדיניות, וזה הרקע לביקוש לזהב ולחולשת הדולר בימים האחרונים.
* מאקרו ואירועים: הנתון המרכזי ביום שני הוא מדד מנהלי הרכש במגזר השירותים ISM Services PMI ליוני, שיתפרסם בשעה 17:00 שעון ישראל, עם צפי של 54.5 מול 54.5 בקריאה הקודמת. אחרי נתוני התעסוקה החלשים, השוק יחפש בנתון הזה אישור שצד השירותים והצריכה של הכלכלה מחזיק מעמד. הפתעה כלפי מטה תחזק את תרחיש ההאטה, בעוד קריאה יציבה תתמוך בהמשך תיאבון הסיכון.
* דוחות ומניות במוקד: לוח הדוחות ביום שני דל לקראת פתיחת עונת הדוחות, והאירוע הבולט בשבוע הקרוב הוא רישום מניות SK Hynix למסחר בנאסד"ק. מניית טסלה (TSLA): שירות הרובוטקסי הושק במיאמי ומבחני ההנדסה של ה-Cybercab הראשון מקו הייצור החלו באוסטין, אך למרות החדשות, המניה ירדה בחדות ביום המסחר האחרון. מניית מיקרון (MU): לפי דיווחים, מייקל ביורי פתח פוזיציית שורט על המניה, שירדה גם היא ביום המסחר האחרון. מניית מטא (META): דיווח חדש על מגעים עם סמסונג לייצור שבב בינה מלאכותית ייעודי בהיקף של כ-100 טריליון וון, אך למרות הדיווח, המניה ירדה.
* שורה תחתונה: כיוון המסחר ביום שני ייקבע בעיקר בנתון ה-ISM בשעה 17:00 ובשאלה אם הרוטציה מהטכנולוגיה אל הסקטורים הדפנסיביים נמשכת או מתמתנת. גורם מעצים שכדאי להכיר: פעילות האיזון היומית של תעודות סל ממונפות הגיעה לשיא של כ-50 מיליארד דולר ומהווה 1.6% מנפח החוזים על S&P 500, ולכן תנועה כיוונית עשויה להתעצם דווקא בשעה האחרונה של המסחר.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-03. Never mention in the review that these came from tweets/posts:

@wallstengine [Fri Jul 03 19:15:22 +0000 2026]: Trump’s outgoing AI adviser Sriram Krishnan told FT the administration will not create a formal AI licensing regime. “There will not be an FDA for AI,” he said. Krishnan said requiring companies to go through lawyers before releasing a model would put “sand in the gears” of AI development and is “never, never going to happen under President Trump.” He also blamed part of the AI backlash on the industry’s own messaging, saying AI companies focused too much on dystopian risks and “have done a terrible job” explaining real benefits like medical diagnosis.

@StockMKTNewz [Fri Jul 03 18:52:24 +0000 2026]: I'm hosting a FREE Webinar on Thursday at 4:15 PM ET. You just need to secure your seats before the webinar starts I used my connections to get some great Traders and Stock Pickers to join us to give their best advice for navigating these markets! https://t.co/ky7GEzhC8X

@wallstengine [Fri Jul 03 19:07:57 +0000 2026]: Running a 4th of July giveaway with TrendSpider, a charting platform for traders I secured 5 giveaways for our followers Each winner gets 3 months of TrendSpider Premium ($378) To enter: Follow @wallstengine & tap the bell for notification Like & RT this post Comment a ticker Entries close July 7 EOD. Winners will be picked by random draw from valid entries and announced July 8. TrendSpider is also running 42% off right now. Affiliate link: https://t.co/JRGhR9rAfr

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.