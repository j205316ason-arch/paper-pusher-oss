from pathlib import Path

from paper_pusher.cli import run


def test_evidence_2_outputs(tmpdir):
    """Run the CLI against the second example set and verify outputs."""
    root = Path(__file__).resolve().parents[1]
    run(
        root / "examples" / "claims_2.yaml",
        root / "examples" / "evidence_2.csv",
        str(tmpdir),
    )
    report = tmpdir.join("claim_audit_report.md").read_text("utf-8")
    assert "C3" in report
    assert "C4" in report

    matrix = tmpdir.join("claim_evidence_matrix.md").read_text("utf-8")
    assert "E3" in matrix
    assert "E5" in matrix

    assert tmpdir.join("reviewer_response_skeleton.md").exists()
    assert tmpdir.join("figure_table_checklist.md").exists()
