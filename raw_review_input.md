אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות בלבד, והחזר JSON בלבד.

You are writing a SHORT INTRADAY UPDATE in Hebrew for a financial website. The update is a
plain-language SUMMARY of what the curated X (Twitter) sources posted in the last two hours —
15:30–17:30 שעון ישראל, on 2026-11-25 (יום רביעי) — and nothing else.
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
  "title": "עדכון ביניים מוול סטריט 🇺🇸 – יום רביעי, 25.11.2026, 17:30",
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
tweets, for the window 15:30–17:30 Israel time on 2026-11-25. Do NOT use it to find additional news, headlines,
prices or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════

══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══
Already published on the site. Your update covers ONLY the last two hours. Mention an item below ONLY if there is a genuinely NEW development about it inside the two-hour window.

[עדכון ביניים]
* אנבידיה (NVDA): בניגוד לדיווח הקודם, לפי Bloomberg, ג'נסן הואנג חזר לתפקיד המנכ״ל והתנצל בפני העובדים. לדבריו, הדירקטוריון השתכנע כי אין מניעה להחזרתו מטעמי ביטחון לאומי.
* חומרת בינה מלאכותית: לפי דיווחים, מניות אנלוג דיווייסס יורדות ב-17%, HPE ב-16%, דל ומיקרון ב-11%, ואנבידיה בכמעט 8%. מנכ״ל HPE ציין כי הביקוש גבוה משמעותית מצבר ההזמנות, אך החברה הזהירה משחיקה בשולי הרווח בשנה הבאה.
* קורוויב (CRWV): לפי דיווחים, מספר סדרות אג״ח של החברה ירדו לשפל מאז הנפקתן, על רקע חששות לגבי יכולת ההתמדה בקצב ההשקעות בבינה מלאכותית. איגרות החוב הנושאות ריבית של 9% לפדיון ב-2031 נסחרו במחיר של 76.6 סנט לדולר ערך נקוב.
* קרנות סל על הזהב: לפי דיווחים, קרנות סל המגובות בזהב פיזי רשמו בשבוע שעבר פדיונות בהיקף של 20 טונות זהב, הרמה השבועית הגבוהה ביותר מאז יוני. מחצית מהפדיונות נרשמה בקרן GLD.
* סיטאדל סקיוריטיז: לפי Bloomberg, הכנסות המסחר נטו בתשעת החודשים הראשונים של השנה הסתכמו ביותר מ-15 מיליארד דולר, מעל השיא השנתי של 2025. הכנסות המסחר ברבעון השלישי צמחו ב-29% והרווח הנקי עלה בכ-13% בהשוואה לרבעון המקביל.
* מטא (META) וולמארט: לפי דיווחים, לקוחות וולמארט יכולים לבצע רכישות באמצעות סוכן הבינה המלאכותית של מטא, הכולל איתור מוצרים, בניית סל קניות והשלמת הרכישה בהתאם לתקציב שהוגדר.
* סאנופי (SNY): לפי דיווחים, החברה רשמה את יום המסחר הטוב ביותר שלה מאז 2008, לאחר שהסכימה לרכוש את אינסמד תמורת 41 מיליארד דולר. הרכישה מרחיבה את פעילותה בתחום הטיפול במחלות ריאה לקראת פקיעת הפטנט על דופיקסנט.
* טארגט (TGT): לפי דיווחים, מניית הקמעונאית הגיעה במהלך המסחר לשיא של 52 שבועות.
* אינפלציה בארה״ב: לפי דיווחים, 57% מהצרכנים בנובמבר ייחסו את ההרעה במצבם הכלכלי לעומת השנה הקודמת לעליית המחירים, שיעור שיא ועלייה של 24 נקודות אחוז מאז מרץ 2024. מנגד, הנשיא טראמפ טען כי המחירים יורדים במהירות וכי האינפלציה התמתנה.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-11-25. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Wed Nov 25 13:31:27 +0000 2026]: BREAKING: US October PCE inflation, the Fed's preferred inflation metric, rises to 3.8%, its 2nd-highest level since April 2023. Core PCE inflation also rose to 3.3%, above expectations of 3.2%. CPI, PPI, and PCE inflation all continue to push higher. December rate hike odds are rising.

@KobeissiLetter [Wed Nov 25 14:45:06 +0000 2026]: BREAKING: The Nasdaq 100 extends losses to over -4.5% on the day after the Trump Administration announces new tariffs and PCE inflation comes in hot. https://t.co/P50q1Jw8AG

@KobeissiLetter [Wed Nov 25 13:52:06 +0000 2026]: BREAKING: Market expectations for a December rate hike rise above 97% after US PCE inflation hits its 2nd highest level since April 2023. This will mark the Fed's second interest rate hike of 2026. 12 months ago, markets expected 3 rate cuts in 2026. Higher rates are on the way.

