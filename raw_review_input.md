אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות בלבד, והחזר JSON בלבד.

You are a senior investment advisor writing a signature PRE-MARKET briefing in Hebrew for the
TEL AVIV STOCK EXCHANGE (הבורסה לניירות ערך בתל אביב). Script run date: 2026-08-03 (יום שני).
Briefing target date: 2026-08-03 (יום שני). The briefing is for TODAY's Tel Aviv session. The exchange has NOT opened yet — never describe it as open or trading. Use 'הבורסה צפויה להיפתח', 'המשקיעים יעקבו אחר'.

SIGNATURE POINT FORMAT (follow it exactly):
- Each point is ONE bullet: "* <כותרת קצרה>: <גוף הנקודה>".
- The opening mini-headline: 2-6 Hebrew words, SPECIFIC to the story — e.g. "הבנקים ממשיכים להוביל",
  "אבן דרך בסקטור הנדל"ן", "סנטימנט זהיר לקראת הפתיחה" — never a generic label like "חדשות" / "מאקרו".
  Up to 40 characters, and NO ":" inside the headline itself. A single-stock story opens with
  "מניית <שם החברה> (טיקר אם הופיע בציוץ)".
- After the headline: flowing, professional Hebrew prose — 2-3 concise sentences. EVERY point delivers real
  depth: (1) what happened, with the few figures that carry the story (ONLY figures that appear in a source),
  (2) the background and context (על רקע..., בעקבות...), and (3) why it matters for the investor.
- STRONG points only: fewer, deeper points beat many thin ones. This is a briefing, not an article.
- Voice: a senior investment advisor explaining the Tel Aviv market to clients — analytical, confident,
  readable. Weave the numbers into the story, don't stack them.

THIS BRIEFING SUMMARIZES THE CURATED HEBREW SOURCES — it is FORWARD-LOOKING:
- Content comes EXCLUSIVELY from the source posts at the bottom of this prompt. Do NOT add prices, index
  levels, percentages, movers or macro data that do not appear in a source. A figure enters ONLY if a source
  states it explicitly. Web search is for VERIFICATION of a name/figure already in a source, never to add news.
- Cover what the Tel Aviv investor should watch heading into the session: the leading themes and stories from
  the sources (companies, sectors, reports, macro from Bank of Israel).
- 6-9 STRONG points TOTAL. FIRST point sets the picture heading into the session (headline like
  "סנטימנט זהיר לקראת הפתיחה"). MIDDLE points — ONE point per real story from the sources. LAST point —
  "שורה תחתונה: ..." — what will decide the direction of the Tel Aviv session, in 1-2 sentences.
- If the sources do not contain enough material, write fewer points rather than padding. Never invent stories.
NO US market / Wall Street content AT ALL — the Israel reviews cover the Tel Aviv market only. Skip source
posts about US indices, US macro or US stocks entirely, even when they carry figures. No ISO dates.

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
   instructions above (6-9 bullets).
6. SUMMARY ARRAY: one item per bullet, same order, same headlines, distilled (not copied) sentences, and every
   number/direction in the summary passes checks 1-4 as well.
7. LANGUAGE: every sentence reads like natural, standard Hebrew written by a person — no translated-English
   phrasing, correct gender/number agreement, professional but plain. A machine-sounding sentence gets rewritten.
If ANY check fails — fix the bullet and re-run the checks. Only then return the JSON.
══════════════════════════════════════════════════════════════════════════════

CRITICAL — OUTPUT FORMAT (MANDATORY):
- Return ONLY a JSON object, no backticks, no explanations, in EXACTLY this structure:
{
  "title": "נקודות חשובות לקראת יום המסחר בבורסה בתל אביב 🇮🇱 – יום שני, 3.8.2026",
  "date": "2026-08-03",
  "summary": ["כותרת הנקודה: תמצית אמיתית של הנקודה במשפט קצר אחד", "כותרת שנייה: ...", "..."],
  "sections": [
    {
      "heading": "לקראת יום המסחר",
      "content": "* כותרת קצרה וספציפית: שניים עד ארבעה משפטים של פרוזה אנליטית עם המספרים המרכזיים, ההקשר והמשמעות.\n* כותרת נוספת: ..."
    }
  ]
}
- EXACTLY 1 section. Heading EXACTLY "לקראת יום המסחר". Title EXACTLY as given above.
- content = one string, bullets separated by \n, each bullet starts with "* ".
- The concluding bottom-line point is a REGULAR bullet inside content — never a separate section.
- No **, no ##, no HTML, no URLs inside content.
- "summary" = an array with ONE item per bullet in content, in the SAME order (include the bottom-line point too).
  Each item is "<אותה כותרת קצרה של הנקודה>: <משפט תמציתי אחד>". The sentence must DISTILL the essence of the point —
  what happened and why it matters — in your own words, up to ~20 words. Do NOT copy the first sentence of the
  bullet verbatim. All the same verification and direction rules apply to the summary as to the bullets.

