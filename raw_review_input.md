אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות בלבד, והחזר JSON בלבד.

You are a senior investment advisor writing a signature PRE-MARKET briefing in Hebrew for the
TEL AVIV STOCK EXCHANGE (הבורסה לניירות ערך בתל אביב). Script run date: 2026-07-22 (יום רביעי).
Briefing target date: 2026-07-22 (יום רביעי). The briefing is for TODAY's Tel Aviv session. The exchange has NOT opened yet — never describe it as open or trading. Use 'הבורסה צפויה להיפתח', 'המשקיעים יעקבו אחר'.

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
  "title": "נקודות חשובות לקראת יום המסחר בבורסה בתל אביב 🇮🇱 – יום רביעי, 22.7.2026",
  "date": "2026-07-22",
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

@ModiShafrir [Tue Jul 14 12:47:53 +0000 2026]: האינפלציה (CPI) ב- 🇺🇸 הפתיעה בחדות כלפי מטה, כך שההסתברות להעלאת ריבית בחודש הקרוב צפויה לרדת, הדולר בעולם נחלש, תשואות ה- Treasuries יורדות, והחוזים על מדדי המניות עולים בחדות יחסית (חרף העלייה הנוספת והחדה במחירי הנפט): ✅האינפלציה (headline) ירדה ביוני ב- 0.4% (צפי ל- 0.1%-). ✅יתרה מכך, ליבת האינפלציה (Core CPI) נותרה לל"ש (צפי ל- 0.2%+), כך שקצב העלייה השנתי התמתן בחדות ל- 2.6%+ YoY (לעומת 2.9%+ במאי). 1/

@ModiShafrir [Sun Jul 05 06:01:20 +0000 2026]: תמצית הסקירה השבועית 05.07.26: 1. שווקים ונפט 🌏- חרף הירידה החדה במניות השבבים (מדד ה- SOX ירד השבוע ב- 4.4%), מדד ה- S&P 500 במשקל שווה (equal weighted) עלה לרמת שיא, בתמיכת ידיעות גיאופוליטיות חיוביות, התבססות מחירי הנפט ברמת שפל של ארבעה חודשים, והתמתנות הציפיות להעלאת ריבית קרובה בארה"ב.

@ModiShafrir [Wed Jul 15 16:50:51 +0000 2026]: מדד חודש יוני נותר לל"ש, בדומה להערכתנו ומעל לממוצע תחזיות החזאים והשוק לירידה של כ- 0.1%. חרף ההפתעה כלפי מעלה (וההאצה במחירי השכירות), האינפלציה השנתית התמתנה ל- 1.60% YoY (לעומת 1.90%+ בחודשיים האחרונים), והתמתנות נרשמה גם במדדי הליבה השונים. מה ההשלכות לגבי ריבית בנק ישראל? 1/

@matanshitrit [Sun Jul 19 04:40:31 +0000 2026]: *סקירה שבועית 19/07/26 | מחירי הדירות בישראל בירידה החדה ביותר מזה 8 שנים* אשמח לשיתופים 🫶🏻 לינק ליוטיוב וספוטיפיי למטה שבוע טוב׳ *נושאים* - - סיכום ביצועים בשווקים הפיננסים וסביבת מכפילים - ⁠השווקים לוקחים הפוגה – עונת הדו"חות עוברת למרכז הבמה - ⁠סיכום דו"חות הבנקים, טכנולוגיה ושבבים - מדד המחירים לצרכן בארה"ב מפתיע כלפי מטה - נקודות מרכזיות מתוך העדות של קווין וורש בקונגרס ותמחור ריבית הפד - ⁠פעילות כלכלית בישראל – המדד החודשי לפעילות המשק ושוק העבודה - ⁠שוק הדיור בישראל – משכנתאות, עסקאות ומדד מחירי הדירות - ⁠מדד מחירים לצרכן חודש יוני ותחזית 12 חודשים קדימה - ⁠מבט לשבוע הקרוב – מאקרו ועונת הדו"חות *יוטיוב* – https://t.co/kjm3yUF1O6 *ספוטיפיי* – https://t.co/gtpjExRQ9a

