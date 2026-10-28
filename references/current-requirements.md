# Current Requirements

Status: source list re-verified and current as of 2026-10-28. Rows whose source was re-checked on 2026-10-28 carry that retrieval date; other rows keep their 2026-06-23 verification. See the refresh log at the end of this file.

## Refresh Cadence

Monthly for YouTube Creators and Help Center guides plus YouTube Studio analytics references; on-changelog for recommendation and monetization policy changes; quarterly for practitioner benchmarks (vidIQ, TubeBuddy).

## Required Source Standard

Use official, primary, vendor, standards-body, regulator, or API documentation first. Record URL, retrieval date, version or last-seen state, deprecation or sunset notes, and confidence. The structured ledger lives in `source-ledger.json`; the dated citation packs are `wiki/sources/research-pack-2026-06-23.md` (initial research) and `wiki/sources/research-pack-2026-10-28.md` (verification refresh).

## Current Platform Facts (retrieved 2026-06-23)

| Fact | Value (current) | Source | Retrieved | Confidence | Notes |
|---|---|---|---:|---|---|
| Full YPP eligibility | 1,000 subscribers + 4,000 qualified watch hours in 12 months, OR 1,000 subscribers + 10,000,000 qualified Shorts views in 90 days | YouTube Help 72851 | 2026-10-28 | high | Help Center now says "qualified"; Shorts Feed watch time does not count toward the 4,000 hours |
| Lower fan-funding YPP tier | 500 subscribers + 3 public uploads/90 days + 3,000 watch hours/12 months OR 3,000,000 Shorts views/90 days | YouTube Help 13429240 | 2026-10-28 | high | Unlocks memberships, Super Chat, Super Thanks, Shopping |
| Long-form ad revenue split | Creator keeps 55% of Watch Page ad net revenue | YouTube Help 72902 | 2026-10-28 | high | Fixed, non-negotiable |
| Shorts revenue split | Creator keeps 45% of allocated Shorts Creator Pool revenue | YouTube Help 12504220 | 2026-06-23 | high | Music reduces the pool contribution |
| Fan-funding split | Creator keeps 70% (memberships, Super Chat, Super Stickers, Super Thanks) | YouTube Help 72902 | 2026-10-28 | high | Stable |
| Mid-roll ad threshold | Video must be 8:00 minutes or longer | YouTube Help 6175006 | 2026-10-28 | high | Hybrid auto + manual slots since 2025-05 |
| Three-minute Shorts | Uploads on or after 2024-10-15 can be up to 3 minutes | YouTube Help 15424877 | 2026-10-28 | high | Most music capped at 90 seconds |
| View counting | From 2026-08-24 public views across all formats (Shorts, long-form, podcasts, live) count from the first frame; the previous definition is now an engaged view | YouTube Blog "What are 'Engaged' Views" 2026-08-19 | 2026-10-28 | high | YPP still uses qualified views; CTR, AVD, retention, and recommendations unchanged |
| Inauthentic content policy | Repetitious renamed inauthentic on 2025-07-15 | YouTube Help 1311392 | 2026-06-23 | high | Targets mass-produced or templated content |
| Shopping affiliate threshold | Requires YPP membership and the YPP subscriber threshold, in an eligible country | YouTube Help 13376398 | 2026-10-28 | high | Help Center now states the threshold indirectly; brand-set commission rates |
| Thumbnail and title A/B testing | Test up to 3 variants; winner by watch-time share; title testing global ~2025-12-09 | YouTube Help 13861714 | 2026-06-23 | high | Desktop Studio only |
| Official CTR benchmark | Half of channels and videos sit between 2% and 10% impressions CTR | YouTube Help 7628154 | 2026-06-23 | high | Averages mislead across traffic sources |

## Watch Windows

The fastest-moving facts are monetization thresholds, Shorts mechanics, and recommendation-policy wording. Re-verify these against the official Help Center before any monetization or growth recommendation. See `safety-gates.md` for the refusal rules tied to stale data.

## Refresh Log

### 2026-10-28

- All 156 ledger URLs were requested and compared against the recorded article title. 154 resolved; 19 redirect to new paths (12 YouTube Data API pages moved from `/youtube/v3/` to `/youtube/data/`); three Help Center IDs now serve a different article and were remapped (chapters 9884579, playlists 57792, copyright strikes 2814000).
- One market source (RetentionRabbit benchmark) is 404 at the origin; the ledger and the Audience Retention note now cite the 2026-07-25 Wayback capture, whose text still contains the 23.7% / 16.8% figures.
- One source (Search Engine Land, VRC non-skippable) blocks automated clients with HTTP 403; the March 2026 article was verified from its archive capture.
- Claims corrected where the page text no longer matched: view counting, YPP "qualified" terminology, Shopping affiliate eligibility wording, CPM Masthead access path, Video Action Campaign upgrade dates, and the subscribers-by-content-type report.
- YouTube changed public view counting on 2026-08-24 (first-frame counting across all formats; engaged views is the successor metric). Facts, wiki notes, and the ledger now reflect that change.
- Open item: `yt-hype-leaderboard` states the bonus-size rule only directionally on the page.
