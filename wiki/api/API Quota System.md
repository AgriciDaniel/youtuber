---
type: concept
title: "API Quota System"
status: mature
created: 2026-06-24
updated: 2026-06-24
tags: [youtube, api, data-api, quota, limits, developer]
domain: "Developer API"
difficulty: advanced
related:
  - "[[API Overview and Auth]]"
  - "[[API Resources and Methods]]"
  - "[[Analytics and Reporting API]]"
  - "[[API Policies and Limits]]"
  - "[[Source Intake and Refresh]]"
  - "[[Studio Analytics]]"
source_urls:
  - "https://developers.google.com/youtube/v3/getting-started"
  - "https://developers.google.com/youtube/v3/determine_quota_cost"
  - "https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits"
---

# API Quota System

Every Google Cloud project that enables the YouTube Data API gets a default
quota of 10,000
units per day, and the single most common way integrations fail is by spending
that budget
faster than expected. Quota is a per-project daily allowance, not a rate limit,
and it
resets at midnight Pacific time. Understanding the per-call costs before you
build prevents
the surprise of a tool that stops working at noon. This pairs with
[[API Resources and Methods]] for what each call does.

## The default allowance

- 10,000 units per day, combined across most endpoints.
- Plus separate granular caps of 100 `search.list` calls per day and 100
  `videos.insert` calls per day. As of the 2026-06-01 granular rollout, those
  two charge their own buckets rather than the shared 10,000-unit pool.

## Per-call costs

- Reads (list operations) usually cost 1 unit each: `videos.list`,
  `channels.list`, `playlists.list`, `playlistItems.list`, `comments.list`,
  `subscriptions.list`, `activities.list`.
- Writes usually cost 50 units each: update, delete, insert, `videos.rate`,
  `thumbnails.set`, `subscriptions.insert`.
- `search.list` costs 1 unit but is capped at 100 calls per day, so a
  search-heavy tool hits the search cap, not the unit pool.
- Captions are the costly exception: `captions.insert` is 400 units and
  `captions.update` is 450 units.
- In 2025-12 the video-upload cost was cut from roughly 1,600 units to roughly
  100 units.

## What happens when you run out

Exhausting quota returns a `quotaExceeded` error until the daily reset. There is
no overage
billing; the project simply cannot call the API again until reset. Plan for this
with
caching and back-off.

## Getting more

To exceed the default, a developer completes a compliance audit through the
Audit and Quota
Extension Form, proving the application follows the YouTube API Services Terms
of Service.
Projects audited in the prior 12 months use a faster form for further increases.
See
[[API Policies and Limits]].

## How to apply

- Map every call your tool makes to its unit cost and multiply by expected
  volume before launch.
- Cache results and avoid re-fetching unchanged data within the 30-day storage
  window; see [[Source Intake and Refresh]] and [[API Policies and Limits]].
- Treat `search.list` as scarce: search once for IDs, then list the details
  cheaply.
- Request a quota increase early if you need it; the audit takes time.

## Sources

- YouTube Data API Overview, Google for Developers, retrieved 2026-06-24,
  https://developers.google.com/youtube/v3/getting-started
- Quota Calculator, Google for Developers, retrieved 2026-06-24,
  https://developers.google.com/youtube/v3/determine_quota_cost
- Quota and Compliance Audits, Google for Developers, retrieved 2026-06-24,
  https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits
- See [[research-pack-2026-06-23]] and [[index]].
