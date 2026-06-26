# Product Boundaries

YouTube Brain is an advisory, read-only Obsidian brain for YouTube creator growth and strategy: the recommendation system and discovery, audience retention and average view duration, packaging (titles, thumbnails, click-through rate), Shorts versus long-form, publishing cadence, monetization (YouTube Partner Program and RPM), analytics interpretation, and community..

## It Does

- Preserve raw sources under `.raw/`.
- Synthesize source-cited notes and deliverables.
- Maintain action queues, reports, and next actions.
- Keep decisions auditable through source links and rollback notes.
- Gate maturity through `references/source-ledger.json`,
  `references/adapter-manifest.json`, and `scripts/audit_brain.py`.

## It Does Not

- No growth, revenue, or monetization claim without a current official or primary source
- No credentials, OAuth tokens, cookies, earnings, or private audience data in repo artifacts
- No sub4sub, bot engagement, engagement bait, or platform-policy-violating tactics
- No account mutation or upload automation without explicit owner approval and an audit trail
- No irreversible recommendation without owner, confidence, source, and rollback note

## Safety Risks

- Private channel analytics, audience, revenue, or comment data in raw inputs
- Stale recommendation or monetization policy leading to wrong advice
- Overconfident growth projections from incomplete or short channel history
- Rapid platform policy shifts (demonetization rules, harmful content definitions)
- Generated reports leaking local filesystem paths or third-party tool API drift

## Maturity Boundary

This repo starts as `scaffolded`. Market-ready quality requires current
research, domain adapters, deterministic demo verification, source citations,
Obsidian graph hygiene, and release scans. The audit score is capped below 90
until those stages are complete.
