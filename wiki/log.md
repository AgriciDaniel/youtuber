---
type: meta
title: "Log"
status: evergreen
created: 2026-06-23
updated: 2026-06-26
tags: [meta, log, changelog]
domain: "Meta"
---

# Log

Append-only history of the YouTube Brain. Newest entries on top. See [[index]]
for the
catalog and [[Source Intake and Refresh]] for the refresh discipline.

## 2026-06-26 deep audit | Coverage completion and accuracy refresh

- Audited the whole vault for gaps and graph health, ran an official-source
  research pass, and authored 12 new sourced notes (now 67 substantive notes).
- Creator-growth coverage: [[Subscriptions and Subscribers]] (the bell and
  notification delivery), [[Channel Memberships]],
  [[Supers and Gifted Memberships]], [[YouTube Shopping and Product Tagging]],
  [[Podcasts on YouTube]], [[Courses and Playables]],
  [[Brand Account and Channel Permissions]], and
  [[Handles and Channel Identity]].
- Developer API: [[Subscriptions and Members API]] and
  [[Push Notifications and WebSub]].
- Advertising: [[Brand Suitability and Inventory Controls]] and
  [[Masthead and Reservation Buying]].
- Accuracy fixes: corrected `search.list` to 1 unit in its own 100-call-per-day
  bucket (granular quota since 2026-06-01) in [[hot]] and
  [[API Resources and Methods]]; recorded the Google Ads inventory-mode rename to
  Maximum, Moderate, and Limited; captured the YouTube Shopping affiliate
  500-subscriber expansion and globally available ad-supported Courses.
- Enriched the graph: reciprocal `related:` links, new inbound links to the new
  notes, and updated `_index`, [[index]], [[YouTube Brain Home]], and [[hot]].
- Expanded `references/source-ledger.json` with the new official citations.

## 2026-06-24 expansion | Review fixes plus API and Ads pillars

- Applied the full-review fixes: corrected the [[Thumbnails]] resolution spec to
  3840 by 2160, re-sourced the [[Hype]] point figures to launch coverage,
  corrected the title A/B rollout date to 2025-12-04 in [[Titles]] and
  [[Packaging]], reconciled the Shorts RPM band across [[Shorts Monetization]],
  [[RPM and CPM]], and [[Shorts-to-Long-Form Funnel]], corrected the red
  advertiser icon to a copyright claim in [[Advertiser-Friendly Guidelines]],
  and cited Gemini for Creator Partnerships in [[Revenue Streams]].
- Hardened `youtube_brain/adapters.py`: empty exports now render cleanly, null
  and non-finite and boolean fields raise clear errors, with new regression
  tests in `tests/test_adapters.py`.
- Added 24 notes across three new areas. Creator-growth gaps:
  [[End Screens and Cards]], [[Playlists and Series]],
  [[Video SEO and Metadata]], [[Captions Localization and Dubbing]],
  [[Channel Page and Branding]], [[Audience Overlap]],
  [[Niche Selection and Positioning]], [[Ideation and Inspiration]],
  [[Copyright Content ID and Strikes]], [[Community Guidelines Strikes]],
  [[Made for Kids and COPPA]], [[Live Streaming and Premieres]], and the
  [[Collaborations and Cross-Promotion]] pattern.
- Developer API pillar: [[API Overview and Auth]],
  [[API Resources and Methods]], [[API Quota System]],
  [[Analytics and Reporting API]], [[API Policies and Limits]].
- Advertising pillar: [[Ad Formats]], [[Ad Campaign Types]],
  [[Ad Bidding and Budget]], [[Ad Targeting]], [[Ad Measurement]],
  [[Connected TV and Shorts Ads]].
- Expanded the source pack to 87 ledger sources and 143 dated citations;
  converted the research-pack citation separators to hyphens to honor house
  style.
- Broadened the spec domain, the plugin description, and the agent scope to
  include the API and advertising pillars.

## 2026-06-23 build | Initial market-ready release

- Created the brain from `specs/youtube-brain.yaml` (creator growth and strategy
  focus).
- Ran six official-source-biased research passes (discovery, retention,
  packaging, Shorts, monetization, analytics) and captured the raw result in
  `.raw/research/youtube-deep-research-2026-06-23.md`.
- Built the initial source pack: `references/source-ledger.json` with 44 dated
  sources and [[research-pack-2026-06-23]] with 84 dated citations.
- Authored 31 substantive notes (19 concepts, 5 patterns, 4 antipatterns, 3
  flows) and built the domain adapters, schema, fixture, deterministic demo, and
  tests.
- Key facts captured: full YPP 1,000 subscribers plus 4,000 watch hours or 10M
  Shorts views; lower tier 500 subscribers; 55 percent long-form and 45 percent
  Shorts splits; 8 minute mid-roll threshold; 3 minute Shorts since 2024-10-15;
  Shorts view counting change 2025-03-31; inauthentic content policy 2025-07-15.

## Maintenance schedule

- 2026-07-23 and 2026-07-24: refresh YouTube Help, Studio, Google Ads, and
  developer docs (monthly cadence).
- 2026-09-23 and 2026-09-24: refresh practitioner benchmarks (quarterly
  cadence).
