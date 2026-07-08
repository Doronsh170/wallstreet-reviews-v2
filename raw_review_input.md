אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are writing a SHORT INTRADAY UPDATE in Hebrew for a financial website. The update is a
plain-language SUMMARY of what the curated X (Twitter) sources posted in the last two hours —
11:23–13:23 שעון ישראל, on 2026-07-08 (יום רביעי) — and nothing else.
Market state right now: טרום מסחר (pre-market) — השוק טרם נפתח היום. Never describe the market as trading or reacting when the regular
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
  "title": "עדכון ביניים מוול סטריט 🇺🇸 – יום רביעי, 8.7.2026, 13:23",
  "date": "2026-07-08",
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
tweets, for the window 11:23–13:23 Israel time on 2026-07-08. Do NOT use it to find additional news, headlines,
prices or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════

══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══
Already published on the site. Your update covers ONLY the last two hours. Mention an item below ONLY if there is a genuinely NEW development about it inside the two-hour window.

[נקודות מרכזיות]
* סנטימנט זהיר ומוטה סיכון בפתיחה: וול סטריט צפויה להיפתח תחת ענן גיאופוליטי כבד אחרי שהצבא האמריקאי פתח בלילה בגל מתקפות נגד יעדים באיראן, ואיראן הגיבה בהאשמה שהמהלך מפר את מזכר ההבנות בין המדינות. הזרם אל נכסי המקלט ואל סחורות האנרגיה מכתיב את מצב הרוח, והמשקיעים יעקבו אחר השאלה אם ההסלמה תתרחב לפני פרסום פרוטוקול ה-Fed בהמשך היום. בסביבה כזו הרוטציה מהצמיחה אל הסקטורים הדפנסיביים עלולה להימשך גם היום.
* פרוטוקול ה-Fed במוקד היום: בשעה 21:00 שעון ישראל יפורסם פרוטוקול ישיבת הריבית האחרונה של הפדרל ריזרב, והוא צפוי להיות אירוע המאקרו המרכזי של המסחר בהיעדר נתון כלכלי כבד אחר בלוח. המשקיעים יחפשו בו רמזים לקצב הורדות הריבית ולמידת חילוקי הדעות בין חברי הוועדה. על רקע קפיצת מחירי הנפט והחשש מאינפלציית אנרגיה מתחדשת, כל נימה נצית בפרוטוקול עלולה להכביד על מניות הצמיחה שכבר נמצאות בלחץ.
* ההסלמה מול איראן דוחפת את הנפט: מחירי הנפט ממשיכים לטפס בחדות על רקע המשבר במפרץ הפרסי, כשה-WTI מוסיף כ-4.4% והברנט מזנק כ-5% אל מעל 76 דולר לחבית, לאחר שארה"ב ביטלה את רישיון הייצוא של איראן והחלה בתקיפות. מיצר הורמוז מעביר כחמישית מצריכת הנפט העולמית, ולכן כל החרפה נוספת בשיט בו מתורגמת מיידית לפרמיית סיכון על האנרגיה ולבריחה מנכסי צמיחה. השאלה המרכזית להיום היא אם גל התקיפות האמריקאי יתרחב או יתפוגג, שכן זה הגורם שיכתיב את כיוון הנפט ואת תיאבון הסיכון.
* שרשרת האספקה של ה-AI ממשיכה לרכז עניין: סביב מניות השבבים נמשכת זרימת חדשות חיובית שמנוגדת לחולשת המחירים בימים האחרונים. סמסונג החלה בייצור המוני של כונן האחסון המתקדם שלה שישולב בפלטפורמת Vera Rubin הקרובה של אנבידיה, אנבידיה מדווחת כי היא משלבת חומרה עם הסטארטאפ D-Matrix במערכת חדשה להרצת מודלים, ו-SK Hynix צפויה להכנסות של כ-231 מיליארד דולר השנה לעומת 67 מיליארד אשתקד. מניית אנבידיה (NVDA) עלתה במתינות של 0.71%, אך עוצמת הביקושים לתשתית ה-AI נותרת הסיפור המבני שמזין את המגזר.
* מניית ספייס-אקס (SPCX): עם תום תקופת השקט שלאחר ההנפקה פרסמה וול סטריט את גל יעדי המחיר הראשון שלה למניה, וטווח ההערכות חושף פערים דרמטיים בין האנליסטים. ריימונד ג'יימס הציב יעד של 800 דולר, שגלום בו שווי של כ-10 טריליון דולר, בעוד יתר היעדים נעים סביב 200 עד 300 דולר, זאת מול מחיר נוכחי של כ-150 דולר. למרות ההתלהבות והדיווח שקאתי ווד וקרן ARK רכשו כ-44 אלף מניות, המניה עצמה ירדה 6.83% ונסחפה עם החולשה הרוחבית במניות הצמיחה.
* מניית פינגווין סולושנס (PENG): החברה פרסמה דוחות רבעון שלישי חזקים במיוחד, עם הכנסות שיא של 478.7 מיליון דולר מול צפי של 421.4 מיליון, רווח מתואם למניה של 0.84 דולר מול צפי של 0.56 דולר, והעלאת תחזית הרווח השנתית ל-2.60 דולר למניה. הצמיחה הובלה על ידי זינוק של 111% בהכנסות הזיכרון המשולב על רקע ביקושי ה-AI. למרות התוצאות המרשימות המניה ירדה 7.38%, עדות לרף הציפיות הגבוה שהשוק מציב כעת בפני מניות ה-AI.
* מניית מטא (META): החברה משיקה את Muse Image, מודל יצירת התמונות הראשון שלה ממעבדות Meta Superintelligence Labs, במהלך שממצב אותה בחזית מרוץ ה-AI הגנרטיבי מול OpenAI וגוגל. המניה בלטה לחיוב עם עלייה של 2.55% והייתה מהבודדות בקבוצת המגה-קאפ הטכנולוגית שהתנתקו מהסנטימנט השלילי שרבץ על המגזר. עבור המשקיעים זהו אות נוסף לכך שמטא ממירה את השקעות ה-AI הכבדות שלה למוצרים ממשיים.
* שורה תחתונה: כיוון המסחר היום ייקבע בצומת של שני כוחות, ההתפתחויות במפרץ הפרסי שיכתיבו את מחיר הנפט ואת מפלס החשש, ופרוטוקול ה-Fed ב-21:00 שעון ישראל שיאותת על נתיב הריבית. כל עוד ההסלמה נמשכת והנפט מזנק, הלחץ על מניות הצמיחה והטכנולוגיה עלול להימשך, בעוד סקטור האנרגיה והנכסים הדפנסיביים ממשיכים ליהנות מהבריחה מסיכון.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-08. Never mention in the review that these came from tweets/posts:

