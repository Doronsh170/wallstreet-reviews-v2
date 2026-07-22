אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות בלבד, והחזר JSON בלבד.

You are a senior investment advisor writing a signature END-OF-DAY review in Hebrew for the
TEL AVIV STOCK EXCHANGE (הבורסה לניירות ערך בתל אביב) for 2026-07-22 (יום רביעי). PAST TENSE.

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

THIS REVIEW SUMMARIZES THE CURATED HEBREW SOURCES — it explains the day that ended:
- Content comes EXCLUSIVELY from the source posts at the bottom of this prompt. Do NOT add prices, index
  levels, percentages, movers or macro data that do not appear in a source. A figure (index move, a stock's
  change, a report number) enters ONLY if a source states it explicitly. Web search verifies a name/figure
  already in a source, never adds news of its own.
- Do NOT independently determine who rose or fell. Direction and magnitude for any story come from the source.
- 6-9 STRONG points TOTAL. FIRST point tells the day's story in one narrative (headline like
  "יום ירוק בהובלת הבנקים") from what the sources reported about the session. MIDDLE points — ONE point per
  real story (companies, sectors, reports, Bank of Israel, notable moves) as the sources framed them.
  LAST point — "שורה תחתונה למחר: ..." — what the Tel Aviv investor should watch next session and why.
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
  "title": "סיכום יום המסחר בבורסה בתל אביב 🇮🇱 – יום רביעי, 22.7.2026",
  "date": "2026-07-22",
  "summary": ["כותרת הנקודה: תמצית אמיתית של הנקודה במשפט קצר אחד", "כותרת שנייה: ...", "..."],
  "sections": [
    {
      "heading": "סיכום המסחר",
      "content": "* כותרת קצרה וספציפית: שניים עד ארבעה משפטים של פרוזה אנליטית עם המספרים המרכזיים, ההקשר והמשמעות.\n* כותרת נוספת: ..."
    }
  ]
}
- EXACTLY 1 section. Heading EXACTLY "סיכום המסחר". Title EXACTLY as given above.
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

══ CONTEXT: THIS SESSION'S TEL AVIV PRE-MARKET BRIEFING ══
Published before the session. Use it to resolve what was expected into what happened, do NOT quote it verbatim.

