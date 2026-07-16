אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are writing a SHORT INTRADAY UPDATE in Hebrew for a financial website. The update is a
plain-language SUMMARY of what the curated X (Twitter) sources posted in the last two hours —
17:44–19:44 שעון ישראל, on 2026-07-16 (יום חמישי) — and nothing else.
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
  Anchor a bullet to its time when known using "בשעה 22:40" only. All times in this update are Israel time
  (already stated once in the window line above), so do NOT append "שעון ישראל" to individual bullets — it is
  redundant. At most one bullet may carry it if truly needed for clarity.
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
- NEVER use an em dash / double hyphen ("—" or "--") as a clause separator. Use a comma, a colon, or start a new sentence instead.
- Never OPEN a bullet with a raw ticker like "$TSLA:" or "$AMZN:". Open with the Hebrew company name: "מניית טסלה (TSLA):", "מניית אמזון (AMZN):", "מניית מטא (META):".
- Never mention in the review that the items came from tweets/posts/X accounts.

CRITICAL — OUTPUT FORMAT (MANDATORY):
- Return ONLY a JSON object, no backticks, no explanations, in EXACTLY this structure:
{
  "title": "עדכון ביניים מוול סטריט 🇺🇸 – יום חמישי, 16.7.2026, 19:44",
  "date": "2026-07-16",
  "summary": ["כותרת הנקודה: תמצית אמיתית של הנקודה במשפט קצר אחד", "כותרת שנייה: ...", "..."],
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

══ WEB SEARCH POLICY ══
Web search is for VERIFICATION ONLY — confirming a name, time or figure that already appears in the source
tweets, for the window 17:44–19:44 Israel time on 2026-07-16. Do NOT use it to find additional news, headlines,
prices or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════

══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══
Already published on the site. Your update covers ONLY the last two hours. Mention an item below ONLY if there is a genuinely NEW development about it inside the two-hour window.

[נקודות מרכזיות]
* החוזים נבלמים אחרי יומיים של ראלי: החוזים על S&P 500 יורדים כ-0.2% ואלו של הנאסד"ק כ-0.6%, בעוד חוזי הדאו עולים כ-0.2%, כשמניות השבבים שוב מושכות את הטכנולוגיה מטה. העצירה מגיעה אחרי יומיים של עליות ולקראת יום עמוס: שלישיית נתוני מאקרו ב-15:30 שעון ישראל ובראשם המכירות הקמעונאיות ליוני, המשך דוחות הבנקים, ונטפליקס (NFLX) שתדווח אחרי הנעילה. ברקע, מחירי הנפט שהוסיפו כ-1% ונסחרים מעל 80 דולר לחבית ממשיכים להעיב על נרטיב הדיסאינפלציה.
* מכירות קמעונאיות ותביעות אבטלה במוקד: היום ב-15:30 שעון ישראל יתפרסמו המכירות הקמעונאיות ליוני, עם צפי לעלייה של 0.2% לעומת 0.9% בקריאה הקודמת ולירידה של 0.1% בנטרול רכבים, לצד תביעות האבטלה השבועיות לאחר נתון קודם של 215 אלף, ומדד הפעילות של שלוחת הפד בפילדלפיה. אחרי שמדד המחירים לצרכן שפורסם ביום שלישי הפתיע לטובה והגדיל את הציפיות להורדת ריבית, הנתונים של היום יספקו קריאת חוזק לצרכן האמריקאי ולשוק העבודה. נתונים יציבים יחזקו את תרחיש הנחיתה הרכה, בעוד חולשה חדה עלולה להעלות חשש מהאטה דווקא כשמחירי האנרגיה גבוהים.
* מניית יונייטדהלת' (UNH): ענקית ביטוח הבריאות פתחה את יום הדוחות עם רבעון חזק במיוחד, רווח מתואם של 6.38 דולר למניה מול צפי של 4.85 דולר, הכנסות של 112 מיליארד דולר והעלאת תחזית הרווח השנתית לטווח של 19.50 עד 20 דולר למניה. בתגובה נרשם זינוק של יותר מ-8% במסחר המוקדם, שמציב את המניה יותר מ-75% מעל השפל של סוף מרץ. הדוח מעניק פתיחה אופטימית לעונת הדוחות ורוח גבית למגזר הבריאות כולו.
* השבבים בין דוח חזק לאיום רגולטורי: טייוואן סמיקונדקטור (TSM) היכתה את התחזיות עם רווח של 4.31 דולר למניה מול צפי של 3.95 דולר, צפי הכנסות של כ-45.2 מיליארד דולר לרבעון הבא מעל ההערכות, והכרזה על השקעה נוספת של 100 מיליארד דולר באריזונה שמביאה את סך השקעתה בארה"ב ל-265 מיליארד דולר. מנגד, לפי Financial Times מחוקקים בוושינגטון קוראים לממשל לאסור שבבי זיכרון מתוצרת סין, התפתחות שמוסיפה אי-ודאות ליצרניות הזיכרון כמו מיקרון (MU) וסאנדיסק (SNDK) אחרי שבוע סוער בסקטור. למרות הדוח החזק, מניית טייוואן סמיקונדקטור יורדת כ-3.2% במסחר המוקדם, ויצרניות הזיכרון ווסטרן דיגיטל (WDC) וסיגייט (STX) נחלשות כ-3.9% וכ-3.3% בהתאמה, איתות שהמשקיעים ממקדים את הדאגה בסיכון הרגולטורי ובמחירי הזיכרון.
* איתותי פיוס מול איראן והנפט נשאר גבוה: הנשיא טראמפ מסר כי קיבל פנייה מטהרן המבקשת להיפגש ולהגיע להסדר, ואיראן שחררה אזרח אמריקאי במחווה של רצון טוב. למרות זאת מחירי הנפט הוסיפו כ-1% והם נסחרים מעל 80 דולר לחבית, כאשר יבוא הגולמי של סין ירד ביוני כ-41% בהשוואה שנתית לרמה הנמוכה בעשור, עדות לעומק זעזוע ההיצע שיצרה המלחמה. עבור המשקיעים, אנרגיה יקרה נשארת תעלת ההזנה המרכזית של האינפלציה, גם אם ההסלמה הצבאית תתקרר.
* שורה תחתונה: את כיוון המסחר היום יכתיבו נתוני המאקרו של 15:30 שעון ישראל, המכירות הקמעונאיות ליוני עם צפי לעלייה של 0.2%, תביעות האבטלה השבועיות ומדד הפד של פילדלפיה, קריאת חוזק ראשונה לצרכן אחרי ההקלה באינפלציה. עונת הדוחות החזקה מעניקה לשוק עוגן חיובי, אבל מחירי הנפט מעל 80 דולר לחבית שומרים את סיכון האינפלציה על השולחן, כך שנתון צרכני חם מדי עלול דווקא להחיות את חששות הריבית.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-16. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Thu Jul 16 15:59:34 +0000 2026]: Retail is cashing-in tech profits: Retail investors sold -$125 million in SanDisk, $SNDK, stock last week, the largest sale among any stock. This was followed by Apple, $AAPL, at -$120 million, and Tesla, $TSLA, at -$105 million. Furthermore, retail investors sold -$65 million in Nvidia, $NVDA, -$40 million in American Airlines, $AAL, and -$22 million in Meta, $META. This brings 2-week retail sales volume in $TSLA and $AAPL up to -$200 million. Meanwhile, the total retail turnover in single stocks rose to a record $370 billion, up from $220 billion at the start of 2026. Retail investors are locking in gains following a historic tech rally.

