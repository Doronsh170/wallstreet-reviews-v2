אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות בלבד, והחזר JSON בלבד.

You are writing a SHORT INTRADAY UPDATE in Hebrew for a financial website. The update is a
plain-language SUMMARY of what the curated X (Twitter) sources posted in the last two hours —
19:52–21:52 שעון ישראל, on 2026-11-02 (יום שני) — and nothing else.
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
  "title": "עדכון ביניים מוול סטריט 🇺🇸 – יום שני, 2.11.2026, 21:52",
  "date": "2026-11-02",
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
tweets, for the window 19:52–21:52 Israel time on 2026-11-02. Do NOT use it to find additional news, headlines,
prices or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════

══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══
Already published on the site. Your update covers ONLY the last two hours. Mention an item below ONLY if there is a genuinely NEW development about it inside the two-hour window.

[נקודות מרכזיות]
* חוזים בעלייה קלה לפני האינפלציה: החוזים על S&P 500 עולים 0.19%, החוזים על הדאו ג'ונס מוסיפים 151 נקודות והחוזים על נאסד״ק 100 כמעט ללא שינוי. השוק צפוי להיפתח ב-16:30 שעון ישראל אחרי ארבעה ימי ירידות רצופים. באסיה נרשמו ירידות חדות, הקוספי הקוריאני איבד 2.8% והניקיי ירד 2.6%.
* מדד המחירים לצרכן של 15:30: הלשכה לסטטיסטיקה של העבודה תפרסם היום ב-15:30 שעון ישראל את מדד המחירים לצרכן לאוגוסט, בצפי לעלייה של 0.4% בחודש ו-3.4% בשנה, ובליבה 0.4% בחודש ו-2.4% בשנה, לעומת נתון קודם של 3.4% ו-2.5%. אתמול עלה מדד המחירים ליצרן ל-5.4% מול צפי ל-5.3%, והליבה טיפסה ל-4.6%.
* התשואות מתקרבות ל-5 אחוזים: תשואת האג״ח ל-10 שנים עומדת על 4.955% והתשואה ל-30 שנה על 5.362%, אחרי עלייה של כ-95 נקודות בסיס מאז תחילת המלחמה באיראן. תשואה גבוהה יותר מעלה את שיעור ההיוון של הרווחים העתידיים ומייקרת מימון, ולכן הלחץ מתרכז במניות הצמיחה. האג״ח הארוכות יורדות 1.16% והתנודתיות עולה 3.42%.
* מחיר הסולר שובר שיא: מחיר הסולר בארה״ב חצה לראשונה 6 דולר לגלון, עלייה של 74% בתשעה חודשים, ובחלק מהמדינות הוא כבר מעל 8 דולר על רקע מחסור בהיצע. מחיר הנפט עולה היום 5.61% ומחיר הברנט 6.42%, לפי דיווחים סביב 105 דולר לחבית. דלק יקר מחלחל לסעיפי התחבורה במדד ומרים את ציפיות האינפלציה לקראת הנתון.
* מניית אורקל (ORCL) אחרי הדוח: המניה ירדה 5.38% במסחר הרגיל לקראת הפרסום, ולאחר הנעילה דיווחה החברה על הכנסות של 19.3 מיליארד דולר, צמיחה של 30%, ורווח מתואם של 1.92 דולר למניה, שניהם מעל הצפי. צבר ההתחייבויות לביצוע הגיע ל-664 מיליארד דולר לעומת 455.3 מיליארד לפני שנה, והמניה עלתה במסחר המאוחר. המשקיעים יבחנו היום אם המהלך מחזיק בפתיחה.
* שורה תחתונה: נתון האינפלציה של 15:30 יקבע את כיוון המסחר ואת השאלה אם ה-Fed יעלה ריבית בהחלטה של השבוע הבא. לפי דיווחים השוק מתמחר הסתברות של 62% להעלאה כבר בישיבה הקרובה ו-71% עד אוקטובר, ולכן קריאה חמה מהצפי תדחוף את התשואה ל-10 שנים מעל 5% ותכביד קודם כל על הטכנולוגיה.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-11-02. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Mon Nov 02 18:21:16 +0000 2026]: The Intel situation is insane. Intel, $INTC, is now down another -6% today after falling -29% on Friday in its biggest decline since 1971. This puts the stock down -57% from its record high seen just 86 trading days ago. That's -$440 billion of market cap. But, it gets better. Despite this historic reversal, the stock is STILL up +58% this year. What a time to be an investor.

@wallstengine [Mon Nov 02 18:51:24 +0000 2026]: CrowdStrike $CRWD announced several partnerships and expansions at its Fal.Con Europe event today. Here are the key developments: 1. DELL / NVIDIA: Integrating Falcon security into Dell AI Factory, covering AI agents, cloud workloads and security operations. Dell will also offer managed detection and response. 2. CoreWeave: Expanding its partnership to provide Falcon protection, 24/7 threat …

@StockMKTNewz [Mon Nov 02 18:44:12 +0000 2026]: Apple $AAPL reports earnings today after the stock markets close You should expect the numbers to come out at 4:30PM ET followed by the earnings call at 5PM ET https://t.co/9gVLtaaezz

