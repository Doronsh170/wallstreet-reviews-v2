# סקירות וול סטריט v2 — Market Desk

מערכת סקירות וול סטריט בעברית, **לפי דרישה בלבד**, **ללא שום API של מודל שפה**
(לא OpenAI, לא Claude API, לא Gemini). הקוד אוסף חומר גלם ומאמת בלבד;
את הסקירה עצמה כותבים ידנית ב-Claude / ChatGPT (בצ'אט, לא ב-API).

מצבים עיקריים: `daily_prep` (נקודות לקראת פתיחת המסחר) · `daily_summary` (סיכום יום מסחר) · `weekly_summary` (סיכום שבועי **והכנה לשבוע הבא** — סקירה משולבת אחת) · `intraday_update` (עדכון ביניים — סיכום המקורות מהשעתיים האחרונות, בכל רגע שתרצה) · `daily_digest` (**מבזק מקורות** — מסירה נאמנה בנקודות של מה שהמקורות כתבו, מקובצת לפי נושא, בלי סיכום או פרשנות).

**הסגנון**: כל נקודה נפתחת בכותרת קצרה וספציפית ("מניות השבבים ממשיכות לרכז עניין") ואחריה 2–4 משפטי
פרוזה אנליטית עם הקשר ומשמעות — הסגנון של הסקירות שדורון כותב, לא סיכום חדשות יבש. האתר מדגיש
את הכותרת של כל נקודה אוטומטית.

האתר (`index.html`) קורא **אך ורק** מ-`data.json`.

---

## מבנה הריפו

| קובץ / תיקייה | תפקיד |
|---|---|
| `index.html` | האתר — שלושה טאבים, קורא רק את `data.json` (+ טאב ארכיון שקורא מ-`archive/`) |
| `data.json` | מסד הנתונים של האתר: `dailyPrep` / `intradayUpdate` / `dailySummary` / `weeklySummary` + חגים |
| `archive/` | ארכיון הסקירות: קובץ לכל חודש (`2026-07.json`) + `index.json`. מתעדכן אוטומטית בכל פרסום |
| `gather_review_input.py` | **שלב 1** — איסוף חומר גלם (ציוצים + Finnhub). בלי מודל שפה |
| `raw_review_input.md` | נוצר בשלב 1 — הבלוק שמעתיקים לצ'אט (כולל את כל ההנחיות) |
| `raw_review_input.json` | נוצר בשלב 1 — snapshot נתונים מאומתים לאימות בשלב 3 |
| `review_output.json` | **שלב 2** — לכאן מדביקים את תשובת ה-JSON מהצ'אט |
| `paste_review.py` | **שלב 3** — אימות דטרמיניסטי ופרסום ל-`data.json` |
| `sources/wallstreet.txt` | רשימת חשבונות X/Twitter — מקור יחיד |
| `.github/workflows/gather_review.yml` | הרצת שלב 1 מגיטהאב (בחירת מצב ידנית) |
| `.github/workflows/publish_review.yml` | הרצת שלב 3 אוטומטית אחרי עדכון `review_output.json` |
| `tests/` | בדיקות pytest לשכבת האימות (`paste_review.py`) — הקובץ הקריטי במערכת |
| `.github/workflows/tests.yml` | הרצת הבדיקות אוטומטית על כל שינוי קוד Python |
| `requirements.txt` | `requests` בלבד |

---

## התקנה חד-פעמית

1. **ריפו חדש בגיטהאב** — צור ריפו (למשל `wallstreet-reviews-v2`), העלה את כל תוכן התיקייה כמו שהוא
   (כולל תיקיית `.github` — ודא שהיא לא נשמטת בהעלאה).
2. **GitHub Pages** — Settings → Pages → Deploy from branch → `main` → `/ (root)`.
   האתר יעלה בכתובת `https://<user>.github.io/wallstreet-reviews-v2/`.
3. **Secrets** — Settings → Secrets and variables → Actions → New repository secret:
   - `TWITTER_API_KEY` — המפתח של TwitterAPI.io
   - `FINNHUB_API_KEY` — המפתח של Finnhub

   זהו. **אין** `OPENAI_API_KEY` ואין שום מפתח של מודל שפה.
4. **Permissions ל-Actions** — Settings → Actions → General → Workflow permissions →
   בחר **Read and write permissions** (נדרש כדי שה-workflows יוכלו לעשות commit).

---

## מחזור עבודה מלא (מהדפדפן, כולל מהטלפון)

### שלב 1 — איסוף חומר גלם
Actions → **"1 - Gather Review Input"** → Run workflow → בחר מצב (`daily_prep` / `daily_summary` / `weekly_summary` / `intraday_update` / `daily_digest`).

`intraday_update` הוא סקירה לפי דרישה: מכסה **רק את השעתיים שקדמו לרגע ההרצה** (חדשות, נתוני מאקרו
ותנועות שוק בתוך החלון), עם ציון מצב השוק (פתוח / טרום מסחר / אפטר-מרקט / סגור) ושעת ההרצה בכותרת.
אפשר להריץ אותו כמה פעמים ביום — כל הרצה מחליפה את העדכון הקודם באתר.
בסיום, הקובץ `raw_review_input.md` מעודכן בריפו.

### שלב 2 — כתיבת הסקירה בצ'אט
פתח את `raw_review_input.md` בריפו, העתק את **כל** התוכן, והדבק ב-Claude או ChatGPT
(עם חיפוש אינטרנט מופעל). הקובץ כבר כולל את כל ההנחיות ואת מבנה ה-JSON הנדרש —
אין צורך לנסח כלום. הצ'אט מחזיר JSON.

### שלב 3 — פרסום
ערוך את `review_output.json` בממשק גיטהאב (אייקון העיפרון), מחק את התוכן הישן,
הדבק את תשובת הצ'אט (מותר כולל ```json והסברים מסביב — הסקריפט מחלץ את ה-JSON), ועשה Commit.

ה-push מפעיל אוטומטית את **"2 - Publish Review"**, שמריץ את כל האימותים:
כפיית כותרת/תאריך/מבנה, בדיקת כיוון מול נתוני Finnhub מהאיסוף, הסרת קישורים וכפילויות.

- ✅ **עבר** → `data.json` מתעדכן והאתר מציג את הסקירה.
- ❌ **נכשל** (למשל sign-flip במניה) → `data.json` לא נגעים בו, וה-workflow אדום עם הודעה
  בעברית שמסבירה בדיוק מה לבקש מהצ'אט לתקן. מתקנים בצ'אט, מדביקים שוב, commit — וזה רץ שוב.

### חלופה: הרצה מקומית
```bash
pip install -r requirements.txt
export TWITTER_API_KEY=...   # לא בקוד, רק במשתני סביבה
export FINNHUB_API_KEY=...

python gather_review_input.py daily_summary
# → מעתיקים את raw_review_input.md לצ'אט, מדביקים את התשובה ל-review_output.json
python paste_review.py
git add data.json archive && git commit -m "review" && git push
```

---

## עבודה עם Claude Cowork

פתח את Cowork ותן לו גישה **לתיקיית הריפו הזו בלבד** (לא לכל המחשב).
Cowork יכול להריץ את הסקריפטים, לקרוא את חומר הגלם, לכתוב את הסקירה בעצמו
(בלי API — הוא המודל), להדביק ל-`review_output.json` ולהריץ את האימות.

### הנחיית העבודה היומית ל-Cowork (העתק-הדבק)

```
עבוד רק בתוך תיקיית הריפו הזו. משימה:
1. הרץ: python gather_review_input.py <daily_prep / daily_summary / weekly_summary / intraday_update / daily_digest — לפי מה שאבקש>.
2. קרא את raw_review_input.md במלואו.
3. כתוב את הסקירה לפי כל ההנחיות שבקובץ, בפורמט JSON בלבד, בדיוק במבנה שהוגדר בו.
4. שמור את ה-JSON לקובץ review_output.json (החלף את תוכנו).
5. הרץ: python paste_review.py
6. אם האימות נכשל — קרא את הודעת השגיאה, תקן את הסקירה בהתאם, ושוב משלב 4.
7. עצור רק כאשר paste_review.py הסתיים בהצלחה ו-data.json עודכן.
8. אל תשנה שום קובץ אחר בריפו. אם היה הכרח לגעת בקובץ נוסף — ציין זאת במפורש בסיכום.
בסיום: הצג לי את הבולטים שפורסמו, ושאל אם לדחוף (git push).
```

הערה: בהרצה מקומית/Cowork צריך ש-`TWITTER_API_KEY` ו-`FINNHUB_API_KEY` יהיו מוגדרים
כמשתני סביבה. אם אינם מוגדרים, שלב האיסוף ידלג על ציוצים/נתונים בהתאמה וימשיך —
וההנחיות בקובץ יורו לצ'אט להסתמך על חיפוש אינטרנט.

---

## עקרונות קבועים

- שום API key לא נמצא בקוד — רק GitHub Secrets או משתני סביבה.
- שום קריאה למודל שפה מהקוד. הכתיבה נעשית בצ'אט או ב-Cowork.
- `paste_review.py` אף פעם לא מוחק מפתחות קיימים ב-`data.json` — הוא מעדכן רק את
  המפתח של המצב שפורסם ואת `lastUpdated`.
- כל כישלון אימות משאיר את `data.json` בדיוק כפי שהיה.

⚠️ גילוי נאות: התוכן באתר נוצר באמצעות AI לצרכים אינפורמטיביים בלבד. אין באמור ייעוץ
השקעות או המלצה לפעולה בניירות ערך.

פותח ע"י דורון שרייבמן.
