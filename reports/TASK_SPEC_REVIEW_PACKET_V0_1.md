# KreyolBench v0.1 Task Specification Review Packet

## Purpose

Provide one bounded interface for independent review of the five v0.1 pilot task specifications. Project-policy approval permits this design work but does not freeze task semantics, authorize data acquisition, or support release claims.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Project lead

Required review: Independent external review before any task becomes `EXPERT_VALIDATED`

## Provisional v0.1 Project-Lead Direction

On 2026-09-09, Jeff Pierre approved the following provisional v0.1 task-instance drafting direction:

- `kb_cls_topic_multilabel_v0_1` should use multi-label topic prediction;
- `kb_ie_ner_charspan_v0_1` should use canonical character spans, with nesting representable but not mandatory;
- `kb_ret_hybrid_query_v0_1` should use hybrid real-need and expert-authored queries;
- `kb_norm_orthography_v0_1` should be orthography-only;
- `kb_lc_token_language_id_v0_1` should use factorized token language, type, contact-status, and uncertainty annotations;
- independent external review is required before task freeze.

These statements describe candidate task instances, not permanent definitions of their task families. Independent review may revise them. Deferral from v0.1 does not remove a task from the KreyolBench research roadmap. This internal direction establishes `KB-GOV-002` and the starting proposals; it is not independent validation of `KB-TASK-CLS-001`, `KB-TASK-NER-001`, `KB-TASK-RET-001`, `KB-TASK-NORM-001`, or `KB-TASK-CS-001`.

## Long-Term Scope Protection

KreyolBench is a long-term research program and extensible benchmark ecosystem. The v0.1 release record contains a bounded set of pilot, feasibility, and deferred task instances; it does not define the global task universe.

`KB-SCOPE-002` establishes an open-world task architecture. Under this policy, new task families, task types, variants, instances, domains, modalities, challenge sets, and evaluation paradigms may be registered when scientifically justified. Registration is not implementation, validation, release membership, data authorization, metric approval, or publication evidence.

The authoritative hierarchy and machine-readable registries are documented in `datasets/TASK_TAXONOMY.md`, `configs/task_taxonomy.yaml`, and `configs/releases/v0_1.yaml`. Future text, speech, audio, OCR, document, multimodal, robustness, and LLM-evaluation work remains possible without expanding this pilot.

### KB-SCOPE-002 Review

- [x] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer: Jeff Pierre

Reviewer role: Project Lead and Scientific Reviewer

Review independence: `INTERNAL_PROJECT_LEAD`

Date: 2026-09-09

Rationale: The open-world architecture prevents a bounded pilot from becoming a permanent limitation on Haitian Creole AI research while retaining explicit scientific and release controls.

Conditions:

- registration or roadmap placement does not authorize implementation or establish priority;
- each task, source, dataset, annotation protocol, metric, and evaluation paradigm must pass its applicable scientific, legal, ethical, provenance, and engineering gates;
- release membership remains an explicit, versioned decision;
- this approval validates no v0.1 task specification, taxonomy entry, source, dataset, metric, or release expansion;
- public scope and novelty claims remain bounded by available evidence.

## Review Rules

For each task, mark one outcome. An approval is valid only when reviewer identity, affiliation, relevant expertise, conflicts, date, rationale, and conditions are complete.

- `APPROVE`: accept the specification and change its decision and task artifacts to `EXPERT_VALIDATED`.
- `REVISE`: record required changes and change the decision to `NEEDS_REVISION`.
- `DEFER`: retain `SUBMITTED_TO_REVIEW` and block task freeze.

An external independent reviewer must be outside the core drafting and implementation team at review time. Prospective authorship, institutional interests, dataset ownership, and other conflicts must be disclosed.

Under `KB-GOV-003`, an approval also requires the reviewer's affiliation, relevant expertise tags, conflict status, human attestation, date, and an existing evidence file. One reviewer may cover multiple qualifications when documented; several reviewers may cover them collectively. Internal review or automated output without external human ownership never satisfies an external minimum.

## Internal Pre-Review Disposition

On 2026-09-10, Jeff Pierre adopted an AI-assisted internal scientific audit before external recruitment. The audit is attributed to the project lead, has independence `INTERNAL_PROJECT_LEAD`, and cannot validate any task. Its evidence is `reports/INTERNAL_TASK_SCIENTIFIC_AUDIT_V0_1.md`.

