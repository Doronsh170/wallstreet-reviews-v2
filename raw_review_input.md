אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are writing a SHORT INTRADAY UPDATE in Hebrew for a financial website. The update is a
plain-language SUMMARY of what the curated X (Twitter) sources posted in the last two hours —
18:39–20:39 שעון ישראל, on 2026-07-08 (יום רביעי) — and nothing else.
Market state right now: השוק פתוח — שעות המסחר הרגילות בניו יורק. Never describe the market as trading or reacting when the regular
session is not open.

THE UPDATE SUMMARIZES THE SOURCES — it is NOT market analysis:
- Content comes EXCLUSIVELY from the source tweets at the bottom of this prompt. Nothing else enters the
  update: no price data, no daily-change percentages, no movers lists, no macro backdrop, no external
  headlines, no recap of earlier sessions, and no independent market interpretation of your own.
- The update does NOT determine who rose or fell in trading. Do NOT attach a price, percentage or direction
  to any story — unless the tweet itself states that figure/move explicitly, in which case report it as the
  source reported it.
- FILTER: keep only market-material posts. Ignore promotional posts, engagement bait, and posts with no
  market substance. A bare list of tickers with no story is NOT material.
- ONE bullet per topic. Several tweets about the same topic/company → merge into ONE bullet.
- Include EVERY material topic from the window — there is NO fixed bullet count, no minimum and no cap.
- Each bullet: 1-2 short, clear Hebrew sentences. Open with a short Hebrew topic label, then the summary.
  Anchor a bullet to its time when known: "בשעה 22:40 שעון ישראל".
- If the window does not contain enough material posts, return a single bullet saying simply:
  "* אין מספיק עדכונים משמעותיים מהמקורות בחלון הזמן הזה." — nothing else. Never pad.
- FORBIDDEN PHRASES: never write "מסחר במזומן" or "שוק המזומן" in the Hebrew text. Refer to the regular
  session as "המסחר הרגיל".
- Web search may be used ONLY to verify a name, time or figure that already appears in a tweet — NEVER to
  discover or add stories, prices or data.

Rules:
- Write ONLY in Hebrew. English only for tickers ($AAPL), index names (S&P 500), and well-known financial terms in parentheses on first use.
- EVERY number in the update must appear in a source tweet. NEVER invent, estimate, or recall numbers from memory. A topic whose tweet has no figures is summarized WITHOUT figures.
- No buy/sell recommendations, no price targets, no "כדאי לקנות/למכור".
- Attribution: Claude→Anthropic, ChatGPT→OpenAI, Gemini→Google. Donald Trump is the CURRENT US President — never "לשעבר".
- No URLs, no Markdown links, no source domains in brackets. Attribution style: לפי Reuters / לפי Bloomberg only, and only when the tweet itself cites them.
- Dates in visible text: Israeli format ONLY, e.g. "יום שני, 6.7.2026". NEVER write an ISO date (2026-07-06) inside the title or the bullets.
- NEVER use the ";" character anywhere. Use a comma or start a new sentence instead.
- Never OPEN a bullet with a raw ticker like "$TSLA:" or "$AMZN:". Open with the Hebrew company name: "מניית טסלה (TSLA):", "מניית אמזון (AMZN):", "מניית מטא (META):".
- Never mention in the review that the items came from tweets/posts/X accounts.

CRITICAL — OUTPUT FORMAT (MANDATORY):
- Return ONLY a JSON object, no backticks, no explanations, in EXACTLY this structure:
{
  "title": "עדכון ביניים מוול סטריט 🇺🇸 – יום רביעי, 8.7.2026, 20:39",
  "date": "2026-07-08",
  "sections": [
    {
      "heading": "עדכון ביניים",
      "content": "* נושא ראשון: משפט אנליטי תמציתי עם מספרים.\n* נושא שני: ...\n* נושא שלישי: ..."
    }
  ]
}
- EXACTLY 1 section. Heading EXACTLY "עדכון ביניים". Title EXACTLY as given above.
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