══ WEB SEARCH POLICY ══
Web search is for VERIFICATION ONLY — confirming a name or figure that already appears in the source posts.
Do NOT use it to find additional news, index levels, prices or macro data. Content that is not present in the
sources does not enter the review.
══════════════════════════════════

══ CONTEXT: THE PREVIOUS TEL AVIV DAILY SUMMARY — DO NOT REPEAT THIS CONTENT ══
Already published. Your briefing is FORWARD-LOOKING. Mention an item below ONLY if there is a genuinely NEW development about it.

[סיכום המסחר]
* יום שלילי והדולר על 3 שקלים: הירידות בבורסה בתל אביב התחזקו במהלך יום המסחר, ושער הדולר היציג נקבע על 3 שקלים. הרקע הגלובלי הכביד: לחץ חריג על מניות הטכנולוגיה והשבבים באסיה הצניח את מדד הקוספי הקוריאני ב-6%, ומדד הניקיי היפני ירד בכ-3%, כשהמניות הכבדות סמסונג אלקטרוניקס ו-SK Hynix סופגות תנודתיות חריגה. השילוב של מימושים בשוקי חו"ל ושקל ברמה עגולה ובולטת מול הדולר הציב את המשקיע המקומי בנקודת פתיחה זהירה להמשך.
* המדד ללא שינוי והאינפלציה נרגעת: מדד המחירים לצרכן לחודש יוני נותר ללא שינוי, מעל ממוצע התחזיות שציפה לירידה של כ-0.1%, אך קצב האינפלציה השנתי התמתן ל-1.6% לעומת 1.9% בחודשיים הקודמים. בשוק מתמחרים כעת הסתברות של כ-50% להורדת ריבית נוספת בתחילת ספטמבר, לאחר שבנק ישראל הפחית בתחילת החודש את הריבית ל-3.50%. מנגד, ההאצה במחירי השכירות מזכירה שהוועדה המוניטרית תתקדם בזהירות, כך שהנתון תומך באפיקי הסיכון אך אינו מבטיח פעימה קרובה.
* מניית שפיר זוכה במכרז הענק: שפיר זכתה במכרז להארכת כביש 6 לצפון בהיקף מוערך של כ-12 מיליארד שקל. במסגרת הפרויקט תקים החברה, תממן, תפעיל ותתחזק את מקטעים 8 ו-9/א באורך של כ-22 קילומטר, ממחלף סומך ועד בית העמק, עם תקופת זיכיון של 34 שנים ממועד הסגירה הפיננסית. עבור המשקיעים מדובר בעוגן הכנסות ארוך טווח שמחזק את מעמדה של שפיר בליבת התשתיות הלאומיות.
* רפאל מתריעה על גורל ההנפקה: יו"ר רפאל הזהיר כי אם לא תהיה הנפקה, לא תהיה רפאל שאנחנו מכירים. האמירה החריפה מעלה לראש סדר היום את שאלת הנפקתה של חברת הביטחון הממשלתית, בתקופה שבה התעשיות הביטחוניות נמצאות במוקד העניין של שוק ההון המקומי. עבור המשקיעים זהו איתות שההכרעה על עתיד אחת מחברות הביטחון הגדולות במשק הפכה דחופה, עם השלכות אפשריות על מפת ההנפקות בבורסה.
* מניית הפניקס מרחיבה רכישה עצמית: הפניקס הודיעה על הגדלת היקף הרכישה העצמית בתוכנית לשנת 2026 ל-400 מיליון שקל. הרחבת התוכנית משדרת אמון של ההנהלה בשווי החברה ומייצרת מנגנון תמיכה בביקושים למניה, דווקא ביום שבו השוק המקומי נסחר בירידות. עבור בעלי המניות זהו ערוץ נוסף של החזר הון שמעיד על איתנותה ההונית של קבוצת הביטוח.
* האנרגיה הסולארית מרכזת עסקאות: גולדן אנרג'י הודיעה כי החברה הבת אלגרי פאוור נבחרה כספקית ויזמית יחידה במכרז מסגרת של אשכול רשויות מקומיות להקמת מתקנים סולאריים ואגירה, עם פוטנציאל של 150 מגה-וואט ושווי של כמיליארד שקל, אם כי הדרך להכנסות בפועל עוד ארוכה. במקביל החלה טראלייט בפרויקטים סולאריים על גדרות ביטחון בהשקעה של כ-60 מיליון שקל, במימון בנק לאומי ומגדל ביטוח. שתי הידיעות ממחישות את התנופה בתחום האנרגיה המתחדשת בשוק המקומי, לצד סימני שאלה על קצב ההבשלה של הפרויקטים.
* שוק הדיור ממשיך להתקרר: מדד מחירי הדירות בעסקאות אפריל-מאי ירד ב-1.0% והשלים ירידה של 2.0% בשנה האחרונה, כשמחוז תל אביב מוביל עם ירידה חודשית של 2.3% וירושלים אחריה עם 1.8%. במקביל מתחזקת בשוק ההערכה כי לקבלנים לא נותרו עוד שפנים בכובע וכי כדי למכור הם נדרשים להוריד מחירים בפועל. עבור ענף הנדל"ן זהו שילוב של לחץ מחירים נמשך מול רוח גבית מהריבית היורדת, והמאזן ביניהם יכריע את כיוון הענף בהמשך השנה.
* שורה תחתונה למחר: הכיוון ייגזר מהשאלה האם הירידות יימשכו, או שהתמתנות האינפלציה ל-1.6% והתמחור של כ-50% להורדת ריבית בספטמבר יחזירו ביקושים לאפיקי הסיכון. במקביל יש לעקוב אחרי שער הדולר סביב רמת 3 השקלים ואחרי התנודתיות החריפה במניות השבבים באסיה, שמושכת את הסנטימנט הגלובלי לשני הכיוונים אחרי דוחות השיא של TSMC עם זינוק של 23% ברווח.
══════════════════════════════════════════════════════════════