[לקראת יום המסחר]
* סנטימנט זהיר על רקע תמחור מלא: הבורסה בתל אביב נכנסת ליום המסחר של יום שני לאחר שבוע עמוס בגיוסים, הנפקות והורדת ריבית, כשהמשקיעים נותרים סלקטיביים. קול בולט בשוק מזהיר כי אין כיום מגזר אחד בתמחור מעניין וכי הכל יקר מאוד, אמירה שמשקפת חשש מרמות המחירים לאחר תקופה ארוכה של עליות. ברקע ממשיך לרחף נתיב הריבית של בנק ישראל, שהופחתה לאחרונה ל-3.50% בנימה יונית, גורם שתומך בתיאבון לסיכון אך גם מחדד את השאלה על ההצדקה לתמחור הנוכחי.
* מדד יוני במוקד: תשומת הלב הכלכלית לקראת יום שני מופנית אל פרסום מדד המחירים לצרכן לחודש יוני. הכלכלן הראשי של בנק מזרחי טפחות מעריך כי השקל החזק והוזלת מחירי הטיסות יובילו למדד שלילי ביוני, אך מזהיר כי הפיחות שנרשם בשקל בשבועות האחרונים עלול להפוך לגורם אינפלציוני בהמשך. מדד נמוך יחזק את הציפיות להמשך הורדות ריבית, בעוד האזהרה מהפיחות מזכירה שהתמונה האינפלציונית עשויה להתהפך.
* הנדל״ן בזירת הריבית היורדת: בסביבת ריבית יורדת חוזר סקטור הנדל״ן למרכז העניין, והשאלה היא אילו חברות ייהנו יותר, יזמיות בנייה, חברות קניונים או חברות תשתית. ברקע, קרן המטבע הבינלאומית הזהירה בסקירתה על ישראל מפני סיכונים הולכים וגוברים בשוק הנדל״ן ומהחשיפה של הבנקים אליו. המשקיעים נדרשים לאזן בין הרוח הגבית של הריבית הנמוכה לבין אזהרות על תמחור וסיכון אשראי בענף.
* הקוונטום הישראלי לוול סטריט: בסוף השבוע נחשף כי שתי חברות קוונטום ישראליות נמצאות בדרך להנפקה בוול סטריט לפי שווי כולל של כ-5 מיליארד דולר. המהלך ממחיש את המגמה שבה חברות דיפ-טק ישראליות פונות אל השווקים בארה״ב לגיוסי ענק. עבור השוק המקומי זו תזכורת לכוח המשיכה של וול סטריט לחברות הצמיחה, ולשאלת הערך שנותר או שאובד לבורסה בתל אביב.
* שוק ההנפקות נותר רותח: התיאבון בשוק הראשוני המקומי אינו מראה סימני האטה. סמח״ט גולני לשעבר הנפיק חברת רחפנים קטנה בבורסה והצהיר כי אין סיכון למשקיעים ושהשוק רותח, בעוד אקונרג׳י השלימה בהצלחה את השלב המוסדי בהנפקת סדרת אג״ח חדשה. גל ההנפקות והגיוסים ממשיך להעמיד למבחן את הביקוש של המשקיעים, במיוחד כשקולות בשוק מזהירים מפני תמחור מלא.
* השקל ורכישות המט״ח של בנק ישראל: בנק ישראל רכש בחודש יוני מטבע חוץ בהיקף של כמיליארד דולר, המשך למאמץ למתן את התחזקות השקל. לפי הערכת הכלכלן הראשי של מזרחי טפחות, ההשפעה הממתנת של השקל החזק קרובה למיצוי, והפיחות האחרון עלול אף להפוך לאינפלציוני. תנועות המטבע יישארו גורם מרכזי שישפיע הן על היצואנים והן על מדד המחירים הקרוב.
* רקע גלובלי מעורב: בזירה הבינלאומית נקלעה קבוצת פולקסווגן למשבר לאחר צניחה במכירות בסין ובארה״ב, ובחברה מתכננים להפסיק את ייצורם של מחצית מדגמי הקבוצה, הכוללת גם את סקודה ואאודי. מנגד, יצרנית השבבים הקוריאנית SK Hynix זינקה ביום המסחר הראשון שלה בנאסד״ק, המשך לעניין הגובר בשבבים ובבינה מלאכותית. התפתחויות אלו ממחישות עד כמה השוק המקומי רגיש לסנטימנט הגלובלי בטכנולוגיה ובתעשייה.
* שורה תחתונה: כיוון המסחר ביום שני יוכרע במידה רבה מהציפיות לקראת מדד המחירים לחודש יוני ומהפרשנות להמשך נתיב הריבית של בנק ישראל. במקביל יבחנו המשקיעים האם שוק ההנפקות הרותח והנדל״ן הרגיש לריבית ימשיכו למשוך ביקושים, זאת על רקע אזהרות חוזרות כי התמחור בבורסה המקומית מלא.
══════════════════════════════════════════════════════════════

מקורות מרשת X (בעברית) — Never mention in the review that these came from posts/X:

@ModiShafrir [Tue Jul 14 12:47:53 +0000 2026]: האינפלציה (CPI) ב- 🇺🇸 הפתיעה בחדות כלפי מטה, כך שההסתברות להעלאת ריבית בחודש הקרוב צפויה לרדת, הדולר בעולם נחלש, תשואות ה- Treasuries יורדות, והחוזים על מדדי המניות עולים בחדות יחסית (חרף העלייה הנוספת והחדה במחירי הנפט): ✅האינפלציה (headline) ירדה ביוני ב- 0.4% (צפי ל- 0.1%-). ✅יתרה מכך, ליבת האינפלציה (Core CPI) נותרה לל"ש (צפי ל- 0.2%+), כך שקצב העלייה השנתי התמתן בחדות ל- 2.6%+ YoY (לעומת 2.9%+ במאי). 1/

