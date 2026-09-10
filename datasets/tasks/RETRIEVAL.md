# Information Retrieval Specification

## Status

Current status: SUBMITTED_TO_REVIEW

Decision: `KB-TASK-RET-001`

Task instance: `kb_ret_hybrid_query_v0_1`

Task family / type / variant: retrieval / information retrieval / hybrid queries with graded qrels

Scope status: PILOT_CANDIDATE for v0.1

Owner: Retrieval working group

Required external review: Haitian public-information expert and information-retrieval researcher

This specification defines one provisional v0.1 retrieval instance. It does not constrain future ad-hoc, semantic, cross-lingual, conversational, evidence, RAG, long-document, or multimodal retrieval research.

## Purpose and Construct

Measure whether a system ranks Haitian Creole documents by usefulness for a Haitian Creole information need. The task evaluates retrieval, not answer generation or factual correctness beyond the relevance judgment.

## Research Value and Use Cases

- Search public-health, education, civic, and disaster-response information.
- Study lexical, orthographic, semantic, and cross-domain retrieval failure.
- Compare sparse, dense, multilingual, and reranking methods in a low-resource setting.

## Canonical Artifacts

- `corpus.jsonl`: `doc_id`, text, language, domain, temporal snapshot, publication date where known, source provenance, metadata.
- `queries.jsonl`: `query_id`, query-family ID, text, language, domain, split, query origin, provenance note.
- `qrels.jsonl`: `query_id`, `doc_id`, `judgment_status=JUDGED`, relevance 0–3, assessor ID, adjudication status.

The corpus is shared across queries. Candidate documents must not be embedded in canonical query rows. Missing qrels mean `UNJUDGED`, not relevance zero. Standard metric code may computationally treat an unjudged result as nonrelevant, but this evaluation choice must be explicit and cannot alter canonical qrels.

## Query Construction

Use a hybrid design with explicit provenance:

1. `CONSENTED_USER_NEED`: directly contributed under an approved consent and privacy protocol.
2. `STAKEHOLDER_ELICITED`: elicited from an authorized community, service, or domain stakeholder process.
3. `DOMAIN_EXPERT_RECONSTRUCTED`: reconstructed by an expert from a documented real-world need without access to target-document wording.
4. `EXPERT_AUTHORED_FROM_BRIEF`: independently written from an information-need brief without copying target-document phrases.
5. `DOCUMENT_DERIVED_DIAGNOSTIC`: derived from a document only for declared diagnostics; prohibited from principal public or hidden test splits.

Record origin, query-family ID, construction protocol, consent or ethics evidence where applicable, and whether target text was visible to the author. Public help-seeking material is not automatically eligible merely because it is visible online.

## Relevance Scale

- `0`: not useful for satisfying the information need.
- `1`: topically related but insufficient or only marginally useful.
- `2`: substantively relevant and useful, though incomplete.
- `3`: highly relevant and directly useful for the stated need.

Judges assess the query-document pair, not publisher prestige. Factual-quality or safety concerns should be recorded separately from topical relevance rather than hidden in the score.

## Pooling and Judgment

Construct pools from at least BM25, character n-gram, multilingual dense, and reranking systems. Record each run, depth, union size, duplicate handling, and contribution to newly judged relevant documents. Randomly include documents outside the pool for quality checks. Independently judge an overlapping pilot subset, adjudicate major disagreements, and report judgment depth, assessor overlap, unjudged rate, and agreement. Do not publish exhaustive-recall claims unless judgment coverage supports them.

## Sources and Representativeness

Candidate collections include approved health, education, civil-protection, civic, MIT-Ayiti, UN Haiti, and Wikimedia subsets. Assess authority, date, reading level, register, content origin, document length, duplication, and geographic relevance. Legal access to a document does not establish its factual reliability.

## Splits and Leakage

Assign splits at query-family and source-document group level. Keep paraphrases of one need together. Prevent a query from reproducing its relevant document text. Every corpus release must carry a temporal snapshot ID; time-sensitive documents retain publication or effective dates where known. Report document overlap and source-domain transfer. Authority and freshness are separate metadata dimensions, not hidden relevance shortcuts.

## Evaluation Candidates

Candidate primary metric: nDCG@10 using graded qrels, with the standard unjudged-as-nonrelevant computation stated explicitly. Required sensitivity evidence: judged@10, bpref at a preregistered relevance cutoff, and pooling-depth analysis. Secondary evidence: MRR@10, Recall@10/100, MAP only where judgment coverage permits, per-domain performance, and bootstrap confidence intervals resampled by query. No primary metric is frozen before the pilot coverage audit and external review.

## Baselines

- BM25 with documented tokenization;
- character n-gram retrieval for orthographic robustness;
- multilingual sentence embedding retrieval;
- cross-encoder reranking over a fixed candidate pool;
- zero-shot multilingual instruction reranking where licensing permits.

## Error Analysis

Analyze orthographic mismatch, lexical gap, query length, code-switching, rare terminology, stale documents, source authority, domain transfer, unjudged top results, duplicate documents, and real versus expert-authored queries.

## Pilot Gate

Require an authorized corpus subset, an ethical query protocol, reviewed relevance definitions, at least two retrieval paradigms for pooling, pilot agreement, qrel coverage analysis, split/leakage checks, metric tests, and independent Haitian-domain/IR approval.

## Publication Artifacts

- corpus and query-source distributions;
- query-construction flow diagram;
- pooling and judgment-coverage table;
- inter-assessor agreement;
- sparse/dense/reranking baseline table;
- per-query-origin and robustness analysis.

## Open Questions

- Which real-needs collection route is legally and ethically feasible?
- What pool depth is supportable within the annotation budget?
- Should document authority or freshness become separate evaluation dimensions?
- Can public and hidden qrels share one corpus without contamination?

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-09 | Proposed hybrid-query corpus/query/qrels protocol. | SUBMITTED_TO_REVIEW |
| 2026-09-10 | Internal AI-assisted audit requested query-provenance, pooling, and unjudged-treatment revisions. | NEEDS_REVISION |
| 2026-09-10 | Added operational provenance, judgment, pooling, and sensitivity rules; resubmitted for external review. | SUBMITTED_TO_REVIEW |
