אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are writing a SHORT INTRADAY UPDATE in Hebrew for a financial website. The update is a
plain-language SUMMARY of what the curated X (Twitter) sources posted in the last two hours —
00:40–02:40 שעון ישראל, on 2026-07-07 (יום שלישי) — and nothing else.
Market state right now: אחרי סגירה (after-hours) — המסחר הרגיל הסתיים היום. Never describe the market as trading or reacting when the regular
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
  "title": "עדכון ביניים מוול סטריט 🇺🇸 – יום שלישי, 7.7.2026, 02:40",
  "date": "2026-07-07",
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
tweets, for the window 00:40–02:40 Israel time on 2026-07-07. Do NOT use it to find additional news, headlines,
prices or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════

══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══
Already published on the site. Your update covers ONLY the last two hours. Mention an item below ONLY if there is a genuinely NEW development about it inside the two-hour window.

[עדכון ביניים]
* חברת Grab (GRAB): מנכ״ל Uber דארה חוסרושאהי פרש מדירקטוריון החברה. זהו שינוי ממשל תאגידי נקודתי בחברה שממוקדת בתחבורה, משלוחים ותשלומים בדרום-מזרח אסיה.
* שוק העבודה בארה״ב: אינדיקציה נוספת מצביעה על חולשה מתחת לפני השטח, כאשר הפער בין צרכנים שאומרים שמשרות זמינות בשפע לבין כאלה שאומרים שקשה למצוא עבודה ירד ביוני ל-2.4 נקודות, הרמה הנמוכה מאז 2020. רק 24.9% אמרו שמשרות זמינות בשפע, מול 22.5% שאמרו שקשה למצוא עבודה, והמדד מצביע על סיכון לעלייה באבטלה עד 6.0% לעומת 4.2% כיום.
* קרנות האנרגיה: נרשמה האצה ביציאת כספים מהסקטור, עם פדיונות של 3.2 מיליארד דולר מקרנות אנרגיה בשבוע שהסתיים ב-1 ביולי. זו המשיכה השבועית הגדולה מאז יולי 2024 והשנייה בגודלה בעשור לפחות, והממוצע ל-4 שבועות עבר ליציאות של 1.8 מיליארד דולר אחרי כניסות של 2.5 מיליארד דולר רק לפני חודשיים.
* קרן Appaloosa: לפי Bloomberg, הקרן של דיוויד טפר הניבה תשואה של 32% במחצית הראשונה של השנה. הקרן מנהלת 23 מיליארד דולר, וכל התשואה נוצרה ברבעון השני.
* Millennium Management: שתי יחידות מסחר סביב איזוני מדדים הרוויחו כ-3.7 מיליארד דולר. Millennium עלתה 4.1% ביוני ותשואתה מתחילת השנה עומדת על 10.5%, כאשר הצוותים ייצרו יותר ממחצית מהרווח החודשי לפני עמלות, כ-6.6 מיליארד דולר.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-07. Never mention in the review that these came from tweets/posts:

@wallstengine [Mon Jul 06 23:27:47 +0000 2026]: Syntiant, an Intel and Microsoft-backed edge-AI chip/software maker, filed for IPO. The company makes ultra-low-power AI chips and software for on-device AI in earbuds, wearables, and industrial systems. Q1 results: Revenue: $64.5M vs $66.6M YoY Net loss: $26.2M vs $16.8M YoY Syntiant has raised $311M to date and was valued at $646.4M after its Dec. 2024 round. Expected Nasdaq ticker: $SYTN

@StockMKTNewz [Mon Jul 06 21:57:55 +0000 2026]: Rivian $RIVN is offering to sell 75 million shares as the EV vehicle company seeks to fund equity contributions related to a US Department of Energy loan Rivian basically erased all of its gains from the day https://t.co/Zm0WfgsIFZ