@ModiShafrir [Sun Jul 05 06:01:20 +0000 2026]: תמצית הסקירה השבועית 05.07.26: 1. שווקים ונפט 🌏- חרף הירידה החדה במניות השבבים (מדד ה- SOX ירד השבוע ב- 4.4%), מדד ה- S&P 500 במשקל שווה (equal weighted) עלה לרמת שיא, בתמיכת ידיעות גיאופוליטיות חיוביות, התבססות מחירי הנפט ברמת שפל של ארבעה חודשים, והתמתנות הציפיות להעלאת ריבית קרובה בארה"ב.

@ModiShafrir [Wed Jul 15 16:50:51 +0000 2026]: מדד חודש יוני נותר לל"ש, בדומה להערכתנו ומעל לממוצע תחזיות החזאים והשוק לירידה של כ- 0.1%. חרף ההפתעה כלפי מעלה (וההאצה במחירי השכירות), האינפלציה השנתית התמתנה ל- 1.60% YoY (לעומת 1.90%+ בחודשיים האחרונים), והתמתנות נרשמה גם במדדי הליבה השונים. מה ההשלכות לגבי ריבית בנק ישראל? 1/

@matanshitrit [Sun Jul 19 04:40:31 +0000 2026]: *סקירה שבועית 19/07/26 | מחירי הדירות בישראל בירידה החדה ביותר מזה 8 שנים* אשמח לשיתופים 🫶🏻 לינק ליוטיוב וספוטיפיי למטה שבוע טוב׳ *נושאים* - - סיכום ביצועים בשווקים הפיננסים וסביבת מכפילים - ⁠השווקים לוקחים הפוגה – עונת הדו"חות עוברת למרכז הבמה - ⁠סיכום דו"חות הבנקים, טכנולוגיה ושבבים - מדד המחירים לצרכן בארה"ב מפתיע כלפי מטה - נקודות מרכזיות מתוך העדות של קווין וורש בקונגרס ותמחור ריבית הפד - ⁠פעילות כלכלית בישראל – המדד החודשי לפעילות המשק ושוק העבודה - ⁠שוק הדיור בישראל – משכנתאות, עסקאות ומדד מחירי הדירות - ⁠מדד מחירים לצרכן חודש יוני ותחזית 12 חודשים קדימה - ⁠מבט לשבוע הקרוב – מאקרו ועונת הדו"חות *יוטיוב* – https://t.co/kjm3yUF1O6 *ספוטיפיי* – https://t.co/gtpjExRQ9a

