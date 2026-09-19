# CreoleVal Haitian Component Matrix v0.1

## Status

Current status: `SUBMITTED_TO_REVIEW`

Authorization effect: `NONE`.

This matrix prevents the CreoleVal family from being treated as one uniformly licensed or independent resource. Exact component names, revisions, licenses, hashes, and overlap evidence must be verified before use.

| Haitian task/component | Candidate subset | Scientific role | License state | Overlap and contamination action |
| --- | --- | --- | --- | --- |
| Machine translation | MIT-Haiti parallel material | Comparison and future MT reference | Per-asset verification required | Protect published evaluation partitions; reconcile with Kreyol-MT and upstream MIT-Ayiti assets. |
| Reading comprehension / QA | Haitian QA component | Benchmark comparison | Component license `TO_VERIFY` | Do not train on published evaluation examples; record parent dataset and exact split. |
| Classification | Haitian classification component | Benchmark comparison | Component license `TO_VERIFY` | Compare ontology and source lineage before mapping to KreyolBench. |
| Relation or information extraction | Haitian structured component | Benchmark comparison | Component license `TO_VERIFY` | Audit source text, labels, and overlap with public multilingual mixtures. |
| Other aggregated tasks | Exact component `TO_VERIFY` | Discovery and comparison only | Per-component review required | Register one child per selected artifact; never infer uniform rights from the family repository. |

## Required Child Record Fields

`component_id`, upstream dataset, task, language configuration, split, immutable revision, hash, license evidence, content origin, derivation steps, protected-evaluation status, known or possible overlap, and citation.

## Completion Gate

No component may enter training, evaluation, redistribution, or a release until its child record and every applicable authorization gate are approved.