| Decision | Internal outcome | Correction incorporated | Current status |
| --- | --- | --- | --- |
| `KB-TASK-CLS-001` | REVISED | Versioned flat ontology, boundary guidance, multi-label agreement, validation-only thresholding. | `SUBMITTED_TO_REVIEW` |
| `KB-TASK-NER-001` | REVISED | Unicode offset semantics, contiguous scored spans, disabled routine nesting, versioned ontology. | `SUBMITTED_TO_REVIEW` |
| `KB-TASK-RET-001` | REVISED | Governed query origins, unjudged distinction, pooling systems, coverage and sensitivity analysis. | `SUBMITTED_TO_REVIEW` |
| `KB-TASK-NORM-001` | REVISED | Core/auxiliary strata, normative evidence, decision classes, deterministic cleanup boundary. | `SUBMITTED_TO_REVIEW` |
| `KB-TASK-CS-001` | REVISED | Factorized language-contact contract, borrowing rules, token offsets, derived-boundary policy. | `SUBMITTED_TO_REVIEW` |

The external review forms below intentionally remain blank. Reviewers must evaluate the corrected specifications rather than merely endorse the internal disposition.

## Cross-Task Questions

- Are the five constructs distinct and meaningful for Haitian Creole research?
- Are annotation burdens proportionate to publication value?
- Are source and split safeguards adequate for each task?
- Do candidate metrics measure the intended construct rather than annotation artifacts?
- Which tasks are realistically supportable within 12 months?

## KB-TASK-CLS-001: Multi-Label Topic Classification

Specification: `datasets/tasks/CLASSIFICATION.md`

Primary review concerns: ontology validity and coverage, topic/provenance separation, boundary examples, multi-label agreement, rare-label claims, and threshold protocol.

- [ ] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer / affiliation / expertise:

Independence and conflicts:

Date:

Rationale and conditions:

## KB-TASK-NER-001: Character-Span NER

Specification: `datasets/tasks/NER.md`

Required reviewers: Haitian Creole linguistic expert and NER methodology expert; one person may fill both roles only with documented qualifications.

Primary review concerns: entity ontology, Unicode boundaries, contiguous-span policy, disabled routine nesting, privacy, tokenizer-independent evaluation, and entity leakage.

- [ ] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer / affiliation / expertise:

Independence and conflicts:

Date:

Rationale and conditions:

## KB-TASK-RET-001: Hybrid-Query Retrieval

Specification: `datasets/tasks/RETRIEVAL.md`

Required reviewers: Haitian public-information/domain expert and information-retrieval methodologist.

Primary review concerns: query-origin validity, ethical acquisition, qrel semantics, pooling depth, unjudged evaluation treatment, source authority, and temporal validity.

- [ ] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer / affiliation / expertise:

Independence and conflicts:

Date:

Rationale and conditions:

## KB-TASK-NORM-001: Orthography-Only Normalization

Specification: `datasets/tasks/NORMALIZATION.md`

Required reviewer: Haitian Creole linguist or orthography specialist independent of the drafting team.

Primary review concerns: normative authority, orthography/lexicon boundary, legitimate alternatives, core versus auxiliary strata, semantic preservation, and over-normalization.

- [ ] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer / affiliation / expertise:

Independence and conflicts:

Date:

Rationale and conditions:

## KB-TASK-CS-001: Token-Level Code-Switching

Specification: `datasets/tasks/CODE_SWITCHING.md`

Required reviewer: Haitian Creole sociolinguist or code-switching specialist independent of the drafting team.

Primary review concerns: factorized contact ontology, borrowing, ambiguity, named entities, language-contact context, tokenization, source ethics, and derived switch metrics.

- [ ] APPROVE
- [ ] REVISE
- [ ] DEFER

Reviewer / affiliation / expertise:

Independence and conflicts:

Date:

Rationale and conditions:

## Freeze Conditions

A task may be frozen only when:

- its external review is approved and recorded in the YAML decision history;
- source-specific legal, ethical, provenance, and scientific gates permit a pilot;
- annotation guidance and uncertainty representation are reviewed;
- canonical schema and metrics pass tests;
- split and leakage rules are task-specific;
- pilot evidence supports feasibility and agreement;
- publication artifacts and limitations are identified.

## Current Conclusion

`KB-SCOPE-002`, `KB-GOV-002`, and `KB-GOV-003` are `EXPERT_VALIDATED` governance policies. The five corrected task decisions remain `SUBMITTED_TO_REVIEW`; the internal `REVISED` events do not count toward their external gates. Metadata assessment and synthetic contract testing may continue. Data acquisition, annotation, metric/split freeze, leaderboard use, and release claims remain unauthorized.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-09 | Added consolidated external-review interface and project-lead drafting direction. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Protected long-term scope, added stable task-instance references, and exposed KB-SCOPE-002 for review. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Recorded internal project-lead approval of KB-SCOPE-002 at project-scope governance level; downstream task and release gates remain unchanged. | EXPERT_VALIDATED |
| 2026-09-10 | Recorded the AI-assisted internal pre-review, incorporated five task revisions, and added qualified external-review evidence requirements while leaving external forms blank. | SUBMITTED_TO_REVIEW |
