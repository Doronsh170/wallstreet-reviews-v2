אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are a senior investment advisor writing a signature END-OF-DAY review in Hebrew for the
TEL AVIV STOCK EXCHANGE (הבורסה לניירות ערך בתל אביב) for 2026-07-10 (יום שישי). PAST TENSE.

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
No US market data, no Wall Street framing unless a source raises it, no ISO dates.

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
  "title": "סיכום יום המסחר בבורסה בתל אביב 🇮🇱 – יום שישי, 10.7.2026",
  "date": "2026-07-10",
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

מקורות מרשת X (בעברית) — Never mention in the review that these came from posts/X:

@ModiShafrir [Sun Jun 07 06:06:31 +0000 2026]: תמצית הסקירה השבועית 07.06.26: 1. שווקים 🌏 - לאחר 9 שבועות רצופים של עלייה, מדד ה- S&P 500 ירד השבוע ב- 2.6% על רקע דוח התעסוקה החזק שהגביר את הציפיות להעלאת ריבית הפד ב- 2026, עלייה בחששות המשקיעים באשר לכדאיות הכלכלית של ההשקעות העצומות ב- AI, בין היתר בשל תחזית חלשה של Broadcom להכנסות משבבי ה- AI, ואי וודאות גיאופוליטית.

@ModiShafrir [Sun Jul 05 06:01:20 +0000 2026]: תמצית הסקירה השבועית 05.07.26: 1. שווקים ונפט 🌏- חרף הירידה החדה במניות השבבים (מדד ה- SOX ירד השבוע ב- 4.4%), מדד ה- S&P 500 במשקל שווה (equal weighted) עלה לרמת שיא, בתמיכת ידיעות גיאופוליטיות חיוביות, התבססות מחירי הנפט ברמת שפל של ארבעה חודשים, והתמתנות הציפיות להעלאת ריבית קרובה בארה"ב.

@SponserNews [Thu Jul 09 11:47:13 +0000 2026]: מטריקס נכנסת לתחום הביטחוני-אנרגטי: רוכשת 80% מלאור אנרגיה בכ-73 מיליון שקל: לאור מספקת מערכות חשמל וקרונות שליטה לצה"ל ולתעשיות הביטחוניות; רשמה זינוק ברווח התפעולי וירידה בהתחייבויות ב-2025; הסכם הרכישה כולל אופציות הדדיות לרכישת יתרת המניות https://t.co/qnP9TrjRib

@ModiShafrir [Mon Jul 06 14:43:04 +0000 2026]: ב"י הוריד את הריבית ב- 25bp לרמה של 3.50% (בהתאם להערכתנו, ולהערכת הקונצנזוס). דברי הנגיד במסיבת העיתונאים היו יחסית 'יוניים' (במיוחד בהשוואה להודעת הריבית הקודמת) ✅ הנגיד הדגיש אמנם כי קיימת אי וודאות גדולה מאד סביב עתיד הריבית, וכי ההחלטות התקבלו בהתאם לנתונים שיתפרסמו (Data depended), אך בנימה 'יונית' ציין ש"ככל שציפיות האינפלציה יורדות, ובוודאי אם יתקרבו לגבול התחתון של היעד, הדבר מצדיק מדיניות מוניטרית מרחיבה יותר, ובקצבים מהירים יותר". בנוסף, כמענה לשאלת אחד העיתונאים - הנגיד לא פסל את האפשרות התיאורטית לכך שב"י יוריד את הריבית בפעימה אחת בשיעור של 50bp. ✅ בנימה 'ניצית' יותר - הנגיד ציין את האצת שכר הדירה, והשכר הממוצע וכן את ההתפתחויות האחרונות בתקציב המדינה, כגורמים המחייבים זהירות רבה יותר מצד ב"י. ✅ התייחסות ב"י לעתיד האינפלציה הייתה 'יונית' בהשוואה להודעות הקודמות – בעוד שבהודעות הריבית הקודמות צוין כי " להערכת הוועדה קיימים סיכונים לעלייה מחודשת של האינפלציה", בהודעה הנוכחית ציינו בב"י כי "להערכת הוועדה, קיימים מספר גורמים שיכולים להשפיע בכיוונים מנוגדים על התפתחות האינפלציה". ✅ חטיבת המחקר הורידה את תחזיתה לרמת הריבית בעוד כשנה ל- 3.0% (ריבית ממוצעת ברבעון השני של 2027) – מעט מעל לציפיות השוק לכ- 2.85%. ✅בנימה 'נניצית יותר - הנגיד הזהיר כי עליית תקציב הבטחון מעבר למוסכם תוביל לעלייה חדה בגירעון ולעליית האינפלציה בכ- 0.3% שורה תחתונה – אנו נותרים בינתיים בהערכתנו (התואמת עתה גם את תחזית חטיבת המחקר של ב"י) כי הריבית תעמוד בעוד כשנה על כ- 3.0%.

