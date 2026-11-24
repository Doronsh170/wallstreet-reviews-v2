אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות בלבד, והחזר JSON בלבד.

You are writing a SHORT INTRADAY UPDATE in Hebrew for a financial website. The update is a
plain-language SUMMARY of what the curated X (Twitter) sources posted in the last two hours —
19:41–21:41 שעון ישראל, on 2026-11-24 (יום שלישי) — and nothing else.
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
  "title": "עדכון ביניים מוול סטריט 🇺🇸 – יום שלישי, 24.11.2026, 21:41",
  "date": "2026-11-24",
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
tweets, for the window 19:41–21:41 Israel time on 2026-11-24. Do NOT use it to find additional news, headlines,
prices or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════

══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══
Already published on the site. Your update covers ONLY the last two hours. Mention an item below ONLY if there is a genuinely NEW development about it inside the two-hour window.

[עדכון ביניים]
* אנבידיה (NVDA): לפי CNBC, דירקטוריון החברה אינו שוקל להחזיר את ג'נסן הואנג לתפקיד המנכ״ל. בעקבות הדיווח המניה ירדה לשפל יומי חדש, והשלימה ירידה של 34% מהשיא שנרשם ב-6 באוקטובר. מנכ״ל OpenAI, סם אלטמן, אמר שקשה לדמיין את מהפכת הבינה המלאכותית ללא מעורבותו של הואנג.
* נאסד״ק 100: המדד העמיק את הירידות ל-2.3% במהלך המסחר הרגיל, על רקע הדיווחים שלפיהם דירקטוריון אנבידיה אינו שוקל את החזרת ג'נסן הואנג לתפקיד המנכ״ל.
* פיגורים בהלוואות בארה״ב: שיעור הפיגורים החמורים בהלוואות סטודנטים עלה ברבעון השלישי של 2026 ל-10.9%, הרמה הגבוהה ביותר מאז סוף 2019. שיעור הפיגורים החמורים בהלוואות רכב הגיע ל-5.7%, שיא בנתונים, ומצביע על המשך הלחץ על יכולת ההחזר של לווים.
* הנפקת אנתרופיק (Anthropic): לפי CNBC, בראד גרסטנר מקרן Altimeter Capital מתכנן להשקיע 5 מיליארד דולר בהנפקת החברה. מדובר בהתחייבות הגבוהה פי חמישה מכל השקעה קודמת שלו בהנפקה ראשונית.
* מחשוב על של AMD: לפי דיווחים, מחשב העל Lux, המבוסס על מעבדי AMD, נפתח לשימוש חוקרים במעבדה הלאומית אוק רידג'. המערכת משמשת תשתית בינה מלאכותית למשימת Genesis של משרד האנרגיה האמריקאי.
* ספקיות טכנולוגיה זרות: לפי דיווחים, סגן מזכיר המדינה האמריקאי הלברג הבהיר כי וושינגטון אינה מתכוונת לפגוע בספקיות כמו אריקסון, ASML, סמסונג ו-SK Hynix או להוציא אותן משרשראות האספקה בארה״ב.
* תקלות בבנקים בארה״ב: התקבלו דיווחים רבים על קשיים בגישה לחשבונות ובכניסה לשירותי הבנקאות המקוונת של JPMorgan Chase, בנק אוף אמריקה, וולס פארגו ו-U.S. Bank. לפי הדיווחים, אלפי לקוחות נתקלו בתקלות, אך טרם הובהר הגורם להן.
* ביקוש לשבבי בינה מלאכותית: מנכ״ל OpenAI, סם אלטמן, הזהיר מפני ספירה כפולה של ביקושים בתוכניות יצרניות השבבים. לדבריו, כמה יצרניות מניחות במקביל שחברות הבינה המלאכותית הגדולות ירכשו חלק משמעותי מתפוקתן, אף שלא כולן יזדקקו לכל הכמויות המתוכננות.
* חברת הבינה המלאכותית Noeri: לפי דיווחים, החברה הושקה עם מימון של 110 מיליון דולר לפיתוח מערכות בינה מלאכותית ארגוניות המסוגלות לשפר את ביצועיהן באופן עצמאי.
* תמונת העדכונים: הדיווחים על עתיד הנהלת אנבידיה מלווים בהעמקת הירידות בנאסד״ק, ובמקביל עולות שאלות לגבי היקף הביקוש העתידי לשבבי בינה מלאכותית.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-11-24. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Tue Nov 24 17:46:05 +0000 2026]: BREAKING: Global physical gold-backed ETFs posted -20 tonnes in gold outflows last week, their largest weekly withdrawal since June. Gold ETFs have seen outflows in 3 of the last 5 weeks, totalling -30 tonnes net. Last week's outflows were driven by the US's largest gold-backed ETF, $GLD, which recorded -10 tonnes in withdrawals. US outflows totalled -12 tonnes, followed by China and the UK, both …