@wallstengine [Mon Nov 02 17:54:15 +0000 2026]: $ASTS and AT&T $T say they completed the first successful handoff of an active connection between a ground-based cellular network and a satellite network using an unmodified smartphone. The test connected AT&T's terrestrial network with AST's BlueBird satellites, using technology from Ericsson and Nokia. AT&T says real-world beta testing is the next step before commercial service.

@StockMKTNewz [Mon Nov 02 17:59:08 +0000 2026]: HERE ARE SOME OF THE STOCKS HITTING NEW 52-WEEK HIGHS TODAY Coca-Cola $KO Visa $V Mastercard $MA Berkshire Hathaway $BRK.B Regeneron $REGN Vertex $VRTX Marriott $MAR Hilton $HLT Nasdaq $NDAQ Etsy $ETSY Crocs $CROX Abercrombie &amp; Fitch $ANF https://t.co/TJVKcMus6H

@AIStockSavvy [Mon Nov 02 18:27:51 +0000 2026]: $MRVL | B.Riley 𝗺𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝘀 𝗕𝘂𝘆 on 𝗠𝗮𝗿𝘃𝗲𝗹𝗹, cuts PT to $𝟮𝟳𝟱 from $𝟯𝟲𝟱 Analyst sees Marvell capturing a growing share of AI spend, while the pending Lumentum deal raises dilution and integration concerns. https://t.co/zYhiDHUck4

@AIStockSavvy [Mon Nov 02 18:27:37 +0000 2026]: $LITE | Stifel 𝗱𝗼𝘄𝗻𝗴𝗿𝗮𝗱𝗲𝘀 𝗟𝘂𝗺𝗲𝗻𝘁𝘂𝗺 from 𝗕𝘂𝘆 to 𝗛𝗼𝗹𝗱, cuts PT to $𝟴𝟬𝟲 from $𝟭,𝟮𝟯𝟮 Analyst sees the fixed-ratio MRVL deal and deal spread capping Lumentum’s standalone upside despite strong growth and margins. https://t.co/tKijPvmt8s

@AIStockSavvy [Mon Nov 02 18:25:20 +0000 2026]: $CIFR | H.C. Wainwright 𝗿𝗲𝗶𝘁𝗲𝗿𝗮𝘁𝗲𝘀 𝗕𝘂𝘆 on 𝗖𝗶𝗽𝗵𝗲𝗿 𝗠𝗶𝗻𝗶𝗻𝗴, PT $𝟮𝟬, 'Defending Cipher Mining' Analyst sees strong tenant demand, proven financing and a 5.9 GW pipeline positioning Cipher for continued HPC growth. https://t.co/68t7eVGp8i

@StockMKTNewz [Mon Nov 02 19:37:20 +0000 2026]: SANDISK $SNDK'S GROSS MARGIN NEARLY TRIPLED IN A YEAR For every $1 of revenue, Sandisk kept: - Fiscal Q1 2026: 29.8¢ of gross profit - Fiscal Q1 2027: 85.0¢ of gross profit https://t.co/wMw1Z5esHv

@AIStockSavvy [Mon Nov 02 18:28:00 +0000 2026]: $CIFR | Northland 𝗺𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝘀 𝗢𝘂𝘁𝗽𝗲𝗿𝗳𝗼𝗿𝗺 on Cipher Mining, 𝗰𝘂𝘁𝘀 PT to $𝟭𝟰.𝟬𝟬 from $𝟮𝟳.𝟱𝟬 https://t.co/Apw6Pv5sH4

@AIStockSavvy [Mon Nov 02 18:22:45 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: MISSION SUCCESS: $RKLB Rocket Lab Launches 99th Electron Mission https://t.co/sWO45Z13Zs

@AIStockSavvy [Mon Nov 02 17:57:04 +0000 2026]: $META | Meta Eyes at Least $20 Billion From Potential Bond Offerings - Bloomberg

@KobeissiLetter [Mon Nov 02 19:18:00 +0000 2026]: Markets are heading into their strongest seasonal period of the year: Since 1980, the S&P 500 has rallied +2.1% on average in November, making it the strongest month of the year. Over this period, positive returns occurred 74% of the time, the best hit rate of any month. Furthermore, the S&P 500 has gained +1.6% on average in November since 1964, with positive returns occurring 69% of the time. …

@wallstengine [Mon Nov 02 18:08:59 +0000 2026]: ANTHROPIC IS PLANNING A UK 🇬🇧 RETAIL SHARE OFFERING ALONGSIDE ITS U.S. IPO: BBG

@StockMKTNewz [Mon Nov 02 19:25:46 +0000 2026]: In 2026 you can have a full custom earnings dashboard directly on your stock broker with my sponsors over at Aries Infinite https://t.co/whCMovPNy8

@wallstengine [Mon Nov 02 19:13:25 +0000 2026]: Howard Marks on investing in AI: If you want to invest in AI, you should probably buy the stocks The issue is that when you buy debt, you have no upside. Best you get the interest & principal repayment that you bargained for After that, it's all different degrees of downside h/t @KellyCNBC

@AIStockSavvy [Mon Nov 02 19:22:27 +0000 2026]: Anyone else feel like the Fear &amp; Greed Index should be at ZERO right now? 😂 https://t.co/OaH1Q4W0e2

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.