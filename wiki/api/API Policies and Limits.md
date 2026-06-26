---
type: concept
title: "API Policies and Limits"
status: mature
created: 2026-06-24
updated: 2026-06-24
tags: [youtube, api, policy, terms-of-service, compliance, developer]
domain: "Developer API"
difficulty: advanced
related:
  - "[[API Overview and Auth]]"
  - "[[API Quota System]]"
  - "[[API Resources and Methods]]"
  - "[[Analytics and Reporting API]]"
  - "[[Source Intake and Refresh]]"
  - "[[Bought Engagement and Sub4Sub]]"
source_urls:
  - "https://developers.google.com/youtube/terms/developer-policies"
  - "https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits"
  - "https://developers.google.com/youtube/v3/live/getting-started"
---

# API Policies and Limits

The YouTube API is governed by the API Services Terms of Service and the
Developer Policies,
and the compliance audit enforces them before granting extended quota. A tool
can be
technically correct and still get its access revoked for a policy violation, so
the rules
matter as much as the endpoints. This note covers the constraints; the cost
model is in
[[API Quota System]] and auth in [[API Overview and Auth]].

## Data handling rules

- Most authorized API data must be deleted or refreshed within 30 calendar days.
- Non-authorized data is capped at 30-day storage.
- A user-requested deletion must be completed within 7 days.

These rules mean a tool cannot hoard stale YouTube data indefinitely; it must
refresh or
drop it. This mirrors the brain's own [[Source Intake and Refresh]] discipline.

## Prohibited behavior

The Developer Policies prohibit:

- Scraping, or circumventing quota or geo-restrictions.
- Automating views or engagement without user consent, the API-level version of
  the [[Bought Engagement and Sub4Sub]] antipattern.
- Replicating YouTube's core experience, or modifying API-returned data or
  search-result ordering.

Clients must also surface YouTube Terms of Service links, publish a privacy
policy, obtain
consent before requesting scopes, and allow easy revocation.

## The compliance audit

To exceed the default 10,000-unit quota, a project passes a compliance audit
through the
Audit and Quota Extension Form. YouTube runs periodic reviews and requires a
Change of
Control form when ownership changes. Failing an audit can cap a project at the
default quota
or revoke access.

## Live Streaming API note

The Live Streaming API (`liveBroadcasts`, `liveStreams`, `cuepoint`) sits in the
v3
namespace; `bind` links a broadcast to a stream and `transition` advances it
through ready,
testing, and live. All insert, update, and delete operations require OAuth,
never an API
key. See [[Live Streaming and Premieres]] for the creator-facing side.

## Recent changes to watch

The 2026-06-01 granular quota rollout separated `search.list` and
`videos.insert` into their
own buckets; 2026-06-03 added `videos.batchGetStats`; 2025-12-04 cut upload cost
to about
100 units; 2025-03-26 changed how Shorts views are counted in
`statistics.viewCount`.
Re-verify these on the official revision history before relying on them; see
[[Source Intake and Refresh]].

## How to apply

- Build deletion and refresh into your storage from day one; the 30-day and
  7-day rules are not optional.
- Never automate engagement or scrape; it is both a policy breach and an
  integrity failure.
- Pass the audit before you need the extra quota, not after you hit the wall.

## Sources

- YouTube API Services Developer Policies, Google for Developers, retrieved
  2026-06-24, https://developers.google.com/youtube/terms/developer-policies
- Quota and Compliance Audits, Google for Developers, retrieved 2026-06-24,
  https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits
- YouTube Live Streaming API Overview, Google for Developers, retrieved
  2026-06-24, https://developers.google.com/youtube/v3/live/getting-started
- See [[research-pack-2026-06-23]] and [[index]].