@ModiShafrir [Mon Jul 06 14:43:04 +0000 2026]: ב"י הוריד את הריבית ב- 25bp לרמה של 3.50% (בהתאם להערכתנו, ולהערכת הקונצנזוס). דברי הנגיד במסיבת העיתונאים היו יחסית 'יוניים' (במיוחד בהשוואה להודעת הריבית הקודמת) ✅ הנגיד הדגיש אמנם כי קיימת אי וודאות גדולה מאד סביב עתיד הריבית, וכי ההחלטות התקבלו בהתאם לנתונים שיתפרסמו (Data depended), אך בנימה 'יונית' ציין ש"ככל שציפיות האינפלציה יורדות, ובוודאי אם יתקרבו לגבול התחתון של היעד, הדבר מצדיק מדיניות מוניטרית מרחיבה יותר, ובקצבים מהירים יותר". בנוסף, כמענה לשאלת אחד העיתונאים - הנגיד לא פסל את האפשרות התיאורטית לכך שב"י יוריד את הריבית בפעימה אחת בשיעור של 50bp. ✅ בנימה 'ניצית' יותר - הנגיד ציין את האצת שכר הדירה, והשכר הממוצע וכן את ההתפתחויות האחרונות בתקציב המדינה, כגורמים המחייבים זהירות רבה יותר מצד ב"י. ✅ התייחסות ב"י לעתיד האינפלציה הייתה 'יונית' בהשוואה להודעות הקודמות – בעוד שבהודעות הריבית הקודמות צוין כי " להערכת הוועדה קיימים סיכונים לעלייה מחודשת של האינפלציה", בהודעה הנוכחית ציינו בב"י כי "להערכת הוועדה, קיימים מספר גורמים שיכולים להשפיע בכיוונים מנוגדים על התפתחות האינפלציה". ✅ חטיבת המחקר הורידה את תחזיתה לרמת הריבית בעוד כשנה ל- 3.0% (ריבית ממוצעת ברבעון השני של 2027) – מעט מעל לציפיות השוק לכ- 2.85%. ✅בנימה 'נניצית יותר - הנגיד הזהיר כי עליית תקציב הבטחון מעבר למוסכם תוביל לעלייה חדה בגירעון ולעליית האינפלציה בכ- 0.3% שורה תחתונה – אנו נותרים בינתיים בהערכתנו (התואמת עתה גם את תחזית חטיבת המחקר של ב"י) כי הריבית תעמוד בעוד כשנה על כ- 3.0%.

