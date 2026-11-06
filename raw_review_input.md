אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות בלבד, והחזר JSON בלבד.

You are writing a SHORT INTRADAY UPDATE in Hebrew for a financial website. The update is a
plain-language SUMMARY of what the curated X (Twitter) sources posted in the last two hours —
18:29–20:29 שעון ישראל, on 2026-11-06 (יום שישי) — and nothing else.
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
  "title": "עדכון ביניים מוול סטריט 🇺🇸 – יום שישי, 6.11.2026, 20:29",
  "date": "2026-11-06",
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
tweets, for the window 18:29–20:29 Israel time on 2026-11-06. Do NOT use it to find additional news, headlines,
prices or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════

══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══
Already published on the site. Your update covers ONLY the last two hours. Mention an item below ONLY if there is a genuinely NEW development about it inside the two-hour window.

[עדכון ביניים]
* ירידות חדות בוול סטריט: לפי דיווחים, מדד S&P 500 מחק במהלך המסחר כ-3 טריליון דולר משווי החברות הכלולות בו. מדובר באומדן במהלך המסחר ולא בנתון נעילה.
* קרן הגידור Walleye מחזירה הון: לפי Bloomberg, קרן Walleye מתכננת להחזיר למשקיעים חלק מההון המנוהל, על פי מכתב ללקוחות. לא דווח על הנזלה כפויה.
* מניות הטכנולוגיה בשוק דובי: לפי דיווחים, סנדיסק (SNDK) איבדה 66% מהשיא, מארוול (MRVL) איבדה 59%, אורקל (ORCL) איבדה 56% וסרוויסנאו (NOW) איבדה 57%. אלה ירידות מהשיא ולא שינויים יומיים.
* אנתרופיק חושפת התחייבויות ענק: לפי דיווחים, התחייבויות עתידיות לתשתיות בינה מלאכותית מסתכמות ב-895 מיליארד דולר, מהם כ-448 מיליארד דולר עד סוף 2030 וכ-70 מיליארד דולר ב-12 החודשים הקרובים. התחייבויות לברודקום (AVGO) מסתכמות בכ-161 מיליארד דולר.
* מיקרוסופט מוותרת על הרחבת תשתיות: לפי Bloomberg, מיקרוסופט (MSFT) ויתרה על אפשרות להוספת מאות מגה-ואט של קיבולת במיזם Nscale בטקסס, בשל עיכוב באישור חיבור לרשת החשמל.
* גוגל מרחיבה השקעות בבינה מלאכותית: לפי דיווחים, אלפבית (GOOGL) מתכננת השקעה של 17 מיליארד דולר במרכז נתונים ראשון בוויומינג. במקביל דווח על השקת Gemini Omni 1.2 Flash עם יצירה ועריכת סרטונים באורך של עד 15 שניות.
* איראן בוחנת הצעות גרעין: לפי NYT, איראן בוחנת הצעות קונקרטיות בנוגע לתוכנית הגרעין שלה. אין בדיווח אישור להשגת הסכם.
* מנכ״ל ARM מתייחס למימושים: מנכ״ל ARM (ARM), רנה האס, טען כי הירידות במניות הטכנולוגיה משקפות חשיבה קצרת טווח ביחס להשפעה הכלכלית העתידית של הבינה המלאכותית.
* התפתחויות בתחום אבטחת הסייבר: לפי דיווחים, OpenAI הציגה את GPT-6 Cyber, מודל המתמחה בזיהוי חולשות תוכנה ובפיתוח תיקוני אבטחה. ביצועיו המדווחים לא אומתו עצמאית.
* ג׳יי.פי מורגן תחת בחינה אפשרית: לפי CNBC, מחוקקים דמוקרטים נערכים לבחון את קשרי ג׳יי.פי מורגן (JPM) עם ג׳פרי אפשטיין. מדובר בהיערכות לבחינה ולא בממצאי חקירה.
* עדכוני אנליסטים: ברנשטיין הותירה המלצת תשואת יתר לריוט פלטפורמס (RIOT) והעלתה יעד מ-18 ל-30 דולר. BTIG הותירה המלצת קנייה ליוניטי (U) והעלתה יעד מ-53 ל-60 דולר.
* ג׳נרל מילס בוחנת מכירת פעילות: לפי WSJ, ג׳נרל מילס שוקלת למכור את פעילות האגן דאז הבינלאומית. התכנון נמצא בשלב מוקדם ולא דווח על הסכם מחייב.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-11-06. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Fri Nov 06 17:43:18 +0000 2026]: BREAKING: Oracle stock, $ORCL, falls -5% after Microsoft ends its deal to rent AI cloud capacity from the company. Oracle is now down -68% from its record high. https://t.co/SshVPMuGH5

@StockMKTNewz [Fri Nov 06 17:40:45 +0000 2026]: MICROSOFT $MSFT IS REPORTEDLY WINDING DOWN ITS DEAL TO RENT AI CLOUD CAPACITY FROM ORACLE $ORCL https://t.co/rA6ZTZeufc

