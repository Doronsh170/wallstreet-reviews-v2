אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are writing a SHORT INTRADAY UPDATE in Hebrew for a financial website. The update is a
plain-language SUMMARY of what the curated X (Twitter) sources posted in the last two hours —
17:21–19:21 שעון ישראל, on 2026-07-14 (יום שלישי) — and nothing else.
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
  "title": "עדכון ביניים מוול סטריט 🇺🇸 – יום שלישי, 14.7.2026, 19:21",
  "date": "2026-07-14",
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
tweets, for the window 17:21–19:21 Israel time on 2026-07-14. Do NOT use it to find additional news, headlines,
prices or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════

══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══
Already published on the site. Your update covers ONLY the last two hours. Mention an item below ONLY if there is a genuinely NEW development about it inside the two-hour window.

[סיכום המסחר]
* יום אדום בהובלת הטכנולוגיה: וול סטריט פתחה את השבוע בירידות, כשזעזוע אנרגיה מהמפרץ הפרסי הכתיב את הטון והוביל למכירות ממוקדות בטכנולוגיה. מדד הנאסד"ק 100 בלט לשלילה וצנח כ-1.9%, מדד S&P 500 ירד כ-0.77%, בעוד מדד הדאו ג'ונס נשאר עמיד יחסית ואיבד כ-0.25% בלבד בזכות משקלן הנמוך של מניות הצמיחה. מדד המניות הקטנות ראסל 2000 ירד כ-0.85%, כך שהחולשה הייתה רוחבית אך התרכזה בעיקר בשמות הטכנולוגיים היקרים.
* מצר הורמוז מצית את הנפט: הסיפור המרכזי של היום היה גיאופוליטי, לאחר שהנשיא טראמפ הכריז כי ארה"ב מחזירה את החסימה על מצר הורמוז וגובה אגרת מעבר בשיעור 20% משווי המטען. מחירי הנפט הגיבו בזינוק חד, כשה-WTI עלה כ-8.4% והברנט קפץ כ-9.1% ונסחר מעל 79 דולר לחבית. מהלך כזה מחזיר את סיכון האינפלציה אל קדמת הבמה, שכן התייקרות אנרגיה מתגלגלת דרך שרשרת ההובלה והייצור אל המחירים לצרכן ומצרה את מרחב התמרון של הפדרל ריזרב.
* השבבים מובילים את הירידה: הלחץ על הטכנולוגיה יובא הבוקר מאסיה, שם מפולת במניות השבבים גלשה אל המסחר בניו יורק וסקטור הטכנולוגיה איבד כ-2.4% והיה החלש ביותר במסחר. מניית קורוויב (CRWV) בלטה לשלילה וצנחה כ-6.3%, בזמן שאלפבית (GOOGL) ירדה כ-1.3% חרף הדיווח על הרחבת מכירת שבבי ה-TPU שלה ללקוחות ענן חדשים. הירידות מגיעות דווקא לאחר שבוע שבו קרנות הגידור הגדילו אחזקות בשבבים לרמה הגבוהה ביותר מזה כ-3.5 שנים, מה שהופך את הסקטור לרגיש במיוחד לשינויי סנטימנט.
* וולר מזהיר מפני העלאות ריבית: נגיד הפדרל ריזרב כריסטופר וולר הוסיף שמן למדורה כשאמר כי אם נתון אינפלציית הליבה שיתפרסם השבוע יפתיע כלפי מעלה, ייתכן שהבנק המרכזי ייאלץ לשקול העלאות ריבית בטווח הקרוב. האמירה הניצית, על רקע קפיצת הנפט, דחפה את תשואות אג"ח ארה"ב ל-10 שנים כלפי מעלה והכבידה על מכפילי מניות הצמיחה. עבור המשקיעים זהו שילוב מדאיג של הלם היצע באנרגיה יחד עם בנק מרכזי שמאותת כי סבלנותו כלפי אינפלציה מתקרבת לקצה.
* רוטציה הגנתית מתחת לפני השטח: תמונת הסקטורים חשפה מעבר ברור לעמדה הגנתית, כשמגזר האנרגיה זינק כ-3% ורכב על גל הנפט והוביל בפער ניכר את המסחר. במקביל, המגזרים ההגנתיים נצבעו בירוק, כשהחשמל והמים הוסיפו כ-0.68%, מוצרי הצריכה הבסיסיים עלו כ-0.56% והפיננסים התחזקו כ-0.65% לקראת פתיחת עונת הדוחות. בצד הנגדי בלטו לשלילה הטכנולוגיה שאיבדה כ-2.4% והצריכה המחזורית שירדה כ-1%, תמהיל שמעיד על משקיעים שברחו מסיכון לעבר עוגני הכנסה יציבים.
* מניית אפל (AAPL) בולטת לחיוב: בים האדום של הטכנולוגיה, אפל דווקא בלטה לחיוב ועלתה כ-0.63%, אחת המעטות מבין ענקיות הטכנולוגיה שנסחרה בירוק. ברקע, החברה הגישה תביעה פדרלית נגד OpenAI בטענה לגניבת סודות מסחריים, ובמקביל דווח כי הסכימה לרכוש נכסים ולקלוט עובדים מחברת סיגסקאלר. השילוב בין מהלך משפטי אגרסיבי להגנה על הקניין הרוחני לבין רכישת כישרונות טכנולוגיים חיזק את התחושה שאפל נערכת להאיץ את מאמצי הבינה המלאכותית הפנימיים שלה.
* הזהב נסוג למרות המתיחות: באופן שנראה מנוגד לאינטואיציה, דווקא ביום של הסלמה גיאופוליטית הזהב עלה כ-2.6% והכסף הוסיף כ-3.3%, כשמקום הבריחה למקלט נלקח הפעם על ידי הדולר והנפט. הדולר האמריקאי נחלש כ-0.39% והתשואות העולות ייקרו את עלות ההחזקה במתכת שאינה נושאת ריבית, מה שמסביר את הנסיגה. מדד הפחד VIX עלה כ-3.3%, עלייה שמשקפת חשש מוגבר אך עדיין רחוקה מרמות של פאניקה רחבה בשוק.
* שורה תחתונה למחר: הזרקור עובר מחר אל מדד המחירים לצרכן (CPI) בארה"ב שיתפרסם ב-15:30 שעון ישראל, הן המדד הכללי והן מדד הליבה, אירוע המאקרו המהותי ביותר של השבוע. וולר כבר התריע כי הפתעה כלפי מעלה באינפלציית הליבה עלולה לחייב העלאות ריבית, ולכן על רקע זינוק הנפט כל קריאה גבוהה מהצפי עלולה להצית מחדש את חששות הריבית וללחוץ על מכפילי מניות הצמיחה. במקביל נפתחת מחר עונת הדוחות עם ג'יי.פי מורגן (JPM) וענקיות הבנקאות, שיספקו קריאת כיוון ראשונה על בריאות הצרכן והאשראי, כך שהשילוב בין נתון האינפלציה לטון הבנקים יכתיב את מגמת המסחר.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-14. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Tue Jul 14 14:57:32 +0000 2026]: BREAKING: US officials say shipments of Nvidia, $NVDA, H200 chips to China have begun. Nvidia shares extend gains to a new high of day on the news.

