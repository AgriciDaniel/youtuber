# Source Map

## Raw Sources

- YouTube Studio analytics exports and CSVs, video metadata lists, transcripts, thumbnails, competitor channel snapshots, deep-research reports, and dated operator notes on platform changes

## Enrichment Sources

- Official YouTube Creators and Help Center guides on growth, retention, and policy
- YouTube Studio analytics metric reference (watch time, AVD, CTR, traffic sources)
- YouTube Official Blog and Creator Insider announcements on the recommendation system
- YouTube Partner Program and monetization policy documentation
- Practitioner analytics methodology and benchmarks (vidIQ, TubeBuddy) and published creator case studies

## Import Strategy

- Copy raw source files into `.raw/sources/`.
- Record path, hash, retrieval date, owner, and source type.
- Record external research sources in `references/source-ledger.json`.
- Record implemented schemas and adapters in `references/adapter-manifest.json`.
- Create a source note under `wiki/sources/`.
- Link affected entities, workflows, and deliverables.
