---
type: meta
title: "Hot"
status: evergreen
created: 2026-06-23
updated: 2026-06-26
tags: [meta, hot, cache, working-context]
domain: "Meta"
---

# Hot

Current working context for the YouTube Brain, kept to one screen. Read this
first, then
[[index]] and [[YouTube Brain Home]].

## State

- The brain is built and current as of 2026-06-26. It now covers three pillars:
  creator growth and strategy, the developer API, and paid advertising.
- 67 substantive notes (39 concepts, 6 patterns, 4 antipatterns, 3 flows, 7 API,
  8 ads); sources tracked in `references/source-ledger.json` and dated in
  [[research-pack-2026-06-23]].
- 2026-06-26 deep audit added Subscriptions, fan funding
  ([[Channel Memberships]], [[Supers and Gifted Memberships]]),
  [[YouTube Shopping and Product Tagging]], [[Podcasts on YouTube]],
  [[Courses and Playables]], [[Brand Account and Channel Permissions]],
  [[Handles and Channel Identity]], two API notes, and two ads notes; see [[log]].
- Domain adapters turn a Studio export into a sourced scorecard via
  `scripts/render_channel_report.py`, hardened against empty and malformed
  exports.

## The one idea

YouTube rewards satisfying a specific audience, not gaming a number. The
[[Recommendation System]] weights watch time by satisfaction. Everything else is
the funnel:
[[Packaging]] earns the click, [[Audience Retention]] keeps the promise,
[[Revenue Streams]]
capture the value. The API and advertising pillars sit beside this as the
developer and paid
surfaces.

## Most-used entry points

- Audit a channel: [[Channel Health Audit]].
- Plan a month: [[Monthly Optimization Roadmap]].
- Fix clicks: [[Packaging]], [[Thumbnails]], [[Titles]],
  [[Title-Thumbnail A-B Test Loop]].
- Fix watch: [[Hook in the First 30 Seconds]], [[Audience Retention]].
- Money questions: [[YouTube Partner Program]], [[RPM and CPM]],
  [[Mid-Roll Ads]], [[Channel Memberships]], [[Supers and Gifted Memberships]].
- Audience questions: [[Subscriptions and Subscribers]],
  [[Community and Engagement]].
- Risk questions: [[Copyright Content ID and Strikes]],
  [[Made for Kids and COPPA]].
- Build a tool: [[API Quota System]], [[API Overview and Auth]].
- Run ads: [[Ad Campaign Types]], [[Ad Bidding and Budget]].

## Known footguns

- Monetization thresholds, Shorts mechanics, and ad campaign types change often;
  re-verify via [[Source Intake and Refresh]] before quoting figures.
- A Content ID claim is not a copyright strike; do not conflate them. See
  [[Copyright Content ID and Strikes]].
- `search.list` now costs 1 unit but is capped at 100 calls per day in its own
  bucket (granular quota since 2026-06-01); a search-heavy tool hits the call
  cap, not the unit pool. See [[API Quota System]].
- Demand Gen absorbed Video Action Campaigns; the old campaign no longer exists.
  See [[Ad Campaign Types]].

## Next maintenance

- Monthly refresh of YouTube Help, Studio, and Google Ads pages (refresh_due
  2026-07-23 and 2026-07-24).
- Quarterly refresh of practitioner benchmarks (refresh_due 2026-09-23 and
  2026-09-24).
- Watch the API revision history and Made On YouTube announcements; update
  [[log]].

## Sources

- See [[research-pack-2026-06-23]] and `references/source-ledger.json`.