מקורות מרשת X (בעברית) — Never mention in the review that these came from posts/X:

@ModiShafrir [Sun Jul 26 08:26:17 +0000 2026]: תמצית הסקירה השבועית 26.07.26: 1. שווקים 🌎 ונפט - מדדי המניות ירדו בחדות ביום חמישי, על רקע הזינוק במחירי הנפט אל מעל ל- 100 דולר ואכזבת המשקיעים מהדוחות של Tesla ו- Alphabet (Google העלתה את תחזית ה- CapEx). https://t.co/BCuDoizbGJ

@ModiShafrir [Tue Jul 14 12:47:53 +0000 2026]: האינפלציה (CPI) ב- 🇺🇸 הפתיעה בחדות כלפי מטה, כך שההסתברות להעלאת ריבית בחודש הקרוב צפויה לרדת, הדולר בעולם נחלש, תשואות ה- Treasuries יורדות, והחוזים על מדדי המניות עולים בחדות יחסית (חרף העלייה הנוספת והחדה במחירי הנפט): ✅האינפלציה (headline) ירדה ביוני ב- 0.4% (צפי ל- 0.1%-). ✅יתרה מכך, ליבת האינפלציה (Core CPI) נותרה לל"ש (צפי ל- 0.2%+), כך שקצב העלייה השנתי התמתן בחדות ל- 2.6%+ YoY (לעומת 2.9%+ במאי). 1/

@ModiShafrir [Sun Jul 05 06:01:20 +0000 2026]: תמצית הסקירה השבועית 05.07.26: 1. שווקים ונפט 🌏- חרף הירידה החדה במניות השבבים (מדד ה- SOX ירד השבוע ב- 4.4%), מדד ה- S&P 500 במשקל שווה (equal weighted) עלה לרמת שיא, בתמיכת ידיעות גיאופוליטיות חיוביות, התבססות מחירי הנפט ברמת שפל של ארבעה חודשים, והתמתנות הציפיות להעלאת ריבית קרובה בארה"ב.

@matanshitrit [Sun Aug 02 06:03:59 +0000 2026]: הפד ודוחות הטכנולוגיה עוברים למרכז הבמה | סקירה שבועית 02/08/26 לבקשתכם - מעכשיו גם באפל פודקאסט אשמח לשיתופים 🙏 נושאים - ⁠- סיכום ביצועים בשווקים הפיננסים וסביבת מכפילים ⁠- דרום קוריאה – כשהמינוף משתלט על המדד ⁠- הסיפור הגדול של הסופ"ש בוול סטריט – ליאופולד אשנברנר ⁠- עונת הדו"חות בוול סטריט – תמונת מצב עד כה, כולל מייקרוסופט, אמזון, אפל ומטא ⁠- החלטת הריבית הניצית של הפד, הזינוק בתשואות האג"ח הארוכות ותמחור הריבית ⁠- נתוני הצמיחה לרבעון השני בארה"ב – חזקים יותר מהשורה העליונה ⁠- עוצמת הצריכה הפרטית בישראל לקראת נתוני הצמיחה ⁠- שוק האג"ח המקומי ותמחור ריבית בנק ישראל ⁠- מבט לשבוע הקרוב – מאקרו ועונת הדו"חות שבוע טוב! יוטיוב – https://t.co/Let6BMnokh ספוטיפיי - https://t.co/MyrXpZI8i7 אפל פודקאסט – https://t.co/On12Am2dLf

