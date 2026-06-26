---
type: meta
title: "Index"
status: evergreen
created: 2026-06-23
updated: 2026-06-26
tags: [meta, index, catalog]
domain: "Meta"
---

# YouTube Brain

<p align="center">
  <img src="/static/logo.png" alt="YouTube Brain" width="116" />
</p>

A source-cited operating layer for everything YouTube: creator growth and
strategy, the developer API, and paid advertising. Every claim traces to an
official or primary source with a date.

![notes](https://img.shields.io/badge/notes-67-FF0000)
![audit](https://img.shields.io/badge/audit-100%2F100%20market--ready-FF0000)
![grade](https://img.shields.io/badge/grade-SSS%2B-FF0000)
![sources](https://img.shields.io/badge/sources-156%20dated-FF0000)
![license](https://img.shields.io/badge/license-Apache--2.0-blue)

> Unofficial community project. Not affiliated with, sponsored by, or endorsed by
> YouTube or Google.

## The three pillars

- **Creator growth and strategy** — the [[Recommendation System]],
  [[Subscriptions and Subscribers|subscriptions]], [[Audience Retention|retention]],
  [[Packaging]], [[Shorts]], and monetization. Start at [[YouTube Brain Home]].
- **Developer API** — build tools on the Data, Analytics, Reporting, and Live
  Streaming APIs. Start at [[API Overview and Auth]] and respect the
  [[API Quota System]].
- **Advertising** — run paid campaigns through Google Ads. Start at
  [[Ad Campaign Types]] and [[Ad Formats]].

## What it produces

- A channel health scorecard from a [[Channel Health Audit]] on a Studio export.
- A [[Monthly Optimization Roadmap]] of prioritized experiments.
- Packaging, monetization, and risk audits, each tied to a current source.

## Set it up in five minutes

Open this folder as an Obsidian vault and start at [[YouTube Brain Home]], or
install the agent layer:

```bash
python -m pip install -e .
youtube-brain demo
youtube-brain report --vault examples/sample-vault --html-only
```

Then audit a real channel from a Studio export and get the next action:

```bash
youtube-brain new acme --client-name "Acme Co" --owner "You"
youtube-brain report --vault ~/youtube-brain-vaults/acme --html-only
youtube-brain next --vault ~/youtube-brain-vaults/acme
```

Keep every claim current with [[Source Intake and Refresh]].

## Full catalog

Read [[overview]] for scope and [[YouTube Brain Home]] for a guided tour. Every
claim traces to [[research-pack-2026-06-23]] and
`references/source-ledger.json`.

## Concepts: Discovery

- [[Recommendation System]]: automated word of mouth, satisfaction over raw
  watch time, eight signals.
- [[Discovery Surfaces]]: Home, Suggested, Search, and the Shorts feed as
  separate models.
- [[Hype]]: discovery boost weighted toward channels under 500,000 subscribers.
- [[Subscriptions and Subscribers]]: the bell, notification delivery, and why the
  count is not reach.

## Concepts: Retention

- [[Watch Time and AVD]]: watch time, average view duration, and average
  percentage viewed.
- [[Audience Retention]]: the retention graph, key moments, and the first 60
  seconds.

## Concepts: Packaging and SEO

- [[Click-Through Rate]]: the 2 to 10 percent band and why falling CTR can be
  success.
- [[Packaging]]: the title and thumbnail unit at the top of the funnel.
- [[Thumbnails]]: the strongest CTR driver and how to design one.
- [[Titles]]: front loading, curiosity versus clarity, and search matching.
- [[Video SEO and Metadata]]: descriptions, chapters, tags, and hashtags.

## Concepts: Formats

- [[Shorts]]: the short form feed, the 3 minute length, and the 2025 view count
  change.
- [[Shorts Monetization]]: the 45 percent pooled model and the RPM gap.
- [[Live Streaming and Premieres]]: real-time formats, Super Chat, and Premiere
  mechanics.
- [[Podcasts on YouTube]]: podcasts as playlists, RSS ingestion, and YouTube
  Music distribution.
- [[Courses and Playables]]: structured learning products and in-app games.

## Concepts: Monetization

- [[YouTube Partner Program]]: the two tiers and their thresholds.
- [[RPM and CPM]]: the two revenue metrics and RPM by niche.
- [[Revenue Streams]]: ads, fan funding, Shopping, and Premium.
- [[Mid-Roll Ads]]: the 8 minute threshold and the 2025 hybrid update.
- [[Advertiser-Friendly Guidelines]]: the green, yellow, and red icons and
  self-certification.
- [[Channel Memberships]]: recurring monthly support, tiers, perks, and the 70
  percent split.
- [[Supers and Gifted Memberships]]: Super Thanks, Super Chat, Super Stickers, and
  gifting.
- [[YouTube Shopping and Product Tagging]]: affiliate versus own store and product
  tagging.

## Concepts: Policy and risk

- [[Copyright Content ID and Strikes]]: claims versus strikes, and
  channel-ending risk.
- [[Community Guidelines Strikes]]: the graduated penalty model.
- [[Made for Kids and COPPA]]: the audience setting and disabled features.

## Concepts: Operations and analytics

- [[Studio Analytics]]: the tabs, traffic sources, and the funnel as a
  diagnostic.
- [[Audience Overlap]]: what else your viewers watch, and how to use it.
- [[Publishing Cadence]]: consistency, sustainability, and the frequency data.
- [[Community and Engagement]]: posts, Communities, live, and memberships.
- [[End Screens and Cards]]: the on-video tools for session continuation.
- [[Playlists and Series]]: a traffic source and a session-time engine.
- [[Channel Page and Branding]]: the conversion surface, trailer, and specs.
- [[Captions Localization and Dubbing]]: accessibility, translated metadata,
  auto-dubbing.
- [[Niche Selection and Positioning]]: the highest-leverage growth and revenue
  decision.
- [[Ideation and Inspiration]]: the Studio Inspiration tab and demand
  validation.
- [[Brand Account and Channel Permissions]]: ownership, roles, and safely sharing
  a channel.
- [[Handles and Channel Identity]]: the @handle, channel URLs, and mentions.

## Patterns

- [[Packaging-First Workflow]]: design the title and thumbnail before filming.
- [[Hook in the First 30 Seconds]]: win the opening or lose the video.
- [[Title-Thumbnail A-B Test Loop]]: let Test and Compare decide on watch time
  share.
- [[Shorts-to-Long-Form Funnel]]: Shorts for reach, long form for revenue.
- [[Diversify Revenue Streams]]: do not depend on ads alone.
- [[Collaborations and Cross-Promotion]]: borrow a compatible audience to grow.

## Antipatterns

- [[Misleading Clickbait]]: a promise the video does not keep.
- [[Bought Engagement and Sub4Sub]]: hollow numbers the system discounts.
- [[Chasing Views Over Satisfaction]]: optimizing the vanity number, not the
  viewer.
- [[Inauthentic Mass-Produced Content]]: templated low value output that risks
  monetization.

## Flows

- [[Channel Health Audit]]: read the funnel, localize the weakest link.
- [[Monthly Optimization Roadmap]]: turn the audit into a small set of
  experiments.
- [[Source Intake and Refresh]]: keep every claim dated and current.

## Developer API

- [[API Overview and Auth]]: Data API v3, API key vs OAuth, scopes, the token
  flow.
- [[API Resources and Methods]]: search, videos, channels, playlists, comments,
  captions.
- [[API Quota System]]: the 10,000 units/day model and per-call costs.
- [[Analytics and Reporting API]]: targeted queries vs bulk daily reports.
- [[Subscriptions and Members API]]: the `subscriptions` resource and the
  creator-only members surface.
- [[Push Notifications and WebSub]]: real-time upload pushes instead of polling.
- [[API Policies and Limits]]: Terms of Service, data-handling rules, the
  compliance audit.

## Advertising

- [[Ad Formats]]: in-stream, bumper, in-feed, Shorts, Masthead.
- [[Ad Campaign Types]]: Demand Gen, video reach, video views, and the VAC
  migration.
- [[Ad Bidding and Budget]]: CPV vs CPM vs conversion bidding.
- [[Ad Targeting]]: audience segments, restricted categories, EU consent.
- [[Ad Measurement]]: paid vs earned vs view-through, Brand Lift.
- [[Connected TV and Shorts Ads]]: CTV as the growth surface, shoppable
  carousels.
- [[Brand Suitability and Inventory Controls]]: inventory modes and content and
  placement exclusions.
- [[Masthead and Reservation Buying]]: the premium Home-feed reach format and
  reservation buys.

## Sources

- [[research-pack-2026-06-23]]: dated citations across all pillars.
- `references/source-ledger.json`: structured, dated sources.
- `.raw/research/`: raw research captures.