@AIStockSavvy [Mon Jul 06 23:05:13 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Large Banks Held Preliminary Discussions to Acquire a Network From Fiserv That Could Allow Them to Bypass Federal Debit-Card Fee Caps - WSJ - $BAC $JPM $FISV

@AIStockSavvy [Mon Jul 06 22:55:46 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: Samsung Reports Preliminary Q2 Results, Profit Beats Estimates - $MU $SNDK 👉 𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬: ➤ 𝐒𝐚𝐦𝐬𝐮𝐧𝐠 reported preliminary Q2 revenue of 𝟏𝟕𝟏 𝐭𝐫𝐢𝐥𝐥𝐢𝐨𝐧 𝐰𝐨𝐧. ➤ Q2 revenue missed the 𝟏𝟕𝟑.𝟗 𝐭𝐫𝐢𝐥𝐥𝐢𝐨𝐧 𝐰𝐨𝐧 consensus estimate. ➤ Q2 operating profit reached 𝟖𝟗.𝟒 𝐭𝐫𝐢𝐥𝐥𝐢𝐨𝐧 𝐰𝐨𝐧. ➤ Operating profit exceeded the 𝟖𝟕.𝟑 𝐭𝐫𝐢𝐥𝐥𝐢𝐨𝐧 𝐰𝐨𝐧 consensus forecast. ➤ Q1 revenue was 𝟏𝟑𝟑.𝟗 𝐭𝐫𝐢𝐥𝐥𝐢𝐨𝐧 𝐰𝐨𝐧, with operating profit of 𝟓𝟕.𝟐 𝐭𝐫𝐢𝐥𝐥𝐢𝐨𝐧 𝐰𝐨𝐧. ➤ Year-ago Q2 revenue was 𝟕𝟒.𝟔 𝐭𝐫𝐢𝐥𝐥𝐢𝐨𝐧 𝐰𝐨𝐧. ➤ Year-ago Q2 operating profit was 𝟒.𝟕 𝐭𝐫𝐢𝐥𝐥𝐢𝐨𝐧 𝐰𝐨𝐧. 👉 𝐖𝐡𝐲 𝐈𝐭 𝐌𝐚𝐭𝐭𝐞𝐫𝐬: ➤ Profit beat suggests stronger 𝐨𝐩𝐞𝐫𝐚𝐭𝐢𝐧𝐠 performance despite softer-than-expected sales. ➤ Results offer insight into demand trends across Samsung's 𝐜𝐡𝐢𝐩 and electronics businesses. ➤ The earnings may influence investor expectations for Samsung's 𝐬𝐞𝐜𝐨𝐧𝐝-𝐡𝐚𝐥𝐟 performance

@KobeissiLetter [Mon Jul 06 21:58:39 +0000 2026]: Foreign debt demand is no longer keeping up with America's growing debt: Foreign official holdings of US Treasuries are down to 12.5% of total Treasuries outstanding, the lowest this century. This percentage has declined -24 points since the 2009 peak. Over this period, marketable US Treasury debt has surged +$23 trillion, or +379%, to $29.1 trillion, near an all-time high. At the same time, US Treasuries held by foreign government entities have increased by just +$1.5 trillion, or +63%, to ~$3.9 trillion. China's Treasury holdings have more than halved, to $651.1 billion, the lowest since September 2008. The US is issuing record levels of debt.

@wallstengine [Mon Jul 06 21:45:32 +0000 2026]: Vertex Pharmaceuticals $VRTX agreed to buy Crinetics Pharmaceuticals $CRNX for $10B cash, expanding into endocrinology. Deal price: $85/share, a 102% premium to Crinetics’ prior close. Crinetics’ lead drug, Palsonify, targets acromegaly, with another program in congenital adrenal hyperplasia. Vertex says the assets could generate over $5B in peak annual revenue. Deal expected to close in Q3.

@StockMKTNewz [Mon Jul 06 22:41:29 +0000 2026]: Leopold Aschenbrenner is looking to invest in the SK Hynix IPO https://t.co/CdPDkzi1rT

@wallstengine [Mon Jul 06 22:39:23 +0000 2026]: Texas Stock Exchange has started its phased trading rollout in Dallas. Initial activity runs through test symbols from July 6-9, with live trading in select securities scheduled to begin July 10. Broader symbol rollout is expected through July. TXSE expects ETP listings in September, corporate listings in October, and IPOs in 2027 The exchange is backed by major firms including BlackRock, Citadel Securities, Charles Schwab, and JPMorgan, with more than $250M raised.

@StockMKTNewz [Mon Jul 06 22:51:14 +0000 2026]: THE TEXAS STOCK EXCHANGE IS HERE The Texas Stock Exchange officially began operating today with some test trades Live stock trading is expected to begin Friday with a small group of securities https://t.co/G2sQwXG0V0

@wallstengine [Mon Jul 06 22:45:52 +0000 2026]: SAMSUNG ELECTRONICS REPORTED Q2 OPERATING PROFIT OF ABOUT $57.6 BILLION, ABOVE THE ~$55.6 BILLION ESTIMATE.

@KobeissiLetter [Mon Jul 06 22:50:57 +0000 2026]: Stress in the US private credit market is intensifying: Investors requested a record -$15.6 billion in redemptions from private credit funds in Q2 2026. This marks the 3rd consecutive quarterly increase by a total of +$13 billion, or +500%. Furthermore, just 38% of these requests were met, down from 53% in Q1 2026, leaving $9.7 billion in unmet redemptions, the largest backlog on record. Blue Owl's flagship fund, Blue Owl Credit Income, was the most impacted at 19% of shares outstanding, with 14% unmet, the highest redemption rate among its large competitors. This was followed by Apollo, at 16% requested with 11% unmet, and Ares, at 14% requested with 9% unmet. Meanwhile, inflows into the private credit industry declined -75% since January to ~$500 million in May, the smallest monthly intake in at least 18 months. The private credit crisis shows no signs of slowing.

@StockMKTNewz [Mon Jul 06 21:43:50 +0000 2026]: There is a 75% chance that Anthropic goes public this year according to Polymarket traders https://t.co/nwBFG0Z2Vl

@wallstengine [Mon Jul 06 23:16:35 +0000 2026]: Samsung Electronics prelim Q2 operating profit surged 19x YoY to ~$58.4B, above $55.3B consensus, on AI memory demand. However, prelim Q2 revenue came in slightly shy at ~$111.8B, vs $113.1B consensus, though still up 129% YoY. https://t.co/7YFzWAOSMl

@wallstengine [Mon Jul 06 21:56:48 +0000 2026]: Kid: “mom, how did we get so rich?” Mom: “your father and i ordered $25 of snacks on gopuff during the gold bar promo” https://t.co/zgiDqTVErF

@StockMKTNewz [Mon Jul 06 23:07:00 +0000 2026]: Samsung's quarterly profit has increased by 19x The world’s largest memory maker reported preliminary operating income of $58 billion in the three months through June, dwarfing its performance for all of 2025 Samsung is expected to release a full financial statement around the end of the month - Bloomberg

@wallstengine [Mon Jul 06 22:21:56 +0000 2026]: Here’s what each LLM portfolio looks like in @ralliesarena https://t.co/cYW0EACYu6

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.