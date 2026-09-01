אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות בלבד, והחזר JSON בלבד.

You are a senior investment advisor writing a signature END-OF-DAY review in Hebrew for the
TEL AVIV STOCK EXCHANGE (הבורסה לניירות ערך בתל אביב) for 2026-08-31 (יום שני). PAST TENSE.

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
  "title": "סיכום יום המסחר בבורסה בתל אביב 🇮🇱 – יום שני, 31.8.2026",
  "date": "2026-08-31",
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
* שיא בשווי השוק לפני הפתיחה: חודש יולי ננעל בבורסה בתל אביב בעליות בהובלת מניות הבנקים, ושווי השוק הכולל טיפס לשיא של מעל 3 טריליון שקל. לפי דיווחים, תעשיית קרנות הנאמנות גייסה ביולי כ-3.1 עד 3.3 מיליארד שקל בגיוס נטו, בהובלת הקרנות הכספיות והאג"ח המקומי. הכסף המקומי ממשיך לזרום אל השוק, וזו נקודת פתיחה תומכת לקראת יום המסחר.
* רגיעה מול איראן ומחיר הנפט צונח: הנשיא טראמפ מסר כי השיחות עם איראן יתחדשו, לצד הסברים מדוע ביטל את התקיפה. על רקע זה יורד מחיר הנפט לכ-83 דולר לחבית, ירידה של כ-4%. עבור המשקיע המקומי זהו שילוב נדיר של הפחתת פרמיית הסיכון הגיאופוליטית יחד עם הוזלת תשומה מרכזית במשק, ושני הגורמים פועלים לטובת אפיקי הסיכון בתל אביב.
* שני מדדי מחירים גבוהים לפנינו: מחיר הדלק הרשמי לאוגוסט זינק ל-8.09 שקלים לליטר, עלייה של 61 אגורות שהן כ-8% לעומת החודש הקודם. קונצנזוס החזאים עומד על כ-0.3% למדד יולי וכ-1.0% למדד אוגוסט, כלומר שני מדדים גבוהים ממתינים למשק. זהו הגורם שעלול להאט את קצב הורדות הריבית של בנק ישראל, גם אם האינפלציה השנתית אינה צפויה להאיץ בשלב הזה.
* לידר מזהיר מהאפיקים הארוכים: בלידר מציינים כי למרות האטרקטיביות שבשוק האג"ח המקומי, רמת אי הוודאות הגיאופוליטית והפוליטית הגבוהה יחד עם לחץ לעליית תשואות בחו"ל עלולים להעיב דווקא על האפיקים הארוכים. להערכתם, הורדת הריבית הבאה תידחה עד לרגיעה מסוימת במצב הגיאופוליטי. זו תזכורת שהתמחור בשוק המקומי כבול לזירה הביטחונית לא פחות מאשר לנתוני האינפלציה.
* מניית הפניקס מגדילה אחזקה בפאוורג'ן: הפניקס תזרים כ-234 מיליון שקל לזרוע האנרגיה המתחדשת פאוורג'ן ותגדיל את אחזקותיה ל-12.4%, לפי שווי חברה של 3.25 מיליארד שקל. במקביל נחתמו הבנות עם משקיעים מוסדיים נוספים להשקעה של עד 800 מיליון שקל, וג'נריישן צפויה לרשום רווח של עד 320 מיליון שקל. העסקה ממחישה את התיאבון המוסדי הגובר לתשתיות אנרגיה מתחדשת בשוק המקומי.
* מניית נאוויטס מתרחבת במפרץ אמריקה: לפי דיווחים, נאוויטס רוכשת 33% משתי תגליות נפט, טיבריוס ולוגן, מענקיות האנרגיה אוקסידנטל וקוסמוס. גדעון תדמור ציין כי הפרויקט סינרגטי לבקסקין וצפוי להפיק באמצעות מתקן הפקה המשמש כמרכז אזורי. עבור המשקיעים מדובר בהעמקת הנוכחות של החברה בזירה האמריקאית תוך הישענות על תשתית הפקה קיימת במקום הקמה מאפס.
* עונת הדוחות עוברת הילוך: השבוע צפוי להיות עמוס במיוחד בבורסה בתל אביב, עם פרסום דוחות של עשרות חברות ממגוון ענפים, מטכנולוגיה ושבבים דרך נדל"ן ואנרגיה ועד מזון ותעשייה. ריכוז כזה של דיווחים בתוך שבוע אחד מגדיל את הסיכוי לתנודתיות חדה ברמת המניה הבודדת. המשקיעים יעקבו אחר החברות שירכזו את תשומת הלב ואחר ההפתעות בשורה התחתונה.
* מניית מאסיבית בדרך להודו: לפי דיווחים, מאסיבית חתמה על מזכר הבנות ראשוני עם Lohia Aerospace ההודית, שתקבל בלעדיות של שנתיים ותתחייב ליעדי רכישה. עם זאת, ההסכם אינו מחייב בשלב זה, וכל הציוד והקניין הרוחני יישארו בידי מאסיבית. הפער בין ההצהרה לבין הכנסות בפועל הוא בדיוק מה שראוי לבחון לפני שמתמחרים את הידיעה.
* שורה תחתונה: כיוון המסחר בתל אביב ייקבע היום לפי השאלה האם הרגיעה בחזית האיראנית וירידת מחיר הנפט יספיקו כדי להאריך את המומנטום שהעלה את שווי השוק לשיא של מעל 3 טריליון שקל. במקביל, גל הדוחות הכבד של השבוע מסיט את מוקד העניין אל הסיפורים הספציפיים ברמת החברה, בעוד ששני מדדי המחירים הגבוהים הצפויים ממשיכים לרחף מעל תמחור הריבית.
══════════════════════════════════════════════════════════════

