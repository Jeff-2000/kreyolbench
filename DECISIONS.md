# Decision Register

## Purpose

Track important scientific and architectural decisions using stable identifiers.

## Status

Current status: IN_PROGRESS

Owner: Codex

Requires expert validation: Yes for scientific decisions.

## Decision Format

```text
ID:
Title:
Date:
Status:
Context:
Decision:
Alternatives considered:
Scientific rationale:
Engineering implications:
Risks:
Requires expert approval:
Expert decision:
```

## KB-DEC-001

Title: Project-wide review-status policy

Date: 2026-09-01

Status: SUBMITTED_TO_REVIEW

Context: KreyolBench needs durable expert review gates across scientific artifacts and implementation work.

Decision: Use `DRAFT`, `IN_PROGRESS`, `TO_REVIEW_LATER`, `SUBMITTED_TO_REVIEW`, `EXPERT_VALIDATED`, `NEEDS_REVISION`, `BLOCKED`, and `DEPRECATED` across major knowledge files, task specs, metrics, source review, paper sections, and releases.

Alternatives considered: informal TODOs only; GitHub issue labels only; no status model.

Scientific rationale: benchmark validity depends on distinguishing provisional scaffold decisions from expert-validated decisions.

Engineering implications: Markdown files should include status blocks; future schemas may encode status fields.

Risks: too much blocking could slow engineering; too little blocking could create unsupported scientific claims.

Requires expert approval: Yes

Expert decision: Pending

## KB-DATA-001

Title: Source registry and redistribution gate

Date: 2026-09-01

Status: SUBMITTED_TO_REVIEW

Context: Candidate sources exist, but not all licenses permit redistribution.

Decision: Every source must have registry metadata before collection or release; redistribution requires explicit review status and source-specific evidence.

Alternatives considered: commit downloaded public web text directly; rely on README source lists only.

Scientific rationale: provenance and legal clarity are required for credible dataset releases.

Engineering implications: source configs and future validation checks should enforce required metadata.

Risks: source review may delay dataset size growth.

Requires expert approval: Yes

Expert decision: Pending

## KB-DATA-002

Title: Raw and normalized text preservation policy

Date: 2026-09-01

Status: SUBMITTED_TO_REVIEW

Context: Haitian Creole orthographic variation is scientifically meaningful but normalization may be useful for evaluation.

Decision: Preserve raw text whenever normalized text is created; normalization must not overwrite or erase raw forms.

Alternatives considered: normalize all text early; avoid normalization entirely.

Scientific rationale: raw forms support analysis of spelling variation, register, and domain differences.

Engineering implications: schemas and preprocessing should maintain raw-to-normalized linkage.

Risks: storage and annotation complexity increase.

Requires expert approval: Yes

Expert decision: Pending

## KB-ANN-001

Title: Annotation quality-control policy

Date: 2026-09-01

Status: SUBMITTED_TO_REVIEW

Context: Existing annotation guidelines mention gold sets, double annotation, adjudication, and agreement reporting.

Decision: Annotation campaigns require pilot review, gold examples, double annotation of a defined subset, adjudication, agreement reporting, and uncertainty labels where appropriate.

Alternatives considered: single annotation only; informal review after annotation.

Scientific rationale: benchmark reliability depends on annotator agreement and transparent disagreement handling.

Engineering implications: annotation exports must preserve annotator/adjudication metadata privately.

Risks: annotation cost and coordination burden increase.

Requires expert approval: Yes

Expert decision: Pending

## KB-EVAL-001

Title: Metric and statistical-testing policy

Date: 2026-09-01

Status: SUBMITTED_TO_REVIEW

Context: Current metric implementations are scaffold-level for several tasks.

Decision: Every metric must document definition, averaging, limitations, uncertainty method, and appropriateness. Leaderboards must not interpret small differences as meaningful without uncertainty or significance analysis.

Alternatives considered: rank by one aggregate score only; report point estimates only.

Scientific rationale: low-resource benchmarks are sensitive to small samples, imbalance, and domain effects.

Engineering implications: result JSON should eventually include confidence intervals and run metadata.

Risks: statistical testing may be misused if sample sizes are too small.

Requires expert approval: Yes

Expert decision: Pending

## KB-SPLIT-001

Title: Split, leakage, and contamination policy

Date: 2026-09-01

Status: SUBMITTED_TO_REVIEW

Context: Train/validation/test split names exist, but split logic and contamination policy are not yet formalized.

Decision: Dataset splits require stable IDs, hashing, source-aware grouping, duplicate checks, and test contamination review before release.

Alternatives considered: random row-level splits only.

Scientific rationale: leakage can invalidate benchmark claims.

Engineering implications: future validators should check duplicate IDs, source overlap, and near-duplicate contamination.

Risks: strict grouping may reduce split size.

Requires expert approval: Yes

Expert decision: Pending

## KB-PUB-001

Title: Publication artifact traceability policy

Date: 2026-09-01

Status: SUBMITTED_TO_REVIEW

Context: The paper outline needs to evolve with implementation artifacts.

Decision: Tables, figures, datasets, metrics, and experiments intended for publication must be linked to paper sections with status, evidence requirements, and implementation dependencies.

Alternatives considered: write paper after implementation from memory.

Scientific rationale: traceability reduces publication drift and unsupported claims.

Engineering implications: reports and results should reference artifact IDs where practical.

Risks: documentation overhead.

Requires expert approval: Yes

Expert decision: Pending

## KB-ENG-001

Title: Machine-readable governance registry

Date: 2026-09-08

Status: TO_REVIEW_LATER

Context: Markdown decision records are authoritative research memory but are not a reliable runtime validation interface.

Decision: Maintain executable decision identifiers and statuses in `configs/governance/decisions.yaml`. Require each machine-readable record to have a matching narrative record in this file with the same status.

Alternatives considered: Parse all Markdown semantics at runtime; keep status only in prose; duplicate the full rationale in YAML.

Scientific rationale: None; this is an engineering traceability mechanism and does not validate scientific content.

Engineering implications: Configuration audits fail on missing decision references or status drift between the YAML registry and this document.

Risks: Duplicate representations can drift if updates bypass the governance audit.

Requires expert approval: No

Expert decision: Not required

## KB-ENG-002

Title: Structural validity and release eligibility separation

Date: 2026-09-08

Status: TO_REVIEW_LATER

Context: KreyolBench must support ongoing engineering while scientific decisions remain unresolved.

Decision: A governance audit may return `PASS` when files and invariants are structurally valid while reporting `release_eligible: false` because scientific approvals remain pending. Structural errors return `FAIL` and a nonzero CLI exit code.

Alternatives considered: Fail every audit while any scientific decision is pending; treat a structurally valid repository as release-ready.

Scientific rationale: The distinction prevents provisional implementation from being misrepresented as scientific validation.

Engineering implications: CI can enforce structural correctness without bypassing expert review gates.

Risks: Users may read `PASS` without checking release eligibility; CLI output therefore reports both fields prominently.

Requires expert approval: No

Expert decision: Not required

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial decision register and first seven decision records. | IN_PROGRESS |
| 2026-09-08 | Added executable-governance and audit-semantics engineering decisions. | IN_PROGRESS |
