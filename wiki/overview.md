---
type: meta
title: "Overview"
status: evergreen
created: 2026-06-23
updated: 2026-06-24
tags: [meta, overview, scope]
domain: "Meta"
---

# Overview

The YouTube Brain is a source-cited knowledge and decision layer for YouTube,
spanning three
pillars: creator growth and strategy, the developer API, and paid advertising.
Its job is to
make repeatable, defensible decisions with every claim traceable to an official
or primary
source. It serves creators, channel managers, editors, strategists, tool
builders, and
advertisers. See [[YouTube Brain Home]] to start reading.

## Scope

The brain now covers the whole YouTube surface a practitioner touches:

- Creator growth: the [[Recommendation System]], [[Discovery Surfaces]],
  [[Hype]], retention ([[Watch Time and AVD]], [[Audience Retention]]),
  packaging ([[Click-Through Rate]], [[Packaging]], [[Thumbnails]], [[Titles]],
  [[Video SEO and Metadata]]), formats ([[Shorts]],
  [[Live Streaming and Premieres]]), monetization ([[YouTube Partner Program]],
  [[RPM and CPM]], [[Revenue Streams]], [[Mid-Roll Ads]],
  [[Advertiser-Friendly Guidelines]]), policy
  ([[Copyright Content ID and Strikes]], [[Community Guidelines Strikes]],
  [[Made for Kids and COPPA]]), and operations ([[Studio Analytics]],
  [[Publishing Cadence]], [[Community and Engagement]],
  [[End Screens and Cards]], [[Playlists and Series]],
  [[Channel Page and Branding]], [[Captions Localization and Dubbing]],
  [[Audience Overlap]], [[Niche Selection and Positioning]],
  [[Ideation and Inspiration]]).
- Developer API: [[API Overview and Auth]], [[API Resources and Methods]],
  [[API Quota System]], [[Analytics and Reporting API]], and
  [[API Policies and Limits]].
- Advertising: [[Ad Formats]], [[Ad Campaign Types]], [[Ad Bidding and Budget]],
  [[Ad Targeting]], [[Ad Measurement]], and [[Connected TV and Shorts Ads]].

It also carries patterns to apply, antipatterns to avoid, and flows to run, all
listed in
[[index]].

## Sourcing

Every claim is researched from official and primary sources. The result is 156
structured sources in `references/source-ledger.json` and 143 dated citations in
[[research-pack-2026-06-23]], the majority from YouTube Help, the YouTube
Official Blog, How YouTube Works, developers.google.com, and Google Ads Help.
Domain adapters in `scripts/` and `youtube_brain/adapters.py` turn a Studio
export into a sourced channel-health scorecard.

## How it stays current

YouTube's rules move fast, so the brain refreshes on a cadence: monthly for Help
Center,
Studio, and Google Ads pages, on changelog for recommendation, monetization,
API, and
ad-campaign changes, and quarterly for practitioner benchmarks. The discipline
lives in
[[Source Intake and Refresh]].

## Safety posture

- No credentials, OAuth tokens, cookies, API keys, or private audience data ever
  enter the repo.
- No growth, revenue, monetization, API, or ad claim ships without a current
  official or primary source.
- No account mutation; the brain is advisory and read only toward any real
  channel, project, or ad account.
- No sub for sub, bought engagement, fake API traffic, or policy-violating
  tactics; see [[Bought Engagement and Sub4Sub]] and
  [[API Policies and Limits]].
- No irreversible recommendation without owner, confidence, source, and a
  rollback note.

## Sources

- [[research-pack-2026-06-23]], `references/source-ledger.json`, and [[index]]
  hold the full source map.
