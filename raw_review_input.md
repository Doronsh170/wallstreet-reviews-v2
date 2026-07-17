אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are writing a SHORT INTRADAY UPDATE in Hebrew for a financial website. The update is a
plain-language SUMMARY of what the curated X (Twitter) sources posted in the last two hours —
19:44–21:44 שעון ישראל, on 2026-07-17 (יום שישי) — and nothing else.
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
  "title": "עדכון ביניים מוול סטריט 🇺🇸 – יום שישי, 17.7.2026, 21:44",
  "date": "2026-07-17",
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
tweets, for the window 19:44–21:44 Israel time on 2026-07-17. Do NOT use it to find additional news, headlines,
prices or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════

══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══
Already published on the site. Your update covers ONLY the last two hours. Mention an item below ONLY if there is a genuinely NEW development about it inside the two-hour window.

[נקודות מרכזיות]
* החוזים מאותתים על לחץ חד: חוזי Nasdaq 100 יורדים 2.05% וחוזי S&P 500 יורדים 1.03%, כך שהשוק צפוי להיפתח בירידות בהובלת הטכנולוגיה. מדד VIX עולה לרמה של 18.53, על רקע המשך המכירות במניות הזיכרון והלילה השישי ברציפות של תקיפות אמריקאיות באיראן. השילוב בין ירידה במניות ה־AI לסיכון גיאופוליטי מגדיל את הביקוש להגנות ומקשה על התאוששות מהירה בפתיחה.
* נתוני המאקרו במוקד: ב־15:30 שעון ישראל צפויות התחלות הבנייה לעלות לקצב שנתי של 1.33 מיליון לעומת 1.177 מיליון, והיתרי הבנייה צפויים לעמוד על 1.40 מיליון לעומת 1.413 מיליון. ב־17:00 צפוי הייצור התעשייתי לעלות 0.2% לאחר 0.1%, ומדד אמון הצרכנים של אוניברסיטת מישיגן צפוי לעלות ל־51.0 לעומת 49.5. נתונים חזקים מהצפי עשויים לחזק את ציפיות הריבית ולהכביד במיוחד על מניות צמיחה בעלות מכפילים גבוהים.
* סין מאבדת תנופה: כלכלת סין צמחה ברבעון השני ב־4.3% בלבד לעומת 5.0% ברבעון הראשון, מתחת לטווח היעד הממשלתי של 4.5% עד 5.0%. ההשקעות בנכסים קבועים ירדו 5.7% במחצית הראשונה וההשקעות בנדל״ן צנחו 18%, בעוד המכירות הקמעונאיות עלו ביוני רק 1.0%. ההאטה בכלכלה השנייה בגודלה בעולם עלולה לפגוע בביקוש לחומרי גלם, למוצרים תעשייתיים ולחברות אמריקאיות החשופות לצרכן הסיני.
* מניית אפל (AAPL): HSBC העלה את ההמלצה למניית אפל לקנייה מהחזקה והעלה את מחיר היעד ל־366 דולר מ־260 דולר. הבנק מעריך שבסיס של 2.5 מיליארד מכשירים, שדרוג Siri והשקת מוצרים חדשים עשויים ליצור מחזור החלפה, תוך השקעות הון של 2.5% בלבד מהמכירות הצפויות ב־2026. תחזית הרווח למניה ל־2027 הועלתה בכ־8% ל־10.26 דולר, רמה הגבוהה ב־7.5% מהקונצנזוס.
* מניית 3M (MMM): ג׳יי.פי מורגן העלה את ההמלצה למניית 3M למשקל יתר מניטרלי ואת מחיר היעד ל־180 דולר מ־178 דולר. הבנק מצביע על צמיחה אורגנית של יותר מ־3%, לצד ביקוש ממרכזי נתונים ומשבבים שמקזז חולשה באלקטרוניקה צרכנית וברכב. שיפור בתמחור והפחתת עלויות עשויים להוסיף כ־0.10 דולר לרווח השנתי למניה מהרבעון הרביעי ועד 2027.
* שורה תחתונה: כיוון המסחר ייקבע לפי השאלה אם הירידה של 2.05% בחוזי Nasdaq 100 תתמתן לאחר פרסום נתוני המאקרו. כל עוד ה־VIX ברמה של 18.53 והלחץ על מניות הזיכרון נמשך לצד המלחמה באיראן, הסיכון לפתיחה תנודתית נשאר גבוה.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-17. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Fri Jul 17 16:46:29 +0000 2026]: BREAKING: The Trump Administration has notified Israel that it is sending "dozens more" refueling planes to the country ahead of a potential "massive offensive" in Iran, per Axios. Details include: 1. President Trump is reportedly considering a "massive offensive" in Iran 2. Among the options being considered are bombing Iranian infrastructure facilities like power plants and nuclear sites 3. President Trump could order the escalation "in the coming days" Brent oil prices surge toward $88/barrel on the news.

@wallstengine [Fri Jul 17 17:27:43 +0000 2026]: JUDGE WILL NOT BLOCK $META LAYOFFS IN AI DISCRIMINATION CASE

@wallstengine [Fri Jul 17 16:54:45 +0000 2026]: APPLE $AAPL IN EARLY SETTLEMENT TALKS WITH US DOJ OVER ANTITRUST SUIT

@KobeissiLetter [Fri Jul 17 17:50:25 +0000 2026]: It's official: US oil prices are now up over +20% in 15 days as the Iran War has resumed. In another sudden turn of events, Brent oil prices are on the verge of rising back above $90/barrel. https://t.co/wtuupOLHQN

@StockMKTNewz [Fri Jul 17 18:30:23 +0000 2026]: Michael Burry has covered his short position in Oracle $ORCL and is no longer short https://t.co/o60vZfTX7O

@wallstengine [Fri Jul 17 17:23:54 +0000 2026]: FAA TO ANNOUNCE IT WILL ALLOW BOEING TO RESUME TICKETING FOR ALL 737 MAX, 787 AIRPLANES - REUTERS CITING AN EMAIL TO CONGRESS

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.