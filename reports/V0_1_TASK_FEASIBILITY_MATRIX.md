# KreyolBench v0.1 Task Feasibility Matrix

## Purpose

Assess whether each retained task can proceed to a controlled pilot using documented evidence rather than unsupported readiness scores.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Project lead and task working groups

Requires expert validation: Yes

## Interpretation

- `EVIDENCE_AVAILABLE`: a documented basis exists; it is not automatic approval.
- `PARTIAL`: some scaffold or rationale exists, but validation is incomplete.
- `MISSING`: required evidence has not been established.
- `BLOCKED`: a known condition currently prevents the activity.
- `PILOT_FEASIBLE`: all critical evidence exists for a bounded pilot.
- `CONDITIONAL`: promising, but one or more gates remain unresolved.
- `BLOCKED`: a known gate prevents a pilot.

No numerical aggregate is used because legal permission, construct validity, annotation reliability, and compute are not interchangeable quantities.

## Task Instance IDs

| Working label | Stable task instance |
| --- | --- |
| Classification | `kb_cls_topic_multilabel_v0_1` |
| NER | `kb_ie_ner_charspan_v0_1` |
| Retrieval | `kb_ret_hybrid_query_v0_1` |
| Normalization | `kb_norm_orthography_v0_1` |
| Code-switching | `kb_lc_token_language_id_v0_1` |

These are v0.1 pilot instances, not permanent definitions of their task families. Feasibility findings apply only to these instances and candidate release context.

## Evidence Matrix

| Dimension | Classification | NER | Retrieval | Normalization | Code-switching |
| --- | --- | --- | --- | --- | --- |
| Source authorization/availability | MISSING | MISSING | MISSING | MISSING | MISSING |
| Linguistic representativeness | MISSING | MISSING | MISSING | MISSING | MISSING |
| Annotation complexity evidence | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| Native-speaker requirement defined | EVIDENCE_AVAILABLE | EVIDENCE_AVAILABLE | EVIDENCE_AVAILABLE | EVIDENCE_AVAILABLE | EVIDENCE_AVAILABLE |
| Schema readiness | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| Metric validity | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| Split/contamination analysis | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| Baseline readiness | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| Compute feasibility | EVIDENCE_AVAILABLE | EVIDENCE_AVAILABLE | EVIDENCE_AVAILABLE | EVIDENCE_AVAILABLE | EVIDENCE_AVAILABLE |
| Publication novelty evidence | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| 12-month feasibility evidence | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| Overall | CONDITIONAL | CONDITIONAL | CONDITIONAL | CONDITIONAL | CONDITIONAL |

Compute is marked available only for a small pilot using conventional baselines. This is not approval for expensive frontier-model evaluation.

## Source-to-Task Metadata Assessment

| Task | Candidate source records | Scientific role | Current authorization conclusion |
| --- | --- | --- | --- |
| Classification | MSPP, MENFP, government publications, media family, Wikimedia | overlapping public-interest topics and domain transfer | Metadata candidates only; no real corpus approved |
| NER | MSPP, MENFP, government communication, media, Radio Haiti research corpus | Haitian institutions, places, events, policy and health entities | Metadata candidates only; taxonomy and privacy review pending |
| Retrieval | MSPP, MENFP, Civil Protection, MIT-Ayiti, Wikimedia, UN Haiti | public-information corpus candidates | Document rights, authority, freshness, and query ethics unresolved |
| Normalization | AKA publications, Radio Haiti corpus, media, diaspora, social media | orthographic guidance and naturally varying forms | AKA may guide rules; no source approved as benchmark data |
| Code-switching | Radio Haiti archive/corpus, media, diaspora, social media | spoken/written contact and register variation | Rights, privacy, representativeness, and platform terms unresolved |

Registration under `KB-DATA-003` authorizes metadata review only. A source family cannot support dataset examples, and no row may be created from these candidates until collection-level or subset-level gates permit it.

## Task-Specific Blockers

### Classification

- source-specific authorization;
- qualified external review of the versioned flat multi-label ontology;
- pilot evidence for label boundaries, co-occurrence, uncertainty, and `other`;
- evidence that overlapping labels can be annotated reliably;
- threshold-selection and rare-label reporting protocol.

### Named Entity Recognition

- source-specific authorization and privacy review;
- qualified Haitian Creole linguistic and NER-methodology review;
- resolution of `LOC`/`GPE`, `ORG`/`FACILITY`, and domain-specific types;
- contiguous-span agreement evidence; nesting remains disabled for routine annotation;
- entity-overlap leakage analysis.

### Retrieval

- an authorized document collection;
- a lawful and ethical real-information-need collection route;
- qualified Haitian public-information and IR-methodology review;
- pooling depth, judgment coverage, `bpref`, sensitivity, and assessor evidence;
- policy for authority, freshness, and unjudged documents.

### Normalization

- qualified external orthography review;
- evidence for every versioned normative rule and ambiguity policy;
- multiple-reference and over-normalization evaluation;
- authorized sources containing natural variation.

### Code-Switching

- qualified external Haitian Creole sociolinguistic and language-contact review;
- empirical borrowing, ambiguity, contact-status, and tokenization guidance;
- speaker/document grouping and source ethics;
- pilot agreement for language, borrowing, and intra-token mixing.

## Recommended Sequence

1. Review normalization and code-switching early because they offer distinctive Haitian Creole contributions but carry the greatest linguistic ambiguity.
2. Run classification and NER specification reviews in parallel because conventional baselines and annotation tooling are more mature.
3. Complete retrieval metadata and query-ethics design before any real query collection.
4. Select no single “first task” until source-specific reviews identify at least one legally and scientifically viable pilot corpus.

## Promotion Rule

A task moves from `CONDITIONAL` to `PILOT_FEASIBLE` only after critical source, construct, annotation, schema, metric, split, and external-review evidence is available. Promotion authorizes only the bounded pilot described in the approved task record.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-09 | Added evidence-coded task and source-to-task feasibility assessment. | SUBMITTED_TO_REVIEW |
| 2026-09-10 | Reconciled the internal revision audit; all five tasks remain conditional pending qualified external review and pilot evidence. | SUBMITTED_TO_REVIEW |