@ModiShafrir [Mon Jul 06 14:43:04 +0000 2026]: ב"י הוריד את הריבית ב- 25bp לרמה של 3.50% (בהתאם להערכתנו, ולהערכת הקונצנזוס). דברי הנגיד במסיבת העיתונאים היו יחסית 'יוניים' (במיוחד בהשוואה להודעת הריבית הקודמת) ✅ הנגיד הדגיש אמנם כי קיימת אי וודאות גדולה מאד סביב עתיד הריבית, וכי ההחלטות התקבלו בהתאם לנתונים שיתפרסמו (Data depended), אך בנימה 'יונית' ציין ש"ככל שציפיות האינפלציה יורדות, ובוודאי אם יתקרבו לגבול התחתון של היעד, הדבר מצדיק מדיניות מוניטרית מרחיבה יותר, ובקצבים מהירים יותר". בנוסף, כמענה לשאלת אחד העיתונאים - הנגיד לא פסל את האפשרות התיאורטית לכך שב"י יוריד את הריבית בפעימה אחת בשיעור של 50bp. ✅ בנימה 'ניצית' יותר - הנגיד ציין את האצת שכר הדירה, והשכר הממוצע וכן את ההתפתחויות האחרונות בתקציב המדינה, כגורמים המחייבים זהירות רבה יותר מצד ב"י. ✅ התייחסות ב"י לעתיד האינפלציה הייתה 'יונית' בהשוואה להודעות הקודמות – בעוד שבהודעות הריבית הקודמות צוין כי " להערכת הוועדה קיימים סיכונים לעלייה מחודשת של האינפלציה", בהודעה הנוכחית ציינו בב"י כי "להערכת הוועדה, קיימים מספר גורמים שיכולים להשפיע בכיוונים מנוגדים על התפתחות האינפלציה". ✅ חטיבת המחקר הורידה את תחזיתה לרמת הריבית בעוד כשנה ל- 3.0% (ריבית ממוצעת ברבעון השני של 2027) – מעט מעל לציפיות השוק לכ- 2.85%. ✅בנימה 'נניצית יותר - הנגיד הזהיר כי עליית תקציב הבטחון מעבר למוסכם תוביל לעלייה חדה בגירעון ולעליית האינפלציה בכ- 0.3% שורה תחתונה – אנו נותרים בינתיים בהערכתנו (התואמת עתה גם את תחזית חטיבת המחקר של ב"י) כי הריבית תעמוד בעוד כשנה על כ- 3.0%.