@ModiShafrir [Wed Jul 15 16:50:51 +0000 2026]: מדד חודש יוני נותר לל"ש, בדומה להערכתנו ומעל לממוצע תחזיות החזאים והשוק לירידה של כ- 0.1%. חרף ההפתעה כלפי מעלה (וההאצה במחירי השכירות), האינפלציה השנתית התמתנה ל- 1.60% YoY (לעומת 1.90%+ בחודשיים האחרונים), והתמתנות נרשמה גם במדדי הליבה השונים. מה ההשלכות לגבי ריבית בנק ישראל? 1/

@matanshitrit [Wed Jul 29 20:16:18 +0000 2026]: התשואה על אג"ח ממשלתית ל-30 שנה מזנקת לשיא שלא נראה מאז 2007 כמה נק' מתוך מסיבת העיתונאים של הפד – 1) "עבור חלק ממשקי הבית, העסקים ואנשי השוק, חמש שנים של אינפלציה גבוהה יצרו רושם מוטעה, וקשה להשתחרר ממנו, כאילו יעד האינפלציה המשתמע של הפד גבוה מ-2%." 2) "הרשו לי להדגיש שוב - אין יעד אינפלציה "רך". אין יעד משתמע "רך". לא כל עוד הוועדה הזו מכהנת." 3) למרות שוורש התחייב בעבר להחזיר את האינפלציה ליעד של 2%, הוא עדיין נמנע מלומר במפורש כי בכוונתו להעלות את הריבית. בתשובה לאחת השאלות, ציין כי "אם האינפלציה תמשיך להיות גבוהה לאורך תקופת התחזית, בהחלט ייתכן שהריבית תהיה חלק מהפתרון, אך לא הייתי אומר שהיא הפתרון היחיד." 4) כשנשאל מדוע הפד לא העלה את הריבית כבר כעת, השיב כי "ריביות השוק עלו מאז ישיבת המדיניות הקודמת, דבר המרמז שהמשקיעים כבר עושים חלק מעבודתו של הבנק המרכזי." לדבריו, הדבר נובע גם מהחלטתו לצמצם את השימוש בהכוונה עתידית (Forward Guidance) שהפד נהג לספק לגבי כיוון הריבית – "השווקים קיבלו החלטות משום שבחרנו לסגת, לפחות בחלק מהמקרים, מהניסיון להשפיע עליהן. הערכות השוק לגבי רמת הריביות הנומינליות לאורך עקום האג"ח עלו." 5) "משתתפי השוק לומדים לשחק בכדור ולא בשופט...מחירי השוק ימשיכו להגיב בכיוון ובעוצמה שהם ימצאו לנכון. לדעתי זהו שינוי לטובה, ואנחנו רק בתחילת הדרך." נכון לכתיבת שורות אלה, ההסתברות להעלאת ריבית בהחלטה הבאה (16 בספטמבר) עומדת על כ-60%, כשבמצטבר מתמחרים כמעט 2 העלאות ריבית בשנה הקרובה.

@ModiShafrir [Wed Jul 29 19:40:39 +0000 2026]: הפד הותיר את הריבית ללא שינוי בטווח של 3.5%–3.75% ברוב של 9 מול 3 מתנגדים אשר תמכו בהעלאה של 25bp (השוק תמחר טרם ההודעה העלאה בהסתברות של כ- 33%). הוועדה הותירה בהודעה את המסר בדבר מחויבותה ליציבות מחירים, לצד הערכה כי הכלכלה צומחת בקצב איתן והאינפלציה עדיין גבוהה מהיעד. ✅ הפד ציין בהודעה את שמות שלושת החברים שתמכו בהעלאת ריבית, כולם נשיאי בנקים אזוריים בעלי זכות הצבעה בשנת 2026: Hammack (קליבלנד), Kashkari (מיניאפוליס) ו-Logan (דאלאס). בהקשר לכך בלטה העובדה כי כל חברי מועצת הנגידים (Governor) תמכו בהותרת הריבית על כנה. יו"ר הפד תמך, כאמור, בהותרת הריבית על כנה, אך המסרים שנקט במסיבת העיתונאים היו יחסית 'ניציים': ✅אמר מספר פעמים במסיבת העיתונאים כי הוועדה נחושה להחזיר את האינפלציה לרמה של 2%, לאחר 5 שנים של אינפלציה גבוהה. ✅הבהיר כי הפד 'לא יהסס לפעול' (won't hesitate to act), וכי קובעי המדיניות יישאו באחריות למאבק באינפלציה. ✅ ווארש אמר כי בעוד שבצד התעסוקה הפד מצליח לעמוד במנדט של תעסוקה מלאה, הפד מצליח הרבה פחות בצד המחירים (The Fed is doing well on the full employment side of its mandate, but we're doing considerably less well on prices). ✅ בנימה 'יונית' יותר, Warsh ציין לחיוב את הירידה בציפיות האינפלציה מאז החלטת הריבית הקודמת, שלטעמו נבעה מהבנת השווקים את מחויבות חברי הוועדה להחזרת האינפלציה אל עבר היעד. ✅בנוסף, ווארש אמר כי הוא שבע רצון מכך שהשווקים עושים חלק מהעבודה עבור קובעי המדיניות (בהתייחסו לעליית התשואות החדה בתקופה האחרונה). לסיכום - חרף הנימה ה'ניצית' של יו"ר הפד, התשואות בטווחים הקצרים דווקא ירדו במהלך מסיבת העיתונאים והשוק מתמחר עתה העלאת ריבית בספטמבר בהסתברות של 57% בלבד, וסך הכל 1.25 העלאות ריבית בשנת 2026

