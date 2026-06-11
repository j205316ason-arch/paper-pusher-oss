from pathlib import Path

from paper_pusher.cli import run
from paper_pusher.claim_audit.audit import audit_claims


def test_demo_outputs(tmpdir):
    root = Path(__file__).resolve().parents[1]
    run(root / "examples" / "claims.yaml", root / "examples" / "evidence.csv", str(tmpdir))
    report = tmpdir.join("claim_audit_report.md").read_text("utf-8")
    assert "C1" in report
    assert "overstated" in report
    assert tmpdir.join("figure_table_checklist.md").exists()


def test_missing_evidence_is_flagged():
    claims = [{"id": "C_missing", "text": "Toy claim", "strength": "moderate", "evidence": ["E404"]}]
    audited = audit_claims(claims, evidence={})
    assert audited[0]["audit"] == "missing_evidence"
