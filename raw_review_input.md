אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות בלבד, והחזר JSON בלבד.

You are writing a SHORT INTRADAY UPDATE in Hebrew for a financial website. The update is a
plain-language SUMMARY of what the curated X (Twitter) sources posted in the last two hours —
19:18–21:18 שעון ישראל, on 2026-11-16 (יום שני) — and nothing else.
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
- SINGLE-SOURCE ATTRIBUTION: a story appearing in only ONE source post with no outlet attribution is written with a hedge: "לפי דיווחים" — never as an established fact.
- Dates in visible text: Israeli format ONLY, e.g. "יום שני, 6.7.2026". NEVER write an ISO date (2026-07-06) inside the title or the bullets.
- NEVER use the ";" character anywhere. Use a comma or start a new sentence instead.
- NEVER use an em dash / double hyphen ("—" or "--") as a clause separator. Use a comma, a colon, or start a new sentence instead.
- Never OPEN a bullet with a raw ticker like "$TSLA:" or "$AMZN:". Open with the Hebrew company name: "מניית טסלה (TSLA):", "מניית אמזון (AMZN):", "מניית מטא (META):".
- NATURAL HEBREW: the update must read as if a person wrote it — modern, standard Hebrew (עברית תקנית), flowing and clear, professional but plain. NO translated-English phrasing (תרגומית), no literal English idioms, correct gender and number agreement. A sentence that would sound odd spoken aloud gets rewritten in simpler Hebrew.
- Never mention in the review that the items came from tweets/posts/X accounts.

══ PRE-OUTPUT SELF-VERIFICATION (MANDATORY — do this BEFORE returning the JSON) ══
Go over every bullet you wrote and check, one by one:
1. NUMBERS: every percentage, price and figure traces to a specific source post.
   Any number you cannot point to a source line for — DELETE it or the whole claim.
2. SCOPE: no story, price, index level or data point appears that is absent from the source posts.
3. DIRECTIONS: every directional claim (עלה/ירד/זינק/צנח) is stated by a source post — you did not determine
   any direction or magnitude yourself.
4. ATTRIBUTION: a story a source reports citing a news outlet keeps "לפי <outlet>". A story appearing in only
   ONE source post with no outlet attribution carries "לפי דיווחים" — never stated as an established fact.
5. FORMAT: no ";", no em dash, no ISO dates, no raw-ticker bullet openings, and the bullet count fits the
   instructions above (one bullet per material topic, no minimum and no cap).
6. SUMMARY ARRAY: one item per bullet, same order, same headlines, distilled (not copied) sentences, and every
   number/direction in the summary passes checks 1-4 as well.
7. LANGUAGE: every sentence reads like natural, standard Hebrew written by a person — no translated-English
   phrasing, correct gender/number agreement, professional but plain. A machine-sounding sentence gets rewritten.
If ANY check fails — fix the bullet and re-run the checks. Only then return the JSON.
══════════════════════════════════════════════════════════════════════════════

