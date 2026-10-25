"""Gather summary and preparation for one market into one review."""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

MODES = {"israel_weekly_review": ("israel_weekly_summary", "israel_weekly_prep"),
         "wallstreet_weekly_review": ("weekly_summary", "weekly_prep")}

def combine(mode, materials, snapshots):
    market = "ישראל" if mode == "israel_weekly_review" else "וול סטריט"
    title = f"סקירה שבועית | {market} | סיכום {snapshots[0]['week_range']} | הכנה {snapshots[1]['week_range']}"
    snapshot = {"mode": mode, "expected_title": title, "first_heading": "סיכום שבועי", "review_date": snapshots[1]["review_date"],
                "generated_at": snapshots[1]["generated_at"], "parts": snapshots}
    instructions = f'''כתוב סקירה משולבת אחת בעברית: {title}.
שני המסמכים בהמשך הם חומר גלם לאותו שוק בלבד: {market}. הראשון לסיכום והשני להכנה. הוראות הפלט המשולב כאן גוברות על הוראות הפלט בכל מסמך.
החזר אובייקט JSON אחד בלבד, ללא מעטפת Markdown, במבנה:
{{"title": {json.dumps(title, ensure_ascii=False)}, "date": "{snapshot['review_date']}", "sections": [
{{"heading":"סיכום שבועי", "summary":["תקציר כל נקודה"], "content":"* כותרת: תוכן\\n* כותרת: תוכן"}},
{{"heading":"הכנה לשבוע הקרוב", "summary":["תקציר כל נקודה"], "content":"* כותרת: תוכן\\n* כותרת: תוכן"}}]}}
כל חלק שומר על כללי המקורות, האימות, מספר הנקודות ואופק הזמן במסמך שלו. אין להעביר נתונים בין השווקים.
אין להשמיט את הסיכום או ההכנה. אם חסר חומר, ציין זאת במפורש בחלק הרלוונטי לפי כללי המסמך שלו. כל הסקירה מתייחסת ל-{market} בלבד.
סיכום שבועי עוסק בשבוע שהסתיים; הכנה עוסקת בשבוע הקרוב ובאירועים מאומתים עם תאריך ושעת ישראל.
'''
    prompt = instructions + "\n\nחומר לסיכום השבוע:\n" + materials[0] + "\n\nחומר להכנה לשבוע הקרוב:\n" + materials[1] + "\n\n" + instructions
    return prompt, snapshot

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "wallstreet_weekly_review"
    mode = {"weekly_summary": "wallstreet_weekly_review", "israel_weekly_summary": "israel_weekly_review"}.get(mode, mode)
    if mode not in MODES:
        raise SystemExit("Choose israel_weekly_review or wallstreet_weekly_review")
    # Child gathers write to a private directory. Publish the combined files only
    # after both succeed, so a failed preparation cannot leave a partial snapshot.
    script = Path(__file__).with_name("gather_review_input.py").resolve()
    materials, snapshots = [], []
    with tempfile.TemporaryDirectory() as temp:
        target = Path(temp)
        shutil.copytree("sources", target / "sources")
        for name in ("data.json", "market_history.json"):
            if Path(name).exists():
                shutil.copy2(name, target / name)
        for child in MODES[mode]:
            subprocess.run([sys.executable, str(script), child], cwd=target, check=True)
            materials.append((target / "raw_review_input.md").read_text(encoding="utf-8"))
            snapshots.append(json.loads((target / "raw_review_input.json").read_text(encoding="utf-8")))
        prompt, snapshot = combine(mode, materials, snapshots)
        Path("raw_review_input.md").write_text(prompt, encoding="utf-8")
        Path("raw_review_input.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")
        if (target / "market_history.json").exists():
            shutil.copy2(target / "market_history.json", "market_history.json")

if __name__ == "__main__":
    main()