@ModiShafrir [Sun Jun 21 10:35:21 +0000 2026]: תמצית הסקירה השבועית 21.06.26: 1. שווקים ונפט 🌎 - התמתנות חששות המשקיעים מסטגפלציה הובילה לעליית מדדי המניות בארה"ב ובאירופה, למרות הודעת הריבית ה'ניצית' בארה"ב (אשר הובילה גם להתחזקות הדולר בעולם). https://t.co/EMtkBgnITn

@ModiShafrir [Wed Jun 10 12:47:53 +0000 2026]: על רקע הזינוק במחירי האנרגיה, האינפלציה (CPI) ב- 🇺🇸עלתה במאי ב- 0.47% (צפי ל- 0.50%) ועלייה מתונה מהציפיות נרשמה בליבת מדד ה- CPI – עלתה ב- 0.21% (צפי ל- 0.30%) – אינדיקציה לכך שאינפלציית מחירי האנרגיה לא מתפשטת בינתיים לשאר הכלכלה. 1/ https://t.co/Qh4Ms5vqaf

@SponserNews [Fri Jul 10 07:39:37 +0000 2026]: רימון מגייסת הון בהיקף של כ-400 מיליון שקל בהקצאת מניות פרטית לכלל ביטוח: כספי ההנפקה יחזקו משמעותית את בסיס ההון של החברה ויתמכו בהמשך צמיחה ותנופת פעילות, בין היתר באמצעות רכישות ומיזוגים משמעותיים https://t.co/hbMElP8kZS

@SponserNews [Thu Jul 09 10:08:13 +0000 2026]: בנק ישראל: ירידה בביקוש לאשראי לענפי הבינוי והנדל”ן; האשראי הצרכני מתחזק: הבנקים מדווחים על ירידה בביקוש לאשראי בענפי הבינוי והנדל"ן וצופים שהמגמה תימשך גם ברבעון השלישי. במקביל נרשמה עלייה בביקוש לאשראי צרכני והתייצבות בביקוש למשכנתאות https://t.co/ycsUcz7PA1

@calcalist [Fri Jul 10 07:30:00 +0000 2026]: נגיד בנק ישראל נלחם על הדמוקרטיה למען הכלכלה | @AdrianFilut, מתוך הסיכום השבועי של #מוסף_כלכליסט המשפט החשוב ביותר שאמר השבוע נגיד בנק ישראל לא עסק בריבית, באינפלציה או בתוצר, אלא בחשיבות של שלטון החוק ועצמאות המוסדות הלא־ממשלתיים. כשנשאל על האפשרות שהממשלה לא תכבד את פסיקת בג"ץ בנושא יו"ר הרשות השנייה, השיב אמיר ירון כי "בית המשפט העליון הוא הסמכות העליונה וצריך לכבד את החלטותיו. נקודה". כשנשאל אם להתנהלות כזו עלולות להיות השלכות כלכליות, השיב בפשטות: "ככל שהדבר יחזור על עצמו – זה רע לכלכלה". נגידי בנק ישראל נזהרים בדרך כלל מלהתערב במחלוקות חוקתיות, ודאי בעיצומה של אחת ממערכות הבחירות הסוערות ביותר, תחת ממשלה שמשתלחת נגד פקידים באופן אלים וחסר תקדים. אבל ירון הוכיח השבוע שהוא מבין את גודל השעה, ושעם כל הכבוד להורדת הריבית, שעליה הכריז, הדבר הכי דחוף וחשוב שהוא צריך לעשות, מתוקף היותו האוטוריטה הכלכלית החשובה במשק, הוא להגן על שלטון החוק בקול רם וברור, ולהזכיר שזה לא רק עניין ערכי או דמוקרטי, אלא גם נכס כלכלי.