@wallstengine [Wed Jul 08 09:07:27 +0000 2026]: Raymond James Upgrades $DLTR to Outperform from Market Perform, PT $140 Analyst comments: "We are upgrading Dollar Tree to Outperform and establishing a $140 price target, reflecting what we view as an increasingly favorable risk/reward setup. In our view, FY26 EPS guidance of $6.70-$7.10 embeds a conservative set of assumptions, including elevated fuel costs through year-end, no benefit from tariff refunds or any associated comparable-sales demand drivers, and no incremental share repurchases. We believe each of these assumptions is tracking more favorably than guidance implies, creating multiple avenues for upside and increasing the likelihood of estimate revisions. Our upgrade is not predicated on imminent traffic recovery in F2Q, with recent traffic and credit card data mixed against a difficult comparison, although traffic could turn positive in F2H as prior-year comparisons ease. Rather, our more constructive stance reflects our view that the full-year guidance framework is de-risked from a profit and loss perspective. Our upgrade is based on five key factors: (1) several headwinds embedded in FY26 guidance are easing or beginning to reverse; (2) operational execution continues to improve, with further runway ahead through Gold Store standards progress; (3) tariff refunds, excluded from guidance, provide management with incremental flexibility to reinvest in the business flywheel; (4) traffic trends should improve sequentially in F2H as comparisons ease and traffic-driving initiatives gain further traction; and (5) the current valuation does not fully reflect the improving earnings trajectory of the business." Analyst: Bobby Griffin

