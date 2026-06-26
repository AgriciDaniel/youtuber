---
type: concept
title: "API Resources and Methods"
status: mature
created: 2026-06-24
updated: 2026-06-26
tags: [youtube, api, data-api, endpoints, resources, developer]
domain: "Developer API"
difficulty: advanced
related:
  - "[[API Overview and Auth]]"
  - "[[API Quota System]]"
  - "[[Analytics and Reporting API]]"
  - "[[Subscriptions and Members API]]"
  - "[[Push Notifications and WebSub]]"
  - "[[API Policies and Limits]]"
  - "[[Live Streaming and Premieres]]"
  - "[[Studio Analytics]]"
source_urls:
  - "https://developers.google.com/youtube/v3/docs"
  - "https://developers.google.com/youtube/v3/docs/search/list"
  - "https://developers.google.com/youtube/v3/docs/videos/list"
---

# API Resources and Methods

The YouTube Data API v3 is organized as resources, each with a set of methods
such as list,
insert, update, and delete. Knowing which resource holds which data, and that
`search.list`
returns only lightweight identifiers, is what separates an efficient integration
from one
that burns its [[API Quota System]] in minutes. This note maps the resources a
creator-tool
builder uses most. Auth and credential rules are in [[API Overview and Auth]].

## Search

`search.list` returns search results that identify video, channel, and playlist
resources.
The default `type` is `video,channel,playlist`, `part` must be `snippet`, and
`maxResults`
ranges 0 to 50 with a default of 5. It returns only IDs and snippet info, not
full resource
details, so a typical pattern is to search for IDs, then call the matching
resource's list
method for full data. `pageInfo.totalResults` is an approximation. Crucially,
since the
2026-06-01 granular-quota change `search.list` costs only 1 unit but is capped at
100 calls
per day in its own bucket, so call volume, not unit cost, is the real constraint;
see [[API Quota System]].

## Videos and channels

- `videos` supports list, insert, update, delete, rate, getRating, and
  reportAbuse. `videos.list` `part` values include snippet, contentDetails,
  statistics (viewCount, likeCount, commentCount), status, and
  liveStreamingDetails. Filters include `id`, `chart=mostPopular`, and
  `myRating` (OAuth only).
- `videos.insert` requires OAuth, supports resumable upload up to 256 GB.
- `channels.list` filters by `id`, `forHandle`, `forUsername`, `mine`, or
  `managedByMe`, and returns statistics with viewCount, subscriberCount, and
  videoCount.

## Playlists, comments, and more

- `playlists` and `playlistItems` each support list, insert, update, and delete
  for building and reordering collections, which matters for the
  [[Playlists and Series]] strategy.
- `comments` and `commentThreads` read and post comment threads and replies,
  relevant to [[Community and Engagement]].
- `captions` manages timed subtitle tracks (list, insert, update, delete,
  download), relevant to [[Captions Localization and Dubbing]].
- `subscriptions` handles list, insert, and delete, and `members` plus
  `membershipsLevels` expose the creator-only memberships surface; both are
  detailed in [[Subscriptions and Members API]] and underpin
  [[Subscriptions and Subscribers]]. `thumbnails.set` uploads a custom thumbnail,
  the spec for which is in [[Thumbnails]].
- For upload-watching tools, prefer WebSub push over polling these resources; see
  [[Push Notifications and WebSub]].

## Live streaming

The Live Streaming API lives in the same v3 namespace with `liveBroadcasts`,
`liveStreams`,
and `cuepoint`; see [[API Policies and Limits]] and
[[Live Streaming and Premieres]].

## How to apply

- Search returns IDs only; always plan a follow-up list call for full data, and
  budget against the 100-calls-per-day search cap rather than a unit cost.
- Choose the smallest set of `part` values you need; each part can add cost and
  payload.
- Any insert, update, or delete needs OAuth, never just an API key. See
  [[API Overview and Auth]].

## Sources

- API Reference, Google for Developers, retrieved 2026-06-24,
  https://developers.google.com/youtube/v3/docs
- Search: list, Google for Developers, retrieved 2026-06-24,
  https://developers.google.com/youtube/v3/docs/search/list
- Videos: list, Google for Developers, retrieved 2026-06-24,
  https://developers.google.com/youtube/v3/docs/videos/list
- See [[research-pack-2026-06-23]] and [[index]].