מקורות מרשת X (בעברית) — Never mention in the review that these came from posts/X:

@ModiShafrir [Sun Jul 26 08:26:17 +0000 2026]: תמצית הסקירה השבועית 26.07.26: 1. שווקים 🌎 ונפט - מדדי המניות ירדו בחדות ביום חמישי, על רקע הזינוק במחירי הנפט אל מעל ל- 100 דולר ואכזבת המשקיעים מהדוחות של Tesla ו- Alphabet (Google העלתה את תחזית ה- CapEx). https://t.co/BCuDoizbGJ

@ModiShafrir [Tue Jul 14 12:47:53 +0000 2026]: האינפלציה (CPI) ב- 🇺🇸 הפתיעה בחדות כלפי מטה, כך שההסתברות להעלאת ריבית בחודש הקרוב צפויה לרדת, הדולר בעולם נחלש, תשואות ה- Treasuries יורדות, והחוזים על מדדי המניות עולים בחדות יחסית (חרף העלייה הנוספת והחדה במחירי הנפט): ✅האינפלציה (headline) ירדה ביוני ב- 0.4% (צפי ל- 0.1%-). ✅יתרה מכך, ליבת האינפלציה (Core CPI) נותרה לל"ש (צפי ל- 0.2%+), כך שקצב העלייה השנתי התמתן בחדות ל- 2.6%+ YoY (לעומת 2.9%+ במאי). 1/

@matanshitrit [Sun Aug 30 04:56:52 +0000 2026]: סקירה שבועית | הרווחים חזקים, וורש ניצי, ומה יעשה בנק ישראל? אשמח לשיתופים 🫶🏻 השבוע בשווקים - עונת הדוחות בארה"ב מסתיימת עם צמיחת רווחים חזקה משמעותית מהציפיות, אנבידיה ממשיכה לחזק את סיפור ה-AI, ובסקטור התוכנה מתחילה להתחדד ההבחנה בין מנצחות למפסידות מהמהפכה. במקביל, האינפלציה בארה"ב עדיין גבוהה, קווין וורש שולח מסר ניצי מג'קסון הול וספטמבר מגיע עם עונתיות מאתגרת. בישראל נבחן את מצב שוק המניות המקומי ואת התמחור שלו מול ארה"ב, רגע לפני החלטת הריבית של בנק ישראל. לינק לסופטיפיי, אפל פודקאסט, ורשימת נושאים בתגובה. שבוע טוב! https://t.co/dxkNfQxUn7

