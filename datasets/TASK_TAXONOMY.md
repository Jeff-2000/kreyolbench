# KreyolBench Task Taxonomy

## Purpose

Define the scientific hierarchy that separates the long-term KreyolBench research program from any one controlled release. This document prevents a current implementation or release list from becoming an accidental permanent task boundary.

## Status

Current status: SUBMITTED_TO_REVIEW

Decision: `KB-SCOPE-002`

Requires expert validation: Yes

`KB-SCOPE-002` validates the open-world architecture at project-scope level. It does not validate the individual task families, types, variants, instances, domains, or roadmap entries registered here; this taxonomy therefore remains `SUBMITTED_TO_REVIEW`.

## Hierarchy

```text
KreyolBench Research Program
  -> KreyolBench Benchmark Ecosystem
    -> Task Family
      -> Task Type
        -> Task Variant
          -> Task Instance
            -> Release Membership
```

| Level | Meaning | Example |
| --- | --- | --- |
| Research program | Long-term scientific initiative, collaborations, infrastructure, and publications | KreyolBench |
| Benchmark ecosystem | Extensible datasets, tasks, challenge sets, evaluations, modalities, and releases | KreyolBench benchmark ecosystem |
| Task family | Broad capability area | classification |
| Task type | Distinct scientific construct inside a family | topic classification |
| Task variant | Methodologically meaningful formulation | multi-label |
| Task instance | Stable governed specification | `kb_cls_topic_multilabel_v0_1` |
| Release membership | Explicit relationship to one version | v0.1 `PILOT_CANDIDATE` |

Runtime aliases such as `classification` and `ner` exist for current CLI compatibility. They are not a list of every task KreyolBench may ever support. Stable task-instance IDs are authoritative for scope and release governance.

## Scope and Scientific Status

Scope answers where an artifact sits in planning or release progression. Scientific status answers whether its construct and protocol have been reviewed. They are independent.

Allowed scope states are `ROADMAP`, `DISCOVERY`, `FEASIBILITY_ONLY`, `PILOT_CANDIDATE`, `RELEASE_CANDIDATE`, `DEFERRED`, and `INCLUDED_IN_RELEASE`.

Allowed scientific statuses remain `DRAFT`, `IN_PROGRESS`, `TO_REVIEW_LATER`, `SUBMITTED_TO_REVIEW`, `EXPERT_VALIDATED`, `NEEDS_REVISION`, `BLOCKED`, and `DEPRECATED`.

A roadmap task may be scientifically plausible without being implemented. A pilot candidate may remain scientifically unvalidated. Nothing may become a release candidate or included task while its scientific decisions remain unresolved.

## Current v0.1 Instances

| Task instance | Family | Type | Variant | v0.1 scope | Scientific status |
| --- | --- | --- | --- | --- | --- |
| `kb_cls_topic_multilabel_v0_1` | classification | topic classification | multi-label | PILOT_CANDIDATE | SUBMITTED_TO_REVIEW |
| `kb_ie_ner_charspan_v0_1` | information extraction | named entity recognition | character spans, optional nesting | PILOT_CANDIDATE | SUBMITTED_TO_REVIEW |
| `kb_ret_hybrid_query_v0_1` | retrieval | information retrieval | hybrid query, graded qrels | PILOT_CANDIDATE | SUBMITTED_TO_REVIEW |
| `kb_norm_orthography_v0_1` | normalization | orthographic normalization | multi-reference, orthography-only | PILOT_CANDIDATE | SUBMITTED_TO_REVIEW |
| `kb_lc_token_language_id_v0_1` | language contact | code-switch identification | token language ID | PILOT_CANDIDATE | SUBMITTED_TO_REVIEW |
| `kb_qa_extractive_v0_1_feasibility` | question answering | extractive QA | answerable/unanswerable | FEASIBILITY_ONLY | SUBMITTED_TO_REVIEW |
| `kb_mt_text_v0_1_deferred` | translation | machine translation | multilingual text candidate | DEFERRED | BLOCKED |

Sentiment and summarization remain ecosystem roadmap instances and have no v0.1 membership.

## Open-World Expansion

The task-family registry is not a permanent whitelist. A new family or task type may be registered without changing the existing pilot. Registration permits structured scientific discussion only; it does not authorize implementation, source use, annotation, metrics, release, or publication claims.

Future directions may include richer classification, information extraction, retrieval, QA, generation, translation, normalization, language-contact research, robustness, LLM evaluation, speech, OCR, document understanding, and multimodal evaluation. The registry is intentionally non-exhaustive.

KreyolBench-specific research axes include orthographic and lexical variation, borrowing, code-switching, Haitian named entities, institutional versus informal Kreyol, Haiti and diaspora usage, multilingual influence, source and temporal shift, human versus translated or generated content, contamination, uncertainty, metric disagreement, ranking stability, and benchmark saturation. These axes need not become standalone tasks.

## Expansion Gate

A proposed task instance must document construct validity, Haitian Creole relevance, intended use, source feasibility, legal and ethical handling, schema, annotation needs, metrics, uncertainty, splits, contamination risks, baselines, compute, publication value, and qualified review. Release membership requires a separate explicit decision.

## Known Risks

- A long roadmap can be mistaken for delivered capability.
- Broad family names can hide materially different constructs.
- Compatibility aliases can be mistaken for stable scientific identifiers.
- Task count can displace representativeness, reliability, and linguistic depth.

## Acceptance Criteria

- No release list defines the global task universe.
- Every implemented task resolves to one stable task instance, family, type, and variant.
- Scope status and scientific status remain separate.
- Deferred and roadmap tasks remain traceable but excluded from releases.
- Future registration never bypasses scientific or data-governance review.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-09 | Added the open-world hierarchy and v0.1 instance mapping. | SUBMITTED_TO_REVIEW |
