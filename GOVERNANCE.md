# Governance

KreyolBench uses a controlled collaboration model. The project welcomes international collaborators, but access, authorship, public representation, and release authority are staged according to role, trust, and contribution history.

## Roles

### Project Lead

The project lead owns project direction, public representation, sensitive-access approval, release approval, and dispute escalation.

### Maintainers

Maintainers review pull requests, triage issues, enforce contribution standards, and approve non-sensitive changes in their area. Maintainers do not receive unrestricted data access by default.

### Working-Group Leads

Working-group leads coordinate scoped areas:

- Data Governance
- Annotation and Linguistics
- NLP Benchmarking
- ASR/Speech
- LLM Evaluation
- Statistical Evaluation
- Paper and Grants
- Infrastructure and Release

### Core Collaborators

Core collaborators contribute substantially to research design, data creation, experiments, writing, or release preparation. They may receive access to private drafts or non-sensitive internal materials.

### Verified Contributors

Verified contributors have completed at least one accepted contribution and may receive scoped issue assignments, annotation tasks, or branch access when needed.

### Public Contributors

Public contributors participate through issues, forks, documentation fixes, public sample data, and pull requests.

### Data Stewards

Data stewards are a small trusted group approved to handle restricted data, PII-risk data, consent records, or non-redistributable corpora. Data stewardship is a separate role from maintainer status.

## Access Levels

| Level | Typical Access | Example Work |
| --- | --- | --- |
| Public | Public repo, issues, docs, sample data | Docs, public bug reports, small fixes |
| Verified | Assigned issues, public branches, non-sensitive annotation | Baselines, validation, public samples |
| Core | Private planning docs, paper drafts, internal results | Paper sections, experiments, roadmap |
| Data Steward | Restricted storage, consent records, raw/private data | License review, PII review, release approval |

Use least privilege. Access must be reviewed monthly and removed when no longer needed.

## Decision Rules

- Code, docs, and configs require pull-request review.
- Data releases require data-steward review and project-lead approval.
- Paper submissions require authorship confirmation and project-lead approval.
- Grant submissions require written agreement among named participants.
- Mission, license, security, and governance changes require project-lead approval.

## Working Rhythm

KreyolBench uses six-week sprint cycles:

1. Week 1: goals and task assignment.
2. Weeks 2--4: implementation, annotation, experiments, or writing.
3. Week 5: review, validation, and error analysis.
4. Week 6: write-up, release notes, and next sprint planning.

Recommended meetings:

- Monthly all-hands.
- Biweekly working-group meetings.
- Weekly maintainer check-in.
- Async updates for global time zones.

## Required Update Format

Each collaborator should report:

- What I completed.
- What I am doing next.
- What is blocked.
- What decision I need.

## Decision Records

Important decisions must be documented in at least one durable place:

- GitHub issue comments.
- Pull-request discussion.
- Architecture decision records.
- Meeting notes.
- Updated governance documents.

Slack, Discord, and informal chat are useful for discussion but are not the final source of truth.

## Disputes

Disputes should be handled first by the relevant working-group lead, then by maintainers, then by the project lead. Authorship, restricted data, misconduct, and security disputes should be escalated immediately to the project lead.