@AIStockSavvy [Tue Jul 14 14:53:58 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $NVDA Nvidia H200 chip shipments to China remain limited A senior U.S. government official told lawmakers Tuesday that Nvidia Corp has shipped minimal quantities of its H200 chips to China and Hong Kong. Jeffrey Kessler, under secretary of commerce for industry and security, informed a U.S. House committee that shipments of the H200 chip have started but remain at "very few" units.

@KobeissiLetter [Tue Jul 14 15:36:00 +0000 2026]: BREAKING: DeepSeek is preparing for an IPO and may file as soon as this year, per Bloomberg. Details include: 1. The company is reportedly in talks with accounting and banking advisors and the IPO is expected to be listed in China 2. DeepSeek has begun talks for a fresh funding round valuing the company at $71 billion 3. Amid rumors of an IPO, DeepSeek is now looking to expand into the agentic AI market The AI arms race is accelerating.

@AIStockSavvy [Tue Jul 14 16:03:16 +0000 2026]: Stifel: 'Kratos $400M DoW award a positive read-through to Rocket Lab'. - $KTOS $RKLB "Kratos $400M DoW award a positive read-through to Rocket Lab. Earlier today, Kratos Defense & Security Solutions, Inc. (KTOS, $50.09, Buy - covered by our colleague Jon Siegmann) announced that it has recently received ~$400M in funding from the Department of War (DoW) related to certain hypersonic system and other National Security related programs. While details of the award were relatively sparse and there are no direct links to subcontractor awards, we nonetheless see this as a positive read-through to Rocket Lab given their direct supplier relationship with Kratos as we believe more vehicle development from Kratos could translate to incremental launch service procurement from Rocket Lab. While the $400M has been positioned by the Kratos team as funding to “accelerate organic growth, increasing operating cash receipts and reduce receivables/inventory/assets” we still see this as a potential catalyst and raises the probability for Rocket Lab to see an additional TO for its HASTE hypersonic test vehicle as incremental funding is allocated to hypersonic testing. We also see this new funding as a positive development in the context of the broader hypersonic testing environment (and confirmation of the MACH-TB 2.0 supplier chain) as is potentially de-risks the conversion of Rocket Lab’s 20 launch backlog into revenue and keeps the program on schedule."

@AIStockSavvy [Tue Jul 14 15:03:38 +0000 2026]: Kalshi: Announces Compute Forward Curves Which Are Now Live for $NVDA Nvidia B200, H200, and a100 Chips

@AIStockSavvy [Tue Jul 14 14:29:01 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: $NVDA NVIDIA, Mitsubishi heavy eye cooperation on AI data center cooling and power - Nikkei

@wallstengine [Tue Jul 14 14:34:19 +0000 2026]: CrowdStrike $CRWD shares are up nearly 9% after IBM pointed to clients facing “rapidly evolving, industry-wide cybersecurity concerns.” https://t.co/L3sfR1PWiI

@KobeissiLetter [Tue Jul 14 15:10:33 +0000 2026]: BREAKING: President Trump announces a "full blockade" on the Strait of Hormuz. Trump also says he has decided to "replace the 20% US reimbursement fee with trade and investment deals" from Gulf countries. https://t.co/pJDSPa6IA2

@StockMKTNewz [Tue Jul 14 15:00:56 +0000 2026]: JPMorgan $JPM sold $4.6 Billion shares of Visa $V stock during Q2 JPMorgan has been holding the shares since Visa's 2008 IPO https://t.co/YuCGjPXfH7

@StockMKTNewz [Tue Jul 14 14:42:33 +0000 2026]: Frontier Airlines $FRO plans to install SpaceX’s $SPCX Starlink Internet Service on its planes by early 2027 - Bloomberg https://t.co/T5fZWxvwx2

@AIStockSavvy [Tue Jul 14 15:08:38 +0000 2026]: Trump: Oil Is Flowing Like Never Before, To Replace 20% Hormuz Cargo Fee With Trade Deals - $QQQ $SPY $USO

@StockMKTNewz [Tue Jul 14 15:04:30 +0000 2026]: The 2x Long SK Hynix ETF $SKHX from my partners over at Leverage Shares has now had more than 1 Million shares traded so far today https://t.co/zzGbqkY9ns

@StockMKTNewz [Tue Jul 14 14:50:27 +0000 2026]: $IBM stock is now down by more than 25% so far today and is on pace for its worst day since at least 1968 🔴🔴🔴🔴🔴 https://t.co/KWJy2Y4a4B

@StockMKTNewz [Tue Jul 14 14:37:19 +0000 2026]: $UBER is in advanced talks to acquire German food-delivery company Delivery Hero Delivery Hero is currently worth just under $13B https://t.co/mbOG24pLCv

@wallstengine [Tue Jul 14 15:11:03 +0000 2026]: JEFFREY KESSLER CONFIRMED DURING A HEARING THAT $NVDA H200 SHIPMENTS TO CHINA HAVE TAKEN PLACE, BUT DESCRIBED THE VOLUME SHIPPED AS “TRIVIAL.”

@wallstengine [Tue Jul 14 15:05:41 +0000 2026]: SK Hynix $SKHY just hit a new all-time high, with options and leveraged products now live. $SKHX has already traded over 1 million shares. https://t.co/JLTzn2RuvD

@StockMKTNewz [Tue Jul 14 14:35:43 +0000 2026]: The AI model wars are now on

@AIStockSavvy [Tue Jul 14 14:28:37 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: DeepSeek Begins IPO Preparations, Eyes 2027 Public Debut 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐃𝐞𝐞𝐩𝐒𝐞𝐞𝐤 has begun preparations for an 𝐈𝐏𝐎, according to Bloomberg. ➤ Company is targeting a 𝐦𝐚𝐢𝐧𝐥𝐚𝐧𝐝 𝐂𝐡𝐢𝐧𝐚 IPO filing in 2026. ➤ Public market debut is planned for 𝐭𝐰𝐞𝐧𝐭𝐲-𝐭𝐰𝐞𝐧𝐭𝐲-𝐬𝐞𝐯𝐞𝐧. ➤ DeepSeek is working with 𝐚𝐜𝐜𝐨𝐮𝐧𝐭𝐢𝐧𝐠 and banking advisors. ➤ Company is seeking at least 𝐂𝐍𝐘 𝟏𝟎 𝐛𝐢𝐥𝐥𝐢𝐨𝐧 in new private funding. ➤ New funding targets a 𝐩𝐫𝐞-𝐦𝐨𝐧𝐞𝐲 𝐯𝐚𝐥𝐮𝐚𝐭𝐢𝐨𝐧 of at least 𝐂𝐍𝐘 𝟒𝟖𝟎 𝐛𝐢𝐥𝐥𝐢𝐨𝐧. ➤ Target valuation equals approximately 𝐒𝟕𝟏 𝐛𝐢𝐥𝐥𝐢𝐨𝐧. ➤ DeepSeek closed a record 𝐒𝟕 𝐛𝐢𝐥𝐥𝐢𝐨𝐧 financing round weeks earlier. ➤ IPO timing and fundraising plans remain 𝐬𝐮𝐛𝐣𝐞𝐜𝐭 𝐭𝐨 𝐜𝐡𝐚𝐧𝐠𝐞 based on conditions.

@wallstengine [Tue Jul 14 15:45:07 +0000 2026]: FED WARSH: DOLLAR LIQUIDITY SWAP LINES ARE PART OF MONETARY POLICY

@wallstengine [Tue Jul 14 15:44:18 +0000 2026]: FED WARSH: MISSION ACCOMPLISHED' IS NOT MY VIEW AFTER TODAY'S DATA DO NOT THINK AFTER TODAY'S CPI REPORT THAT EVERYTHING IS WELL

@wallstengine [Tue Jul 14 14:53:54 +0000 2026]: FED WARSH: WE DO NOT WANT TO BE IN THE BAILOUT BUSINESS WANT TO BE IN A POSITION WE AREN'T BAILING OUT ANYONE INCLUDING CRYPTO

@wallstengine [Tue Jul 14 14:38:38 +0000 2026]: FED WARSH: ANY CHANGE IN BALNACE SHEET POLICY WOULD BE PREVIEWED, EXPLAINED,

@wallstengine [Tue Jul 14 14:38:17 +0000 2026]: Fed Chair Warsh said the task forces are still in discovery mode and are starting with a blank sheet of paper. Their initial views will be shared with all 19 policymakers before a broader public discussion.

@wallstengine [Tue Jul 14 15:06:38 +0000 2026]: Trump: I have decided to replace the 20% United States Reimbursement Fee with Trade and Investment Deals that the various Gulf States will be making into the United States. Those Investments will be MASSIVE but, at the same time, extraordinarily good for them, and their future. https://t.co/Q6YXE51r29

@StockMKTNewz [Tue Jul 14 15:40:55 +0000 2026]: A Tyrannosaurus Rex named Gus just sold for $50.1M, the highest price ever paid for a dinosaur at auction - Bloomberg https://t.co/8nM4eUU0hY

@AIStockSavvy [Tue Jul 14 15:22:09 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Switch Targets $80 Billion Valuation, Switch IPO Could Happen as Early as Fourth Quarter

@wallstengine [Tue Jul 14 15:53:02 +0000 2026]: FED WARSH: I AM DOUBLING DOWN ON 2% INFLATION TARGET THIS FED WILL DELIVER 2% INFLATION BROADER PRICE STABILITY OBJECTIVE IS STILL IN THE BACK OF MY MIND, WE'LL SEE IF THERE ARE FURTHER REFORMS TO BE HAD PREPARED TO DO EVERYTHING I CAN DO ENSURE INDEPENDENT CONDUCT OF MONETARY POLICY

@wallstengine [Tue Jul 14 15:51:17 +0000 2026]: CEO Jane Fraser said the Middle East conflict has “weighed a bit on global growth” and given inflation “a second wind,” while consent-order timing is “fully at the discretion of our regulators.” The bank did not raise its 2026 ROTCE target. https://t.co/TPoGzH0KzQ

@StockMKTNewz [Tue Jul 14 15:31:00 +0000 2026]: 🇺🇸 President Trump just posted this: "I have decided to replace the 20% United States Reimbursement Fee with Trade and Investment Deals that the various Gulf States will be making into the United States." https://t.co/VSUDbrg6Wk

@wallstengine [Tue Jul 14 14:36:39 +0000 2026]: More Price cuts coming?

@wallstengine [Tue Jul 14 14:23:05 +0000 2026]: 👀

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.