@gurgavin [Tue Nov 24 18:10:42 +0000 2026]: NVIDIA SHARES ARE DOWN ALMOST 8% TODAY MAYBE THEY SHOULD FIRE AND HIRE JENSEN AGAIN $NVDA https://t.co/F4kpQbGaMC

@AIStockSavvy [Tue Nov 24 19:19:57 +0000 2026]: 📊 𝐈𝐍𝐕𝐄𝐒𝐓𝐎𝐑 𝐍𝐎𝐓𝐄: COREWEAVE BONDS HIT 𝗥𝗘𝗖𝗢𝗥𝗗 𝗟𝗢𝗪𝗦, ERASING MONDAY’S GAINS - $CRWV $NVDA Several CoreWeave bonds fell to their lowest prices since issuance on Tuesday as investors again questioned whether the pace of AI investment is sustainable. 👉 𝗞𝗲𝘆 𝗛𝗶𝗴𝗵𝗹𝗶𝗴𝗵𝘁𝘀 ➤ 𝟮𝟬𝟯𝟭 𝗡𝗢𝗧𝗘𝗦: CoreWeave’s 9% notes due in 2031 traded as low as 𝟳𝟲.𝟲 𝗰𝗲𝗻𝘁𝘀 on the dollar. ➤ 𝟮𝟬𝟯𝟮 𝗡𝗢𝗧𝗘𝗦: Its 9.625% notes due in 2032 fell …

@StockMKTNewz [Tue Nov 24 19:17:38 +0000 2026]: NVIDIA $NVDA CEO JENSEN HUANG APOLOGIZED TO EMPLOYEES IN A TUESDAY ALL-HANDS MEETING He reportedly called it "the hardest company meeting" he's ever done, per Bloomberg. Then he explained why the board brought him back: Not because he's a "tech bro" or above the law. Not because the government wanted him back. The board was assured there was no national security threat, he told staff. What else …

@wallstengine [Tue Nov 24 18:58:10 +0000 2026]: AI HARDWARE IS GETTING HIT HARD TODAY Analog Devices -17% $HPE -16% $DELL -11% Micron -11% Nvidia -7% HPE's CEO says AI demand is "multiples" of its backlog and supply is "severely constrained," but the company warned the servers it's selling will squeeze margins next year.

@wallstengine [Tue Nov 24 18:54:02 +0000 2026]: YOU CAN NOW LET $META'S AI DO YOUR WALMART BLACK FRIDAY SHOPPING Starting today, customers can shop Walmart's Black Friday deals directly through Muse, Meta's personal AI agent. Muse can search for products, build a cart and complete the purchase on Walmart's website and at Sam's Club. Shoppers set a spending limit and can approve purchases and review everything the agent buys. Walmart says …

@wallstengine [Tue Nov 24 19:11:46 +0000 2026]: JENSEN HUANG THANKED THE TRUMP ADMIN IN FRONT OF NVIDIA STAFF FOR INTELLIGENCE THAT HELPED THE BOARD BRING HIM BACK AS $NVDA CEO https://t.co/7j9EZfWNl8

@StockMKTNewz [Tue Nov 24 18:12:51 +0000 2026]: My sponsors over at Tradr ETFs now have options on $ANTT and $ANTZ ... Calls and puts on the 2x daily long and short Anthropic $ANT ETFs Options may not be suitable for all investors. Leveraged ETFs involve significant risk. See https://t.co/EUgWBjY4CM https://t.co/JH5c5auizc

@AIStockSavvy [Tue Nov 24 19:14:40 +0000 2026]: NIGHTGLASS FLAGGED $589.66 BEFORE THE BELL Mizuho initiated $LMT at Buy with a $765 target. Shares popped on the news and hit $590.10 before slipping back below $589.66. Nightglass had $589.66 marked as resistance before the bell. That gave you a price to watch as the stock ran. https://t.co/Bemj9oq9dw