@matanshitrit [Mon Jul 06 13:15:08 +0000 2026]: שימו לב לקצב הגידול המהיר בשכר הממוצע במשק (מתוך מצגת החלטת הריבית 06/07) בהחלטת הריבית במרץ 2026, שבנק ישראל הותיר את הריבית ללש, הדגישו את ההאצה המחודשת בשכר. היום, השכר מאיץ בקצב הרבה יותר מהיר ממה שהיה בהחלטה במרץ, אבל ממתי שכר משנה לאינפלציה? שנה קדימה 3.0% ריבית. ואגב, שימו לב לשכר הריאלי.... בהצלחה 😅

@matanshitrit [Mon Jul 06 13:03:55 +0000 2026]: בנק ישראל מפחית ריבית ב-25 נ"ב לרמה של 3.50% (בהתאם לציפיות) לפי תחזית חטיבת המחקר - הריבית צפויה להמשיך לרדת לרמה של 3.0% (שנה קדימה), בהתאם למה שמתומחר בשווקים https://t.co/g6qwZ4Ym96

@matanshitrit [Sun Jul 05 07:29:45 +0000 2026]: סקירה שבועית 05/07/26 (לינקים ליוטיוב & ספוטיפיי למטה) אשמח לשיתופים 🫶🏻 רשימת נושאים - • סיכום ביצועים בשווקים הפיננסים וסביבת מכפילים • ⁠מחצית ראשונה מאחורינו, מחצית שניה לפנינו • ⁠שוק העבודה האמריקאי – לא חם ולא קר • ⁠שינוי דמוגרפי בשוק העבודה – פחות עובדים ויותר תלות ב-AI • ⁠תחזיות כלכליות – צמיחה ל-Q2 ואינפלציה יוני • ⁠תמחור ריבית הפד והתבטאויות של חברי פד • ⁠נתוני כלכליים בישראל • ⁠הדו"ח של IMF • ⁠לקראת החלטת הריבית בישראל • ⁠מבט לשבוע הקרוב יוטיוב - https://t.co/RKAbXPJ68L ספוטיפיי - https://t.co/Bpdtarhm4y

@SponserNews [Fri Jul 10 10:53:12 +0000 2026]: האג”ח האמריקאית קוהאן צוללת: רשות ניי”ע חשפה אי-סדרים חמורים ועסקאות בעלי עניין: האג"ח של קוהאן שרק גייסה לאחרונה 412 מיליון שקל מהמוסדיים בישראל צוללת; שני ליקויים חמורים נחשפו במסגרת בדיקה של רשות ניירות ערך https://t.co/po6DmIfQiw

@globesnews [Fri Jul 10 07:21:58 +0000 2026]: למרות המגמה: קרן פימי דוחפת את רפא לבורסה אך מפחיתה את שוויה ב-30% https://t.co/OkLffjKDR1 https://t.co/MYHP2lEqRh

@calcalist [Fri Jul 10 15:00:01 +0000 2026]: מומחיות טכנולוגית כבר לא מספיקה: בעידן ה-AI חברות ההייטק מעניקות משקל גובר ליצירתיות, לחשיבה ביקורתית, ליכולת למידה עצמית ולאמפתיה. מומחים ומנהלי משאבי אנוש מסבירים מדוע הכישורים האנושיים הפכו ליתרון התחרותי המרכזי - ואיך זה משנה את דרכי הגיוס @mayanahumshahl https://t.co/p5Z2pNxEHv

