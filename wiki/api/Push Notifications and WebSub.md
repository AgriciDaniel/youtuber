---
type: concept
title: "Push Notifications and WebSub"
status: mature
created: 2026-06-26
updated: 2026-06-26
tags: [youtube, api, push, websub, pubsubhubbub, developer]
domain: "Developer API"
difficulty: advanced
related:
  - "[[API Resources and Methods]]"
  - "[[API Quota System]]"
  - "[[API Overview and Auth]]"
  - "[[API Policies and Limits]]"
  - "[[Subscriptions and Members API]]"
  - "[[Subscriptions and Subscribers]]"
  - "[[Source Intake and Refresh]]"
source_urls:
  - "https://developers.google.com/youtube/v3/guides/push_notifications"
  - "https://developers.google.com/youtube/v3/determine_quota_cost"
  - "https://developers.google.com/youtube/v3/revision_history"
---

# Push Notifications and WebSub

Instead of polling the Data API to discover new uploads, a tool can have YouTube
push a notification the moment a channel publishes or edits a video. YouTube
exposes this through the WebSub protocol (formerly PubSubHubbub), and for any
upload-watching integration it is both cheaper and faster than repeated
`search.list` or `activities.list` polling, sparing the budget tracked in
[[API Quota System]].

## Push versus polling

Polling for new uploads wastes quota and adds latency: you either poll often and
burn units, or poll rarely and miss the early window that the
[[Recommendation System|recommendation system]] cares about. A push subscription
flips the model. YouTube notifies your callback when a video is uploaded or when
its title or description changes, so your tool reacts in near real time and spends
no quota receiving the event. This is the right backbone for upload-triggered
automations such as cross-posting or alerting.

## Topic and callback setup

You subscribe at the hub `https://pubsubhubbub.appspot.com/subscribe`. The topic
is a channel's upload feed at
`https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID`. A subscription
request supplies your callback URL, the topic URL, and `hub.mode` set to
`subscribe` (or `unsubscribe` to stop). Resolve a handle to its channel ID first
using the techniques in [[Subscriptions and Members API]] and
[[API Resources and Methods]].

## Verification and lease renewal

The YouTube guide intentionally defers the handshake details to the WebSub
specification rather than documenting them itself. Under that spec the hub
verifies intent by calling your callback with a challenge you must echo back, an
optional shared secret lets you validate that notifications really came from the
hub, and each subscription is granted for a limited lease that you must renew
before it expires or delivery silently stops. Treat lease length and the exact
verification parameters as protocol behavior to confirm against the WebSub spec,
not as YouTube-published values.

## Payload and failure handling

Notifications arrive as Atom feed payloads containing the video and channel IDs
plus standard Atom metadata, fired on upload and on title or description edits.
Because delivery is at-least-once and best-effort, design idempotently: dedupe by
video ID, tolerate occasional duplicate or out-of-order events, and keep a
lightweight reconciliation poll as a backstop for missed pushes. Renew leases on a
schedule and re-subscribe after any callback outage.

## How to apply

- Use WebSub push as the primary upload trigger and reserve polling for backfill
  and reconciliation.
- Track every active subscription's lease and renew ahead of expiry; expired
  leases fail quietly.
- Verify the challenge and validate the optional secret so you cannot be fed spoof
  notifications.
- Persist processed video IDs to stay idempotent under duplicate deliveries, and
  honor the storage rules in [[API Policies and Limits]] and
  [[Source Intake and Refresh]].

## Sources

- Push Notifications, Google for Developers, retrieved 2026-06-26,
  https://developers.google.com/youtube/v3/guides/push_notifications
- Determine quota cost, Google for Developers, retrieved 2026-06-26,
  https://developers.google.com/youtube/v3/determine_quota_cost
- Revision History, Google for Developers, retrieved 2026-06-26,
  https://developers.google.com/youtube/v3/revision_history
- See [[research-pack-2026-06-23]] and [[index]].