@ModiShafrir [Mon Jul 06 14:43:04 +0000 2026]: ב"י הוריד את הריבית ב- 25bp לרמה של 3.50% (בהתאם להערכתנו, ולהערכת הקונצנזוס). דברי הנגיד במסיבת העיתונאים היו יחסית 'יוניים' (במיוחד בהשוואה להודעת הריבית הקודמת) ✅ הנגיד הדגיש אמנם כי קיימת אי וודאות גדולה מאד סביב עתיד הריבית, וכי ההחלטות התקבלו בהתאם לנתונים שיתפרסמו (Data depended), אך בנימה 'יונית' ציין ש"ככל שציפיות האינפלציה יורדות, ובוודאי אם יתקרבו לגבול התחתון של היעד, הדבר מצדיק מדיניות מוניטרית מרחיבה יותר, ובקצבים מהירים יותר". בנוסף, כמענה לשאלת אחד העיתונאים - הנגיד לא פסל את האפשרות התיאורטית לכך שב"י יוריד את הריבית בפעימה אחת בשיעור של 50bp. ✅ בנימה 'ניצית' יותר - הנגיד ציין את האצת שכר הדירה, והשכר הממוצע וכן את ההתפתחויות האחרונות בתקציב המדינה, כגורמים המחייבים זהירות רבה יותר מצד ב"י. ✅ התייחסות ב"י לעתיד האינפלציה הייתה 'יונית' בהשוואה להודעות הקודמות – בעוד שבהודעות הריבית הקודמות צוין כי " להערכת הוועדה קיימים סיכונים לעלייה מחודשת של האינפלציה", בהודעה הנוכחית ציינו בב"י כי "להערכת הוועדה, קיימים מספר גורמים שיכולים להשפיע בכיוונים מנוגדים על התפתחות האינפלציה". ✅ חטיבת המחקר הורידה את תחזיתה לרמת הריבית בעוד כשנה ל- 3.0% (ריבית ממוצעת ברבעון השני של 2027) – מעט מעל לציפיות השוק לכ- 2.85%. ✅בנימה 'נניצית יותר - הנגיד הזהיר כי עליית תקציב הבטחון מעבר למוסכם תוביל לעלייה חדה בגירעון ולעליית האינפלציה בכ- 0.3% שורה תחתונה – אנו נותרים בינתיים בהערכתנו (התואמת עתה גם את תחזית חטיבת המחקר של ב"י) כי הריבית תעמוד בעוד כשנה על כ- 3.0%.

@matanshitrit [Thu Jul 30 06:56:11 +0000 2026]: פורסם מחיר הדלק הרשמי לאוגוסט - מזנק ל-8.09 שקלים לליטר, עלייה של 61 אג' (כ-8% בהשוואה לחודש הקודם). כאמור, קונצנזוס חזאים למדד אוגוסט צפוי להגיע לעלות מעט ל-1.0%. אבל עד אז, יש לנו את מדד יולי - קונצנזוס חזאים כ-0.3%. שני מדדים גבוהים לפנינו (אם כי האינפלציה השנתית לא צפויה להאיץ יותר מידי בשלב הזה).

