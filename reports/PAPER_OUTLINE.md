# Paper Outline: KreyolBench

## Purpose

Maintain the evolving publication blueprint for KreyolBench.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

## Working Title

KreyolBench: A Kreyol-First Benchmark Suite for Haitian Creole NLP

## Publication Scope Boundary

This outline is for the first controlled benchmark paper. It may describe only task instances, sources, datasets, metrics, and results that pass their applicable review and release gates. It does not define the permanent KreyolBench research program or task universe.

Later task-expansion, dataset/resource, linguistic-analysis, robustness, speech, multimodal, and domain-specific papers remain possible research pathways. They require independent evidence and are not commitments of this paper.

## 1. Introduction

### 1.1 Motivation

Purpose: explain why Haitian Creole NLP needs dedicated benchmark infrastructure.

Evidence needed: speaker community context, low-resource NLP benchmark gap, public-interest use cases.

Artifacts required: source landscape summary.

Tables/Figures: motivation figure or benchmark positioning table.

Status: SUBMITTED_TO_REVIEW

### 1.2 Haitian Creole NLP Context

Purpose: describe Haitian Creole as a language with its own orthography, variation, domains, and sociolinguistic importance.

Evidence needed: linguistic references and existing Haitian Creole resources.

Artifacts required: language/context bibliography.

Status: SUBMITTED_TO_REVIEW

### 1.3 Research Gap

Purpose: define what current multilingual/Creole benchmarks do not cover.

Evidence needed: comparison to CreoleVal, multilingual benchmarks, African-language benchmarks, and task coverage.

Artifacts required: related benchmark matrix.

Status: SUBMITTED_TO_REVIEW

### 1.4 KreyolBench Objectives

Purpose: state benchmark objectives and public-interest domains.

Evidence needed: task specs, domain definitions, governance policy.

Status: SUBMITTED_TO_REVIEW

### 1.5 Contributions

Purpose: list defensible contributions.

Evidence needed: completed artifacts only.

Status: BLOCKED until implementation evidence exists.

## 2. Related Work

### 2.1 Haitian Creole Resources

Purpose: summarize existing corpora, datasets, speech resources, dictionaries, and digital resources.

Evidence needed: source registry review.

Status: SUBMITTED_TO_REVIEW

### 2.2 Creole NLP Benchmarks

Purpose: position KreyolBench relative to Creole-focused resources.

Evidence needed: benchmark comparison table.

Status: TO_REVIEW_LATER

### 2.3 Multilingual and Low-Resource Benchmarks

Purpose: situate within XNLI-style, XTREME-style, African-language, and low-resource benchmark work.

Evidence needed: literature review.

Status: TO_REVIEW_LATER

### 2.4 Benchmark Design and Evaluation

Purpose: justify task choice, splits, metrics, and hidden tests.

Evidence needed: benchmark methodology references.

Status: SUBMITTED_TO_REVIEW

## 3. Dataset Construction

### 3.1 Source Registry

Purpose: explain provenance and license tracking.

Artifacts required: source registry table.

Tables/Figures: source inventory and license matrix.

Status: SUBMITTED_TO_REVIEW

### 3.2 Corpus Inclusion and Exclusion

Purpose: define criteria for source inclusion.

Evidence needed: reviewed sources and excluded sources.

Status: BLOCKED pending source review.

### 3.3 Preprocessing

Purpose: describe cleaning, OCR, dedupe, sentence splitting, PII, and orthography handling.

Artifacts required: preprocessing pipeline diagram.

Status: TO_REVIEW_LATER

### 3.4 Raw and Normalized Text

Purpose: explain preservation of raw forms and normalization fields.

Evidence needed: normalization policy and examples.

Status: SUBMITTED_TO_REVIEW

## 4. Annotation

### 4.1 Annotation Tasks

Purpose: describe each task requiring human labels.

Artifacts required: task specs and annotation guidelines.

Status: SUBMITTED_TO_REVIEW

### 4.2 Annotator Training

Purpose: explain pilot, calibration, and gold examples.

Artifacts required: training examples and onboarding checklist.

Status: DRAFT

### 4.3 Annotation Quality

Purpose: report agreement and adjudication.

Tables/Figures: inter-annotator agreement table, disagreement taxonomy.