@matanshitrit [Sun Aug 30 11:32:46 +0000 2026]: מחיר הדלק בישראל עושה ATH, וזאת למרות שמחיר הנפט והדולר ירדו ביחס לחודש הקודם. הסיבה? מרווח הזיקוק, שזינק ביותר מ-40% בתוך חודש. למי שפחות מכיר את המושג "מרווח זיקוק" - זה פשוט הפער בין מחיר הנפט הגולמי לבין המחיר של הדלק שמייצרים ממנו. דוגמא מעולם אחר - נניח שמחיר החיטה יורד, אבל נהיה יקר יותר להפוך אותה ללחם - מחיר הלחם עדיין יכול לעלות. וזה בדיוק מה שקורה עכשיו בדלק - יש פחות יכולת לייצר ולספק מוצרי דלק מזוקקים, בין היתר בגלל שיבושים בבתי זיקוק וביצוא מהמפרץ הפרסי ופגיעות בבתי זיקוק ברוסיה. כתוצאה מכך, עלות הזיקוק עלתה משמעותית. בשורה התחתונה, למרות שהנפט עצמו זול יותר, הדרך להפוך אותו לבנזין התייקרה. להערכתי, תחזיות האנליסטים למדד ספטמבר צפויות להתעדכן מעט כלפי מעלה, אם כי עדיין צפויה ירידה קלה במדד על רקע עונתיות שלילית.

@ModiShafrir [Sun Aug 30 05:59:55 +0000 2026]: תמצית הסקירה השבועית 30.08.26: 1. שווקים 🌎 ונפט - מדדי המניות בארה"ב עלו השבוע קלות, בתמיכת ירידת מחירי הנפט וציפיות הנהלת Nvidia לצמיחה של כ- 70% בהכנסות בשנה הבאה – הערכה אשר הגבירה את אופטימיות המשקיעים כי הצמיחה המואצת בביקושים ל- AI תימשך. https://t.co/koCjf9lyjT

@ModiShafrir [Wed Jul 15 16:50:51 +0000 2026]: מדד חודש יוני נותר לל"ש, בדומה להערכתנו ומעל לממוצע תחזיות החזאים והשוק לירידה של כ- 0.1%. חרף ההפתעה כלפי מעלה (וההאצה במחירי השכירות), האינפלציה השנתית התמתנה ל- 1.60% YoY (לעומת 1.90%+ בחודשיים האחרונים), והתמתנות נרשמה גם במדדי הליבה השונים. מה ההשלכות לגבי ריבית בנק ישראל? 1/

@fundercoil [Mon Aug 31 11:03:23 +0000 2026]: דוחות YBOX למחצית 2026: ההכנסות נסקו ל-84.4 מיליון שקל; ההון העצמי עומד על כ-421 מיליון שקל https://t.co/Lg3t01TH0Y

@SponserNews [Mon Aug 31 10:10:21 +0000 2026]: גילת מגייסת 100 מיליון דולר באג”ח המרה בפרמיה של 60%: חברת הלוויינים גילת גייסה התחייבויות ממשקיעים מוסדיים ישראליים להקצאה פרטית של אג"ח להמרה; הריבית השנתית תעמוד על 3.75%, אך עשויה לעלות ל-5% אם המניה לא תעמוד ביעד https://t.co/C1Re35ex3f

@SponserNews [Mon Aug 31 10:07:50 +0000 2026]: קבוצת לניר בדרך לבורסה: נערכת להנפקה ראשונית של 200 מיליון שקל: חברת האנרגיה והדאטה סנטרים מפרסמת תשקיף ראשון, ומציגה תחזיות אופטימיות במיוחד לצמיחה מטאורית בהכנסות; אלא שהדרך למימוש עוד ארוכה https://t.co/ZfZWH55JFG

@calcalist [Mon Aug 31 10:15:00 +0000 2026]: האינפלציה ירדה, השקל חזק - אז למה הריבית עשויה להישאר במקום? אחרי ארבע הפחתות רצופות, החשש מהוצאות הממשלה ומהבחירות עשוי לגרום לבנק ישראל לקחת פסק זמן https://t.co/yuPRqnKqmK @AdrianFilut https://t.co/wZU8xsO2MN