@matanshitrit [Tue Jul 14 13:39:36 +0000 2026]: אפשר לחזור לשגרה - מלאי הדירות שבידי הקבלנים חזר לעלות. ירושלים בשיא הכושר ופותחת פערים, אך תל אביב לא מוותרת וצמודה מאחור. בצד של העסקאות (הלמ"ס) - סך הדירות החדשות שנמכרו 3,700, אך בניכוי מחיר למשתכן - אלה הסתכמו ב-2,497, המספר הגבוה ביותר מזה חצי שנה, וגבוה בכ-34% בהשוואה למאי אשתקד. לפי האוצר, מאה דירות נרכשו ע"י קרנות ריט, עם הטבות מימון. כמו כן, ת"א בלטה לחיוב במכירות (481 מול 150 במאי אשתקד), כאשר שני פרויקטים בלבד ריכזו 44% מהמכירות באזור זה. אם כבר ת"א, באוצר הוסיפו כי בת"א נרשמה ירידה בשכיחות הטבות מימון (12% מול 24% במאי אשתקד), כאשר חלק משמעותי מהמכירות בת"א (כולל החודשיים הקודמים) התרכז בפרויקט גדול במסגרתו ניתנה הנחה משמעותית במחיר הדירה. מעניין לראות איך ההנחה המשמעותית תבוא לידי ביטוי במדד מחירי הדיור...

@matanshitrit [Tue Jul 14 04:21:37 +0000 2026]: היום ב-15:30 (שעון ישראל) - מדד המחירים לצרכן בארה"ב (CPI) קונצנזוס - ירידה של 0.1% וקצב שנתי 3.8% (לפי CPINowcast 3.9%) https://t.co/mmqJmgBlsk

@fundercoil [Wed Jul 22 12:04:11 +0000 2026]: המסחר הבוקר: עליות בשווקים, הנפט מטפס וציפייה לדוחות אלפבית וטסלה https://t.co/ScKdZBJUEd

@SponserNews [Wed Jul 22 11:16:48 +0000 2026]: הנפט קפץ ל-90 דולר: הנה מה שיקרה לריבית ולאג”ח שלכם: מחיר חבית נפט מסוג ברנט מטפס ב-3.77% לרמה של 94.4 דולר; מחיר חבית WTI עולה ב-3.5% ל-87 דולר לחבית https://t.co/uVT8LezQa9

@ModiShafrir [Sun Jul 19 05:59:07 +0000 2026]: תמצית הסקירה השבועית 19.07.26 1. שווקים 🌎 ונפט - מניות השבבים ה- AI ירדו ביום שישי בחדות, על רקע דחיית השקת המודל החדש של Gemini, העלאת תחזית ההשקעות (capex) של TSMC, והשקת מודל ה- Kimi K3 של Moonshot הסינית, אשר עוררה חששות כי מודלים סיניים זולים ישחקו את הביקוש לשבבים בארה"ב (בדומה ל'הלם DeepSeek' מתחילת 2025).

@ModiShafrir [Sun Jul 12 08:08:23 +0000 2026]: תמצית הסקירה השבועית 12.07.26: 1. שווקים ונפט 🌎- מחירי הנפט ירדו לקראת הסופ"ש, אך עדיין סגרו את השבוע בעלייה של כ- 5.4%+, על רקע חששות השווקים מחזרה למלחמה במזרח התיכון. ארה"ב הכריזה כי הפסקת האש עם איראן 'הסתיימה' (over), והציבה לאיראן מועד אחרון (ליום שבת) להכרה פומבית בכך שמיצרי הורמוז יוותרו פתוחים לשיט. ✅חרף הסלמת המתיחות במזה"ת, מדד הנאסד"ק עלה השבוע ב- 1.7%, על רקע ידיעות חיוביות ממגזר הטכנולוגיה.

@matanshitrit [Sun Jul 19 15:30:39 +0000 2026]: מדד המחירים לצרכן ביוני סימן כנראה את התחתית, לפחות על בסיס התפתחות האינפלציה השנתית ב-12 חודשים קדימה לפי ממוצע החזאים בשוק (כלכלנים). לניתוח מלא של מדד המחירים לצרכן בישראל, מדד מחירי הדיור, שוק המשכנתא "הרותח" ועוד...מוזמנים לצפות בסקירה השבועית 👇🏻 https://t.co/MWvXm5RtTH

@matanshitrit [Wed Jul 15 15:42:57 +0000 2026]: מדד מחירי הדירות בעסקאות אפריל-מאי ירד ב-1.0%, והשלים ירידה של 2.0% בשנה האחרונה. מחוז ת"א מוביל עם ירידה חודשית של 2.3%, ואחריו ירושלים עם ירידה של 1.8%. מדד מחירי הדירות החדשות בניכוי משתכן (שוק חופשי) - עלה ב-0.2%. כן כן עלה...טוב נו, לפחות המדד הכללי ירד. https://t.co/4ilJHyuaOW

@matanshitrit [Mon Jul 13 06:24:58 +0000 2026]: 11 מיליארד שקל משכנתאות בחודש יוני - השוק רותח? לא כל כך מהר נתחיל מהשורה התחתונה - השוק לא רותח, ונתוני המשכנתאות לא מבשרים על שינוי כיוון. הסיבה פשוטה - מדובר בנתון שמגיב בפיגור לעסקאות בשוק הדיור. לפי בנק ישראל, הפיגור עומד על כ-6-9 חודשים. כלומר, אם רוצים להבין מה קורה עכשיו בשוק הדיור, עדיף להסתכל על מספר העסקאות בפועל. הנתונים זמינים כרגע עד אפריל, ומחר צפוי להתפרסם נתון מאי (הלמ״ס). עד כה, מספר העסקאות המשיך להתקרר בחודשים האחרונים. בהינתן הפיגור שבנק ישראל מציין, אם נלך 6 חודשים אחורה (ומעלה) במספר עסקאות הנדל"ן, נראה שבנובמבר ובדצמבר האחרונים נרשמו כ-8 ו-9 אלף עסקאות, בהתאמה. לאחר מכן, ברבעון הראשון של 2026, הממוצע החודשי כבר ירד לכ-7.6 אלף עסקאות, ובאפריל האחרון עמד הנתון על כ-5.1 אלף. אלא שההתקררות הזו עדיין לא אמורה להשתקף במלואה בנתוני המשכנתאות. ואכן, הפיגור שבנק ישראל מתאר עשוי להסביר את נתוני חודש יוני בשוק המשכנתאות. אז מה היה לנו? • סך המשכנתאות שנטלו הסתכם בכ-11 מיליארד שקל. • מתוך זה, כ-1.625 מיליארד שקל היו הלוואות בולט/בלון. • כ-0.85 מיליארד שקל היו מחזור חיצוני. ומה לגבי מחזור פנימי? הוא לא נכלל בנתון הזה, ומתפרסם בנפרד. אחת הטענות שעולות היא שהלוואות הקבלן "נספרות פעמיים" בתוך נתון ה-11 מיליארד. אבל לפי מה שאני מכיר, את הלוואות הקבלן יש למחזר באותו בנק - כך שבהגדרה מדובר במחזור פנימי, וכאמור, מחזורים פנימיים אינם נכללים בנתון הזה. בניכוי הלוואות הבולט/בלון והמחזור החיצוני, סך המשכנתאות שניטלו ביוני הסתכם בכ-8.58 מיליארד שקל. וזה כבר מסתדר הרבה יותר טוב עם הפיגור הסטטיסטי מול העסקאות שנחתמו כמה חודשים קודם לכן. בשורה התחתונה, להערכתי הנתונים האלה לא מבשרים על שינוי כיוון בשוק הדיור. להפך - ההתקררות בשוק המשכנתאות עוד לפנינו, לפחות בכל הנוגע למשכנתאות בגין עסקאות חדשות. מחזורים, חיצוניים ופנימיים, ייתכן שדווקא יעלו בהמשך לאור הפחתות הריבית (והלוואות הקבלן כאמור שהם חלק מהמחזורים הפנימיים), אבל זה כבר סיפור אחר. בנוסף, חשוב לזכור שהנתון שפורסם הוא במונחי כסף, ולא במונחי מספר הלוואות/עסקאות - אלה יתפרסמו רק בסוף החודש. אמנם אם נניח שהמשכנתא הממוצעת עדיין עומדת סביב 1.1 מיליון שקל, המספרים עדיין גבוהים יחסית לחודשים האחרונים, אבל גם כאן, ייתכן מאוד שהם בעיקר משקפים עסקאות שנחתמו סביב נובמבר-דצמבר, ולא שינוי כיוון בשוק הנוכחי.

@matanshitrit [Sun Jul 12 17:08:40 +0000 2026]: שבוע מדדים יוצא לדרך (ארה״ב וישראל) עונת הדוחות בוול סטריט לרבעון השני יוצאת לדרך גם היא - עם פרסום תוצאות של בנקים, נטפליקס, asml ועוד https://t.co/4AydpY0HgM

@fundercoil [Wed Jul 22 13:03:37 +0000 2026]: סקירת Citadel ולארי פינק: מרוץ האנרגיה ל-AI מול הסלמה במפרץ וזינוק בנפט https://t.co/Et207VxWyg

@fundercoil [Wed Jul 22 10:43:22 +0000 2026]: זינוק בסופר מיקרו: הזמנות של יותר מ־60 מיליארד דולר מקפיצות את המניה בכ־15% במסחר המאוחר https://t.co/6pXwVEKQOY

@SponserNews [Wed Jul 22 05:04:50 +0000 2026]: ”לאור תנאי השוק”: אלקטרה נדל”ן מבטלת את ההנפקה אחרי ירידת המניה: אחרי שהמניה איבדה גובה, ואחרי שחברת האם, אלקו לא הודיעה שתשתתף בגיוס ההון - החברה מודיעה כי החליטה שלא להציע את ניירות הערך לציבור ולא לקיים את המכרז https://t.co/HttoVNF860

@TheMarker [Wed Jul 22 13:00:15 +0000 2026]: העליות במסחר התמתנו; השער היציג של הדולר נקבע על 3.06 שקלים https://t.co/kC4uv99qtu

@ModiShafrir [Thu Jul 02 12:53:08 +0000 2026]: נתוני התעסוקה ב- 🇺🇸 של חודש יוני היו חלשים מהציפיות, כך שהשוק מתמחר עתה הסתברות נמוכה (20%) להעלאת ריבית הפד בחודש יוני, והסתברות של כ- 62% להעלאה בספטמבר: ✅ דו"ח ה NFP הצביע על תוספת של 57 אלף עובדים ביוני (צפי ל- 113+ אלף), שאת לאחר שנתוני החודשיים הקודמים עודכנו כלפי מטה בחדות (-74 אלף משרות). ✅ סקר כח האדם הצביע אמנם על ירידת שיעור האבטלה ל- 4.2% (צפי ל- 4.3%), אך זאת במקביל לירידה חדה מאד בשיעור ההשתתפות בכח העבודה (היצע העובדים) , כך שלפי סקר זה בחודש יוני נגרעו כ- 507 אלף עובדים... בגרף ניתן לראות שבכ- 5 מתוך 6 החודשים האחרונים נרשמה, לפי סקר זה, התכווצות במספר העובדים בשוק התעסוקה. 1/

@ModiShafrir [Sun Jun 28 10:22:08 +0000 2026]: תמצית הסקירה השבועית 28.06.26: 1. שווקים ונפט 🌎- מחירי הנפט ירדו השבוע בחדות (10.6%- למחיר חבית Brent) לרמתם ערב המלחמה עם איראן, על רקע עלייה במספר המכליות שעברו במצר הורמוז ומתן רישיון אמריקאי לאיראן למכור נפט בשוק הבינלאומי לתקופה של 60 יום. בכירים בממשל האמריקאי הבהירו כי איראן לא תגבה דמי מעבר (tolls) במצר הורמוז, כך שגברו ההערכות כי שרשראות האספקה בעולם יחזרו למצבן טרום המלחמה. 2. עם זאת, חששות מהסלמה במצר הורמוז שבו ועלו בסופ"ש, על רקע פגיעה במכלית נפט, תקיפה אמריקאית מנגד ודיווח של בחריין על תקיפת כטב"מים איראניים.

@ModiShafrir [Wed Jun 24 13:42:49 +0000 2026]: פערי הריבית בעולם (לדוג' בין ארה"ב לאירופה) תומכים בהתחזקות הדולר בעולם... - בהמשך לשיחה בערוץ הכלכלה - ראו בגרף https://t.co/TIFrYG0Fdy

@matanshitrit [Mon Jul 20 11:43:56 +0000 2026]: הזיכרון של הציבור הישראלי קצר יותר מהריבית של בנק ישראל? https://t.co/QFZb52RALO

@SponserNews [Wed Jul 22 10:06:11 +0000 2026]: מידע פנים? שילמו 100,000 דולר וקבלו את הפוסט של טראמפ לפני כולם: חברת Trump Media הציעה לגבות עד 100,000 דולר בחודש עבור גישה מהירה לפוסטים של טראמפ; סוחרים ומשקיעים חוששים שיצטרכו לשלם לחברה הקשורה לנשיא עצמו כדי לקבל מידע שמשפיע על השוק https://t.co/0fgykC0w7f

@SponserNews [Wed Jul 22 09:40:02 +0000 2026]: מאנדיי הישראלית מפטרת 20% מכוח האדם: אחת מחברות התוכנה הישראליות הבולטות בוול סטריט נאלצת לבצע התאמות לתקופה; במסגרת השינוי הארגוני תפעל החברה לצמצום שכבות הניהול ולהקמת צוותים קטנים, גמישים ואוטונומיים יותר https://t.co/iiuaiom2fw

@globesnews [Wed Jul 22 11:42:37 +0000 2026]: פרשקובסקי משיקה מכרז דיגיטלי למכירת דירות; תשקיע כ־15 מיליון שקל בקמפיין https://t.co/5KG4ZKmFZh https://t.co/3at63MGV8o

@calcalist [Wed Jul 22 12:33:19 +0000 2026]: יוניקורן חדש נולד: סטארט-אפ הסייבר, Glow, כבר שווה 1.2 מיליארד דולר החברה שהוקמה ב-2025, גייסה 100 מיליון דולר בסבב B והפכה ליוניקורן. המנכ"ל רואי טיגר, לשעבר בכיר במטא: "אנחנו רוצים להיות אחת משלוש החברות המובילות שמאבטחות את עמדות הקצה" https://t.co/VQvVlFDquy https://t.co/qXScU9uk0s

@calcalist [Wed Jul 22 10:00:02 +0000 2026]: רפאל והתעשייה האווירית בדרך לעסקת ענק ביוון https://t.co/Fvs6ZxK7I0 @YAzulai https://t.co/WuECAQUQBG

@calcalist [Wed Jul 22 08:08:42 +0000 2026]: קיצוצי ענק במאנדיי: חברת התוכנה הישראלית תפטר 620 עובדים - כ-20% מעובדי החברה. המניה איבדה כ-50% מערכה מתחילת השנה https://t.co/3IaeSmHLls https://t.co/thetMNPZyc

@TheMarker [Wed Jul 22 15:00:12 +0000 2026]: 1.2 מיליארד דולר: הסטארט-אפ החדש של רואי טיגר - והסערה של האקזיט הקודם https://t.co/1VhvYzdRAc

@TheMarker [Wed Jul 22 11:00:10 +0000 2026]: חברת OpenAI חשפה: מודלים שלנו יצאו משליטה ותקפו אתר https://t.co/5g5TwvGux8

@TheMarker [Wed Jul 22 10:00:19 +0000 2026]: משרד הביטחון בוחן רכש של טילי שיוט במאות מיליוני שקלים https://t.co/N8y1w2YkqI

@TheMarker [Wed Jul 22 09:00:11 +0000 2026]: "זה יותר משתיכננו, אבל הפער מדירת חמישה חדרים חדשה היה רק 100 אלף שקל" https://t.co/xQeqwpsFo2

@matanshitrit [Tue Jul 14 12:31:43 +0000 2026]: מדד ארה״ב - הפתיע חזק כלפי מטה https://t.co/XkS58o8wzc

@fundercoil [Wed Jul 22 13:06:06 +0000 2026]: סקירת השווקים של UBS: מהלכי המכסים של טראמפ חוזרים https://t.co/LdNpCVmZA3

@fundercoil [Wed Jul 22 13:01:23 +0000 2026]: התקדמות משמעותית בפרויקט פינוי בינוי באבא הלל רמת גן: רוטשטיין השלימה 100% חתימות https://t.co/yM1mEdPt1o

@fundercoil [Wed Jul 22 12:01:40 +0000 2026]: אב-גד קיבלה היתר בנייה ראשון בפרויקט ההתחדשות העירונית "צלח שלום" בשכונת עמישב בפתח תקווה https://t.co/xbpoOY7QYq

@fundercoil [Wed Jul 22 11:59:11 +0000 2026]: התקדמות באפרודיטה: נחתם מזכר הבנות למכירת כל הגז מהמאגר למצרים https://t.co/wtwhi68hby

@fundercoil [Wed Jul 22 11:56:40 +0000 2026]: הכלכלן הראשי מפרסם סקירה העוסקת בהשתלבות במערכת ההשכלה הגבוהה בישראל https://t.co/hQtUFAQXxa

@fundercoil [Wed Jul 22 08:41:23 +0000 2026]: BTIG מזהירה: תנודתיות חריגה במניות השבבים וסיכון לתיקון עמוק בשווקים https://t.co/Ge6S6tcUAj

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.