@wallstengine [Wed Jul 08 09:11:20 +0000 2026]: Evercore ISI Upgrades $OXY to Outperform from Underperform, Raises PT to $65 from $58 Analyst comments: "We are upgrading Occidental Petroleum from Underperform to Outperform and raising our price target to $65 from $58. After a prolonged stretch of underperformance versus both crude and the large-cap E&P group, we think two developments now allow OXY to better reflect underlying commodity fundamentals: a materially de-levered balance sheet and a structural step-up in capital efficiency that together reshape the free-cash-flow profile and the path back to shareholder returns. We do not make this call on absolute growth. On a flat $75 WTI deck and flat volumes, we model an ~8% FCF/share CAGR through 2030, below the ~20% we see at CVX, COP, EOG, and FANG. Rather, the call is about rate of change and a closing valuation discount: OXY is inflecting off a depressed, deeply discounted base, and we think the market is under-crediting both the durability of the efficiency gains and the simplification of a capital structure that has long capped common equity leverage to oil. Lower well costs and a strategically shallower base decline reduce maintenance capital over time, which flattens and lifts free cash flow and supports a restart of buybacks around the back half of 2028E. A disciplined, self-help posture also fits the current backdrop, where we see ongoing geopolitical volatility in crude and more friction across hydrocarbon supply chains. Finally, OXY carries one of the deeper, longer-duration resource positions among large-cap peers, spanning domestic onshore, EOR, and the Gulf of America, alongside differentiated footholds in the Persian Gulf." Analyst: Stephen Richardson

@wallstengine [Wed Jul 08 09:35:26 +0000 2026]: Morgan Stanley reiterated Rocket Lab at Overweight with a $105 price target and raised its bull case to $293 from $185, citing the Iridium acquisition, launch and connectivity upside, and $RKLB’s move toward a more vertically integrated space platform. https://t.co/iaQT6f0wAG

@wallstengine [Wed Jul 08 09:01:31 +0000 2026]: Morgan Stanley Downgrades $LMND to Equalweight from Overweight, PT at $75 Analyst comments: "Over the past month, Lemonade rose ~50%. While we continue to believe in Lemonade's strong momentum, especially its tech-enabled growth and underwriting, we will step to the sidelines as we wait for the next major catalyst to emerge. As such, we downgrade the stock to Equalweight. The investment thesis still centers on: (1) the path to profitability and (2) durable long-term growth. From this perspective, the company appears well positioned for net income profitability exiting 2027. How it competes and navigates a softening auto insurance market will be critical to the broader growth story. The stock trades at ~4.4x 2027e EV/Sales versus our price target's implied ~4.2x. We believe the current valuation now largely reflects the positive growth catalysts. We expect ~35%/~30% gross written premium growth in 2026e/2027e and adjusted EBITDA of ~$(26)m/~$66m in 2026e/2027e, respectively. We maintain our $75/share price target." Analyst: Bob Huang

@wallstengine [Wed Jul 08 10:09:08 +0000 2026]: Jefferies analyst John Hecht upgraded PROG Holdings $PRG from Hold to Buy with a price target of $60 from $33

@wallstengine [Wed Jul 08 10:05:02 +0000 2026]: Apple announced a multiyear Broadcom $AVGO deal worth over $30B to design and produce custom silicon and wireless tech for Apple products. The agreement covers 15B+ U.S.-made chips, with Broadcom investing $1.5B to expand its Fort Collins, Colorado facility. https://t.co/6IAePQtVLu

