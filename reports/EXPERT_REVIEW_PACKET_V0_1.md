# KreyolBench v0.1 Expert Review Packet

## Purpose

This packet provides a bounded review interface for the scientific decisions that currently block a KreyolBench v0.1 task freeze, annotation campaign, and release claim. It summarizes existing proposals; it does not replace the detailed specifications linked below.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Project lead

Requires expert validation: Yes

Blocking downstream work:

- final v0.1 benchmark task freeze
- source inclusion and collection authorization
- annotation campaign launch
- primary metric freeze
- train/validation/test split freeze
- publication and leaderboard claims

## Review Instructions

For each decision, mark exactly one outcome:

- `[ ] APPROVE`: accept the decision as written and change its status to `EXPERT_VALIDATED`.
- `[ ] REVISE`: provide required changes; change its status to `NEEDS_REVISION`.
- `[ ] DEFER`: retain `SUBMITTED_TO_REVIEW` and do not start dependent scientific work.

Record reviewer name, date, rationale, and any conditions. Approval applies only to the stated decision, not to every artifact that cites it.

## Decision Summary

| Decision | Subject | Current status | Principal dependency |
| --- | --- | --- | --- |
| KB-DEC-001 | Review-status policy | SUBMITTED_TO_REVIEW | All scientific governance |
| KB-DATA-001 | Source registry and redistribution gate | SUBMITTED_TO_REVIEW | Collection and release |
| KB-DATA-002 | Raw/normalized text preservation | SUBMITTED_TO_REVIEW | Preprocessing and normalization |
| KB-ANN-001 | Annotation quality control | SUBMITTED_TO_REVIEW | Annotation pilot |
| KB-EVAL-001 | Metrics and statistical testing | SUBMITTED_TO_REVIEW | Baselines and leaderboard |
| KB-SPLIT-001 | Splits, leakage, and contamination | SUBMITTED_TO_REVIEW | Dataset freeze |
| KB-PUB-001 | Publication artifact traceability | SUBMITTED_TO_REVIEW | Manuscript claims |

## KB-DEC-001: Project-Wide Review Status Policy

### Proposed Decision

Use the following statuses across major artifacts: `DRAFT`, `IN_PROGRESS`, `TO_REVIEW_LATER`, `SUBMITTED_TO_REVIEW`, `EXPERT_VALIDATED`, `NEEDS_REVISION`, `BLOCKED`, and `DEPRECATED`.

Important scientific decisions must be explicitly validated before dependent scientific work is frozen or released. Routine engineering may continue when it does not change scientific meaning.

### Evidence to Inspect

- `SCIENTIFIC_GOVERNANCE.md`
- `AGENTS.md`
- `configs/governance/decisions.yaml`

### Review Questions

- Are the eight states clear enough for international collaborators?
- Is the boundary between engineering and scientific decisions appropriate?
- Are any review gates unnecessarily strict or dangerously permissive?

### Expert Decision

- [ ] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer:

Date:

Rationale or required revision:

Conditions:

## KB-DATA-001: Source Registry and Redistribution Gate

### Proposed Decision

Require complete source metadata before collection or release. Public availability must not be interpreted as redistribution permission. Each subset must receive an explicit legal/data handling status.

### Current Source Candidates

| Source ID | Data family | Redistribution field | Source review status | Scientific inclusion status |
| --- | --- | --- | --- | --- |
| `cmu_haitian` | speech/language resources | Unknown | `pending_legal_review` | SUBMITTED_TO_REVIEW |
| `creoleval` | multilingual benchmark collection | Unknown | `pending_subset_review` | SUBMITTED_TO_REVIEW |
| `ebible_hat_1985` | religious text | Yes | `reviewed_public_domain_notice` | SUBMITTED_TO_REVIEW |
| `mspp_publications` | public-health HTML/PDF | Unknown | `pending_legal_review` | SUBMITTED_TO_REVIEW |
| `haitian_news_candidates` | news articles | No | `not_approved_for_redistribution` | SUBMITTED_TO_REVIEW |
| `opus` | parallel corpus collection | Unknown | `pending_subset_review` | SUBMITTED_TO_REVIEW |
| `un_haiti_ht` | civic/development HTML | Unknown | `pending_legal_review` | SUBMITTED_TO_REVIEW |
| `wikimedia_htwiki` | encyclopedia dump | Yes | `reviewed_standard_wikimedia_terms` | SUBMITTED_TO_REVIEW |
| `sample` | synthetic software fixtures | Yes | `approved_public_release` | TO_REVIEW_LATER |

The legal/data handling status is separate from scientific inclusion. A redistributable source is not automatically representative or suitable for a benchmark task.

### Review Questions

- Are the source-specific review states sufficient?
- Who is authorized to approve legal, ethical, and scientific inclusion?
- Should any candidate be excluded before feasibility work?

### Expert Decision

- [ ] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer:

Date:

Rationale or required revision:

Conditions:

## KB-DATA-002: Raw and Normalized Text Preservation

### Proposed Decision

Whenever normalization is performed, preserve the source form and an explicit raw-to-normalized linkage. Do not overwrite orthographic, register, dialectal, or code-switching evidence merely to simplify modeling.

### Review Questions

- What transformations qualify as normalization rather than correction?
- Which metadata must accompany each transformation?
- Should multiple acceptable normalized forms be permitted?
- Which transformations require native-speaker or linguist approval?

### Expert Decision

- [ ] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer:

Date:

Rationale or required revision:

Conditions:

## KB-ANN-001: Annotation Quality-Control Policy

### Proposed Decision

Require a pilot, written guidelines, gold examples, double annotation of a defined subset, adjudication, agreement reporting, and explicit uncertainty handling before a task is frozen.

