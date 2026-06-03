# Initial Issues

These are suggested issues to create after the repository is public. They are intentionally scoped to toy examples and public documentation.

## 1. Documentation: add a full claim/evidence walkthrough

**Label:** documentation

Add a step-by-step guide showing how `examples/claims.yaml` and `examples/evidence.csv` produce the claim-evidence matrix, audit report, reviewer-response skeleton, and figure/table checklist.

Acceptance criteria:

- Uses only synthetic examples.
- Includes expected output filenames.
- Explains what an `overstated` audit result means.

## 2. Feature: add a stricter claim-strength rubric

**Label:** feature

Add a small rubric file or module that distinguishes exploratory, moderate, and strong claims using explicit evidence requirements.

Acceptance criteria:

- No private research examples.
- Tests cover at least three claim-strength cases.
- README links to the rubric.

## 3. Bug: report missing evidence IDs more clearly

**Label:** bug

When a claim references an evidence ID that is missing from `evidence.csv`, the audit report should explain which ID is missing instead of only marking the claim as weak or missing.

Acceptance criteria:

- Add a regression test with a missing evidence ID.
- CLI still exits successfully for toy examples.

## 4. Security/privacy: add private-path detection for generated reports

**Label:** security/privacy

Add a defensive scan that warns if generated Markdown contains absolute local paths, such as Windows home paths or drive-letter paths.

Acceptance criteria:

- Scan is documented as a helper, not a guarantee.
- Tests use fake paths only.
- No private paths are committed.

## 5. Roadmap: define v0.2.0 template expansion

**Label:** roadmap

Decide which templates belong in v0.2.0: handoff, project memory, figure checklist, reviewer-response, or release-note templates.

Acceptance criteria:

- Add an ordered roadmap section.
- Keep every planned template generic and toy-data safe.

## 6. Good first issue: add a second toy evidence dataset

**Label:** good first issue

Add another synthetic `examples/evidence_2.csv` and matching claim file to demonstrate weak vs moderate support.

Acceptance criteria:

- No real project names, real data, or private paths.
- Add a small test or CLI command note.

## 7. Documentation: add a maintainer workflow page

**Label:** documentation

Document how maintainers can use Codex to triage issues, review pull requests, and prepare release notes without pasting private manuscripts or data.

Acceptance criteria:

- Includes privacy checklist.
- Uses generic issue examples.