@ModiShafrir [Wed Jul 29 19:40:39 +0000 2026]: הפד הותיר את הריבית ללא שינוי בטווח של 3.5%–3.75% ברוב של 9 מול 3 מתנגדים אשר תמכו בהעלאה של 25bp (השוק תמחר טרם ההודעה העלאה בהסתברות של כ- 33%). הוועדה הותירה בהודעה את המסר בדבר מחויבותה ליציבות מחירים, לצד הערכה כי הכלכלה צומחת בקצב איתן והאינפלציה עדיין גבוהה מהיעד. ✅ הפד ציין בהודעה את שמות שלושת החברים שתמכו בהעלאת ריבית, כולם נשיאי בנקים אזוריים בעלי זכות הצבעה בשנת 2026: Hammack (קליבלנד), Kashkari (מיניאפוליס) ו-Logan (דאלאס). בהקשר לכך בלטה העובדה כי כל חברי מועצת הנגידים (Governor) תמכו בהותרת הריבית על כנה. יו"ר הפד תמך, כאמור, בהותרת הריבית על כנה, אך המסרים שנקט במסיבת העיתונאים היו יחסית 'ניציים': ✅אמר מספר פעמים במסיבת העיתונאים כי הוועדה נחושה להחזיר את האינפלציה לרמה של 2%, לאחר 5 שנים של אינפלציה גבוהה. ✅הבהיר כי הפד 'לא יהסס לפעול' (won't hesitate to act), וכי קובעי המדיניות יישאו באחריות למאבק באינפלציה. ✅ ווארש אמר כי בעוד שבצד התעסוקה הפד מצליח לעמוד במנדט של תעסוקה מלאה, הפד מצליח הרבה פחות בצד המחירים (The Fed is doing well on the full employment side of its mandate, but we're doing considerably less well on prices). ✅ בנימה 'יונית' יותר, Warsh ציין לחיוב את הירידה בציפיות האינפלציה מאז החלטת הריבית הקודמת, שלטעמו נבעה מהבנת השווקים את מחויבות חברי הוועדה להחזרת האינפלציה אל עבר היעד. ✅בנוסף, ווארש אמר כי הוא שבע רצון מכך שהשווקים עושים חלק מהעבודה עבור קובעי המדיניות (בהתייחסו לעליית התשואות החדה בתקופה האחרונה). לסיכום - חרף הנימה ה'ניצית' של יו"ר הפד, התשואות בטווחים הקצרים דווקא ירדו במהלך מסיבת העיתונאים והשוק מתמחר עתה העלאת ריבית בספטמבר בהסתברות של 57% בלבד, וסך הכל 1.25 העלאות ריבית בשנת 2026

@matanshitrit [Mon Aug 31 06:34:50 +0000 2026]: העדכון החודש (יולי 26) - מסלולי S&P 500 מול מסלולי מניות ישראל במוצרים השונים בגופים המוסדיים (לא כולל קרנות מחקות וקרנות סל) במסלולי עוקבי S&P500, סך הניודים נטו הסתכם ביולי במינוס 673 מיליון שקל - כלומר, יציאה נטו של 673 מיליון שקל. מדובר בתנועה נטו שלילית, אך זו היציאה הנמוכה ביותר מאז ספטמבר 2025. בפירוט התנועות - מצד אחד, נוידו החוצה כ-700 מיליון שקל, ואילו מצד שני, נוידו פנימה כ-26 מיליון שקל בלבד. גם במסלולי מניות ישראל נרשמה התמתנות בקצב הכניסות. סך הניודים נטו הסתכם ביולי בכ-88 מיליון שקל - התנועה החיובית הנמוכה ביותר מאז נובמבר 2024. מצד אחד, נוידו פנימה כ-192 מיליון שקל, ואילו מצד שני, נוידו החוצה כ-103 מיליון שקל. מבחינת ביצועים במונחים שקליים - בחודש יולי מדד ת"א 125 רשם ביצועי חסר של כ-0.9% מול המדד האמריקאי, בהמשך לביצועי חסר משמעותיים יותר של כ-14% בחודש יוני. אגב, מאז תחילת פברואר מדד ת"א 125 לא עשה כלום, בעוד המדד האמריקאי הניב כ-8% במונחים שקליים. במהלך אותה תקופה נוידו החוצה כ-9 מיליארד שקל ממסלולי S&P 500, בעוד שמסלולי מניות ישראל קלטו פנימה ניודים בהיקף של כ-4.3 מיליארד שקל. בשורה התחתונה, המגמה אמנם ממשיכה, אך ביולי כבר רואים התמתנות משמעותית בשני הכיוונים - פחות יציאות מה-S&P 500, ופחות כניסות למניות ישראל.