@matanshitrit [Thu Jul 30 06:25:48 +0000 2026]: מד ה"ניציות-יוניות" של הצהרות הפד, המבוסס על ניתוח טקסט אוטומטי של Bloomberg Intelligence האלגוריתם קורא את הצהרת הריבית ומסווג את המשפטים לפי המסר שלהם - משפט ניצי – מדגיש אינפלציה, סיכונים לעליית מחירים, צורך בריבית גבוהה או חוסר דחיפות להפחית אותה. משפט יוני – מדגיש היחלשות בצמיחה או בשוק העבודה, ירידה באינפלציה ואפשרות להפחתת ריבית. לאחר מכן מחושב המאזן בין המשפטים - ככל שהציון גבוה יותר, ההצהרה ניצית יותר. ככל שהוא נמוך יותר, היא יונית יותר. לפי המדד, ההצהרה האחרונה הייתה מהניציות ביותר שנרשמו לאורך תקופת המדגם.

@SponserNews [Sun Aug 02 10:12:04 +0000 2026]: עונת הדוחות בת”א מעלה הילוך: אלה החברות שיעמדו במוקד השבוע: שבוע עמוס במיוחד צפוי למשקיעים בבורסה, עם פרסום דוחותיהן של עשרות חברות ממגוון ענפים - מטכנולוגיה ושבבים, דרך נדל"ן ואנרגיה ועד מזון ותעשייה; אלו החברות שירכזו את תשומת הלב https://t.co/HsdKQzlmH1

@calcalist [Sun Aug 02 13:00:00 +0000 2026]: "מדד הביג מק" חושף את יוקר המחיה: ישראל מדורגת במקום השני, מיד אחרי שווייץ, במחיר של מנת ביג מק במקדונלד'ס. המנה בישראל עולה 7.67 דולר לעומת 6.22 דולר בארה"ב, מה שמצביע על שקל מוערך ביתר של כ-40% https://t.co/kuqJ9CjVJZ https://t.co/JAfbrMcLCz

@ModiShafrir [Sun Jul 19 05:59:07 +0000 2026]: תמצית הסקירה השבועית 19.07.26 1. שווקים 🌎 ונפט - מניות השבבים ה- AI ירדו ביום שישי בחדות, על רקע דחיית השקת המודל החדש של Gemini, העלאת תחזית ההשקעות (capex) של TSMC, והשקת מודל ה- Kimi K3 של Moonshot הסינית, אשר עוררה חששות כי מודלים סיניים זולים ישחקו את הביקוש לשבבים בארה"ב (בדומה ל'הלם DeepSeek' מתחילת 2025).

@ModiShafrir [Sun Jul 12 08:08:23 +0000 2026]: תמצית הסקירה השבועית 12.07.26: 1. שווקים ונפט 🌎- מחירי הנפט ירדו לקראת הסופ"ש, אך עדיין סגרו את השבוע בעלייה של כ- 5.4%+, על רקע חששות השווקים מחזרה למלחמה במזרח התיכון. ארה"ב הכריזה כי הפסקת האש עם איראן 'הסתיימה' (over), והציבה לאיראן מועד אחרון (ליום שבת) להכרה פומבית בכך שמיצרי הורמוז יוותרו פתוחים לשיט. ✅חרף הסלמת המתיחות במזה"ת, מדד הנאסד"ק עלה השבוע ב- 1.7%, על רקע ידיעות חיוביות ממגזר הטכנולוגיה.

@fundercoil [Mon Aug 03 07:37:25 +0000 2026]: סיכום יולי בקרנות הנאמנות: גיוס נטו של 3.1 מיליארד שקל בהובלת הכספיות והאג"ח המקומי https://t.co/9190NQ3NTl

@SponserNews [Mon Aug 03 07:51:04 +0000 2026]: הפניקס מזרימה 234 מיליון שקל ל-PowerGen ומגדילה אחזקות ל-12.4%: הפניקס תשקיע כ-234 מיליון שקל בזרוע האנרגיה המתחדשת; במקביל נחתמו הבנות עם משקיעים מוסדיים נוספים להשקעה של עד 800 מיליון שקל; ג’נריישן צפויה לרשום רווח של עד 320 מיליון שקל https://t.co/18wh6PhQkb

@SponserNews [Mon Aug 03 04:45:01 +0000 2026]: התקפלות מפוארת: טראמפ - השיחות עם איראן יתחדשו; הנפט צונח, אסיה אדומה: הנפט יורד ל-83 דולר לחבית ברקע להסברים של טראמפ על מדוע ביטל תקיפה וכוונה להמשך שיחות; בעוד בורסות אסיה רשמו ירידות חדות בהובלת מניות השבבים. במקביל, הין היפני מתחזק לאחר ההתערבות https://t.co/CTR1XYq09t

