# KreyolBench

KreyolBench is a Kreyol-first research program and extensible benchmark ecosystem for Haitian Creole NLP and AI evaluation. It is designed for reproducible research, controlled releases, Hugging Face compatibility, and explicit source, license, and provenance tracking.

The benchmark prioritizes real-world Haitian Creole use cases: education, public health, civic information, disaster response, administration, translation, search, text normalization, and digital inclusion.

## Quick Start

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"

python -m kreyolbench.cli validate-dataset --task ner --path data/sample/ner.jsonl
python -m kreyolbench.cli audit-governance --root . --format text
python -m kreyolbench.cli evaluate --task classification --predictions data/sample/classification_topic.jsonl --references data/sample/classification_topic.jsonl
python -m pytest
```

Use the activated environment's `python` for every command. Mixing a global `python3.12` with separately installed `pytest` or `kreyolbench` executables can produce missing-dependency errors even when tests pass elsewhere.

The governance audit distinguishes structural validity from scientific approval. A `PASS` result can still report `release_eligible: false` while expert decisions remain unresolved.

## Tasks

Version `v0.1` proposes five pilot tasks: multi-label topic classification, character-span NER, corpus/query/qrels retrieval, orthography-only normalization, and token-level code-switching. Question answering remains feasibility-only; translation is deferred from the core release; sentiment and summarization remain roadmap items.

These task definitions are `SUBMITTED_TO_REVIEW`. They must receive independent external review before their schemas, labels, metrics, annotation protocols, or split rules are frozen. See `datasets/tasks/` and `reports/TASK_SPEC_REVIEW_PACKET_V0_1.md`.

The five tasks are concrete v0.1 instances, not the permanent KreyolBench task universe. The hierarchy is research program -> benchmark ecosystem -> task family -> task type -> task variant -> task instance -> release membership. See `datasets/TASK_TAXONOMY.md`.

KreyolBench aspires to become reference-grade Haitian Creole evaluation infrastructure. The repository does not claim to be first, largest, leading, best, or most comprehensive without systematic evidence.

## Data Policy

This repository does not assume external datasets are redistributable. Source registration is open-world and authorizes metadata discovery only. Legal, ethical, collection, derived-use, redistribution, and scientific-suitability decisions remain independent. Raw external data should be stored under `data/raw/` locally and should not be committed unless redistribution is explicitly approved.

Every benchmark example must retain item-level provenance. Source-family records are discovery containers and cannot be used as final example provenance. See `datasets/EXAMPLE_PROVENANCE.md` and `datasets/SOURCE_REGISTRY.md`.

## Collaboration and Security

KreyolBench uses staged collaboration and least-privilege access. New collaborators should start with a small non-sensitive task before receiving broader access.

- Project mission and ethical boundaries: `PROJECT_CHARTER.md`
- Governance and roles: `GOVERNANCE.md`
- Contribution workflow: `CONTRIBUTING.md`
- Conduct expectations: `CODE_OF_CONDUCT.md`
- Security and incident reporting: `SECURITY.md`
- Authorship and credit: `AUTHORSHIP.md`
- Restricted data rules: `DATA_ACCESS_POLICY.md`
- Full operating guide: `docs/collaboration_security_guide.md`
- Intake form: `docs/collaborator_intake_form.md`
- Onboarding checklist: `docs/onboarding_checklist.md`

## Candidate Source Families

These links are provenance candidates, not blanket approval for collection, redistribution, benchmark inclusion, or scientific representativeness. See `configs/sources/` for source-specific review status.

- CMU Haitian Creole resources: https://www.speech.cs.cmu.edu/haitian/
- CreoleVal: https://huggingface.co/papers/2310.19567
- CreoleVal GitHub: https://github.com/hclent/CreoleVal
- SEACrowd Creole RC: https://huggingface.co/datasets/SEACrowd/creole_rc
- OPUS API: https://opus.nlpl.eu/opusapi/
- OPUS corpora: https://opus.nlpl.eu/
- eBible Haitian Creole Bib La: https://ebible.org/bible/details.php?id=hat
- MSPP publications: https://mspp.gouv.ht/publications
- UN Haiti Kreyol site: https://haiti.un.org/ht
- Wikimedia htwiki dumps: https://dumps.wikimedia.org/htwiki/latest/
- Leipzig Haitian Wikipedia corpus: https://corpora.uni-leipzig.de/en?corpusId=hat_wikipedia_2011

## Repository Layout

- `configs/`: ecosystem, task taxonomy, domain, release, task, label, source, and orthography configuration.
- `data/`: local raw/interim/processed data plus committed tiny sample fixtures.
- `datasets/`: Hugging Face dataset loader, dataset card, provenance, and task taxonomy.
- `datasets/tasks/`: provisional scientific specifications for the five v0.1 pilot tasks.
- `src/kreyolbench/`: installable Python package and CLI.
- `annotation/`: annotation guidelines, Label Studio configs, and examples.
- `eval/`: evaluation configs and generated results.
- `leaderboard/`: submission schema and public table template.
- `docs/`: governance, ethics, release, and collaboration documents.
- `reports/`: expert-review packets, feasibility evidence, and publication planning.
- `tests/`: schema, preprocessing, metric, and CLI tests.
