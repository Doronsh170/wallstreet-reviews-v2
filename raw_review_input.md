אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are writing a SHORT INTRADAY UPDATE in Hebrew for a financial website. The update is a
plain-language SUMMARY of what the curated X (Twitter) sources posted in the last two hours —
18:27–20:27 שעון ישראל, on 2026-07-10 (יום שישי) — and nothing else.
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
  "title": "עדכון ביניים מוול סטריט 🇺🇸 – יום שישי, 10.7.2026, 20:27",
  "date": "2026-07-10",
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
tweets, for the window 18:27–20:27 Israel time on 2026-07-10. Do NOT use it to find additional news, headlines,
prices or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════

══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══
Already published on the site. Your update covers ONLY the last two hours. Mention an item below ONLY if there is a genuinely NEW development about it inside the two-hour window.

[נקודות מרכזיות]
* מומנטום השבבים מול זהירות לפני הפתיחה: וול סטריט נכנסת ליום המסחר האחרון של השבוע כשהשאלה המרכזית היא אם ראלי הטכנולוגיה והזיכרון ישמור על הקצב, על רקע נסיגה במחירי הנפט שממתנת את חששות האינפלציה ומול מתיחות גיאופוליטית מתחדשת מול איראן. היומן הכלכלי דל היום ונטול נתוני מאקרו כבדים, ולכן הזרקורים יופנו לסיפורי המניות, לפתיחת המסחר במניית SK Hynix ולתגובת השוק להתפתחויות סביב טהרן. הסנטימנט נותר תומך אך זהיר, כשהמשקיעים בוחנים אם הריכוזיות הגבוהה בענקיות הטכנולוגיה תמשיך להוביל את המדדים.
* יומן מאקרו דל ודלתא פותחת את הדוחות: הלוח הכלכלי היום דליל, כשתשומת הלב מופנית לדוח הנפט החודשי של סוכנות האנרגיה הבינלאומית (IEA) שיתפרסם סביב 11:00 שעון ישראל ולנתוני מספר אסדות הקידוח של בייקר יוז ב-20:00. בחזית הדוחות, חברת התעופה דלתא (DAL) תדווח לפני הפתיחה בסביבות 13:30 שעון ישראל ותספק אינדיקציה ראשונה לבריאות הצריכה והתעופה לקראת עונת הדוחות. בהיעדר זרז מאקרו, כיוון המסחר יוכתב בעיקר מהמומנטום הסקטוריאלי ומחדשות החברות.
* הנפקת SK Hynix יוצאת לדרך: מניית יצרנית הזיכרון הקוריאנית SK Hynix צפויה להתחיל להיסחר היום תחת הטיקר הזמני SKHYV, לפני מעבר לטיקר הקבוע SKHY בתחילת השבוע הבא, בהנפקת ADR שמשכה ביקושים אדירים של קרוב ל-200 מיליארד דולר ומעל 500 משקיעים. החברה עדכנה כי תגייס כ-40 טריליון וון (כ-26.5 מיליארד דולר), מעט פחות מיעד קודם של 43 טריליון וון. עבור המשקיעים זהו מבחן חי לתיאבון סביב מחזור הזיכרון, שממשיך להזין את מניות מיקרון (MU) וסאנדיסק (SNDK) ואת מגזר השבבים כולו.
* מניית מטא (META): דיווח של פייננשל טיימס חושף כי טנסנט מנהלת מגעים להפוך לבעלת המניות הגדולה בחברת מאנוס (Manus), בעוד משקיעים ממהרים לפרק את הרכישה של מאנוס בידי מטא בשווי כ-2 מיליארד דולר. במקביל, קרן ARK של קאתי ווד הוסיפה כ-34 אלף מניות מטא, המשך להתעניינות הגוברת בחברה על רקע מרוץ ה-AI וההשקעות שלה בתשתיות המחשוב. המשקיעים יבחנו אם הסיבוב סביב מאנוס מסמן שינוי באסטרטגיית הרכישות של החברה.
* גל קניות שיא של בכירי הטכנולוגיה: לפי נתוני SentimenTrader, 28 מנהלים בכירים בחברות מגזר הטכנולוגיה רכשו בחצי השנה האחרונה מניות של החברות שלהם עצמם בשוק הפתוח, המספר הגבוה ביותר שנרשם אי פעם ויותר מכפול לעומת תחילת 2026. הנתון עוקף את השיא הקודם של 25 מנהלים שנקבע ב-2011, בעוד בתחילת 2025 נמנו חמישה קונים בלבד. קניות מסיביות של מקורבים נחשבות לרוב לאות אמון פנימי בהמשך העליות, והן מספקות רוח גבית סנטימנטלית למגזר שמוביל את השוק.
* מתיחות מול איראן וזרקור על הנפט: על פי דיווח ב-וול סטריט ג'ורנל, ישראל העבירה לארה"ב מודיעין חדש לפיו איראן עשויה לשקול מזימה לפגוע בנשיא טראמפ, התפתחות שמחדדת את סיכון הזנב הגיאופוליטי אחרי שהנפט כבר נסוג בחדות מרמות השיא של תחילת השבוע. במקביל, יצוא מוצרי הנפט של ארה"ב ירד לשיא של כ-8.7 מיליון חביות ביום, עדות לביקוש עולמי חזק לדלק אמריקאי. השילוב בין הרגעת מחירים לבין סיכון גיאופוליטי חי הופך את דוח ה-IEA ואת ההתפתחויות סביב טהרן לגורם מפתח בכיוון האנרגיה היום.
* גל המלצות קנייה בטכנולוגיה: בית ההשקעות Stifel המשיך לתדלק את הסנטימנט החיובי עם שדרוג של מניית טוויליו (TWLO) להמלצת קנייה והעלאת מחיר היעד ל-260 דולר מ-175 דולר, בטענה שהחברה ממוצבת היטב לגל ה-AI הסוכני (agentic) דרך פלטפורמת התקשורת שלה. באותה נשימה שדרג הבית גם את מניית שופיפיי (SHOP) להמלצת קנייה עם יעד של 150 דולר, בהצביעו על נתיב ריאלי לצמיחת הכנסות של מעל 30% ב-2026. ההמלצות מצטרפות לזרם החיובי סביב מניות הצמיחה ומחזקות את נרטיב ה-AI כמנוע המרכזי של השוק.
* שורה תחתונה: את כיוון יום המסחר האחרון של השבוע יכריעו בעיקר המשך המומנטום במניות השבבים והזיכרון, ובראשם קבלת הפנים להנפקת SK Hynix, לצד תגובת השוק להתפתחויות הגיאופוליטיות מול איראן והשפעתן על הנפט. בהיעדר נתוני מאקרו כבדים, דוח דלתא וזרם ההמלצות בטכנולוגיה יספקו את הטון, כשהריכוזיות הגבוהה בענקיות ממשיכה להפוך כל תפנית בהן לקריטית עבור המדדים כולם.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-10. Never mention in the review that these came from tweets/posts:

@KobeissiLetter [Fri Jul 10 15:50:01 +0000 2026]: BREAKING: SK Hynix stock, South Korea’s second most valuable company, officially debuts on the Nasdaq and surges +14% at the open, now worth over $1 trillion. The company’s ADRs were priced at $149/share, raising $26.5 billion. https://t.co/BDUARtVkTi

@wallstengine [Fri Jul 10 15:36:44 +0000 2026]: SK HYNIX OPENS UP 14% AT $170, IPO AT $149 $SKHYV $SKHY

@wallstengine [Fri Jul 10 15:50:47 +0000 2026]: Nearly 50 million shares have already traded. $SKHYV $SKHY https://t.co/csb25BvepG

@AIStockSavvy [Fri Jul 10 15:34:40 +0000 2026]: 📢 𝐉𝐔𝐒𝐓 𝐈𝐍: U.S. and Iran are expected to hold a new round of talks next week, possibly in Switzerland. - Axios - $QQQ $SPY $USO

@AIStockSavvy [Fri Jul 10 15:48:39 +0000 2026]: SK Hynix opens at $170 in U.S. debut; IPO price $149 SK Hynix opened at $170 per American depositary receipt (ADR) in its U.S. debut, up 14% from the $149 IPO price; shares climbed to $174 within minutes. Trading under temporary ticker SKHYV, the ADR offering raised $26.51 billion, the largest equity issuance ever by a non-U.S. company, underscoring investor appetite for firms positioned to benefit from the AI boom.

@StockMKTNewz [Fri Jul 10 15:49:34 +0000 2026]: SK Hynix is now a public company https://t.co/vDQbEeVlOY

@StockMKTNewz [Fri Jul 10 16:41:25 +0000 2026]: SK Hynix stock has now had 69 Million shares traded so far in its US Debut https://t.co/p0oXrZ0Rml

@StockMKTNewz [Fri Jul 10 15:42:18 +0000 2026]: SK Hynix has started trading

@wallstengine [Fri Jul 10 17:19:24 +0000 2026]: DELTA CEO SAYS FLIERS CAN AFFORD THESE HIGHER FARES - WSJ

@wallstengine [Fri Jul 10 16:13:25 +0000 2026]: ELON MUSK POSTPONES CNBC INTERVIEW https://t.co/Jrr9O8uQox

@StockMKTNewz [Fri Jul 10 17:22:24 +0000 2026]: RT @WOLF_Financial: SPECIAL ALL DAY LIVE STREAM The SK Hynix US IPO is HERE https://t.co/v07DKn4DJ2

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.