Experiments required: double annotation subset.

Status: BLOCKED until annotation pilot.

## 5. Tasks and Formats

Purpose: describe input/output format, labels, use cases, sources, and evaluation for each task.

Provisional v0.1 task instances:

- `kb_cls_topic_multilabel_v0_1`
- `kb_ie_ner_charspan_v0_1`
- `kb_ret_hybrid_query_v0_1`
- `kb_norm_orthography_v0_1`
- `kb_lc_token_language_id_v0_1`

QA remains feasibility-only. Translation is deferred from v0.1. Sentiment,
summarization, and orthographic robustness remain roadmap work.

Status: SUBMITTED_TO_REVIEW

## 6. Splits and Leakage Prevention

Purpose: document train/validation/test strategy, hashing, deduplication, and hidden-test policy.

Artifacts required: split report, leakage report, hash manifest.

Status: SUBMITTED_TO_REVIEW

## 7. Baseline Models

Purpose: describe random/majority, classical, multilingual encoder, retrieval, MT, and LLM baselines.

Tables/Figures: baseline matrix, compute table.

Experiments required: reproducible baseline runs.

Status: SUBMITTED_TO_REVIEW

## 8. Evaluation and Statistical Analysis

Purpose: define metrics, confidence intervals, significance tests, effect sizes, and per-domain slices.

Tables/Figures: metric table, statistical testing table.

Status: SUBMITTED_TO_REVIEW

## 9. Results

Purpose: present validated benchmark results.

Artifacts required: frozen result JSON, run configs, predictions where releasable.

Status: BLOCKED until dataset and baselines are validated.

## 10. Error Analysis and Robustness

Purpose: explain model failures across domain, register, orthography, code-switching, and label groups.

Artifacts required: error analysis notebooks and tables.

Status: BLOCKED until results exist.

## 11. Ethics, Governance, and Limitations

Purpose: document privacy, licensing, non-extractive collaboration, limitations, and out-of-scope use.

Artifacts required: data governance docs, dataset card, limitations section.

Status: SUBMITTED_TO_REVIEW

## 12. Reproducibility

Purpose: describe code, configs, dataset version, model metadata, and run metadata.

Artifacts required: reproducibility checklist, result schema, release archive.

Status: TO_REVIEW_LATER

## 13. Discussion

Purpose: interpret scientific implications without overclaiming.

Status: BLOCKED until results and error analysis exist.

## 14. Conclusion

Purpose: summarize contributions and future work.

Status: BLOCKED until contribution claims are validated.

## Appendices

- task schemas
- annotation guidelines
- source registry details
- license matrix
- split hashes
- baseline hyperparameters
- full per-domain results
- error examples
- ethics checklist

Status: DRAFT

## Artifact Traceability Table

| Artifact ID | Artifact | Paper dependency | Evidence needed | Status |
| --- | --- | --- | --- | --- |
| KB-PUB-TAB-001 | Source inventory table | 3.1 | reviewed source registry | SUBMITTED_TO_REVIEW |
| KB-PUB-TAB-002 | License matrix | 3.1 | legal/source review | BLOCKED |
| KB-PUB-TAB-003 | Task statistics table | 5 | frozen dataset | BLOCKED |
| KB-PUB-TAB-006 | Task feasibility matrix | 1.4, 5 | task specs and metadata-only source assessment | SUBMITTED_TO_REVIEW |
| KB-PUB-APP-001 | Five task specifications | 4.1, 5, appendices | independent external review | SUBMITTED_TO_REVIEW |
| KB-PUB-TAB-004 | Annotation agreement table | 4.3 | double annotation and adjudication | BLOCKED |
| KB-PUB-TAB-005 | Baseline results table | 9 | validated baseline runs | BLOCKED |
| KB-PUB-FIG-001 | Preprocessing pipeline | 3.3 | finalized preprocessing spec | TO_REVIEW_LATER |
| KB-PUB-FIG-002 | Error analysis slices | 10 | result and error-analysis artifacts | BLOCKED |

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial detailed paper blueprint. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Linked the five-task specification and feasibility artifacts. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Bounded the first paper to validated release instances without narrowing the research program. | SUBMITTED_TO_REVIEW |