@matanshitrit [Tue Jul 14 13:39:36 +0000 2026]: אפשר לחזור לשגרה - מלאי הדירות שבידי הקבלנים חזר לעלות. ירושלים בשיא הכושר ופותחת פערים, אך תל אביב לא מוותרת וצמודה מאחור. בצד של העסקאות (הלמ"ס) - סך הדירות החדשות שנמכרו 3,700, אך בניכוי מחיר למשתכן - אלה הסתכמו ב-2,497, המספר הגבוה ביותר מזה חצי שנה, וגבוה בכ-34% בהשוואה למאי אשתקד. לפי האוצר, מאה דירות נרכשו ע"י קרנות ריט, עם הטבות מימון. כמו כן, ת"א בלטה לחיוב במכירות (481 מול 150 במאי אשתקד), כאשר שני פרויקטים בלבד ריכזו 44% מהמכירות באזור זה. אם כבר ת"א, באוצר הוסיפו כי בת"א נרשמה ירידה בשכיחות הטבות מימון (12% מול 24% במאי אשתקד), כאשר חלק משמעותי מהמכירות בת"א (כולל החודשיים הקודמים) התרכז בפרויקט גדול במסגרתו ניתנה הנחה משמעותית במחיר הדירה. מעניין לראות איך ההנחה המשמעותית תבוא לידי ביטוי במדד מחירי הדיור...

@matanshitrit [Tue Jul 14 04:21:37 +0000 2026]: היום ב-15:30 (שעון ישראל) - מדד המחירים לצרכן בארה"ב (CPI) קונצנזוס - ירידה של 0.1% וקצב שנתי 3.8% (לפי CPINowcast 3.9%) https://t.co/mmqJmgBlsk

@SponserNews [Tue Jul 21 09:44:00 +0000 2026]: ג’נגו מוכרת את פעילותה לבעל השליטה ותהפוך לשלד בורסאי: חמש שנים אחרי ההנפקה החברה תמכור את מלוא פעילותה העסקית לאופיר הרבסט תמורת 300 אלף דולר; כ-30 מיליון שקל יישארו בקופת החברה https://t.co/c0pvSttgmx

@ModiShafrir [Sun Jul 19 05:59:07 +0000 2026]: תמצית הסקירה השבועית 19.07.26 1. שווקים 🌎 ונפט - מניות השבבים ה- AI ירדו ביום שישי בחדות, על רקע דחיית השקת המודל החדש של Gemini, העלאת תחזית ההשקעות (capex) של TSMC, והשקת מודל ה- Kimi K3 של Moonshot הסינית, אשר עוררה חששות כי מודלים סיניים זולים ישחקו את הביקוש לשבבים בארה"ב (בדומה ל'הלם DeepSeek' מתחילת 2025).

@ModiShafrir [Sun Jul 12 08:08:23 +0000 2026]: תמצית הסקירה השבועית 12.07.26: 1. שווקים ונפט 🌎- מחירי הנפט ירדו לקראת הסופ"ש, אך עדיין סגרו את השבוע בעלייה של כ- 5.4%+, על רקע חששות השווקים מחזרה למלחמה במזרח התיכון. ארה"ב הכריזה כי הפסקת האש עם איראן 'הסתיימה' (over), והציבה לאיראן מועד אחרון (ליום שבת) להכרה פומבית בכך שמיצרי הורמוז יוותרו פתוחים לשיט. ✅חרף הסלמת המתיחות במזה"ת, מדד הנאסד"ק עלה השבוע ב- 1.7%, על רקע ידיעות חיוביות ממגזר הטכנולוגיה.

@matanshitrit [Sun Jul 19 15:30:39 +0000 2026]: מדד המחירים לצרכן ביוני סימן כנראה את התחתית, לפחות על בסיס התפתחות האינפלציה השנתית ב-12 חודשים קדימה לפי ממוצע החזאים בשוק (כלכלנים). לניתוח מלא של מדד המחירים לצרכן בישראל, מדד מחירי הדיור, שוק המשכנתא "הרותח" ועוד...מוזמנים לצפות בסקירה השבועית 👇🏻 https://t.co/MWvXm5RtTH

@matanshitrit [Wed Jul 15 15:42:57 +0000 2026]: מדד מחירי הדירות בעסקאות אפריל-מאי ירד ב-1.0%, והשלים ירידה של 2.0% בשנה האחרונה. מחוז ת"א מוביל עם ירידה חודשית של 2.3%, ואחריו ירושלים עם ירידה של 1.8%. מדד מחירי הדירות החדשות בניכוי משתכן (שוק חופשי) - עלה ב-0.2%. כן כן עלה...טוב נו, לפחות המדד הכללי ירד. https://t.co/4ilJHyuaOW

@matanshitrit [Mon Jul 13 06:24:58 +0000 2026]: 11 מיליארד שקל משכנתאות בחודש יוני - השוק רותח? לא כל כך מהר נתחיל מהשורה התחתונה - השוק לא רותח, ונתוני המשכנתאות לא מבשרים על שינוי כיוון. הסיבה פשוטה - מדובר בנתון שמגיב בפיגור לעסקאות בשוק הדיור. לפי בנק ישראל, הפיגור עומד על כ-6-9 חודשים. כלומר, אם רוצים להבין מה קורה עכשיו בשוק הדיור, עדיף להסתכל על מספר העסקאות בפועל. הנתונים זמינים כרגע עד אפריל, ומחר צפוי להתפרסם נתון מאי (הלמ״ס). עד כה, מספר העסקאות המשיך להתקרר בחודשים האחרונים. בהינתן הפיגור שבנק ישראל מציין, אם נלך 6 חודשים אחורה (ומעלה) במספר עסקאות הנדל"ן, נראה שבנובמבר ובדצמבר האחרונים נרשמו כ-8 ו-9 אלף עסקאות, בהתאמה. לאחר מכן, ברבעון הראשון של 2026, הממוצע החודשי כבר ירד לכ-7.6 אלף עסקאות, ובאפריל האחרון עמד הנתון על כ-5.1 אלף. אלא שההתקררות הזו עדיין לא אמורה להשתקף במלואה בנתוני המשכנתאות. ואכן, הפיגור שבנק ישראל מתאר עשוי להסביר את נתוני חודש יוני בשוק המשכנתאות. אז מה היה לנו? • סך המשכנתאות שנטלו הסתכם בכ-11 מיליארד שקל. • מתוך זה, כ-1.625 מיליארד שקל היו הלוואות בולט/בלון. • כ-0.85 מיליארד שקל היו מחזור חיצוני. ומה לגבי מחזור פנימי? הוא לא נכלל בנתון הזה, ומתפרסם בנפרד. אחת הטענות שעולות היא שהלוואות הקבלן "נספרות פעמיים" בתוך נתון ה-11 מיליארד. אבל לפי מה שאני מכיר, את הלוואות הקבלן יש למחזר באותו בנק - כך שבהגדרה מדובר במחזור פנימי, וכאמור, מחזורים פנימיים אינם נכללים בנתון הזה. בניכוי הלוואות הבולט/בלון והמחזור החיצוני, סך המשכנתאות שניטלו ביוני הסתכם בכ-8.58 מיליארד שקל. וזה כבר מסתדר הרבה יותר טוב עם הפיגור הסטטיסטי מול העסקאות שנחתמו כמה חודשים קודם לכן. בשורה התחתונה, להערכתי הנתונים האלה לא מבשרים על שינוי כיוון בשוק הדיור. להפך - ההתקררות בשוק המשכנתאות עוד לפנינו, לפחות בכל הנוגע למשכנתאות בגין עסקאות חדשות. מחזורים, חיצוניים ופנימיים, ייתכן שדווקא יעלו בהמשך לאור הפחתות הריבית (והלוואות הקבלן כאמור שהם חלק מהמחזורים הפנימיים), אבל זה כבר סיפור אחר. בנוסף, חשוב לזכור שהנתון שפורסם הוא במונחי כסף, ולא במונחי מספר הלוואות/עסקאות - אלה יתפרסמו רק בסוף החודש. אמנם אם נניח שהמשכנתא הממוצעת עדיין עומדת סביב 1.1 מיליון שקל, המספרים עדיין גבוהים יחסית לחודשים האחרונים, אבל גם כאן, ייתכן מאוד שהם בעיקר משקפים עסקאות שנחתמו סביב נובמבר-דצמבר, ולא שינוי כיוון בשוק הנוכחי.

@matanshitrit [Sun Jul 12 17:08:40 +0000 2026]: שבוע מדדים יוצא לדרך (ארה״ב וישראל) עונת הדוחות בוול סטריט לרבעון השני יוצאת לדרך גם היא - עם פרסום תוצאות של בנקים, נטפליקס, asml ועוד https://t.co/4AydpY0HgM

@fundercoil [Tue Jul 21 14:28:31 +0000 2026]: לקראת פרסום הדוחות של אלפאבית - גוגל https://t.co/ToqufilI1i

@SponserNews [Wed Jul 22 05:04:50 +0000 2026]: ”לאור תנאי השוק”: אלקטרה נדל”ן מבטלת את ההנפקה אחרי ירידת המניה: אחרי שהמניה איבדה גובה, ואחרי שחברת האם, אלקו לא הודיעה שתשתתף בגיוס ההון - החברה מודיעה כי החליטה שלא להציע את ניירות הערך לציבור ולא לקיים את המכרז https://t.co/HttoVNF860

@SponserNews [Tue Jul 21 08:51:04 +0000 2026]: אלקטרה נדל”ן צונחת ברקע לכוונתה לגייס הון במניות: כל יחידה תכלול 20 מניות רגילות, במחיר למניה שלא יפחת מ-40.14 שקל, ו-10 כתבי אופציה (סדרה 3), ללא תמורה https://t.co/WQbThdDwMw

@calcalist [Tue Jul 21 17:10:00 +0000 2026]: ירידה של 23% במחיר: העסקה ברמת השרון שמעידה על הקיפאון בשוק הנדל"ן https://t.co/tVNBMzmvnG @gazitamitai https://t.co/PdKECaA4K4

@TheMarker [Tue Jul 21 23:00:12 +0000 2026]: לשבור את המצור: לאט לאט, העולם עוקף את משבר הנפט בהורמוז https://t.co/S5taiTeHDL

@ModiShafrir [Thu Jul 02 12:53:08 +0000 2026]: נתוני התעסוקה ב- 🇺🇸 של חודש יוני היו חלשים מהציפיות, כך שהשוק מתמחר עתה הסתברות נמוכה (20%) להעלאת ריבית הפד בחודש יוני, והסתברות של כ- 62% להעלאה בספטמבר: ✅ דו"ח ה NFP הצביע על תוספת של 57 אלף עובדים ביוני (צפי ל- 113+ אלף), שאת לאחר שנתוני החודשיים הקודמים עודכנו כלפי מטה בחדות (-74 אלף משרות). ✅ סקר כח האדם הצביע אמנם על ירידת שיעור האבטלה ל- 4.2% (צפי ל- 4.3%), אך זאת במקביל לירידה חדה מאד בשיעור ההשתתפות בכח העבודה (היצע העובדים) , כך שלפי סקר זה בחודש יוני נגרעו כ- 507 אלף עובדים... בגרף ניתן לראות שבכ- 5 מתוך 6 החודשים האחרונים נרשמה, לפי סקר זה, התכווצות במספר העובדים בשוק התעסוקה. 1/

@ModiShafrir [Sun Jun 28 10:22:08 +0000 2026]: תמצית הסקירה השבועית 28.06.26: 1. שווקים ונפט 🌎- מחירי הנפט ירדו השבוע בחדות (10.6%- למחיר חבית Brent) לרמתם ערב המלחמה עם איראן, על רקע עלייה במספר המכליות שעברו במצר הורמוז ומתן רישיון אמריקאי לאיראן למכור נפט בשוק הבינלאומי לתקופה של 60 יום. בכירים בממשל האמריקאי הבהירו כי איראן לא תגבה דמי מעבר (tolls) במצר הורמוז, כך שגברו ההערכות כי שרשראות האספקה בעולם יחזרו למצבן טרום המלחמה. 2. עם זאת, חששות מהסלמה במצר הורמוז שבו ועלו בסופ"ש, על רקע פגיעה במכלית נפט, תקיפה אמריקאית מנגד ודיווח של בחריין על תקיפת כטב"מים איראניים.

@ModiShafrir [Wed Jun 24 13:42:49 +0000 2026]: פערי הריבית בעולם (לדוג' בין ארה"ב לאירופה) תומכים בהתחזקות הדולר בעולם... - בהמשך לשיחה בערוץ הכלכלה - ראו בגרף https://t.co/TIFrYG0Fdy

@matanshitrit [Mon Jul 20 11:43:56 +0000 2026]: הזיכרון של הציבור הישראלי קצר יותר מהריבית של בנק ישראל? https://t.co/QFZb52RALO

@fundercoil [Wed Jul 22 04:55:19 +0000 2026]: האם עידן ה-AI היקר מתקרב לסיומו? https://t.co/nmsr3RzAux

@fundercoil [Tue Jul 21 16:31:03 +0000 2026]: יום המסחר הסתיים בעליות שערים בבורסה https://t.co/GILifG6tPC

@fundercoil [Tue Jul 21 14:26:01 +0000 2026]: בנקי ההשקעות על מגזר השבבים: מדד ה-SOX בדרך למכירות יתר – הזדמנות קנייה או איתור האטה? https://t.co/YwFRqTIEZF

@SponserNews [Tue Jul 21 13:11:05 +0000 2026]: הבורסה של לונדון תשיק פלטפורמת מסחר 24 שעות ביממה: בורסת לונדון (LSE) תאפשר מסחר כמעט רציף בימי חול ותכוון לדור החדש של מסחר דיגיטלי ואלגוריתמי; השקת המסחר במוצרי סל מתוכננת למחצית הראשונה של 2027, בכפוף לאישור רגולטורי https://t.co/x1ibFi56Fq

@SponserNews [Tue Jul 21 08:42:17 +0000 2026]: תקבל 62 מיליון שקל: אפקון השלימה את הצעת רכש החליפין למחזיקי כתבי האופציה: שיעור ההיענות הגבוה, שעמד מעל ל-95%, משקף את האמון הרב של מחזיקי כתבי האופציה בחברה ובמהלכיה האסטרטגיים https://t.co/sZztN5tsTc

@SponserNews [Tue Jul 21 07:35:58 +0000 2026]: מיטב במו”מ להשקעה בנופר ישראל לפי שווי של 2.1 מיליארד שקל: לפי מזכר ההבנות מיטב תשקיע 200 מיליון שקל בנופר ישראל כנגד 8.7% מהמניות https://t.co/NUbu5hgERq

@SponserNews [Tue Jul 21 07:27:06 +0000 2026]: נקסט-ויז’ן דיווחה על הזמנה נוספת מצד שלישי בסך 6.7 מיליון דולר: שיעור של 15% מהתמורה שולם כמקדמה. יתרת התמורה תשולם בתנאי תשלום של שוטף + 30 לאחר אספקת המוצרים ללקוח https://t.co/U9mF6BU6zD

@globesnews [Wed Jul 22 03:04:47 +0000 2026]: בלי להוציא שקל מהקופה: כך רכש מיטב את מניות הציבור בפנינסולה https://t.co/FCaQl8OnF1 https://t.co/9TlWK7yk7v

@globesnews [Wed Jul 22 03:04:31 +0000 2026]: פרטנר מציגה: לחלק דיבידנד שימומן בחוב, גם כשלא עומדים במבחן הרווח https://t.co/dCxG8cgCsC https://t.co/TJiyYrjc03

@TheMarker [Wed Jul 22 02:00:11 +0000 2026]: הגבלות על מכירת מניות ספייס־אקס יבוטלו, ומכירה של 116 מיליארד דולר תחל https://t.co/6xpGTCxUYV

@TheMarker [Wed Jul 22 01:00:16 +0000 2026]: מטבע בלי מצנח: ממשלת טורקיה תאפשר ללירה ליפול במהירות https://t.co/EXnYt10tg6

@matanshitrit [Tue Jul 14 12:31:43 +0000 2026]: מדד ארה״ב - הפתיע חזק כלפי מטה https://t.co/XkS58o8wzc

@fundercoil [Tue Jul 21 19:41:49 +0000 2026]: תוכנית פרישה מרצון בבנק הבינלאומי לצורך התייעלות - עשרות עובדים צפויים לפרוש https://t.co/EnlOvMt0zG

@fundercoil [Tue Jul 21 15:04:28 +0000 2026]: הלקח שכל עסק משפחתי צריך להפנים: לוותר מראש על העברה בין דורית https://t.co/TX57wqabQh

@fundercoil [Tue Jul 21 15:01:56 +0000 2026]: מיטב בית השקעות השלימה הצעת רכש מלאה למניות פנינסולה - תהפוך להיות חברה פרטית מדווחת ומניותיה ימחקו מהמסחר https://t.co/fIKmCjRd9G

@fundercoil [Tue Jul 21 14:59:25 +0000 2026]: הדאטה סנטרים לא חייבים לחכות לרשת החשמל https://t.co/kQ3Ttcx6qz

@fundercoil [Tue Jul 21 14:56:54 +0000 2026]: רשות שוק ההון עושה סדר בשוק הקריפטו הישראלי ומחייבת הפרדה מלאה בין כספי הציבור לכספי החברות https://t.co/8pcfvrrgEl

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.