### Candidate v0.1 Tasks Requiring Annotation Review

| Task | Candidate label/output structure | Current status |
| --- | --- | --- |
| Classification | topic label | SUBMITTED_TO_REVIEW |
| Named entity recognition | BIO entity tags | SUBMITTED_TO_REVIEW |
| Question answering | extractive answers and unanswerable cases | SUBMITTED_TO_REVIEW |
| Retrieval | graded relevance 0-3 | SUBMITTED_TO_REVIEW |
| Normalization | normalized text and edit records | SUBMITTED_TO_REVIEW |
| Code-switching | sentence and token language labels | SUBMITTED_TO_REVIEW |
| Translation | one or more references | BLOCKED on evaluation protocol |

Sentiment and summarization have configuration/sample scaffolds but are not in the current v0.1 task list.

### Review Questions

- What minimum double-annotation proportion is feasible?
- Which agreement statistic is appropriate for each task?
- Who may adjudicate linguistic disagreements?
- How should annotator uncertainty and alternate valid answers be represented?

### Expert Decision

- [ ] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer:

Date:

Rationale or required revision:

Conditions:

## KB-EVAL-001: Metrics and Statistical Testing

### Proposed Decision

Every metric must document definition, averaging, limitations, uncertainty, and appropriateness. Model comparisons must report effect size or uncertainty and must not treat small point-estimate differences as scientifically meaningful by default.

### Candidate Metric Matrix

| Task | Candidate primary metric | Secondary evidence | Current status |
| --- | --- | --- | --- |
| Classification | macro F1 | accuracy, weighted/per-label F1 | SUBMITTED_TO_REVIEW |
| Sentiment | macro F1 | accuracy, per-label F1 | SUBMITTED_TO_REVIEW; not v0.1 |
| NER | span F1 | precision, recall, token accuracy | SUBMITTED_TO_REVIEW |
| QA | token F1 | exact match, unanswerable accuracy | SUBMITTED_TO_REVIEW |
| Retrieval | nDCG@10 | MRR@k, recall@k | SUBMITTED_TO_REVIEW |
| Normalization | exact match | token accuracy, edit distance, alternate-valid-form analysis | SUBMITTED_TO_REVIEW |
| Code-switching | macro F1 | token/sentence metrics | SUBMITTED_TO_REVIEW |
| Translation | chrF candidate | BLEU, COMET, human evaluation | BLOCKED |
| Summarization | ROUGE-L candidate | ROUGE-1/2, chrF, human evaluation | BLOCKED; not v0.1 |

### Review Questions

- Which metric is primary for each retained v0.1 task?
- Which confidence-interval or paired-test procedure is required?
- How should multiple comparisons across models and tasks be handled?
- Which tasks require human evaluation before publication claims?

### Expert Decision

- [ ] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer:

Date:

Rationale or required revision:

Conditions:

## KB-SPLIT-001: Split, Leakage, and Contamination Policy

### Proposed Decision

Use stable example identifiers, deterministic split generation, source/document-aware grouping, exact and near-duplicate checks, frozen hashes, and hidden-test protection.

### Unresolved Split Questions

- Should split proportions vary by task and source size?
- Which tasks need source-held-out or domain-held-out robustness sets?
- What near-duplicate representation and threshold should be used per task?
- How should parallel translations and document-derived examples be grouped?
- What minimum hidden-test size is defensible?
- When should a time-based split replace or supplement a random/grouped split?

### Expert Decision

- [ ] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer:

Date:

Rationale or required revision:

Conditions:

## KB-PUB-001: Publication Artifact Traceability

### Proposed Decision

Associate planned tables, figures, datasets, experiments, and claims with stable artifact identifiers, evidence requirements, implementation dependencies, and review status.

### Review Questions

- Is the burden proportionate for a small research team?
- Which artifacts require independent reproduction before submission?
- Who may approve a result or claim for manuscript inclusion?
- Should preprint, workshop, and archival submissions use different evidence gates?

### Expert Decision

- [ ] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer:

Date:

Rationale or required revision:

Conditions:

## Cross-Cutting v0.1 Scope Review

### Current Candidate Task List

1. Classification
2. Named entity recognition
3. Question answering
4. Retrieval
5. Normalization
6. Code-switching
7. Translation

This list is provisional. Translation remains blocked for publication-grade scoring. The number of tasks may exceed the capacity of a small first-year team.

### Current Candidate Domains

- health
- education
- civic administration
- disaster response
- religion
- news
- culture
- other

### Scope Recommendation for Expert Consideration

Do not validate the entire seven-task list as one indivisible package. Review task readiness individually using scientific value, source feasibility, annotation cost, evaluation validity, collaborator capacity, and 12-month publication feasibility.

### Scope Decision

- [ ] APPROVE CURRENT CANDIDATE LIST FOR PILOT FEASIBILITY ONLY
- [ ] REVISE TASK LIST
- [ ] DEFER SCOPE FREEZE

Reviewer:

Date:

Tasks retained for pilot:

Tasks deferred:

Rationale:

## Final Review Record

Review completed by:

Affiliation/role:

Review date:

Decision IDs approved:

Decision IDs requiring revision:

Decision IDs deferred:

Authorized next scientific step:

Limitations or conditions:

## Current Status and Next Action

Current status: SUBMITTED_TO_REVIEW

Next action: the project lead and designated Haitian Creole/statistical experts should complete this packet. A maintainer must then update both `DECISIONS.md` and `configs/governance/decisions.yaml` in the same reviewed change. Dataset collection, task freeze, annotation launch, and release claims remain out of scope until the applicable decisions are `EXPERT_VALIDATED`.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-08 | Initial v0.1 expert-review packet. | SUBMITTED_TO_REVIEW |
