# Multi-Label Topic Classification Specification

## Status

Current status: SUBMITTED_TO_REVIEW

Decision: `KB-TASK-CLS-001`

Task instance: `kb_cls_topic_multilabel_v0_1`

Task family / type / variant: classification / topic classification / multi-label

Scope status: PILOT_CANDIDATE for v0.1

Owner: Classification working group

Required external review: Haitian Creole/domain expert and multi-label classification researcher

This specification defines one provisional v0.1 task instance. It does not define classification globally. Future separately reviewed instances may address single-label, hierarchical, domain, genre, register, intent, sentiment, stance, safety, educational, or other classification constructs.

## Purpose and Construct

Measure whether a system can identify every public-interest topic substantively discussed in a Haitian Creole text. The target is topical content, not publisher identity, source domain, genre, register, sentiment, or intended audience.

## Research Value and Use Cases

- Route multilingual public information to relevant services or analysts.
- Measure cross-domain transfer and rare-topic performance.
- Study whether multilingual models recognize overlapping Haitian public-interest topics.
- Support corpus exploration without using predictions as high-stakes eligibility decisions.

## Canonical Contract

```json
{"input":{"text":"..."},"target":{"labels":["health","disaster_response"]}}
```

`target.labels` must be non-empty, unique, and selected from the reviewed taxonomy. `other` is exclusive and must be accompanied by an annotation justification during the pilot. Source `domain`, `genre`, and `register` remain provenance metadata.

## Candidate Taxonomy

`health`, `education`, `civic_admin`, `disaster_response`, `economy`, `security`, `culture`, `religion`, and `other` remain candidates. The versioned definitions, inclusion cases, and counterexamples live in `configs/labels/topic.yaml`. They form a flat v0.1 scoring ontology; proposed relationships may be analysis metadata but do not alter gold labels. The external review must test whether labels are mutually intelligible, sufficiently exhaustive, and separable. `news` is a genre and must not become a topic label.

Topic, source, audience, domain, genre, and register are different constructs. A publisher or institution mentioned only as provenance cannot determine a topic. `other` is mutually exclusive with every substantive label and requires a written taxonomy-gap justification.

## Inclusion and Exclusion

Include self-contained texts with enough semantic content for topic judgment. Exclude navigation fragments, duplicate syndication, texts whose Haitian Creole content is too short to interpret, and records whose topic is inferable only from private metadata. Mixed-language text may be included when Haitian Creole carries substantive content and code-switch metadata are retained.

## Annotation Protocol

1. Read the complete annotation unit and permitted context.
2. Select every topic that is substantively present, not merely mentioned incidentally.
3. Record `CONFIDENT`, `UNCERTAIN`, or `MISSING_CONTEXT` per annotation unit and preserve label-level disagreement before adjudication.
4. Use `other` only when no reviewed label applies; provide a proposed taxonomy gap.
5. Independently annotate the pilot subset and adjudicate systematic co-occurrence disagreements.

The pilot must estimate label prevalence, cardinality, density, pairwise co-occurrence, and per-label agreement before any class balancing or sample-size commitment. Agreement reporting must include per-label binary statistics, set precision/recall/F1, and a bootstrapped chance-adjusted multi-label analysis. Ordinary Cohen's kappa alone is not sufficient for this task.

## Sources and Representativeness

Candidate families include government, health, education, media, and Wikimedia records. No source is approved by this specification. The pilot must assess domain, register, time, publisher, translation-origin, and machine-generation imbalance.

## Splits and Leakage

Group derivatives, near duplicates, syndicated articles, document sections, and items from the same provenance unit. Evaluate source-held-out or domain-held-out robustness if sample sizes permit. Do not use source metadata fields as model inputs.

## Evaluation Candidates

Candidate primary metric: macro F1 over binary labels. Required secondary evidence: micro F1, sample-averaged F1, subset accuracy, per-label precision/recall/F1, prevalence, and bootstrap confidence intervals. Report both a fixed 0.5 threshold and per-label thresholds selected only on validation data. Thresholds are model-evaluation choices and must never modify the gold ontology; the primary threshold protocol remains subject to external review.

## Baselines

- label-frequency and independent prevalence baselines;
- TF-IDF with one-vs-rest logistic regression;
- multilingual encoder with independent sigmoid outputs;
- zero-shot multilingual instruction model where licensing permits.

## Error Analysis

Analyze rare labels, topic co-occurrence, `other`, short texts, code-switching, orthographic variation, source/domain transfer, translation origin, and false correlations with publisher style.

## Pilot Gate

Before freeze, require reviewed taxonomy definitions, pilot agreement by label, an adjudication log, evidence that at least two topics can co-occur reliably, source authorization, split grouping rules, metric implementation tests, and independent external approval.

## Publication Artifacts

- taxonomy and annotation-decision table;
- prevalence/co-occurrence figure;
- per-label agreement table;
- source/domain distribution table;
- baseline and robustness results;
- qualitative error taxonomy.

## Open Questions

- Does `civic_admin` need separate legal, electoral, or public-service subtopics?
- Is `security` distinguishable from disaster and civic communication?
- What minimum positive count supports a stable per-label claim?
- Should hierarchical labels be introduced after v0.1?

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-09 | Proposed multi-label task contract and review gates. | SUBMITTED_TO_REVIEW |
| 2026-09-10 | Internal AI-assisted audit requested ontology, agreement, and threshold-protocol revisions. | NEEDS_REVISION |
| 2026-09-10 | Incorporated pre-review corrections and resubmitted the candidate specification for external review. | SUBMITTED_TO_REVIEW |
