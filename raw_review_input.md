אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות בלבד, והחזר JSON בלבד.

You are writing a SHORT INTRADAY UPDATE in Hebrew for a financial website. The update is a
plain-language SUMMARY of what the curated X (Twitter) sources posted in the last two hours —
18:55–20:55 שעון ישראל, on 2026-11-25 (יום רביעי) — and nothing else.
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
  "title": "עדכון ביניים מוול סטריט 🇺🇸 – יום רביעי, 25.11.2026, 20:55",
  "date": "2026-11-25",
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
tweets, for the window 18:55–20:55 Israel time on 2026-11-25. Do NOT use it to find additional news, headlines,
prices or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════

══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══
Already published on the site. Your update covers ONLY the last two hours. Mention an item below ONLY if there is a genuinely NEW development about it inside the two-hour window.

[עדכון ביניים]
* אינפלציה בארה״ב: בשעה 15:30 פורסם כי מדד ה-PCE באוקטובר עלה בקצב שנתי של 3.8% ובקצב חודשי של 0.3%. מדד הליבה עלה ל-3.3% לעומת תחזית של 3.2% ונתון קודם של 3.1%.
* צמיחה בארה״ב: קצב הצמיחה השנתי ברבעון השלישי עודכן מ-3.4% ל-4.3%, הקצב המהיר ביותר זה כמעט שלוש שנים. לפי דיווחים, ההוצאה הצרכנית עלתה ב-0.3% לעומת תחזית של 0.4%.
* שוק העבודה: מספר הבקשות הראשוניות לדמי אבטלה ירד ל-189 אלף, לעומת תחזית של 200 אלף. מספר הבקשות המתמשכות הסתכם ב-1.697 מיליון, מתחת לתחזית של 1.721 מיליון.
* ריבית הפד: לפי דיווחים, ההסתברות שהשוק מייחס להעלאת ריבית בדצמבר עלתה מעל 97% בעקבות פרסום נתוני האינפלציה. במקביל, לפי דיווחים, קווין האסט מהבית הלבן ציין כי החלטות הפד צפויות להתבסס על הנתונים הכלכליים.
* מכסים: הממשל האמריקאי הציע מכסים חדשים על 14 שותפות סחר, ובהן סין, הודו, יפן ומדינות האיחוד האירופי. לפי דיווחים, האיחוד האירופי דרש מארה״ב לכבד את תקרת המכסים המוסכמת של 15%, לאחר שהוצעו מכסים של עד 20% על מוצרים אירופיים.
* נאסד״ק 100: לפי דיווחים, המדד העמיק את הירידות ליותר מ-4.5% בעקבות נתוני האינפלציה והודעת המכסים. לפי Bloomberg, המדד איבד 20% משיאו ומתקרב לכניסה לשוק דובי.
* סנטימנט המשקיעים: מדד הפחד והחמדנות של CNN ירד ל-9 מתוך 100, רמת פחד קיצוני והנתון הנמוך ביותר מאז מרץ.
* מניות הבינה המלאכותית: בראיון ל-Bloomberg אמר אסטרטג גולדמן זאקס, כריסטיאן מילר-גליסמן, כי השוק נמצא במצב שברירי וכי מוקדם לנצל את הירידות בענף. לדבריו, המשקיעים צריכים לראות רווחים ממשיים כתוצאה מההשקעות בבינה מלאכותית.
* אנבידיה (NVDA): לפי דיווחים, נציג הסחר האמריקאי ג'יימיסון גריר הדגיש את חשיבותה האסטרטגית של אנבידיה ואת הצורך להבטיח שתשמור על מעמדה המוביל.
* סטארבקס (SBUX): לפי Bloomberg, החברה שכרה יועצים לקראת מכירה אפשרית של פעילותה ביפן תמורת מספר מיליארדי דולרים.
* קורוויב (CRWV) וקראודסטרייק (CRWD): לפי דיווחים, החברות הרחיבו את שיתוף הפעולה ביניהן, הכולל איתור איומי סייבר מסביב לשעון בתשתיות קורוויב ושימוש בכוח המחשוב שלה לאימון ולהפעלת מודלים של קראודסטרייק.
* אבטחת מידע: לפי דיווחים, הרשת האמריקאית לאכיפת פשיעה פיננסית (FinCEN) נפגעה ממתקפת סייבר שבמסגרתה התאפשרה גישה בלתי מורשית לחלק ממערכותיה.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-11-25. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Wed Nov 25 17:38:07 +0000 2026]: BREAKING: Anthropic stock, $ANT, erases losses and turns positive on the day. The stock is now trading above its $83/share IPO price. https://t.co/MOgY0OcZVr

@KobeissiLetter [Wed Nov 25 17:30:01 +0000 2026]: Retail demand for Anthropic is accelerating: Retail investors bought +$100 million in Anthropic, $ANT, shares on Monday, marking a 2nd consecutive daily increase in purchases. As a result, $ANT was the 2nd-most purchased stock among retail investors during that session. That compares to +$60 million on Thursday, Anthropic's IPO day, the 3rd-largest retail purchase on the first trading day of any …

@StockMKTNewz [Wed Nov 25 18:46:50 +0000 2026]: S&P PUTS NVIDIA $NVDA 'AA' CREDIT RATINGS ON NEGATIVE WATCH - A credit rating is S&P's grade on how likely a company is to pay back its debt, and AA is one of the highest you can get. Negative watch means S&P is looking at lowering it and will usually decide within about 90 days. It isn't a downgrade yet, it can still end up unchanged, and it doesn't mean Nvidia is struggling to pay its bills.

@AIStockSavvy [Wed Nov 25 17:42:59 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Nvidia Sellers Seek New Buyers as US Curbs China AI Chip Access - CNBC - $NVDA

@KobeissiLetter [Wed Nov 25 17:55:44 +0000 2026]: BREAKING: The Dow Jones Industrial Average erases all losses and turns green on the day. https://t.co/HYCmFEAtTW

@KobeissiLetter [Wed Nov 25 17:16:16 +0000 2026]: BREAKING: President Trump says the US stock market is “down sharply” because he wasn’t on the ballot for the US Midterm Elections. https://t.co/DIJQSV7sJQ

@AIStockSavvy [Wed Nov 25 17:27:02 +0000 2026]: 📢 𝗝𝗨𝗦𝗧 𝗜𝗡: CoreWeave’s lenders will sell $4.5 bln of loans tied to Meta Platforms next week - $CRWV $META

@wallstengine [Wed Nov 25 17:01:28 +0000 2026]: ANTHROPIC'S IPO HAS CREATED ABOUT 5,100 NEW MILLIONAIRES AMONG ITS EMPLOYEES

@StockMKTNewz [Wed Nov 25 17:27:58 +0000 2026]: Michael Burry said this today: “Globally, my portfolio is more long, and less short, than it has been in some time” “In fact, when I say less short, right now apart from Palantir puts and MetLife puts, I am temporarily almost entirely long. Temporarily, because I am continuing to assess short opportunities.”

@AIStockSavvy [Wed Nov 25 17:10:36 +0000 2026]: Recovering.. 👀👀 https://t.co/5gwkIo5wUF

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.