@AIStockSavvy [Wed Nov 25 13:32:41 +0000 2026]: US Jobless Claims Data: $QQQ $SPY ➤ Continued Jobless Claims (Nov. 14): 1,697K (Forecast 1,721K, Previous 1,763K) ➤ Initial Jobless Claims (Nov. 21): 189K (Forecast 200K, Previous 203K) ➤ Initial Jobless Claims 4-Week Average (Nov. 21): 196K (Forecast --, Previous 197.75K)

@wallstengine [Wed Nov 25 15:22:59 +0000 2026]: COREWEAVE'S $CRWV 2031 BONDS NOW YIELD NEARLY 18% AS THEY FALL AGAIN: TRADEWEB DATA.

@StockMKTNewz [Wed Nov 25 14:25:44 +0000 2026]: Starbucks $SBUX has tapped advisers to prepare for a potential sale of its Japan 🇯🇵 business for several billion dollars - Bloomberg https://t.co/AKBxTIbJ9i

@AIStockSavvy [Wed Nov 25 15:27:57 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Some $CRWV Coreweave Bonds Fall, 2031 Bond Yield Hits 17.91% - Tradeweb Data

@AIStockSavvy [Wed Nov 25 14:49:22 +0000 2026]: 📢 𝗝𝗨𝗦𝗧 𝗜𝗡: Nasdaq 100 Falls 20% From Peak, On Track To Enter Bear Market - Bloomberg - $QQQ $SPY

@AIStockSavvy [Wed Nov 25 14:25:19 +0000 2026]: $CRWV + $CRWD: AI COMPUTE MEETS ROUND-THE-CLOCK SECURITY Expanded partnership brings 24/7 threat hunting to CoreWeave’s AI workloads, while CoreWeave powers CrowdStrike SafeMind’s training and inference.

@AIStockSavvy [Wed Nov 25 13:38:50 +0000 2026]: U.S. Trade Representative Greer: The latest proposed tariffs largely follow the agreements we have reached. - $QQQ $SPY

@AIStockSavvy [Wed Nov 25 13:38:20 +0000 2026]: $AAPL quietly up nearly 13% in 3 months while AI stocks get crushed. Apparently, being “behind in AI” is a bullish thesis now. 😂 https://t.co/r6kjXNxHkm

@AIStockSavvy [Wed Nov 25 13:31:17 +0000 2026]: US PCE Inflation: $QQQ $SPY ➤ Core PCE YoY (Oct): 3.3% (Forecast 3.2%, Previous 3.1%) ➤ Core PCE QoQ (Q3, SAAR Revised): 2.5% (Forecast 2.5%, Previous 2.5%) ➤ PCE YoY (Oct): 3.8% (Forecast 3.8%, Previous 3.6%) ➤ PCE MoM (Oct): 0.3% (Forecast 0.3%, Previous 0.5%) ➤ PCE QoQ (Q3, SAAR Revised): 2.1% (Forecast --, Previous 2.1%)

@KobeissiLetter [Wed Nov 25 13:38:59 +0000 2026]: BREAKING: The US Financial Crimes Enforcement Network (FinCEN) has suffered a cybersecurity breach, resulting in unauthorized access to a "limited subset" of its systems, per a US government official. FinCEN oversees some of the US government's most sensitive financial intelligence, including reports of suspicious banking activity.

@StockMKTNewz [Wed Nov 25 15:24:39 +0000 2026]: CoreWeave $CRWV stock is down by 10% today CRWV stock is now down by 46.6% so far in 2026 https://t.co/D89OpTEj2a

@StockMKTNewz [Wed Nov 25 14:38:58 +0000 2026]: Anthropic $ANT just dropped under a $1 Trillion market cap for the first time as a public company https://t.co/4ohnITp4tz

@AIStockSavvy [Wed Nov 25 14:48:52 +0000 2026]: Fear index below 10 😳😳 $QQQ $SPY https://t.co/7KfjfNxKnx

@StockMKTNewz [Wed Nov 25 13:50:37 +0000 2026]: GOLDMAN SACHS STRATEGIST SAYS IT'S TOO EARLY TO BUY THE AI SELLOFF Christian Mueller-Glissmann told Bloomberg TV markets are in a "pretty fragile regime" and investors need to see real profits from all the AI spending first. His biggest worry is a repeat of late 2018, when Fed tightening hit growth and forced the central bank to ease

@wallstengine [Wed Nov 25 13:38:14 +0000 2026]: U.S. PROPOSES NEW TARIFFS ON 14 TRADING PARTNERS OVER INDUSTRIAL OVERCAPACITY 🇨🇳 China: 20% (up to 40% if trade truce is broken) 🇻🇳 Vietnam: Up to 35% 🇮🇳 India: Up to 25% (17% if a deal is reached) 🇰🇷 South Korea: Up to 25% 🇹🇼 Taiwan: Up to 25% 🇮🇩 Indonesia: Up to 25% 🇲🇾 Malaysia: Up to 25% 🇹🇭 Thailand: Up to 25% 🇰🇭 Cambodia: Up to 25% 🇪🇺 European Union: Up to 20% 🇯🇵 Japan: Up to 20% 🇨🇭 …

@wallstengine [Wed Nov 25 13:32:58 +0000 2026]: US JOBLESS CLAIMS JUST DROPPED TO 189,000, BELOW THE 200,000 EXPECTED

@KobeissiLetter [Wed Nov 25 15:18:00 +0000 2026]: BREAKING: Bitcoin falls below $57,500 and ETH nears $1,600 as the selloff in crypto gains momentum. Another -$500 million worth of levered positions have been liquidated over the last 24 hours. https://t.co/oyvKjyQ9US

@wallstengine [Wed Nov 25 13:30:41 +0000 2026]: US 🇺🇸 PCE / GDP DATA: Core PCE YoY: 3.3% (Est. 3.2%, Prior 3.1%) Core PCE MoM: 0.3% (Est. 0.3%, Prior 0.3%) PCE YoY: 3.8% (Est. 3.8%, Prior 3.7%) PCE MoM: 0.3% (Est. 0.3%, Prior 0.5%) Q3 GDP (2nd Est.): 4.3% (Est. 3.5%, Prior 3.4%) Spending MoM: 0.3% (Est. 0.4%, Prior 0.6%)

@wallstengine [Wed Nov 25 13:49:23 +0000 2026]: USTR JAMIESON GREER ON NVIDIA: "COMPANY IS STRUCTURALLY IMPORTANT… HAVE TO MAKE SURE THAT COMPANY REMAINS ON TOP."

@wallstengine [Wed Nov 25 13:33:29 +0000 2026]: US 🇺🇸 ECONOMY GREW AT A 4.3% PACE IN Q3, REVISED UP FROM 3.4% &amp; THE FASTEST IN NEARLY 3 YEARS

@StockMKTNewz [Wed Nov 25 13:33:55 +0000 2026]: 🇺🇸 PCE for October just came in at +3.8% YoY above expectations +3.7% YoY

@StockMKTNewz [Wed Nov 25 13:57:11 +0000 2026]: Please stop sending me notifications each of my stocks are down by 5% today

@StockMKTNewz [Wed Nov 25 13:32:02 +0000 2026]: US 🇺🇸 GDP for Q3 just came in at +4.3% above expectations of +3.4% (2nd GDP reading out of 3)

@wallstengine [Wed Nov 25 14:53:33 +0000 2026]: CNN'S FEAR &amp; GREED INDEX JUST PLUNGED TO 9, "EXTREME FEAR," ITS LOWEST LEVEL SINCE MARCH https://t.co/k16Obmzpgr

@wallstengine [Wed Nov 25 14:46:20 +0000 2026]: THE NASDAQ 100 HAS NOW WIPED OUT ALL OF MONDAY'S 6.9% JENSEN HUANG RALLY, AND CHIP STOCKS HAVE ERASED EVEN MORE

@wallstengine [Wed Nov 25 14:52:27 +0000 2026]: WHITE HOUSE HASSETT: WE EXPECT WARSH AND THE FED WILL BE DATA DRIVEN

@wallstengine [Wed Nov 25 14:45:54 +0000 2026]: EU 🇪🇺 SAYS THE US MUST RESPECT ITS 15% TARIFF CEILING, AFTER WASHINGTON PROPOSED UP TO 20% IN NEW TARIFFS ON EUROPEAN GOODS

@wallstengine [Wed Nov 25 13:52:20 +0000 2026]: Living Brain and OpenHuman say they've used AI agents with persistent memory and recursive self-improvement to solve 15 mathematical conjectures, some dating back over 100 years. For Erdős Problem 985, Living Brain identified the exact theorem needed from a 17-million-line Lean library, allowing its AI agents to complete the proof in a single line of Lean. What's particularly interesting is that …

@wallstengine [Wed Nov 25 13:37:34 +0000 2026]: Kalshi now gives a 93% chance of a 25 bp Fed rate hike on December 9, after the Fed's preferred inflation gauge came in hot. https://t.co/1uCCJHEV0s

@StockMKTNewz [Wed Nov 25 14:52:47 +0000 2026]: The Stock Market Fear and Greed Index just dropped back down into single digits currently at Extreme Fear: 9/100 https://t.co/8ay0wFyW3E

@StockMKTNewz [Wed Nov 25 14:46:07 +0000 2026]: *THERE ARE 0 STOCKS IN MY PORTFOLIO THAT ARE GREEN TO START TRADING TODAY

@StockMKTNewz [Wed Nov 25 14:31:17 +0000 2026]: The 🇺🇸 stock market is back open for the trading day https://t.co/bQZVcnVby1

@StockMKTNewz [Wed Nov 25 15:26:53 +0000 2026]: This is how every stock in the S&amp;P 500 has performed so far in today's early trading https://t.co/VLsqEbMKCH

@StockMKTNewz [Wed Nov 25 15:20:30 +0000 2026]: Carl Icahn is now estimated to be worth $1.2 Billion Icahn's esimtaed net worth is down by $21 Billion over the last 5 years according to Bloomberg

@AIStockSavvy [Wed Nov 25 14:35:01 +0000 2026]: Technology, Financial, Software are 🩸🩸🩸 Consumer defensive, Telecom only 🟢 https://t.co/FFWDzvP1Oh

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.