CRITICAL — OUTPUT FORMAT (MANDATORY):
- Return ONLY a JSON object, no backticks, no explanations, in EXACTLY this structure:
{
  "title": "עדכון ביניים מוול סטריט 🇺🇸 – יום שני, 16.11.2026, 21:18",
  "date": "2026-11-16",
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
tweets, for the window 19:18–21:18 Israel time on 2026-11-16. Do NOT use it to find additional news, headlines,
prices or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════

══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══
Already published on the site. Your update covers ONLY the last two hours. Mention an item below ONLY if there is a genuinely NEW development about it inside the two-hour window.

[עדכון ביניים]
* מניית אורקל (ORCL) תחת לחץ: מניית אורקל יורדת בכ-5% בעקבות דיווח של Bloomberg שלפיו מיקרוסופט (MSFT) מצמצמת את הסכם השכרת קיבולת המחשוב לבינה מלאכותית. לפי הדיווח, מיקרוסופט החליטה שלא לחדש חוזים משנת 2023 שכללו שרתים עם מעבדים מדורות קודמים של אנבידיה (NVDA), שאינם עומדים עוד בדרישותיה.
* המשקיעים הפרטיים ממשיכים לרכוש: לפי דיווחים, משקיעים פרטיים בארה״ב רכשו מניות במשך 22 ימי מסחר רצופים עד 3 בנובמבר, הרצף השלישי באורכו מאז תקופת מניות המם בשנת 2021. היקף הרכישות בתקופה הסתכם בכ-33 מיליארד דולר, מהגבוהים שנרשמו מאז 2017.
* שיא בגיוסים לקרנות ממונפות: לפי דיווחים, קרנות סל ממונפות בארה״ב רשמו גיוסים של 9.5 מיליארד דולר בשבוע שהסתיים ב-16 באוקטובר, שיא שבועי בנתונים מאז 2006. מדובר ביותר מכפליים מהשיא השבועי הקודם, שעמד על 4.5 מיליארד דולר בשנת 2024.
* בייטדאנס בוחנת הרחבת תשתיות: לפי Bloomberg, בייטדאנס בוחנת הרחבה משמעותית של פעילות מרכזי הנתונים שלה בברזיל, מעבר לפרויקט קיים בהיקף של 10 מיליארד דולר ובהספק של 300 מגה-ואט. החברה מחפשת יזמים לשלב נוסף בפרויקט במדינת סיארה ובוחנת הקמת תשתיות נוספות לשוק המקומי.
* OpenAI מנהלת שיחות לגיוס הון: לפי CNBC, סמנכ״לית הכספים של OpenAI אישרה שהחברה מקיימת שיחות לגיוס הון חדש. השווי המשתמע מהשיחות גבוה בכ-50% מהשווי בסבב המימון שהושלם במרץ, אך לא דווח על השלמת עסקה.
* מניית טראוולף (WULF) במוקד: בנק ההשקעות Northland הותיר את המלצת תשואת היתר למניית טראוולף, אך הפחית את מחיר היעד מ-30 ל-22.50 דולר. האנליסטים ממשיכים לראות בחברה הזדמנות בתחום תשתיות הבינה המלאכותית, על רקע יכולות הביצוע של הנהלתה.
* מניית קראטוס (KTOS) במוקד: בנק ההשקעות Canaccord הותיר המלצת קנייה למניית קראטוס, אך הפחית את מחיר היעד מ-135 ל-120 דולר. האנליסטים ציינו צמיחה חזקה בפעילות הביטחונית לצד חולשה בתחום המערכות הבלתי מאוישות ותזרים מזומנים חופשי שלילי.
* מניית סאנראן (RUN) במוקד: מיזוהו הותירה המלצת תשואת יתר למניית סאנראן עם מחיר יעד של 15 דולר. האנליסטים צופים שיפור ביצירת הערך מחוזים בשנים 2027 ו-2028, בתמיכת שילוב מערכות אגירת אנרגיה, למרות הפחתת התחזית לשנת 2026.
* פיתוח חדש ביישומי בינה מלאכותית: לפי דיווחים, Muse הציגה את Spaces, יכולת המאפשרת למשתמשים ליצור יישומים מותאמים אישית באמצעות תיאור מילולי. השירות כולל בניית כלים לתכנון יומי, לפרודוקטיביות ולמשימות יצירתיות, עם אפשרות להתאים את העיצוב והתכונות.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-11-16. Never mention in the review that these came from tweets/posts:

@StockMKTNewz [Mon Nov 16 17:39:49 +0000 2026]: Nvidia's $NVDA board of directors is reportedly NOT CONSIDERING bringing Jensen Huang back as CEO - CNBC https://t.co/JxAIR2uCJH

@StockMKTNewz [Mon Nov 16 17:45:57 +0000 2026]: OpenAI CEO Sam Altman was just asked if he thinks Jensen Huang should be reinstated as CEO of Nvidia $NVDA https://t.co/Y5M9kMIDYp

@KobeissiLetter [Mon Nov 16 17:40:24 +0000 2026]: BREAKING: Nvidia’s board, $NVDA, is not considering bringing Jensen Huang back as CEO, CNBC reports. Nvidia’s stock falls to a new low of the day on the news, now down -34% from its October 6th high.

@StockMKTNewz [Mon Nov 16 17:31:48 +0000 2026]: The NASDAQ 100 $QQQ is now down by more than 2% so far today 🔴🔴 https://t.co/UAfqcvdZ2f

@KobeissiLetter [Mon Nov 16 18:08:48 +0000 2026]: BREAKING: The Nasdaq 100 extends losses to -2.3% on the day amid reports that Nvidia’s board is not considering reinstating Jensen Huang as CEO. https://t.co/CqxnKFopgR

@AIStockSavvy [Mon Nov 16 17:22:43 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: OpenAI founder Altman: It is hard to imagine the AI revolution without former $NVDA NVIDIA CEO Jensen Huang involved.

@KobeissiLetter [Mon Nov 16 17:27:20 +0000 2026]: BREAKING: Student loan serious delinquencies increased +0.3 percentage points in Q3 2026, to 10.9%, the highest percentage since Q4 2019. This marks the 4th consecutive quarterly increase, with a cumulative gain of +1.5 percentage points. Auto loan 90+ day serious delinquencies rose +0.2 percentage points, to 5.7%, their highest level on record. By comparison, the post-2008 Financial Crisis peak …

@StockMKTNewz [Mon Nov 16 18:21:57 +0000 2026]: Brad Gerstner is reportedly looking to put $5 Billion into the Anthropic $ANT IPO

@AIStockSavvy [Mon Nov 16 19:00:21 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $AMD AMD-Powered Lux Supercomputer Opens to Scientific Users at Oak Ridge, Becoming First AI Factory for DOE’s Genesis Mission https://t.co/wQ8zHPtXdy

@AIStockSavvy [Mon Nov 16 18:37:24 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: U.S. Deputy Secretary of State Helberg said Washington has no intention of targeting suppliers such as Ericsson, $ASML, Samsung or $SKHY SK Hynix (SKHY.O), or excluding them from U.S. supply chains.

@AIStockSavvy [Mon Nov 16 18:13:51 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Altimeter's Brad Gerstner Investing $5 Billion In $ANT Anthropic IPO - CNBC

@AIStockSavvy [Mon Nov 16 18:00:44 +0000 2026]: ⚡ 𝗨𝗣𝗗𝗔𝗧𝗘: Noeri Launches with $110 million for Self-Improving Enterprise AI - $NVDA $SNOW $CSCO https://t.co/0ZCmjKe1Y4

@gurgavin [Mon Nov 16 18:20:09 +0000 2026]: JUST IN : MAJOR OUTAGES REPORTED AT BANK OF AMERICA, WELLS FARGO , CHASE , US BANK AND OTHER AMERICAN BANKS 🇺🇸🇺🇸🇺🇸

@StockMKTNewz [Mon Nov 16 17:23:23 +0000 2026]: OpenAI CEO Sam Altman just said the AI revolution without Jensen Huang is "Hard to Imagine" https://t.co/cIDsFcuEKt

@wallstengine [Mon Nov 16 18:08:59 +0000 2026]: Brad Gerstner's Altimeter Capital plans to invest $5 billion in Anthropic's IPO, five times more than Gerstner has ever committed to an IPO, he told CNBC. "I think this is a cornerstone compounder for a long time," Gerstner said. https://t.co/ZewOIrbwm1

@wallstengine [Mon Nov 16 17:42:33 +0000 2026]: NVIDIA BOARD NOT CONSIDERING REINSTATING JENSEN HUANG AS CEO, SOURCE TELLS CNBC https://t.co/6npehBBJNw

@StockMKTNewz [Mon Nov 16 18:41:35 +0000 2026]: WHAT IS HAPPENING RIGHT NOW???? A bunch of banks are reporting some downtime issues right now - DownDetector https://t.co/8HyDRK4nF2

@wallstengine [Mon Nov 16 18:34:59 +0000 2026]: OUTAGES HIT MULTIPLE MAJOR U.S. BANKS JPMorgan Chase, Bank of America, Wells Fargo and U.S. Bank are seeing sharp spikes in outage reports, with thousands of customers reporting trouble accessing accounts and logging into online banking. https://t.co/ZA4qpIR9h2

@wallstengine [Mon Nov 16 18:38:10 +0000 2026]: First Microsoft Outlook Then airports Now major U.S. banks It's been one major outage after another lately

@wallstengine [Mon Nov 16 17:33:05 +0000 2026]: OpenAI CEO Sam Altman says it's "hard to imagine the AI revolution without Jensen." "Jensen has long been a hero of mine. Heroes have flaws." "I think the industry will be fine." https://t.co/Ia6dBYS8ic

@StockMKTNewz [Mon Nov 16 17:54:08 +0000 2026]: OpenAI CEO Sam Altman was just asked about how he and his company are dealing with spys trying to get close to the company and its employees https://t.co/li4qNZFfz2

@wallstengine [Mon Nov 16 18:00:00 +0000 2026]: OpenAI CEO Sam Altman on potential double-counting in AI chip demand: Many AI chipmakers are assuming OpenAI, Anthropic and other major buyers will purchase most of their output. "We're not all gonna be able to or need to buy ... all of our supply from every chip vendor." https://t.co/mjGJV5I6bK

@StockMKTNewz [Mon Nov 16 19:00:34 +0000 2026]: LIVE STREAM HAPPENING RIGHT NOW If you are a trader you should check out what our sponsors over at @MenthorQpro are doing If you find it interesting there is a link below the live stream to check out the product As I put in my last post ... "MenthorQ turns the options and volatility models used by hedge funds and market makers into simple charts and levels for everyday traders."

@StockMKTNewz [Mon Nov 16 18:55:46 +0000 2026]: There is so much more happening under the hood in the options market than price action shows Our sponsors over at MenthorQ help you find that info and make it understandable MenthorQ turns the options and volatility models used by hedge funds and market makers into simple charts and levels for everyday traders.

@AIStockSavvy [Mon Nov 16 19:13:27 +0000 2026]: Tiger Global Management portfolio - Q3 2026 https://t.co/IdNtWYOYyn

@StockMKTNewz [Mon Nov 16 18:09:24 +0000 2026]: RT @WOLF_Financial: Charting Disruption 2027 with Global X https://t.co/Qd1hYnZzBC

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.