# KreyolBench

KreyolBench is a Kreyol-first benchmark scaffold for Haitian Creole NLP. It is designed for reproducible research, Hugging Face compatibility, and public release with explicit source, license, and provenance tracking.

The benchmark prioritizes real-world Haitian Creole use cases: education, public health, civic information, disaster response, administration, translation, search, text normalization, and digital inclusion.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

kreyolbench validate-dataset --task ner --path data/sample/ner.jsonl
kreyolbench audit-governance --root . --format text
kreyolbench evaluate --task classification --predictions data/sample/classification_topic.jsonl --references data/sample/classification_topic.jsonl
pytest
```

The governance audit distinguishes structural validity from scientific approval. A `PASS` result can still report `release_eligible: false` while expert decisions remain unresolved.

## Tasks

Version `v0.1` targets topic/domain classification, NER, extractive QA, retrieval, text normalization, code-switch sentence/token labels, and translation metadata evaluation. Later releases add sentiment, summarization, orthographic robustness, hidden tests, and larger domain transfer settings.

## Data Policy

This repository does not assume external datasets are redistributable. Source adapters and registry files record public HTTPS locations, access methods, licenses, and review status. Raw external data should be stored under `data/raw/` locally and should not be committed unless redistribution is explicitly allowed.

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

- `configs/`: benchmark, task, label, source, and orthography configuration.
- `data/`: local raw/interim/processed data plus committed tiny sample fixtures.
- `datasets/`: Hugging Face dataset loader and dataset card.
- `src/kreyolbench/`: installable Python package and CLI.
- `annotation/`: annotation guidelines, Label Studio configs, and examples.
- `eval/`: evaluation configs and generated results.
- `leaderboard/`: submission schema and public table template.
- `docs/`: governance, ethics, release, and paper planning documents.
- `tests/`: schema, preprocessing, metric, and CLI tests.