@TheMarker [Fri Jul 10 18:00:14 +0000 2026]: "מכונית פורמלה 1 מלגו ב–1,300 שקל, ואנשים קונים": ביצת הזהב של ערן תור https://t.co/fcpKBuq6DL

@ModiShafrir [Thu Jul 02 12:53:08 +0000 2026]: נתוני התעסוקה ב- 🇺🇸 של חודש יוני היו חלשים מהציפיות, כך שהשוק מתמחר עתה הסתברות נמוכה (20%) להעלאת ריבית הפד בחודש יוני, והסתברות של כ- 62% להעלאה בספטמבר: ✅ דו"ח ה NFP הצביע על תוספת של 57 אלף עובדים ביוני (צפי ל- 113+ אלף), שאת לאחר שנתוני החודשיים הקודמים עודכנו כלפי מטה בחדות (-74 אלף משרות). ✅ סקר כח האדם הצביע אמנם על ירידת שיעור האבטלה ל- 4.2% (צפי ל- 4.3%), אך זאת במקביל לירידה חדה מאד בשיעור ההשתתפות בכח העבודה (היצע העובדים) , כך שלפי סקר זה בחודש יוני נגרעו כ- 507 אלף עובדים... בגרף ניתן לראות שבכ- 5 מתוך 6 החודשים האחרונים נרשמה, לפי סקר זה, התכווצות במספר העובדים בשוק התעסוקה. 1/

@ModiShafrir [Sun Jun 28 10:22:08 +0000 2026]: תמצית הסקירה השבועית 28.06.26: 1. שווקים ונפט 🌎- מחירי הנפט ירדו השבוע בחדות (10.6%- למחיר חבית Brent) לרמתם ערב המלחמה עם איראן, על רקע עלייה במספר המכליות שעברו במצר הורמוז ומתן רישיון אמריקאי לאיראן למכור נפט בשוק הבינלאומי לתקופה של 60 יום. בכירים בממשל האמריקאי הבהירו כי איראן לא תגבה דמי מעבר (tolls) במצר הורמוז, כך שגברו ההערכות כי שרשראות האספקה בעולם יחזרו למצבן טרום המלחמה. 2. עם זאת, חששות מהסלמה במצר הורמוז שבו ועלו בסופ"ש, על רקע פגיעה במכלית נפט, תקיפה אמריקאית מנגד ודיווח של בחריין על תקיפת כטב"מים איראניים.

