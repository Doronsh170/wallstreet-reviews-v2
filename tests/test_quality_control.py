import copy
import json
from datetime import datetime, timedelta
from pathlib import Path

import pytest
import paste_review as pr
from quality_control import QualityError, check_quality
from gather_combined_review import combine

NOW = datetime.fromisoformat('2026-10-25T12:00:00+02:00')


def example():
    children = [{"mode":mode,"expected_title":"כותרת", "first_heading":"נקודות מרכזיות", "review_date":"2026-10-25", "week_range":"19–23.10.2026", "generated_at":NOW.isoformat()} for mode in ('weekly_summary','weekly_prep')]
    _, snapshot = combine('wallstreet_weekly_review', ['summary material','prep material'], children)
    raw = {"title":snapshot['expected_title'], "sections":[{"heading":heading,"content":'\n'.join(f'* נושא מספר {j}: הסבר עובדתי ממוקד על השוק והמשמעות למשקיעים.' for j in range(n)), "summary":[f'נושא מספר {j}: הסבר קצר.' for j in range(n)]} for heading,n in [('סיכום שבועי',8),('הכנה לשבוע הקרוב',4)]]}
    report = {"run_id":snapshot['audit_id'], "checked_at":NOW.isoformat(), "factual_review":"passed", "language_review":"passed", "unresolved":[], "corrections":["תוקן ניסוח מסורבל."], "checks":[]}
    for i,section in enumerate(raw['sections']):
        for j,line in enumerate(section['content'].splitlines()):
            report['checks'].append({"section":i,"bullet":j,"text":line[2:], "summary":section['summary'][j], "sources":[{"url":"https://www.boi.org.il/publications/", "date":"2026-10-25", "evidence":"נתוני בדיקה מלאכותיים: המקור תומך בטענה שנבדקה."}]})
    raw['_audit'] = report
    return raw,snapshot


def test_report_covers_final_text_and_summary():
    raw,snapshot=example()
    final=pr.validate_review(copy.deepcopy(raw),snapshot)
    report=check_quality(final,snapshot,raw['_audit'],NOW)
    assert report['checked_bullets']==12
    assert report['status']=='passed'
    assert '_audit' not in final
    assert 'לא אומת אוטומטית' in report['note']


@pytest.mark.parametrize('problem',['missing','wrong_run','unresolved','language','stale','future','missing_source','missing_point','duplicate','changed_text','changed_summary','missing_timezone','bad_date'])
def test_blocks_unsafe_reports(problem):
    raw,snapshot=example()
    report=raw['_audit']
    if problem=='missing': report=None
    elif problem=='wrong_run': report['run_id']='different'
    elif problem=='unresolved': report['unresolved']=['מועד האירוע לא אומת']
    elif problem=='language': report['language_review']='blocked'
    elif problem=='stale': snapshot['generated_at']=(NOW-timedelta(hours=25)).isoformat()
    elif problem=='future': report['checked_at']=(NOW+timedelta(hours=1)).isoformat()
    elif problem=='missing_source': report['checks'][0]['sources']=[]
    elif problem=='missing_point': report['checks'].pop()
    elif problem=='duplicate': report['checks'][-1]=report['checks'][0]
    elif problem=='changed_text': raw['sections'][0]['content']=raw['sections'][0]['content'].replace('נושא מספר 0','נושא מספר אחר',1)
    elif problem=='changed_summary': raw['sections'][0]['summary'][0]='תקציר אחר'
    elif problem=='missing_timezone': report['checked_at']='2026-10-25T12:00:00'
    elif problem=='bad_date': report['checks'][0]['sources'][0]['date']='not-a-date'
    final=pr.validate_review(copy.deepcopy(raw),snapshot)
    with pytest.raises(QualityError):
        check_quality(final,snapshot,report,NOW)


@pytest.mark.parametrize('blocked',[False,True])
def test_publication_gate_is_atomic_and_report_stays_out_of_site(tmp_path,monkeypatch,blocked):
    raw,snapshot=example()
    if blocked: raw['_audit']['unresolved']=['חסר מקור מהותי']
    monkeypatch.chdir(tmp_path)
    class FixedClock(datetime):
        @classmethod
        def now(cls,tz=None): return NOW
    monkeypatch.setattr(pr,'datetime',FixedClock)
    monkeypatch.setattr(pr.sys,'argv',['paste_review.py'])
    Path('raw_review_input.json').write_text(json.dumps(snapshot),encoding='utf-8')
    Path('review_output.json').write_text(json.dumps(raw),encoding='utf-8')
    Path('data.json').write_text('{"original": true}',encoding='utf-8')
    if blocked:
        with pytest.raises(QualityError): pr.cli()
        assert json.loads(Path('data.json').read_text())=={'original':True}
        assert not Path('archive').exists()
    else:
        pr.cli()
        published=json.loads(Path('data.json').read_text(encoding='utf-8'))['wallstreetWeeklyReview']
        assert '_audit' not in published
        assert published['asOf']==snapshot['generated_at']
    status=json.loads(Path('publish_status.json').read_text(encoding='utf-8'))
    assert status['ok'] is not blocked
    assert status['audit']['status']==('blocked' if blocked else 'passed')