@fundercoil [Mon Aug 31 11:21:15 +0000 2026]: גילת מודיעה על הנפקה פרטית של אג"ח להמרה לחמש שנים בהיקף של 100 מיליון דולר ובפרמיית המרה של 60% https://t.co/bgKZJKXhty

@SponserNews [Mon Aug 31 10:16:52 +0000 2026]: מפעל של מזומנים או אירוע חד-פעמי? אולטרייד מציגה זינוק בהכנסות: חברת המיחזור לפסולת אלקטרונית מסכמת חציון ראשון כחברה ציבורית עם עלייה של 123% בהכנסות וזינוק ברווח הנקי https://t.co/6EY2qxDQfe

@ModiShafrir [Sun Jul 19 05:59:07 +0000 2026]: תמצית הסקירה השבועית 19.07.26 1. שווקים 🌎 ונפט - מניות השבבים ה- AI ירדו ביום שישי בחדות, על רקע דחיית השקת המודל החדש של Gemini, העלאת תחזית ההשקעות (capex) של TSMC, והשקת מודל ה- Kimi K3 של Moonshot הסינית, אשר עוררה חששות כי מודלים סיניים זולים ישחקו את הביקוש לשבבים בארה"ב (בדומה ל'הלם DeepSeek' מתחילת 2025).

@ModiShafrir [Sun Jul 12 08:08:23 +0000 2026]: תמצית הסקירה השבועית 12.07.26: 1. שווקים ונפט 🌎- מחירי הנפט ירדו לקראת הסופ"ש, אך עדיין סגרו את השבוע בעלייה של כ- 5.4%+, על רקע חששות השווקים מחזרה למלחמה במזרח התיכון. ארה"ב הכריזה כי הפסקת האש עם איראן 'הסתיימה' (over), והציבה לאיראן מועד אחרון (ליום שבת) להכרה פומבית בכך שמיצרי הורמוז יוותרו פתוחים לשיט. ✅חרף הסלמת המתיחות במזה"ת, מדד הנאסד"ק עלה השבוע ב- 1.7%, על רקע ידיעות חיוביות ממגזר הטכנולוגיה.

@fundercoil [Mon Aug 31 11:55:31 +0000 2026]: סקירת מאקרו: וורש הגביר את הציפיות להעלאת ריבית, אך חיזק את האמינות של ה-Fed https://t.co/3LEVBEfpxE

@fundercoil [Mon Aug 31 10:49:37 +0000 2026]: מבט לוול סטריט: באפולו מעריכים כי הריביות יצנחו ב-2027 בשל ה-AI https://t.co/IDZSngkSdS

@SponserNews [Mon Aug 31 13:42:10 +0000 2026]: לקראת ההודעה מחר: צפי להפחתת ריבית בישראל, אך המגמה קרובה למיצוי: סביר להניח כי בנק ישראל יימנע מלשנות את הריבית בהחלטה באוקטובר, שבוע לפני הבחירות https://t.co/abYxQGmFT0

@SponserNews [Mon Aug 31 11:58:33 +0000 2026]: פלסאנמור מסכמת מחצית: צמיחה בהכנסות, ההפסד העמיק ל-35 מיליון שקל: חברת האולטרסאונד הביתית מציגה גידול במכירות אך הפסד מעמיק בצל הזינוק בהוצאות המימון ושריפת המזומנים השוטפת https://t.co/VSekpUQw1M