@StockMKTNewz [Thu Jul 16 14:47:46 +0000 2026]: Here's Taiwan Semiconductor's $TSM revenue by platform 66% - HPC 22% - Smartphone 5% - IOT 4% - Automotive 2% - Others 1% - DCE Credit to my partners at @LeverageShares for the graphic https://t.co/1fvGKzOd76

@AIStockSavvy [Thu Jul 16 16:09:50 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Intel and Google Cloud are partnering to accelerate Intel's enterprise AI transformation. - $INTC $GOOGL

@StockMKTNewz [Thu Jul 16 15:08:32 +0000 2026]: ~185M SpaceX $SPCX shares are now sold short, representing ~29% of the company’s publicly tradable float and ~$25B in bearish wagers - S3 Partners via CNBC https://t.co/FDFIYJu6gi

@StockMKTNewz [Thu Jul 16 16:09:18 +0000 2026]: Intel $INTC and Google Cloud $GOOGL today announced an expansion of their previously disclosed multi-year strategic collaboration, which would "accelerate Intel’s enterprise-wide digital evolution through the deployment of Gemini Enterprise and Google Cloud." https://t.co/CHRxc3lNjj

@StockMKTNewz [Thu Jul 16 15:32:00 +0000 2026]: Sharkninja $SN just released the new Ninja Crispi Microwave a new Microwave/Airfryer combo that is "built to crisp as well as it heats" https://t.co/B7MGOOAjpa

@wallstengine [Thu Jul 16 14:59:15 +0000 2026]: UNITED AIRLINES $UAL EXPECTS FIRST BOEING 737 MAX 10 DELIVERY IN MID-TO-LATE 2027

@AIStockSavvy [Thu Jul 16 15:57:13 +0000 2026]: Rocket Lab, AST SpaceMobile, and Intuitive Machines have all moved lower on a YTD performance basis. $RKLB $ASTS $LUNR https://t.co/D62rLHQhrP

@KobeissiLetter [Thu Jul 16 16:24:33 +0000 2026]: BREAKING: The average interest rate on a US 30-year fixed mortgage rises to 6.55%, the highest since August 2025. As the Iran War continues, interest rates are hitting new one-year highs.

@StockMKTNewz [Thu Jul 16 15:49:36 +0000 2026]: What is the #1 worst performing stock in your portfolio so far today?

@wallstengine [Thu Jul 16 15:18:53 +0000 2026]: 👀

@wallstengine [Thu Jul 16 14:52:09 +0000 2026]: TSMC Q2 REVENUE MIX HPC accounts for 66% of revenue, up 20% QoQ Smartphones: 22%, -4% QoQ IoT: 5%, +4% QoQ Automotive: 4%, +15% QoQ Other: 2%, +5% QoQ DCE: 1%, +5% QoQ https://t.co/7AyS2fNwYC

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.