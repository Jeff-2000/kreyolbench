# Security Policy

KreyolBench security covers code, infrastructure, data, unpublished research, collaborator access, credentials, and community trust.

## What to Report

Report immediately if you discover:

- Leaked API keys, tokens, passwords, or credentials.
- Raw data committed by mistake.
- PII, private speech, consent records, or annotator identity exposed.
- Unauthorized data access.
- License violations.
- Vulnerabilities in code or infrastructure.
- Model or dataset release that violates the data policy.
- Public misrepresentation of project claims.

## Reporting Process

Do not open a public issue for sensitive security or data-leak reports.

Contact the project lead or designated security maintainer privately with:

- A short description.
- Affected files, links, commits, services, or datasets.
- Whether exposure is public or private.
- Suggested immediate containment if known.

## Incident Response

Maintainers should follow this sequence:

1. Stop exposure: revoke keys, remove links, disable access, or revert public visibility.
2. Preserve evidence: save logs, commit hashes, screenshots, and timestamps.
3. Notify project lead and relevant maintainers.
4. Assess affected data, people, licenses, and systems.
5. Notify affected contributors, data providers, or institutions when needed.
6. Patch the issue and document the fix.
7. Update policy or tooling to prevent recurrence.

## Access Control

- Use least privilege.
- Prefer fork-based contributions for public contributors.
- Give write access only to trusted repeat contributors.
- Give admin access to almost nobody.
- Review access monthly.
- Remove access when a collaborator leaves or no longer needs it.

## Secret Handling

- Never commit `.env` files.
- Use `.env.example` for documentation.
- Do not paste API keys into issues, notebooks, commits, or chat.
- Rotate leaked keys immediately.
- Use secret scanning on hosted repositories when available.

## Data Security

- Keep `data/raw/` local and uncommitted unless redistribution is explicitly allowed.
- Store restricted datasets in controlled storage, not Git.
- Log restricted dataset access.
- Do not share consent records broadly.
- Run PII review before public release.

## Supported Versions

Security review applies to the active development branch and the latest public release.

