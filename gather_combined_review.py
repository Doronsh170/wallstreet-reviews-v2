"""Gather both markets into one prompt and one publish snapshot."""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

MODES = {"combined_weekly_summary": ("israel_weekly_summary", "weekly_summary"),
         "combined_weekly_prep": ("israel_weekly_prep", "weekly_prep")}

def combine(mode, materials, snapshots):
    title = ("סיכום שבועי" if mode.endswith("summary") else "הכנה לשבוע הקרוב") + " | ישראל וול סטריט | " + snapshots[1]["week_range"]
    snapshot = {"mode": mode, "expected_title": title, "first_heading": "ישראל", "review_date": snapshots[1]["review_date"],
                "generated_at": snapshots[1]["generated_at"], "markets": snapshots}
    instructions = f'''כתוב סקירה משולבת אחת בעברית: {title}.
שני המסמכים בהמשך הם חומר גלם והוראות לכל שוק בנפרד. הוראות הפלט המשולב כאן גוברות על הוראות הפלט בכל מסמך.
החזר אובייקט JSON אחד בלבד, ללא מעטפת Markdown, במבנה:
{{"title": {json.dumps(title, ensure_ascii=False)}, "date": "{snapshot['review_date']}", "sections": [
{{"heading":"ישראל", "summary":["תקציר כל נקודה"], "content":"* כותרת: תוכן\\n* כותרת: תוכן"}},
{{"heading":"וול סטריט", "summary":["תקציר כל נקודה"], "content":"* כותרת: תוכן\\n* כותרת: תוכן"}}]}}
כל חלק שומר על כללי המקורות, האימות, מספר הנקודות ואופק הזמן במסמך שלו. אין להעביר נתונים בין השווקים.
אין להשמיט שוק: אם חסר חומר, ציין זאת במפורש בחלק הרלוונטי לפי כללי המסמך שלו.
סיכום שבועי עוסק בשבוע שהסתיים; הכנה עוסקת בשבוע הקרוב ובאירועים מאומתים עם תאריך ושעת ישראל.
'''
    prompt = instructions + "\n\nחומר לישראל:\n" + materials[0] + "\n\nחומר לוול סטריט:\n" + materials[1] + "\n\n" + instructions
    return prompt, snapshot

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "combined_weekly_summary"
    mode = {"weekly_summary": "combined_weekly_summary", "weekly_prep": "combined_weekly_prep"}.get(mode, mode)
    if mode not in MODES:
        raise SystemExit("Choose combined_weekly_summary or combined_weekly_prep")
    # Child gathers write to a private directory. Publish the combined files only
    # after both succeed, so a failed second market cannot leave a partial snapshot.
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