@ModiShafrir [Wed Jun 24 13:42:49 +0000 2026]: פערי הריבית בעולם (לדוג' בין ארה"ב לאירופה) תומכים בהתחזקות הדולר בעולם... - בהמשך לשיחה בערוץ הכלכלה - ראו בגרף https://t.co/TIFrYG0Fdy

@ModiShafrir [Sun Jun 14 05:07:54 +0000 2026]: תמצית הסקירה השבועית 14.06.26: 1. שווקים ונפט 🌏- הודעת טראמפ על כך שארה"ב ואיראן צפויות לחתום על הסכם הכולל את פתיחת מצר הורמוז הובילה לקראת הסופ"ש לעליות חדות בשוקי המניות, לירידה חדה במחירי הנפט ולירידה חדה יחסית בתשואות אגרות החוב בשווקים המפותחים. https://t.co/dUh0lfvJlf

@matanshitrit [Tue Jul 07 10:46:09 +0000 2026]: רכישות המט״ח של בנק ישראל בחודש יוני - 1 מיליארד דולר https://t.co/DqGIDONdqN

@matanshitrit [Sun Jul 05 17:18:18 +0000 2026]: מחר תתקיים החלטת הריבית של בנק ישראל - לפי התמחור בשוק הריביות (והקונצנזוס), הריבית צפויה לרדת ב-25 נ״ב לרמה של 3.50%. במקביל, חטיבת המחקר תפרסם את סט התחזיות הכלכליות שמתפרסם מידי רבעון, ובנוסף תתקיים מסיבת עיתונאים. לפני מספר ימים, ה-IMF פרסמו סקירה על ישראל, כולל התייחסות למדיניות המוניטרית, עם מסר לבנק ישראל שאין מה למהר עם הפחתות הריבית. בנוסף, הם התייחסו לסיכונים שהולכים ועולים בשוק הנדל״ן (מבחינת החשיפה של הבנקים לשוק). כל זה ועוד בסקירה השבועית שעלתה הבוקר 👇🏻

@calcalist [Fri Jul 10 11:00:03 +0000 2026]: חברות התעופה משתמשות בשיטה הכי איטית בטבע כדי לסדר את הבורדינג, ויש לכך סיבות; #הקברניט סוקר את היסטוריית העלייה למטוסים, מציג את הבעיה שיצרו שרוולי הטרמינל והמטוסים עצמם - ומראה מי באמת אשם https://t.co/7Lw3hdC0zJ

@fundercoil [Fri Jul 10 18:12:34 +0000 2026]: SK Hynix אס.קיי. הייניקס הקוראנית מזנקת ביום המסחר הראשון שלה ב NASDAQ https://t.co/2aQiYoe0kc

@fundercoil [Fri Jul 10 15:05:13 +0000 2026]: המשקיעים יושבים על הגדר, הפיננסים עלו והדולר חזר ל 3.006 - סקירת בורסות יומית https://t.co/9KxG9mKzd8

@fundercoil [Fri Jul 10 09:17:23 +0000 2026]: אקונרג׳י השלימה בהצלחה את השלב המוסדי במסגרת הנפקה של סדרת אג״ח חדשה, סדרה ד׳ https://t.co/LS3dUW3CEj

@fundercoil [Fri Jul 10 09:14:21 +0000 2026]: פריורטק מתקדמת לקראת הנפקה אקסס https://t.co/AkSoJx5oEo

@SponserNews [Fri Jul 10 09:27:37 +0000 2026]: פריורטק מתקדמת לקראת הנפקה אקסס: החברה מעריכה, כי בהנחה שיתקבלו האישורים הנדרשים, ההנפקה תושלם עד לסוף ספטמבר 2026 https://t.co/8fmjgyAChH

@SponserNews [Fri Jul 10 07:48:37 +0000 2026]: פריים אנרג’י קיבלה רישיון אספקת חשמל - תשקיע 4.7 מיליארד שקל בקידום פרויקטים: הרישיון יאפשר לחברה למנף תשתיות וחיבורי חשמל לטובת אספקת חשמל לצרכנים, באמצעות הפרויקטים הקיימים והמתוכננים של החברה בישראל, לרבות בנכסי קבוצת להב https://t.co/1alBuq4ziv

@SponserNews [Thu Jul 09 11:11:13 +0000 2026]: הסלמה אזורית: אזעקות בירדן, תקיפות ליד הכור בבושהר: שיגורים לעבר בחריין ועל סדרת פיצוצים שהרעידו את כוויית, כחלק מתקיפות התגובה האיראניות נגד בעלות בריתה של ארה"ב; הברנט עולה ב-1.4% לרמה של 79 דולר לחבית https://t.co/uCvVNK59FU

@SponserNews [Thu Jul 09 09:59:15 +0000 2026]: השקעות ענק מול היעדר החזר על ההשקעה: האם מתפתחת בועת AI חדשה?: הפרדוקס שמבהיל את המשקיעים בענקיות הטכנולוגיה: מצד אחד, גידול מהותי בהוצאות ההון; מצד שני, הן עצמן טרם ראו החזר מוחשי ומניב על ההשקעה https://t.co/q8JkNIOfco

@globesnews [Fri Jul 10 10:23:45 +0000 2026]: חודש וחצי אחרי סימד, תסבוכת ענק ב-BVI חדשה: אג"ח קוהאן פרופרטיס צוללת ב-19% https://t.co/Qi3bOYJoWS https://t.co/GtwhFC6xxp

@globesnews [Fri Jul 10 08:07:27 +0000 2026]: בתוך ימים: איזי ג'ט החליפה את הרוכש המועדף, המניה מזנקת ב-14% https://t.co/fEA8SImtPi https://t.co/VC0n2iF2aZ

@calcalist [Fri Jul 10 13:00:03 +0000 2026]: שר החינוך שוב מזיק במקום להועיל | @shaharilan, מתוך הסיכום השבועי של #מוסף_כלכליסט שר החינוך יואב קיש יצא השבוע לעוד סיבוב במלחמה המתמשכת שלו באקדמיה. אחרי שבעבר איים בחקיקה שלפיה אם האוניברסיטאות ישבתו במחאה על צעדי הממשלה התקציבים שלהן ייפגעו, עכשיו הוא מתכנן לנצל את הרוב שלו במועצה להשכלה גבוהה כדי שהיא תפרסם גילוי דעת שאוסר על האוניברסיטאות "לנקוט עמדה פוליטית" ודורש "ניטרליות מוסדית". לגילוי הדעת הזה אין משמעות מעשית אמיתית - לפי החוק, למל"ג אין אפשרות להתערב בעניינים כאלה של האוניברסיטאות. אבל זה עוד מעשה בריוני שנועד להלך אימים על מנהלי המוסדות והמערכת האקדמית כולה. הקדנציה של קיש מלווה בכישלונות רבים בזירה האקדמית. העיכוב בהקמת אוניברסיטת תל חי, למשל. הירידה במספר הגברים בקרב הסטודנטים. אבל איכשהו נראה שקיש משוכנע שהכישלון החמור ביותר שלו הוא שלא הצליח למנוע מבכירי האקדמיה להיאבק בצעדים האנטי־דמוקרטיים של הממשלה. כך הוא מפספס את הכישלון הגדול באמת שלו: חוסר היכולת לסייע לאקדמיה להתמודד עם החרם האקדמי הבינלאומי, שאליו הובילה התנהלות הממשלה. עד כמה הוא לא מבין את הכישלון הזה? גילוי הדעת שהוא מבקש להוציא רק יזין את החרם, ויהפוך אותו לשותף של ה־BDS.

@TheMarker [Fri Jul 10 19:00:30 +0000 2026]: נמוך מהמתוכנן: נחשף שווייה של חברת התרופות רפא בהנפקה https://t.co/rMgpGqOc6F

@TheMarker [Fri Jul 10 17:00:37 +0000 2026]: חברת נדל"ן נוספת מארה"ב מסבכת את המשקיעים: אג"ח קוהאן נופלות ב-21% https://t.co/SMz38tXVOR

@TheMarker [Fri Jul 10 16:00:44 +0000 2026]: "אין כמו ת"א, אבל רצינו שהילדים יגדלו בטבע — וגם כאן המחירים קפצו" https://t.co/geokcWpEMi

@ModiShafrir [Mon May 25 13:36:06 +0000 2026]: ב- 🇮🇱 - ב"י הוריד את הריבית ב- 25bp לרמה של 3.75% (בהתאם להערכתנו, ולהערכת מרבית החזאים). עם זאת, הודעת הריבית לא הייתה 'יונית' (לדוג' - ב"י כלל לא להתייחס להשפעה הצפויה של הייסוף החד על הייצוא המקומי). להלן עיקרי הדברים (ונמתין עתה לראיונות לתקשורת של הנגיד ושל בכירי ב"י): 1/ https://t.co/gKQB6dMWgA

@matanshitrit [Wed Jul 08 08:40:19 +0000 2026]: הטיעון המרכזי שאיתו פתחו את החלטת הריבית שלשום - מזכר ההבנות...🫣 https://t.co/GdTa9Wa0LW

@matanshitrit [Mon Jul 06 18:14:58 +0000 2026]: הערב בגלובס - שוק הנדל"ן מהזווית של תושבי החוץ, בהמשך לפוסט האחרון של @Galitbennaim מי שבנה על תושבי החוץ כמנוע התאוששות לשוק הדיור - כנראה יצטרך לחפש מנוע אחר. (החלק שלי נמצא בסוף הכתבה). https://t.co/F5JtGWXsu1

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.