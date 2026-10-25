"""Publication gate for a separately reviewed weekly review.

A reviewer report is an attestation, not proof that the cited pages were read.
The server checks coverage, binding, dates and unresolved issues deterministically.
"""
from datetime import datetime, timedelta
from urllib.parse import urlparse


class QualityError(ValueError):
    def __init__(self, message):
        super().__init__(message)
        self.report = {"status": "blocked", "issues": [message]}


def bullet_lines(section):
    return [line.strip()[2:].strip() for line in str(section.get("content", "")).splitlines()
            if line.strip().startswith("* ")]


def check_quality(result, snapshot, raw_report, now):
    def fail(message):
        raise QualityError(message)

    if not snapshot.get("audit_id"):
        fail("חומר הגלם נאסף לפני הוספת הביקורת. יש לבצע איסוף חדש ואז ביקורת בצ׳אט חדש.")
    if not isinstance(raw_report, dict):
        fail("חסר דוח ביקורת. העתק את הטיוטה לביקורת בצ׳אט חדש והדבק את התשובה לאחר ההגהה.")
    report = raw_report
    if report.get("run_id") != snapshot["audit_id"]:
        fail("דוח הביקורת שייך לאיסוף אחר. יש לבצע ביקורת עם חומר הגלם הנוכחי.")
    for field in ("factual_review", "language_review"):
        if report.get(field) != "passed":
            fail("הבדיקה העובדתית וההגהה חייבות להסתיים בהצלחה לפני הפרסום.")
    for field in ("unresolved", "corrections"):
        if not isinstance(report.get(field), list) or not all(isinstance(x, str) and x.strip() for x in report[field]):
            fail("דוח הביקורת חייב לכלול רשימות תקינות של תיקונים ובעיות פתוחות.")
    if report["unresolved"]:
        fail("הפרסום נעצר בגלל בעיות פתוחות: " + " · ".join(report["unresolved"]))
    try:
        gathered = datetime.fromisoformat(snapshot["generated_at"])
        checked = datetime.fromisoformat(report["checked_at"])
        if gathered.utcoffset() is None or checked.utcoffset() is None:
            raise ValueError()
        if not (now - timedelta(hours=24) <= gathered <= now + timedelta(minutes=5)):
            fail("חומר הגלם ישן מ־24 שעות או מתוארך לעתיד. יש לאסוף חומר עדכני ולבצע ביקורת מחדש.")
        if not (max(gathered - timedelta(minutes=5), now - timedelta(hours=24)) <= checked <= now + timedelta(minutes=5)):
            fail("מועד הביקורת אינו תואם לחומר הגלם או לזמן הנוכחי. יש לבצע ביקורת מחדש.")
    except (KeyError, TypeError, ValueError) as exc:
        if isinstance(exc, QualityError):
            raise
        fail("חסר מועד ביקורת תקין הכולל אזור זמן.")
    checks = report.get("checks")
    if not isinstance(checks, list):
        fail("חסרות הפניות למקורות עבור נקודות הסקירה.")
    expected = {(i, j): line for i, section in enumerate(result["sections"])
                for j, line in enumerate(bullet_lines(section))}
    if len(result.get("summary", [])) != len(expected):
        fail("נדרש תקציר אחד לכל נקודה, לאחר ההגהה.")
    summary_by_key = dict(zip(expected, result["summary"]))
    seen = set()
    sources = set()
    for check in checks:
        if not isinstance(check, dict):
            fail("רשומת ביקורת אינה תקינה.")
        i, j = check.get("section"), check.get("bullet")
        if type(i) is not int or type(j) is not int:
            fail("מספור נקודות הביקורת אינו תקין.")
        key = (i, j)
        if key not in expected or key in seen:
            fail("דוח הביקורת כולל נקודה כפולה או נקודה שאינה קיימת בסקירה.")
        if check.get("text") != expected[key]:
            fail("הטקסט השתנה לאחר הביקורת או אינו תואם לדוח. יש לבדוק את הנוסח הסופי מחדש.")
        summary_prefix = result["sections"][i]["heading"] + ": "
        expected_summary = summary_by_key[key].removeprefix(summary_prefix)
        if check.get("summary") != expected_summary:
            fail("התקציר השתנה לאחר הביקורת או אינו מכוסה בדוח.")
        seen.add(key)
        refs = check.get("sources")
        if not isinstance(refs, list) or not refs:
            fail("לכל נקודה חייב להיות מקור שנבדק, עם מועד וראיה תומכת.")
        for ref in refs:
            if not isinstance(ref, dict):
                fail("הפניה למקור אינה תקינה.")
            url = ref.get("url", "")
            parsed = urlparse(url) if isinstance(url, str) else None
            if not parsed or parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
                fail("כתובת מקור חסרה או אינה תקינה. יש לצרף קישור HTTPS למקור שנבדק.")
            try:
                source_date = datetime.strptime(ref.get("date", ""), "%Y-%m-%d").date()
                if source_date > now.date():
                    fail("תאריך פרסום של מקור אינו יכול להיות בעתיד. תאריך אירוע עתידי נכתב בנפרד.")
            except (ValueError, TypeError):
                fail("לכל מקור יש לציין תאריך פרסום או עדכון תקין.")
            if not isinstance(ref.get("evidence"), str) or len(ref["evidence"].strip()) < 15:
                fail("חסרה ראיה תומכת מפורטת מן המקור.")
            sources.add(url)
    if seen != set(expected):
        fail("הביקורת אינה מכסה את כל נקודות הסיכום וההכנה.")
    return {"status": "passed", "checked_at": report["checked_at"], "checked_bullets": len(expected),
            "source_count": len(sources), "corrections": report["corrections"], "issues": [],
            "factual_review": "reported_passed", "language_review": "reported_passed",
            "note": "הביקורת העובדתית וההגהה דווחו בצ׳אט. הקוד בדק כיסוי, התאמה לנוסח, קישורים, מועדים והיעדר בעיות פתוחות; תוכן המקורות לא אומת אוטומטית."}