@wallstengine [Wed Jul 08 09:47:03 +0000 2026]: Needham Reiterates Buy Rating on $FIGR, PT $55; Top Idea Analyst comments: "Figure recently provided strong June key operating metrics, with consumer loan marketplace volume coming in at $1.519 billion, up 155% Y/Y and well above our $1.357 billion estimate. This brings total 2Q marketplace volume to $4.259 billion, beating the high end of the $3.4-$4.1 billion guidance range. We believe the upside is due to good underlying macro conditions for HELOCs, strong performance of the underlying assets, and an ongoing focus on execution and diversification in the capital markets. We are raising our estimates and believe there is further room for upside as additional asset classes, including auto, SMB, and RTL/DSCR loans, continue to become bigger pieces of the story. We are reiterating our Buy rating and $55 target. FIGR remains our Conviction List idea." Analyst: Kyle Peterson

@wallstengine [Wed Jul 08 08:40:17 +0000 2026]: Apple lost its EU 🇪🇺 General Court challenge over DMA rules applying to the App Store and iOS. The court upheld Apple’s gatekeeper designation for both services and dismissed its iMessage claim. $AAPL is separately fighting a €500M App Store fine. https://t.co/nM7by4S1Uf

@wallstengine [Wed Jul 08 10:04:20 +0000 2026]: Salesforce $CRM: The U.S. Air Force’s 441st VSCOS is using Missionforce to manage a $13.5B fleet of 84,000+ vehicles across nearly 389 locations worldwide. The platform has processed 51,000+ asset movement requests and cut contingency inventory checks from days to minutes.

@wallstengine [Wed Jul 08 09:23:04 +0000 2026]: Alibaba $BABA shares jumped the most in 10 months after reports of a pre-earnings update showing narrower instant-commerce losses and steady profitability in the June quarter. https://t.co/N8x9fSgMWM

@wallstengine [Wed Jul 08 10:02:22 +0000 2026]: $COTY will receive $400M to exit its Gucci beauty license one year early, clearing the way for L’Oréal to start selling Gucci beauty products in July 2027 under a 50-year deal. L’Oréal will cover about 70% of the early redemption cost. https://t.co/z23tvgs50X

@wallstengine [Wed Jul 08 09:54:05 +0000 2026]: Citi added four names to its Catalyst Call List. Intuitive Surgical $ISRG, Charles River Laboratories $CRL and GE HealthCare $GEHC were added to its 90-day upside catalyst watch. Haemonetics $HAE was added to its 90-day downside catalyst watch.

@gurgavin [Wed Jul 08 09:16:40 +0000 2026]: FUTURES UPDATE S&amp;P 500 DOWN 1.1% 📉 DOW JONES DOWN 1.4% 📉 NASDAQ 100 DOWN 1.6% 📉

@wallstengine [Wed Jul 08 08:32:37 +0000 2026]: OIL IS SPIKING AFTER TRUMP SAID HE THINKS THE IRAN CEASEFIRE IS OVER. https://t.co/xJnyHTR1EI

@KobeissiLetter [Wed Jul 08 10:21:32 +0000 2026]: BREAKING: Brent crude oil prices surge toward $79/barrel after President Trump says the ceasefire with Iran is “over.” https://t.co/jIjU2Bmh37

@KobeissiLetter [Wed Jul 08 10:18:23 +0000 2026]: BREAKING: President Trump says the ceasefire with Iran is "over." "I don't want to deal with them anymore, they are scum," Trump says. https://t.co/laHQdRKZUV

@wallstengine [Wed Jul 08 08:45:35 +0000 2026]: SOUTH KOREA’S 🇰🇷 KOSPI HAS ENTERED A BEAR MARKET, FALLING 20% FROM ITS JUNE 19 HIGH. https://t.co/rLk3e79wtD

@wallstengine [Wed Jul 08 09:41:41 +0000 2026]: Mercedes-Benz Q2 global deliveries fell 8% YoY as China slumped 30%, with the property crisis weighing on luxury-car demand. North America rose 13%, while fully electric deliveries jumped 51% on strong European demand. https://t.co/E18yOgpJf0

@wallstengine [Wed Jul 08 08:50:42 +0000 2026]: Global nuclear capacity is projected to rise 44% over the next decade to 535 GW by 2036, from 372 GW last year. China had 59 GW under construction at end-2025 and is on track to reach 102 GW by 2030, passing the U.S. https://t.co/r5LbphlNxB

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.