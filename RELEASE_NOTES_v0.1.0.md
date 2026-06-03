# paper-pusher v0.1.0 Release Notes

## Overview

This first clean-room release introduces a small, testable research workflow toolkit for claim/evidence traceability and review scaffolding. The package uses only synthetic examples and is designed for public, privacy-conscious development.

## Included

- Toy `claims.yaml` and `evidence.csv` inputs.
- Claim/evidence matrix generation.
- Conservative claim audit report.
- Reviewer-response skeleton generation.
- Figure/table checklist generation.
- README, privacy, security, roadmap, contribution docs, issue templates, pull-request template, and GitHub Actions test workflow.

## Not Included

- No private manuscripts.
- No real experimental data.
- No reviewer letters.
- No private paths.
- No hardware/control code.

## Tests

Expected local verification:

```bash
python -m pytest
python -m paper_pusher.cli examples/claims.yaml examples/evidence.csv examples/outputs
```

## Known Limitations

- YAML parsing is intentionally tiny and supports only the toy example shape.
- Claim audit logic is a starter heuristic.
- Templates are early-stage and should be expanded with synthetic examples only.

## Recommended Next Steps

- Create the initial issues listed in `docs/initial_issues.md`.
- Publish this release after manual privacy review.
- Add one or two additional toy datasets for v0.2.0.