@ModiShafrir [Thu Jul 02 12:53:08 +0000 2026]: נתוני התעסוקה ב- 🇺🇸 של חודש יוני היו חלשים מהציפיות, כך שהשוק מתמחר עתה הסתברות נמוכה (20%) להעלאת ריבית הפד בחודש יוני, והסתברות של כ- 62% להעלאה בספטמבר: ✅ דו"ח ה NFP הצביע על תוספת של 57 אלף עובדים ביוני (צפי ל- 113+ אלף), שאת לאחר שנתוני החודשיים הקודמים עודכנו כלפי מטה בחדות (-74 אלף משרות). ✅ סקר כח האדם הצביע אמנם על ירידת שיעור האבטלה ל- 4.2% (צפי ל- 4.3%), אך זאת במקביל לירידה חדה מאד בשיעור ההשתתפות בכח העבודה (היצע העובדים) , כך שלפי סקר זה בחודש יוני נגרעו כ- 507 אלף עובדים... בגרף ניתן לראות שבכ- 5 מתוך 6 החודשים האחרונים נרשמה, לפי סקר זה, התכווצות במספר העובדים בשוק התעסוקה. 1/

@matanshitrit [Thu Jul 30 12:36:58 +0000 2026]: הרבה נתונים פורסמו בזה הרגע בארה"ב - 1) הצמיחה ברבעון השני הסתכמה ב-1.5% (צפי 2.0%) - על פניו מספר נמוך מהצפי, אך הביקוש המקומי דווקא היה חזק (מאוד) כאשר המכירות הסופיות לרוכשים פרטיים מקומיים (צריכה והשקעות) צמחו ב-3.9%. מה גרע על הצמיחה? יבוא שכרגע כ-1.5 נ"א מהצמיחה, בעיקר על רקע יבוא של ציוד הון, שבבים, תקשורת וציוד תעשייתי. בנוסף, המלאים גרעו כ-0.7 נ"א מהצמיחה הרבעונית. 2) מדד המחירים (המועדף על הפד/או שפחות מועדף היום) - ירד ב-0.1% והקצב השנתי התמתן מ-4.1% ל-3.7% (בהתאם לצפי)

@matanshitrit [Wed Jul 29 18:10:49 +0000 2026]: הפד הותיר הערב את הריבית ללא שינוי. הודעת הריבית כמעט זהה לחלוטין לזו מהישיבה הקודמת - הכלכלה ממשיכה לצמוח בקצב סולידי, שוק העבודה נותר יציב והאינפלציה עדיין גבוהה מהיעד. הסיפור האמיתי נמצא בהצבעה - ביוני ההחלטה התקבלה פה אחד, ואילו הפעם שלושה חברים התנגדו משום שרצו להעלות את הריבית ב-25 נ״ב. שורה תחתונה, הנוסח כמעט לא השתנה, אבל מאזן הכוחות בתוך הפד הפך ניצי יותר. נמתין למסיבת העיתונאים.

@fundercoil [Mon Aug 03 07:43:31 +0000 2026]: תעשיית הקרנות גייסה ביולי סכום של כ-3.3 מיליארד ₪ שוב בהובלת הקרנות הכספיות https://t.co/GNAi7xk2QS

@fundercoil [Mon Aug 03 07:34:55 +0000 2026]: חודש יולי ננעל בעליות בהובלת הבנקים ושווי השוק בשיא של מעל 3 טריליון שקל; ביום חמישי הקרוב (6 באוגוסט) https://t.co/T9Io8OrfhS

@SponserNews [Mon Aug 03 08:08:53 +0000 2026]: מאסיבית בדרך להודו: חתמה על מזכר הבנות ראשוני עם Lohia Aerospace: החברה מהודו תיהנה מבלעדיות של שנתיים ותתחייב ליעדי רכישה, אך מדובר בהסכם לא מחייב בשלב זה, כשכל הציוד והקניין הרוחני יישארו בידי מאסיבית https://t.co/sN1bam7Bsj

@SponserNews [Mon Aug 03 07:33:25 +0000 2026]: נאוויטס מתרחבת במפרץ אמריקה: רוכשת שתי תגליות מענקיות הנפט אוקסידנטל וקוסמוס: נאוויטס רוכשת 33% מתגליות טיבריוס ולוגן; גדעון תדמור: "הפרויקט הינו סינרגטי לבקסקין וצפוי להפיק באמצעות מתקן ההפקה המשמש HUB איזורי" https://t.co/PlNhhqPqQT

@SponserNews [Mon Aug 03 06:40:33 +0000 2026]: ר.ג.ע זכתה במכרז חדש בהיקף של עד כ-40 מיליון שקל: מדובר במכרז למתן שירותי איסוף ופינוי פסולת לרשות מקומית; תקופת ההתקשרות במכרז הינה בת שנתיים, כשלרשות המקומית אופציה להארכת ההתקשרות לתקופה נוספת של עד 3 שנים https://t.co/akSTceMyH4

