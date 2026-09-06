# סקירות וול סטריט v2 — Market Desk

מערכת סקירות וול סטריט בעברית, **לפי דרישה בלבד**, **ללא שום API של מודל שפה**
(לא OpenAI, לא Claude API, לא Gemini). הקוד אוסף חומר גלם ומאמת בלבד;
את הסקירה עצמה כותבים ידנית ב-Claude / ChatGPT (בצ'אט, לא ב-API).

המצבים: `daily_prep` (נקודות לקראת פתיחת המסחר) · `daily_summary` (סיכום יום מסחר) · `weekly_summary` (סיכום שבוע המסחר שהסתיים) · `weekly_prep` (מפת השבוע הקרוב, Calendar-first, מופק ביום ראשון) · `intraday_update` (עדכון ביניים — סיכום המקורות מהשעתיים האחרונות, בכל רגע שתרצה).

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
| `sources/wallstreet.txt` | רשימת חשבונות X/Twitter — מקור יחיד (ב-`weekly_prep` הם משלימים ללוח האירועים, לא תנאי) |
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

## מחזור עבודה מלא — מסך הניהול (`admin.html`)

זה המסלול הרגיל, כולל מהטלפון. אין בו GitHub, אין Actions, אין JSON ואין קבצים.

1. **בוחרים סקירה** — שורה ראשונה: וול סטריט / ישראל. שורה שנייה: בוקר · תוך יומי · סגירה · שבועי.
   ברירת המחדל היא וול סטריט + בוקר, והבחירה האחרונה נזכרת. לתל אביב אין סקירת תוך-יומי,
   ולכן הכפתור הזה מושבת שם.
2. **לוחצים "אסוף חומר גלם"** — המסך מריץ את האיסוף ומראה מד התקדמות עד שהחומר מוכן.
3. **"העתק חומר" ו"פתח את Claude"** — לחיצה אחת מעתיקה את כל הפרומפט, מדביקים בצ'אט
   (עם חיפוש אינטרנט), ומעתיקים משם את התשובה.
4. **מדביקים ולוחצים "פרסם"** — המסך מריץ את כל בדיקות האימות ומעדכן את `data.json`.
5. **אישור** — "הסקירה באוויר ✓". אם guard פסל את הסקירה, ההודעה שלו בעברית מופיעה
   על המסך עצמו (מה לתקן ואיך), הטקסט שהדבקת נשאר במקומו, מתקנים בצ'אט ומדביקים שוב.

`data.json` לא נגעים בו כשהאימות נכשל — הסקירה הקודמת נשארת באוויר.

### התקנת מסך הניהול (חד-פעמי)

מסך הניהול מדבר עם Cloudflare Worker קטן (`worker/`) שמחזיק את הטוקן של GitHub.
**הטוקן לעולם לא מגיע לדפדפן** — בדפדפן יושבת רק סיסמה שאתה בוחר.

1. צור **fine-grained PAT** בגיטהאב, מוגבל **לריפו הזה בלבד**, עם שתי הרשאות:
   Actions: Read and write · Contents: Read and write. שום דבר נוסף.
2. ערוך את `worker/wrangler.toml` (REPO / BRANCH / ALLOWED_ORIGIN).
3. פרוס:
   ```bash
   cd worker
   npx wrangler secret put GITHUB_TOKEN      # ה-PAT
   npx wrangler secret put ADMIN_PASSWORD    # סיסמה ארוכה שאתה בוחר
   npx wrangler deploy
   ```
4. פתח את `admin.html` באתר, הזן פעם אחת את כתובת ה-Worker ואת הסיסמה. זהו.

להחלפת הסיסמה: `npx wrangler secret put ADMIN_PASSWORD` ו-"החלפת חיבור" במסך. אין
צורך לגעת ב-GitHub.

### חלופה: מגיטהאב ישירות (בלי מסך הניהול)

Actions → **"1 - Gather Review Input"** → Run workflow → בחר מצב. בסיום, מעתיקים את
`raw_review_input.md` לצ'אט, מדביקים את התשובה ב-`review_output.json` דרך העורך של
גיטהאב, ו-Commit מפעיל את **"2 - Publish Review"**.

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
1. הרץ: python gather_review_input.py <daily_prep / daily_summary / weekly_summary / intraday_update — לפי מה שאבקש>.
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