@SponserNews [Mon Aug 31 09:23:13 +0000 2026]: צמיחה במחיר כבד: הכנסות ג’ין טכנולוגיות זינקו, אך ההפסד התפעולי העמיק: חברת הטכנולוגיה מציגה קפיצה משמעותית במכירות במחצית, אך המודל העסקי הנוכחי שורף מזומנים בקצב מוגבר. ככל שהיקף הפעילות גדל, ההפסד התפעולי תופח, והדרך לגיוס הון נוסף נראית קרובה https://t.co/J7BeJnjrXi

@SponserNews [Mon Aug 31 08:29:52 +0000 2026]: עסקת ענק ביטחונית: ישראל תקים ליוון מערך הגנה ב-10 מיליארד שקל: ישראל תספק מערך הגנה רב שכבתית ביוון, הכולל ארכיטקטורת מערכות ישראליות, בהן מערכות ’קלע דוד’ ו’ספיידר’ מתוצרת רפאל ומערכת ’BARAK MX’ מתוצרת התעשייה האווירית IAI https://t.co/g8kDQaWEai

@SponserNews [Mon Aug 31 08:21:19 +0000 2026]: טורבוג’ן הופכת דואלית בנאסד”ק, מגייסת 5 מיליון דולר: חברת האנרגיה הישראלית טורבוג’ן תחל להיסחר בנאסד"ק לצד תל אביב, לאחר השלמת גיוס הון פרטי במטרה להרחיב את פעילותה בשוק האמריקאי https://t.co/iiltzyWL3v

@globesnews [Tue Sep 01 03:10:58 +0000 2026]: הורדה או עמדת המתנה? מה צפוי בהחלטת הריבית של בנק ישראל https://t.co/ZXeRRoH94e https://t.co/Jl9t7fj6C9

@calcalist [Mon Aug 31 07:00:00 +0000 2026]: דויטשה בנק: ישראל בין שלוש הכלכלות החשופות ביותר בעולם לשיבושי AI דו"ח של ענקית הבנקאות הגרמנית מצא שבישראל ישנו שילוב חריג של שוק עבודה שחשוף מאוד ל־AI במקביל לתלות גבוהה ביצוא שירותים. כבר ב־2025 קטן מספר עובדי המו"פ בישראל בכ־3,500 – ירידה ראשונה זה כעשור שמיוחסת לשינויים של מהפכת ה־AI https://t.co/tLexoW7SZD @AdrianFilut

@matanshitrit [Sun Aug 30 16:01:41 +0000 2026]: גם בארה"ב מרווחי הזיקוק משפיעים על המחיר - הדיזל מתנהג כאילו מחיר הנפט (WTI) באזור של כ-120$ לחבית. https://t.co/61TvsQ5GsP

@matanshitrit [Fri Aug 28 04:18:44 +0000 2026]: מה ההיסטוריה מלמדת על ההשפעה של עליית תשואות האג״ח על שוק המניות? תשואה גבוהה יותר לא בהכרח אומרת שוק מניות חלש יותר. כשהתשואות עולות לצד צמיחה חזקה ועלייה ברווחי החברות, הרווחים יכולים לקזז חלק גדול מהלחץ על המכפילים. להבדיל, תקופות של ירידת תשואות הגיעו לא פעם על רקע האטה כלכלית או משבר - ובמצבים כאלה גם ביצועי המניות היו בדרך כלל פחות טובים. לכן השאלה היא לא רק לאן התשואה הולכת - אלא למה היא הולכת לשם. עוד מתוך הסקירה שעלתה אתמול 👇

@matanshitrit [Wed Aug 26 12:35:50 +0000 2026]: אינפלציה כללית (PCE) - 3.7% (צפי 3.6%), ליבה בצפי 3.3% https://t.co/rSijFI5SlQ

