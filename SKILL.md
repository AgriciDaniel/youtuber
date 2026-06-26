---
name: youtube-brain
description: >
  Scaffold and operate YouTube Brain, a source-cited Obsidian brain for YouTube creator growth and strategy: the recommendation system and discovery, audience retention and average view duration, packaging (titles, thumbnails, click-through rate), Shorts versus long-form, publishing cadence, monetization (YouTube Partner Program and RPM), analytics interpretation, and community..
  Use when the user says "youtube-brain", "YouTube Brain", "create a YouTube creator growth and strategy: the recommendation system and discovery, audience retention and average view duration, packaging (titles, thumbnails, click-through rate), Shorts versus long-form, publishing cadence, monetization (YouTube Partner Program and RPM), analytics interpretation, and community. brain",
  "import sources", "synthesize plan", "render report", or wants a persistent
  vault-backed operating system for YouTube creator growth and strategy: the recommendation system and discovery, audience retention and average view duration, packaging (titles, thumbnails, click-through rate), Shorts versus long-form, publishing cadence, monetization (YouTube Partner Program and RPM), analytics interpretation, and community..
argument-hint: "new | ingest | synthesize | report | visuals | lint | next"
license: Apache-2.0
---

# YouTube Brain

Operate the vault first. Read `CODEX.md`, `wiki/hot.md`, and `wiki/index.md`
before changing notes.

## Commands

```bash
/youtube-brain new <client-slug> --owner <name>
/youtube-brain ingest --vault <path> --file <source>
/youtube-brain synthesize --vault <path>
/youtube-brain report --vault <path>
/youtube-brain visuals --vault <path>
/youtube-brain lint --vault <path>
/youtube-brain next --vault <path>
```

Source checkout equivalent:

```bash
youtube-brain new <client-slug> --owner <name>
youtube-brain ingest --vault <path> --file <source>
youtube-brain synthesize --vault <path>
youtube-brain report --vault <path> --html-only
```

## Required Operating Rules

1. Read `<vault>/CODEX.md`.
2. Read `<vault>/wiki/hot.md`.
3. Read `<vault>/wiki/index.md`.
4. Preserve `.raw/` as immutable source material.
5. Never store credentials in the vault.
6. Never make domain-specific claims without dated trustworthy sources.
7. Keep `hot`, `index`, `overview`, and `log` current.
8. Record research evidence in `references/source-ledger.json`.
9. Record domain adapter completion in `references/adapter-manifest.json`.

## Script Mapping

- `new` -> `python scripts/scaffold_vault.py`
- `ingest` -> `python scripts/ingest_source.py`
- `synthesize` -> `python scripts/synthesize_brain.py`
- `report` -> `python scripts/render_brain_report.py`
- `visuals` -> `python scripts/generate_vault_visuals.py`
- `lint` -> `python scripts/lint_vault.py`
- `next` -> `python scripts/guide_next_action.py`

## Quality Gates

- No growth, revenue, or monetization claim without a current official or primary source
- No credentials, OAuth tokens, cookies, earnings, or private audience data in repo artifacts
- No sub4sub, bot engagement, engagement bait, or platform-policy-violating tactics
- No account mutation or upload automation without explicit owner approval and an audit trail
- No irreversible recommendation without owner, confidence, source, and rollback note

Do not call this brain market-ready unless `scripts/audit_brain.py --require
market-ready` passes. A scaffold is not a finished brain.

## Research Refresh

monthly for YouTube Creators and Help Center guides plus YouTube Studio analytics references; on-changelog for recommendation and monetization policy changes; quarterly for practitioner benchmarks (vidIQ, TubeBuddy)


## Community

Built and maintained inside the AI Marketing Hub Pro community. Join, ask questions, and get the latest YouTube creator-growth playbooks at https://www.skool.com/ai-marketing-hub-pro
