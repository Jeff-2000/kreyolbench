# Research Scope

## Purpose

Define what KreyolBench may include, what belongs later, and what requires expert review before expansion.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

## What KreyolBench Is

KreyolBench is a Kreyol-first research program and extensible benchmark ecosystem for scientifically rigorous Haitian Creole language and AI evaluation. It may contain task families, concrete task instances, datasets, challenge sets, domains, modalities, evaluation protocols, controlled releases, and publication artifacts.

KreyolBench is not the current five-task list, a single dataset, a single paper, a translation of an English benchmark, or a claim that all Haitian Creole language use can be represented by one corpus or score.

The governing principle is: bounded releases inside an extensible scientific benchmark ecosystem.

## Scope Levels

- Research program: the long-term scientific initiative.
- Benchmark ecosystem: the extensible collection of evaluated artifacts.
- Task family: a broad capability area.
- Task instance: a concrete, stable, governed specification.
- Pilot scope: feasibility work that does not authorize release.
- Release scope: task instances explicitly associated with a version.

`datasets/TASK_TAXONOMY.md` defines the complete hierarchy. `configs/releases/` is authoritative for release membership.

## Current Scientifically Active Scope

The v0.1 controlled pilot contains five provisional task instances:

- multi-label topic classification;
- character-span NER with optional nesting support;
- hybrid-query information retrieval with graded qrels;
- orthography-only, multi-reference normalization;
- token-level code-switch identification.

All five are `PILOT_CANDIDATE` and `SUBMITTED_TO_REVIEW`. No task is included in a release. Question answering is `FEASIBILITY_ONLY`; translation is `DEFERRED`; sentiment and summarization remain `ROADMAP` instances.

These formulations apply only to the identified v0.1 task instances. They do not permanently define classification, information extraction, retrieval, normalization, or language-contact research in KreyolBench.

## Near-Term Scope

- independent review of the five pilot specifications;
- metadata-only source feasibility and authorization review;
- revision of rejected or conditional task proposals;
- one bounded annotation pilot after both task and source gates are satisfied;
- evidence-based metric, split, agreement, and baseline decisions.

## Long-Term Expansion Capacity

The ecosystem may later support additional classification, information extraction, retrieval, QA, generation, translation, normalization, code-switching, robustness, LLM evaluation, speech, audio, OCR, document, and multimodal task instances. It may also expand into agriculture, environment, law, economics, finance, migration, diaspora, STEM, history, literature, social media, everyday conversation, labor, and humanitarian domains.

These are possible research pathways, not validated components or release commitments. The machine-readable task and domain registries remain open-world and non-exhaustive.

## Signature Research Axes

KreyolBench should support Haitian Creole-specific analysis of orthographic and lexical variation, borrowing, code-switching, Haitian entities, register, institutional and informal language, Haiti and diaspora usage, French/English/Spanish influence, multilingual transfer, source shift, temporal change, human versus translated or generated content, contamination, uncertainty, metric disagreement, ranking stability, and benchmark saturation.

Research axes may define slices, challenge sets, robustness analyses, or future tasks. They must not be normalized away for implementation convenience.

## Expansion Policy

`KB-SCOPE-002` establishes that the task registry remains open-world. Registration or roadmap placement never implies scientific validation, implementation priority, release inclusion, corpus authorization, annotation authorization, metric approval, or publication evidence.

A proposed task instance must document its research gap, construct, Haitian Creole relevance, real-world use, sources and rights, data schema, annotation burden, metrics, uncertainty, splits, leakage risks, baselines, compute needs, limitations, and expert-review requirements. Release membership is a separate explicit decision.

## Claims Policy

The aspiration is to build reference-grade Haitian Creole AI research infrastructure. Current evidence supports only claims about artifacts that exist and have passed their stated gates. Terms such as first, largest, leading, most comprehensive, best, or state of the art require a systematic comparison and must not be inferred from project ambition.

## Explicitly Unresolved

- external validation of the five v0.1 task instances;
- source-specific legal, ethical, provenance, and scientific suitability;
- first pilot task and corpus;
- future modality ownership within this repository or companion components;
- publication-grade metrics, splits, claims, and leaderboard design.

## Acceptance Criteria

- No release list defines the global project scope.
- No task is added only because it is technically easy.
- Every implemented task has a stable instance ID and governed release relationship.
- Scientific status and scope status remain independent.
- Every expansion remains evidence-driven, Kreyol-grounded, and reviewable.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial research scope register. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Distinguished the open-world research program from the bounded v0.1 release. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Recorded project-scope approval of the open-world expansion policy; registry contents remain provisional. | EXPERT_VALIDATED |