@AIStockSavvy [Fri Nov 06 17:58:47 +0000 2026]: ⚡ 𝐔𝐏𝐃𝐀𝐓𝐄: Microsoft Winds Down Oracle AI Computing Deal Amid $80 Billion Cloud Strategy Review — Bloomberg - $MSFT $ORCL $NVDA 👉 𝗞𝗲𝘆 𝗛𝗶𝗴𝗵𝗹𝗶𝗴𝗵𝘁𝘀: ➤ 𝗠𝗶𝗰𝗿𝗼𝘀𝗼𝗳𝘁 is winding down its 𝗢𝗿𝗮𝗰𝗹𝗲 AI computing arrangement. ➤ Microsoft declined to renew contracts involving older-generation 𝗡𝗩𝗜𝗗𝗜𝗔 𝗚𝗣𝗨𝘀. ➤ Oracle's rented computing capacity reportedly no longer met 𝗠𝗶𝗰𝗿𝗼𝘀𝗼𝗳𝘁'𝘀 specifications. ➤ Original 𝟮𝟬𝟮𝟯 …

@wallstengine [Fri Nov 06 17:54:38 +0000 2026]: $MSFT WINDS DOWN AI CLOUD DEAL WITH $ORCL Microsoft has reportedly declined to renew its 2023 agreement to rent AI computing capacity from Oracle and has been gradually shutting down that capacity in recent months, Bloomberg reports. The deal was originally intended to power an AI-enhanced version of Bing. However, the Oracle servers used older-generation Nvidia GPUs that no longer met …

@AIStockSavvy [Fri Nov 06 18:19:38 +0000 2026]: $RUN | Mizuho 𝗿𝗲𝗶𝘁𝗲𝗿𝗮𝘁𝗲𝘀 𝗢𝘂𝘁𝗽𝗲𝗿𝗳𝗼𝗿𝗺 on 𝗦𝘂𝗻𝗿𝘂𝗻, maintains PT at $𝟭𝟱 Analyst sees stronger 2027–28 net contracted value creation offsetting a lower 2026 estimate, with battery attach supporting cash growth. https://t.co/NHmvJXRd4G

@AIStockSavvy [Fri Nov 06 18:01:08 +0000 2026]: I think that's potentially bullish for $NVDA and modern AI infrastructure providers, although it creates risks for $ORCL and companies relying on older hardware. Microsoft cutting AI spending, or preparing for the next massive GPU upgrade cycle?