@matanshitrit [Thu Aug 27 11:51:49 +0000 2026]: מה קורה בשוק האג״ח האמריקאי? אמנם עדיין לא יום ראשון, אבל את כל מה שקורה לאחרונה בשוק האג״ח אין סיכוי לדחוס לתוך סקירה שבועית אחת. אז קיבלתם סקירה ספיישל לסופ״ש - על התשואות הארוכות בארה״ב, הפד, משרד האוצר, החוב האמריקאי, והמשמעות למשקיעים. רשימת נושאים בתיאור הפרק. סופ״ש נעים ! יוטיוב - https://t.co/wPY4NZO1Ce ספוטיפיי - https://t.co/tSPmRQhpGO אפל פודקאסט - https://t.co/bIwJlvnffI

@fundercoil [Mon Aug 31 12:09:01 +0000 2026]: IT – רבעון של ביקושים חזקים הודות ל-AI, כאשר השפעת המט"ח צפויה להכביד פחות בהמשך https://t.co/1KmYlqfBn8

@fundercoil [Mon Aug 31 10:54:01 +0000 2026]: ביטוח תלמידים – מדריך https://t.co/rVrYPpiezb

@fundercoil [Mon Aug 31 09:52:44 +0000 2026]: סקירת דויטשה בנק לשבוע הקרוב: זינוק באנרגיה, האינפלציה באירופה ושוק העבודה האמריקאי https://t.co/fnQW7LMkP4

@SponserNews [Mon Aug 31 08:14:14 +0000 2026]: אנלייט ורפק אנרג’י חותמות על עסקת ענק של 495 מיליון שקל לאספקת חשמל ירוק: הסכם ארוך טווח לאספקת חשמל ממתקנים סולאריים משולבי אגירה, אך חלק מהפרויקטים עדיין בשלבי הקמה וצפויים להתחיל לפעול רק ב-2027 https://t.co/1U932H3wnB

@SponserNews [Mon Aug 31 08:11:43 +0000 2026]: ג’י סיטי מגיעה ל-91% בסיטיקון ומתכננת מחיקה מהמסחר: החברה תפעיל מנגנון Squeeze out ותמחק את סיטיקון מהמסחר בבורסה בפינלנד https://t.co/uoKPRIRZqX

@globesnews [Tue Sep 01 03:10:05 +0000 2026]: מנכ"ל קשת טעמים מכוון לבורסה ועוקץ את המתחרים: "אנחנו לא קורעים את הכיס" https://t.co/ZbWrUeptiQ https://t.co/dDA5XGpFBS

@globesnews [Mon Aug 31 18:04:22 +0000 2026]: צחי נחמיאס בראש, וגם תשובה ברשימה: המסמך שחושף את המרוץ לחוות שרתים https://t.co/FCf9ON57ai https://t.co/urXBXuvBp2

@calcalist [Mon Aug 31 14:17:52 +0000 2026]: המתקנים הושבתו בעקבות רמת עכירות חריגה במי הים. בתל אביב צמצמו את השימוש במים במקלחות בים, בגבעתיים הודיעו כי ייתכנו שיבושים וביקשו מהתושבים לחסוך במים

@calcalist [Mon Aug 31 12:21:26 +0000 2026]: גם נכסי היוקרה מתמודדים עם אתגרי ביקוש: במשך חצי שנה לא נמכרה אף דירה בפרויקט היוקרה בתל אביב https://t.co/fVKgXl2JV4 https://t.co/WdZIuUokMO

@calcalist [Mon Aug 31 08:00:02 +0000 2026]: המשקיע הבכיר מזהיר את יזמי ההייטק: אל תתאגדו בישראל משקיע ההון-סיכון הבכיר אורן זאב יוצא במתקפה חריפה נגד תופעת התאגדות הסטארט-אפים בישראל, ומזהיר כי החלטה של יזמים להירשם כחברה ישראלית ולא אמריקאית (בדלוור) עלולה לעלות להם במיליוני דולרים של מיסוי אישי - ובמקרים מסוימים אף לסכן את עצם קיומה של החברה. https://t.co/NwPOmJuCuY

@TheMarker [Tue Sep 01 01:00:11 +0000 2026]: השיח האלים נגד עיתונאים זינק ב–404%: "מכונת הרעל יודעת לסמן מטרה" https://t.co/0zOlbgbrnQ

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.