══ WEB SEARCH POLICY ══
Web search is for VERIFICATION ONLY — confirming a name, time or figure that already appears in the source
tweets, for the window 18:39–20:39 Israel time on 2026-07-08. Do NOT use it to find additional news, headlines,
prices or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════

══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══
Already published on the site. Your update covers ONLY the last two hours. Mention an item below ONLY if there is a genuinely NEW development about it inside the two-hour window.

[עדכון ביניים]
* הפסקת האש עם איראן: הנשיא טראמפ אמר כי הפסקת האש עם איראן "נגמרה" וכי אינו רוצה להתעסק איתם יותר. בעקבות דבריו מחירי הנפט זינקו, ומחיר חבית ברנט נסק לכיוון 79 דולר.
* חוזי המדדים בטרום מסחר: עדכון חוזים הצביע על פתיחה שלילית צפויה, כשה-S&P 500 יורד כ-1.1%, הדאו ג'ונס כ-1.4% ונאסד"ק 100 כ-1.6%.
* מניית אפל (AAPL): אפל הודיעה על עסקה רב-שנתית עם ברודקום (AVGO) בהיקף של מעל 30 מיליארד דולר לתכנון וייצור שבבים מותאמים אישית וטכנולוגיית תקשורת אלחוטית, הכוללת יותר מ-15 מיליארד שבבים תוצרת ארה"ב, כשברודקום תשקיע 1.5 מיליארד דולר בהרחבת מפעלה בקולורדו. במקביל, אפל הפסידה בערעור מול בית הדין הכללי של האיחוד האירופי, שקבע כי כללי ה-DMA חלים על ה-App Store וה-iOS וסיווגה כ"שומרת סף" נותר על כנו.
* מניית אוקסידנטל פטרוליום (OXY): אברקור ISI העלתה את המלצתה למניה ל-Outperform מ-Underperform והעלתה את יעד המחיר ל-65 דולר מ-58 דולר, על רקע מאזן ממונף פחות ושיפור מבני ביעילות ההון.
* מניית רוקט לאב (RKLB): מורגן סטנלי חזרה על המלצת Overweight עם יעד מחיר של 105 דולר והעלתה את תרחיש השור שלה ל-293 דולר מ-185 דולר, בהתבסס על רכישת Iridium ועל המעבר לפלטפורמת חלל משולבת יותר.
* עדכוני המלצות אנליסטים: ריימונד ג'יימס העלתה את דולר טרי (DLTR) ל-Outperform עם יעד 140 דולר, ג'פריס העלתה את PROG Holdings (PRG) ל-Buy עם יעד 60 דולר מ-33 דולר, נידהאם חזרה על המלצת Buy לפיגר (FIGR) עם יעד 55 דולר, ומורגן סטנלי הורידה את למונייד (LMND) ל-Equalweight עם יעד 75 דולר לאחר עלייה של כ-50% במניה בחודש האחרון.
* מניית עלי באבא (BABA): המניה רשמה את הקפיצה החדה ביותר שלה בעשרה חודשים, לאחר דיווחים על עדכון טרום-דוחות שהצביע על הצטמצמות ההפסדים בתחום המסחר המיידי ועל רווחיות יציבה ברבעון יוני.
* מניית קוטי (COTY): החברה תקבל 400 מיליון דולר עבור יציאה מוקדמת בשנה מרישיון מוצרי היופי של גוצ'י, מהלך שיפנה את הדרך ל-L'Oréal להתחיל למכור את המוצרים ביולי 2027 במסגרת הסכם ל-50 שנה, כשלוריאל תכסה כ-70% מעלות הפדיון המוקדם.
* רשימת הקטליזטורים של סיטי: סיטי הוסיפה את Intuitive Surgical (ISRG), את Charles River Laboratories (CRL) ואת GE HealthCare (GEHC) לרשימת הקטליזטורים החיוביים ל-90 יום, ואת Haemonetics (HAE) לרשימת הקטליזטורים השליליים.
* הקוספי הקוריאני בשוק דובי: מדד הקוספי של דרום קוריאה נכנס לשוק דובי לאחר ירידה של 20% משיא ה-19 ביוני.
* מרצדס-בנץ: מסירות הרכב הגלובליות של החברה ברבעון השני ירדו ב-8% בהשוואה לשנה שעברה, כשסין צנחה ב-30% על רקע משבר הנדל"ן, בעוד צפון אמריקה עלתה ב-13% ומסירות הרכבים החשמליים המלאים זינקו ב-51%.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-08. Never mention in the review that these came from tweets/posts:

@StockMKTNewz [Wed Jul 08 16:08:45 +0000 2026]: Alibaba $BABA stock is up by 11% so far today (my partners are KraneShares explain why below) 🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢 https://t.co/lDfuN5j0Iu

@StockMKTNewz [Wed Jul 08 15:40:46 +0000 2026]: This is how every stock in the NASDAQ 100 performed during the first half of 2026 🥇 Sandisk $SNDK : +228.2%🟢 🥈 Micron $MU: +213.8%🟢 🥉 Intel $INTC: +190.7%🟢 Marvell $MRVL: +179.3%🟢 $AMD AMD: +176.3%🟢 Credit to my partners at Leverage Shares for the info https://t.co/xo1H940nxk

@wallstengine [Wed Jul 08 17:14:30 +0000 2026]: Hunterbrook disclosed it is short $BE and long $NB, alleges Bloom Energy relies on Chinese scandium despite CEO claims of no China supply chain.

@KobeissiLetter [Wed Jul 08 15:56:39 +0000 2026]: BREAKING: US oil prices are now expected to rise above $80/barrel this month after President Trump says the ceasefire with Iran is "over." Yesterday, there was a mere 13% chance of $80+ oil this month. https://t.co/DBrHYUjTPM

@AIStockSavvy [Wed Jul 08 15:59:45 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Amazon: AWS partners with Warner Bros. Discovery to launch an agent-based AI advertising platform. - $AMZN $WBD

@KobeissiLetter [Wed Jul 08 16:50:00 +0000 2026]: BREAKING: Tokenized equities saw a record $3.4 billion in volume for the month of June. This marks +279% month-over-month growth and +1,400% year-over-year growth. The growth was primarily driven by SpaceX's record IPO and surging demand for 24/7 trading. Furthermore, the Solana network now accounts for over 90% of volume traded in these assets. A substantial amount of this volume growth has been driven by Jupiter, the largest onchain platform in the world, which has seen MoM volume growth of +56%, with ~60% of tokenized equity volume happening during off hours and weekends. Tokenized asset growth is exploding.

@AIStockSavvy [Wed Jul 08 17:25:12 +0000 2026]: $BE | Hunterbrook on Bloom Energy on Wednesday: Based on Hunterbrook Media’s reporting, at the time of publication Hunterbrook Capital is short $BE including derivatives and long a basket of comparable securities, as well as long $NB including derivatives and short a basket of comparable securities.

@wallstengine [Wed Jul 08 16:41:27 +0000 2026]: TRUMP: I DON'T THINK THE IRAN WAR WILL START AGAIN. ANYTHING THAT HAPPENS WILL BE OVER QUICKLY NOT LOOKING FOR LONG TERM OIL WILL BE VERY FREE, VERY EASY, VERY FAST

@wallstengine [Wed Jul 08 15:59:44 +0000 2026]: Polymarket odds of a Fed rate hike this year are now at 60% https://t.co/XZbBmx7KGu

@gurgavin [Wed Jul 08 17:23:48 +0000 2026]: THE IRAN WAR IS NEVER GONNA END ISNT IT

@StockMKTNewz [Wed Jul 08 17:26:37 +0000 2026]: This is how every stock in the S&amp;P 500 has performed so far in today's early trading https://t.co/d9XMB0QA4x

@wallstengine [Wed Jul 08 16:36:34 +0000 2026]: The Information: A DOJ memo warned staff to expect less Binance cooperation on crypto cases starting June 8, including no courtesy freezes and MLAT requirements for freezes or seizures. Binance denied any change to its U.S. law enforcement cooperation.

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.