@AIStockSavvy [Fri Nov 06 17:46:41 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Microsoft Is Winding Down Oracle Deal to Rent AI Cloud Capacity - Bloomberg - $MSFT $ORCL In Recent Months, Microsoft Has Been Turning off Rented Computing Capacity From Oracle After Declining to Renew the Contract

@AIStockSavvy [Fri Nov 06 18:09:51 +0000 2026]: 📢 𝗝𝗨𝗦𝗧 𝗜𝗡: $META Muse Introduces AI-Powered Spaces to Build Personalized Apps and Automate Daily Tasks 👉 𝗞𝗲𝘆 𝗛𝗶𝗴𝗵𝗹𝗶𝗴𝗵𝘁𝘀: ➤ 𝗠𝘂𝘀𝗲 introduces 𝗦𝗽𝗮𝗰𝗲𝘀, customizable interactive experiences within its app. ➤ Users can create 𝗽𝗲𝗿𝘀𝗼𝗻𝗮𝗹𝗶𝘇𝗲𝗱 𝘁𝗼𝗼𝗹𝘀 simply by describing their ideas. ➤ Spaces support 𝗱𝗮𝗶𝗹𝘆 𝗽𝗹𝗮𝗻𝗻𝗶𝗻𝗴, productivity, entertainment, and creative projects. ➤ Users can 𝗺𝗼𝗱𝗶𝗳𝘆 𝗱𝗲𝘀𝗶𝗴𝗻𝘀, features, and …

@AIStockSavvy [Fri Nov 06 17:03:31 +0000 2026]: $WULF | Northland 𝗺𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝘀 𝗢𝘂𝘁𝗽𝗲𝗿𝗳𝗼𝗿𝗺 on 𝗧𝗲𝗿𝗮𝗪𝘂𝗹𝗳 𝗜𝗻𝗰., cuts PT to $𝟮𝟮.𝟱𝟬 from $𝟯𝟬.𝟬𝟬 Analyst sees TeraWulf as a top AI infrastructure value proposition, backed by a management team capable of driving meaningful upside. https://t.co/Y2d3h20C1y

@AIStockSavvy [Fri Nov 06 16:50:56 +0000 2026]: 📢 𝗝𝗨𝗦𝗧 𝗜𝗡: ByteDance Eyes Massive Brazil Data Center Expansion Beyond $10 Billion Project - Bloomberg - $NVDA $AMD 👉 𝗞𝗲𝘆 𝗛𝗶𝗴𝗵𝗹𝗶𝗴𝗵𝘁𝘀: ➤ 𝗕𝘆𝘁𝗲𝗗𝗮𝗻𝗰𝗲 is considering a major 𝗔𝗜 𝗱𝗮𝘁𝗮 𝗰𝗲𝗻𝘁𝗲𝗿 expansion in Brazil. ➤ Proposed expansion would exceed the existing $𝟭𝟬 𝗯𝗶𝗹𝗹𝗶𝗼𝗻, 𝟯𝟬𝟬-𝗠𝗪 project. ➤ ByteDance is seeking developers for the 𝘀𝗲𝗰𝗼𝗻𝗱 𝗽𝗵𝗮𝘀𝗲 in Ceará. ➤ Company is exploring another 𝗱𝗼𝗺𝗲𝘀𝘁𝗶𝗰-𝗳𝗼𝗰𝘂𝘀𝗲𝗱 data …

@AIStockSavvy [Fri Nov 06 16:55:14 +0000 2026]: $WULF | Northland 𝗺𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝘀 𝗢𝘂𝘁𝗽𝗲𝗿𝗳𝗼𝗿𝗺 on 𝗧𝗲𝗿𝗮𝗪𝘂𝗹𝗳 𝗜𝗻𝗰., 𝗰𝘂𝘁𝘀 PT to $𝟮𝟮.𝟱 from $𝟯𝟬.𝟬 https://t.co/xXjlp2KaxA

@AIStockSavvy [Fri Nov 06 16:54:19 +0000 2026]: $KTOS | Canaccord 𝗺𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝘀 𝗕𝘂𝘆 on 𝗞𝗿𝗮𝘁𝗼𝘀 𝗗𝗲𝗳𝗲𝗻𝘀𝗲 &amp; 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 𝗦𝗼𝗹𝘂𝘁𝗶𝗼𝗻𝘀, cuts PT to $𝟭𝟮𝟬 from $𝟭𝟯𝟱 Analyst sees strong Q3/26 growth and EBITDA beats, led by elevated KGS demand, despite weaker Unmanned Systems and negative FCF. https://t.co/KUhxaWXLgI

@KobeissiLetter [Fri Nov 06 17:19:00 +0000 2026]: Investors took record leverage into this week's decline: US leveraged ETFs attracted +$9.5 billion in inflows in the week ending October 16th, their largest weekly intake on record in data going back to 2006. This is more than double the previous weekly record inflow of +$4.5 billion, set in 2024. By comparison, the largest weekly outflow was -$7.5 billion in late 2025. This comes as the 3x …

@KobeissiLetter [Fri Nov 06 18:22:00 +0000 2026]: Retail demand for stocks is incredibly strong: Retail investors purchased US equities in the 22 consecutive sessions ending November 3rd, the 3rd-longest streak since the memestock mania in 2021. This also ranks as their 6th-longest purchasing streak since 2017. Over this period, retail investors bought ~$33 billion in equities, their 5th-largest purchase since 2017. This equals an average of …

@AIStockSavvy [Fri Nov 06 16:45:26 +0000 2026]: OpenAI CFO confirmed the company is in fundraising talks, with the implied valuation roughly 50% higher than the financing round completed in March. - CNBC

@StockMKTNewz [Fri Nov 06 17:01:01 +0000 2026]: BRIAN FEROLDI JUST JOINED THE SHOW https://t.co/RCV1nLlWzI

@StockMKTNewz [Fri Nov 06 16:34:50 +0000 2026]: DAN NILES JUST JOINED THE STREAM

@StockMKTNewz [Fri Nov 06 17:20:02 +0000 2026]: RT @WOLF_Financial: BRIAN FEROLDI SAYS HE WAITS A YEAR AFTER AN IPO BEFORE BUYING: “When a company goes from private to public, all of a s…

@StockMKTNewz [Fri Nov 06 17:19:57 +0000 2026]: RT @WOLF_Financial: BRIAN FEROLDI SAYS ANTHROPIC’S FIRST EARNINGS REPORT WILL BE ITS “FIRST TRUE TEST” AS A PUBLIC COMPANY On IPOs in gene…

@StockMKTNewz [Fri Nov 06 17:45:31 +0000 2026]: RT @WOLF_Financial: “If making money was easy, everybody would be a millionaire... So if the game feels hard, that’s because it is and it’s…

@StockMKTNewz [Fri Nov 06 16:54:52 +0000 2026]: RT @WOLF_Financial: WHAT WOULD YOU ASK DAN IVES ABOUT THE ANTHROPIC IPO? @DivesTech is live with us right now. Partner and Senior Managing…

@StockMKTNewz [Fri Nov 06 16:54:41 +0000 2026]: RT @WOLF_Financial: DAN NILES SAYS MOST INVESTORS GET "FOCUS ON THE BIG PICTURE" WRONG "They'll say ignore all this, this is short-term no…

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.