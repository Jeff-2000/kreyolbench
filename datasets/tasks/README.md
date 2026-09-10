# v0.1 Task Specifications

## Purpose

Maintain the scientific contracts for the five retained KreyolBench v0.1 pilot task instances. These files do not define the permanent task families.

## Status

Current status: SUBMITTED_TO_REVIEW

## Specifications

| Decision | Task instance | Specification | Status |
| --- | --- | --- | --- |
| `KB-TASK-CLS-001` | `kb_cls_topic_multilabel_v0_1` | `CLASSIFICATION.md` | SUBMITTED_TO_REVIEW |
| `KB-TASK-NER-001` | `kb_ie_ner_charspan_v0_1` | `NER.md` | SUBMITTED_TO_REVIEW |
| `KB-TASK-RET-001` | `kb_ret_hybrid_query_v0_1` | `RETRIEVAL.md` | SUBMITTED_TO_REVIEW |
| `KB-TASK-NORM-001` | `kb_norm_orthography_v0_1` | `NORMALIZATION.md` | SUBMITTED_TO_REVIEW |
| `KB-TASK-CS-001` | `kb_lc_token_language_id_v0_1` | `CODE_SWITCHING.md` | SUBMITTED_TO_REVIEW |

Supporting ontology contracts:

- `TOPIC_ONTOLOGY.md` for multi-label classification;
- `NER_ONTOLOGY.md` for named entities;
- `configs/orthography/normative_evidence.yaml` for candidate normalization authorities and rules.

These specifications define provisional constructs and contracts. They do not authorize source acquisition or annotation. Review outcomes belong in `reports/TASK_SPEC_REVIEW_PACKET_V0_1.md` and must be synchronized with `DECISIONS.md` and `configs/governance/decisions.yaml`.

The specifications were revised after the internal audit in `reports/INTERNAL_TASK_SCIENTIFIC_AUDIT_V0_1.md`. That audit is AI-assisted and internal; it is not external validation. The open-world family and release architecture is defined in `datasets/TASK_TAXONOMY.md`. Deferring or omitting an instance from v0.1 does not remove its family or future variants from KreyolBench.

## Freeze Rule

No specification may become `EXPERT_VALIDATED` without the qualified independent external human evidence required by `KB-GOV-002` and `KB-GOV-003`. Material changes after approval require a new review event.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-09 | Added the five v0.1 task specifications. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Added stable task-instance identities and long-term scope protection. | SUBMITTED_TO_REVIEW |
| 2026-09-10 | Incorporated the internal scientific revisions and qualified external-review gate. | SUBMITTED_TO_REVIEW |