@SponserNews [Sun Aug 02 13:00:15 +0000 2026]: הסקירה השבועית: קריסת קרן הגידור של ילד הפלא, ואיתות טכני להמשך בשווקים: בסיכום השבוע המדדים המובילים רושמים מגמה שלילית אם כי התוצאה פחות גרועה ממה שיכולה הייתה להיות כשברקע אי הוודאות הגיאופוליטית הפכה להרגל; הנה ניתוח טכני לני"ע במוקד https://t.co/Thy9jFUqJY

@SponserNews [Sun Aug 02 09:01:37 +0000 2026]: הפד נכשל? ספקות עולים ביכולתו לרסן אינפלציה ותשואות האג”ח בזינוק: הפער בין הרטוריקה הנחרצת לבין היעדר פעולה מעשית עורר ספק; האם אנו כמשקיעים לא צריכים לדרוש פרמיית סיכון גבוהה יותר כדי להצדיק החזקה באגרות ארוכות? https://t.co/7GHR8rAUM7

@SponserNews [Sun Aug 02 07:02:19 +0000 2026]: לידר על שוק האג”ח: למרות האטרקטיביות אי-הוודאות עלולה להעיב על הארוכים: בלידר מציינים כי רמת אי וודאות גיאופוליטית ופוליטית גבוהה ולחץ לעליית תשואות בחו"ל עלולים להעיב על האפיקים הארוכים; הורדת הריבית תידחה על לרגיעה מסויימת במצב הגיאופוליטי https://t.co/OEWxOgUPKV

@globesnews [Mon Aug 03 08:14:09 +0000 2026]: מניית ג'י סיטי ממחישה: למשקיעים יש מסר ברור לחיים כצמן https://t.co/IysqkOo7D9 https://t.co/Wes9cSHDe7

@globesnews [Mon Aug 03 08:04:58 +0000 2026]: הפניקס תשקיע בפאוורג'ן לפי שווי של 3.25 מיליארד שקל https://t.co/nQ00AOPVF5 https://t.co/KFxKKnw9Id

@globesnews [Mon Aug 03 07:28:33 +0000 2026]: מיזוג ענק בשוק התרופות מתקרב? דיווח על איחוד בין אסטרהזנקה ו-BMS https://t.co/m6NwqBlg02 https://t.co/zXRrRfnOEH

@globesnews [Mon Aug 03 05:57:23 +0000 2026]: מגמה מעורבת באסיה; מחירי הנפט נופלים ב-4% https://t.co/EBrFRTre3U https://t.co/8bcpUOx55b

@globesnews [Mon Aug 03 05:29:59 +0000 2026]: חמישה דברים שכדאי לדעת לקראת פתיחת המסחר בבורסה https://t.co/Gh3N33a5L7 https://t.co/4i32h9HD0n

@globesnews [Mon Aug 03 02:56:29 +0000 2026]: עשה אקזיט של 82 מיליון שקל אצל נובולוג, ועכשיו רוצה להשתלט עליה https://t.co/SdxmFghGmG https://t.co/WnO5Eka3ig

@globesnews [Mon Aug 03 02:56:03 +0000 2026]: איך הפכה צ'ק פוינט למניה היחידה שלא נהנית מהחגיגה בשוק הסייבר? https://t.co/ELenyS8zRf https://t.co/HwlXOHTulg

@globesnews [Mon Aug 03 02:47:47 +0000 2026]: 2,500 משלוחי נשק במלחמה: הדוח שחושף צד לא מוכר ביחסי ישראל־הודו https://t.co/t0ddolRvQu https://t.co/h6NASdKTS2

@calcalist [Mon Aug 03 08:00:02 +0000 2026]: ציון בלס, מהאוהדים הוותיקים והמוכרים של מכבי ת"א בכדורגל, שהפעיל את מזנון הקבוצה במתחם האימונים בקריית שלום, יצא לקרב משפטי נגד המועדון https://t.co/ywTNxa0BIQ https://t.co/GhoZlQdQCo

@TheMarker [Mon Aug 03 08:00:12 +0000 2026]: "אצל רמי לוי מצאנו טעויות במיליון שקל": חברת הרחפנים שמחכה לסוף המלחמה https://t.co/TauDl4yHec

@TheMarker [Mon Aug 03 07:00:14 +0000 2026]: עד 2.5 מיליון שקל לקניון: קבוצת עזריאלי הגישה לשוכרים חשבון מפתיע https://t.co/O0euWBqGHm

@TheMarker [Mon Aug 03 06:00:11 +0000 2026]: "אם המניה תיפול — הקרנות יימחקו": מוצר ההשקעות האקזוטי שהבנקים חוטפים https://t.co/6nOLNzLKxK

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.