@StockMKTNewz [Tue Nov 24 18:23:18 +0000 2026]: Target $TGT stock hit new 52 WEEK HIGHS 🟢 at some point today https://t.co/ciBinSR49d

@AIStockSavvy [Tue Nov 24 19:32:55 +0000 2026]: Trump: Prices are falling rapidly across the board. Egg prices were four times higher when we took office. We inherited record-high prices and the worst inflation ever, but have brought inflation down to a very good level. - $QQQ $SPY

@wallstengine [Tue Nov 24 18:13:29 +0000 2026]: Sanofi $SNY just had its best day since 2008 after agreeing to buy Insmed for $41 billion, adding lung disease drug Brinsupri ahead of Dupixent's patent cliff. https://t.co/OO4nXIK385

@KobeissiLetter [Tue Nov 24 19:38:05 +0000 2026]: Inflation is America’s biggest concern: In November, a record 57% of US consumers cited higher prices as a reason for their financial situation worsening compared with a year earlier. This figure has surged +24 percentage points since March 2024. By comparison, this proportion peaked at 48% during the 2008 Financial Crisis and the Great Inflation of the 1970s. To put this into perspective, in …

@KobeissiLetter [Tue Nov 24 18:42:02 +0000 2026]: Market corrections are a regular phenomenon: The US equity market has recorded an average of 1 correction of 10%+ per year since 1930. Since 2000, the S&P 500 has seen 24 regular corrections. Despite these declines, the S&P 500 has delivered positive annual returns in 19 calendar years since 2000. Furthermore, US stocks have posted 3.4 pullbacks of 5%+ per year on average since 1930. By …

@wallstengine [Tue Nov 24 19:23:53 +0000 2026]: JENSEN HUANG TOLD NVIDIA STAFF TODAY WAS "THE HARDEST COMPANY MEETING" HE'S EVER DONE THE HARDER MEETING, HE SAID, WAS WITH HIS WIFE https://t.co/t8KTN7BV4s

@wallstengine [Tue Nov 24 19:24:34 +0000 2026]: JENSEN HUANG TO NVIDIA STAFF ON TRUMP: "HE IS MY PRESIDENT. I AM IN SERVICE OF MAKING OUR PRESIDENT — OUR COUNTRY — SUCCESSFUL"; TRUMP LOVES NVIDIA

@wallstengine [Tue Nov 24 19:10:11 +0000 2026]: JENSEN HUANG TOLD NVIDIA EMPLOYEES HE IS IN THERAPY &amp; APOLOGIZED FOR VIOLATING THE COMPANY'S CODE OF CONDUCT: WSJ

@wallstengine [Tue Nov 24 18:52:55 +0000 2026]: For those who trade futures, NinjaTrader is running a holiday offer for new customers. Terms apply. Futures trading involves substantial risk.

@StockMKTNewz [Tue Nov 24 19:28:41 +0000 2026]: CITADEL SECURITIES HAS ALREADY MADE MORE IN 9 MONTHS OF 2026 THAN IN ALL OF 2025, PER BLOOMBERG Net trading revenue is above $15 billion through September, passing last year's record. Here's the quarter that pushed it there: Q3 revenue: more than $3.4B, up 29% year over year Q3 net income: about $1.19B, up about 13% This is the market-making firm, separate from Ken Griffin's Citadel hedge fund.

@wallstengine [Tue Nov 24 19:07:32 +0000 2026]: Ken Griffin's market-making firm, Citadel Securities, generated more than $15 billion in net trading revenue in the first 9 months of 2026, already surpassing its full-year 2025 record. Q3 financials: Trading revenue: $3.4B+, up 29% YoY Net income: $1.19B, up 13% YoY https://t.co/vMaVBwL7vs

@gurgavin [Tue Nov 24 18:56:40 +0000 2026]: RT @McLarenF1: Happy Guru Nanak Jayanti 🧡 #McLarenF1 https://t.co/8QqUaeLqHG

@KobeissiLetter [Tue Nov 24 18:15:25 +0000 2026]: RT @TKL_Adam: Looking forward to joining the great Charles Payne, @cvpayne, at 2:45 PM ET, in my first TV appearance since Jensen Huang has…

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.