# A-to-Z Collaboration Security Guide

This guide explains how to work with international collaborators while protecting KreyolBench assets: ideas, datasets, annotations, code, evaluation results, authorship, community trust, and future grants.

It builds on:

- `PROJECT_CHARTER.md`
- `GOVERNANCE.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `AUTHORSHIP.md`
- `DATA_ACCESS_POLICY.md`
- `docs/data_governance.md`
- `docs/ethics.md`
- `docs/release_checklist.md`

This is operational guidance, not legal advice. Use qualified counsel or institutional review for formal contracts, IRB/ethics review, sensitive data sharing, funding agreements, or disputed authorship.

## Phase 1: Protect the Project Before Onboarding Anyone

1. Define the project lead, mission, scope, allowed uses, prohibited uses, and decision process in `PROJECT_CHARTER.md`.
2. Classify assets as public, private, or sensitive.
3. Use tiered access: public contributor, verified contributor, core collaborator, data steward.
4. Keep governance documents visible and current.

## Phase 2: Screen and Classify Collaborators

Use an intake form for every serious collaborator. Ask for:

- Name, affiliation, country, and time zone.
- Expertise.
- Desired role.
- GitHub, ORCID, Google Scholar, LinkedIn, or equivalent profile if available.
- Conflict-of-interest disclosure.
- Access needs.

Hold a short onboarding call before granting core access. Confirm contribution scope, expectations, desired credit, data needs, and deadline commitment.

Start every new collaborator with a small probation task:

- Review one document.
- Fix one issue.
- Annotate a tiny public sample.
- Run one baseline.
- Write a literature summary.
- Validate one source registry entry.

## Phase 3: Secure the Technical Workflow

- Require pull requests.
- Block direct pushes to `main`.
- Require at least one reviewer.
- Require tests before merge where feasible.
- Use branch names such as `feature/asr-baseline-whisper` or `docs/data-policy-update`.
- Prefer fork-based contributions for public contributors.
- Grant write access only to trusted repeat contributors.
- Review access monthly.
- Never commit API keys or `.env` files.
- Keep `data/raw/` local and uncommitted unless redistribution is explicitly allowed.
- Store restricted datasets in controlled storage, not Git.

## Phase 4: Secure Data, Ethics, and Community Trust

Every data source needs registry metadata:

- URL.
- Access method.
- License.
- Redistribution status.
- Citation.
- Language claim.
- Domain.
- Collection date.
- Hash.
- PII risk.
- Review status.

Do not redistribute data unless permitted. Classify every source as public, link-only, derived-only, internal research, or restricted sensitive.

Before release:

- Run PII detection.
- Manually review sensitive examples.
- Remove private annotator logs.
- Document known risks.
- Preserve dialect, register, and orthographic limitations.

For speech, interviews, annotations, or community text, use plain-language consent and avoid collecting unnecessary identity fields.

## Phase 5: Manage Authorship, IP, and Credit

Set authorship rules before serious writing begins. Substantial research design, data creation, modeling, analysis, or writing can qualify for authorship. Small fixes, brief feedback, or one-off annotation usually receive acknowledgement.

Track contributions through:

- Git commits.
- Pull requests.
- Issue assignments.
- Annotation logs.
- Meeting notes.
- Paper section ownership.
- CRediT taxonomy.

Clarify license boundaries:

- Code uses Apache-2.0 unless changed.
- Data licenses vary by subset.
- Papers need coauthor agreement before preprint.
- Models must document training data and license compatibility.

For core collaborators, use a lightweight MOU when needed, covering scope, contribution, confidentiality, data access, authorship expectations, publication plan, IP/license understanding, and exit process.

## Phase 6: Organize the Work

Create working groups:

- Data Governance.
- Annotation and Linguistics.
- NLP Benchmarking.
- ASR/Speech.
- LLM Evaluation.
- Statistical Evaluation.
- Paper and Grants.
- Infrastructure and Release.

Use six-week sprint cycles:

1. Week 1: goals and task assignment.
2. Weeks 2--4: implementation, annotation, experiments, or writing.
3. Week 5: review, validation, and error analysis.
4. Week 6: write-up, release notes, and next sprint planning.

Maintain one source of truth:

- GitHub Issues for tasks.
- GitHub Projects, Linear, or Trello for sprint board.
- Shared drive for private documents.
- Zotero for papers.
- Slack or Discord for conversation, not final decisions.

## Phase 7: Publication and Grant Workflow

Do not share full paper drafts too broadly. Use levels:

- Public outline.
- Core writing-team draft.
- Advisor review draft.
- Preprint/public release.

Before writing claims:

- Freeze dataset splits.
- Hash evaluation sets.
- Save baseline configs.
- Save results.
- Record failed experiments when relevant.
- Document limitations.

Before submission:

- Dataset card complete.
- Ethics section complete.
- License review complete.
- PII scan complete.
- Reproducibility package complete.
- Authorship confirmed in writing.
- Community-sensitive claims reviewed.

For grants, keep a reusable package:

- One-page concept note.
- Problem statement.
- Team bios.
- Budget template.
- Letters of support.
- Data governance plan.
- Timeline and deliverables.

## Phase 8: Communication Rules

Use official channels:

- Public announcements: website or newsletter.
- Public development: GitHub.
- Collaborator chat: Discord or Slack.
- Formal decisions: email or documented meeting notes.
- Sensitive data: controlled storage only.

Recommended cadence:

- Monthly all-hands.
- Biweekly working-group meetings.
- Weekly maintainer check-in.
- Async updates for global time zones.

Each collaborator update should answer:

- What I completed.
- What I am doing next.
- What is blocked.
- What decision I need.

## Phase 9: Incident Response

Incidents include:

- Leaked data.
- Leaked API key.
- Unauthorized access.
- License violation.
- Plagiarism.
- Authorship conflict.
- Harassment.
- Public misrepresentation of project claims.

Response:

1. Stop exposure: remove access, revoke keys, disable links.
2. Preserve evidence: screenshots, logs, commits.
3. Notify maintainers.
4. Assess harm.
5. Notify affected people if needed.
6. Document fix.
7. Update policy to prevent recurrence.

## Phase 10: First 30 Days Action Plan

### Week 1

- Publish governance, contributing, authorship, security, and data-access documents.
- Define collaborator roles.
- Create intake form.
- Audit repository permissions.

### Week 2

- Set branch protections.
- Create issue templates and pull-request templates.
- Create contributor onboarding checklist.
- Classify current collaborators by access level.

### Week 3

- Launch working groups.
- Assign probation tasks.
- Create sprint board.
- Start source-license audit.

### Week 4

- Review first contributions.
- Promote reliable contributors gradually.
- Freeze the first six-week sprint.
- Publish a public "How to Collaborate" page.

