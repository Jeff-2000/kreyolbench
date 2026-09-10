# Dataset Card for KreyolBench

## Dataset Summary

KreyolBench is a Kreyol-first research program and extensible benchmark ecosystem for Haitian Creole NLP and AI evaluation. The current repository is a governed scaffold, not a released dataset.

## Languages

Primary language: Haitian Creole (`hat`, `ht`). Some subsets explicitly include French, English, or Spanish code-switching labels.

## Tasks

The provisional v0.1 pilot contains multi-label topic classification, character-span NER, hybrid-query retrieval, orthographic normalization, and token-level code-switch identification. QA is feasibility-only, translation is deferred, and sentiment and summarization remain roadmap instances. Future task families are registered separately and are not implemented or released by this card.

## Licensing

Code is Apache-2.0. Data licenses are subset-specific. Rows include source metadata and license fields. Do not redistribute text from sources marked `review_required` or `not_approved_for_redistribution`.

## Annotation

Human annotation uses task-specific guidelines, gold examples, double annotation, adjudication, and agreement reporting.

## Intended Use

Benchmarking Haitian Creole NLP systems, error analysis, low-resource NLP research, and reproducible baseline comparisons.

## Out-of-Scope Use

Do not use KreyolBench for surveillance, sensitive identity inference, automated denial of services, or unsupported claims about all Haitian Creole dialects or speakers.

## Limitations

No validated release currently exists. Future releases may be small, domain-skewed, and may underrepresent informal speech, regional variation, and diaspora language practices; limitations must be measured for each release rather than assumed away.
