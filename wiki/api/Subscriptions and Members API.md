---
type: concept
title: "Subscriptions and Members API"
status: mature
created: 2026-06-26
updated: 2026-06-26
tags: [youtube, api, data-api, subscriptions, members, developer]
domain: "Developer API"
difficulty: advanced
related:
  - "[[API Resources and Methods]]"
  - "[[API Quota System]]"
  - "[[API Overview and Auth]]"
  - "[[Subscriptions and Subscribers]]"
  - "[[Channel Memberships]]"
  - "[[Supers and Gifted Memberships]]"
  - "[[API Policies and Limits]]"
source_urls:
  - "https://developers.google.com/youtube/v3/docs/subscriptions"
  - "https://developers.google.com/youtube/v3/docs/subscriptions/list"
  - "https://developers.google.com/youtube/v3/docs/members/list"
  - "https://developers.google.com/youtube/v3/docs/membershipsLevels/list"
  - "https://developers.google.com/youtube/v3/determine_quota_cost"
---

# Subscriptions and Members API

Two Data API surfaces let a tool read the audience relationships behind
[[Subscriptions and Subscribers]] and [[Channel Memberships]]: the `subscriptions`
resource, available to any authorized user, and the members surface, restricted to
creators. They behave very differently on access and privacy, and confusing them
is a common integration mistake. This note extends the resource map in
[[API Resources and Methods]] and assumes the auth model in
[[API Overview and Auth]].

## The subscriptions resource

A subscription represents a user following a channel. `subscriptions.list` costs 1
unit and requires exactly one filter:

- `mine=true`: the authorized user's own subscriptions. Note there is no
  `mySubscriptions` parameter; `mine` is the correct flag.
- `channelId`: subscriptions made by a specific channel.
- `mySubscribers=true` or `myRecentSubscribers=true`: people who subscribe to the
  authorized channel, newest first for the latter.
- `id`: specific subscription IDs.

Optional parameters include `forChannelId` to filter the result to given
channels, `maxResults` (0 to 50, default 5), and `order` (alphabetical,
relevance, or unread). A common pattern is `mine` plus `forChannelId` to check
whether the authorized viewer subscribes to a particular channel.

`subscriptions.insert` and `subscriptions.delete` each cost 50 units and require
OAuth with one of the youtube, youtube.force-ssl, or youtubepartner scopes. Insert
subscribes the authorized account to the channel named in
`snippet.resourceId`; delete removes a subscription by `id`.

## Members and membership levels

The members surface is creator-only and allowlisted: it can only be used by an
individual creator for their own memberships-enabled channel, and access is
granted by a Google or YouTube representative. Calls return
`channelMembershipsNotEnabled` if memberships are off. Both methods require the
`https://www.googleapis.com/auth/youtube.channel-memberships.creator` scope.

- `members.list` costs 2 units and returns the channel's members. Use `mode`
  (`all_current` or `updates`), `hasAccessToLevel` to filter by minimum level,
  and `filterByMemberChannelId` (up to 100 IDs) to check specific members.
  `maxResults` ranges 0 to 1000.
- `membershipsLevels.list` costs 1 unit and returns the membership levels the
  authorized creator owns.

These power membership integrations and perk automation, but the access
restriction means most third-party tools cannot use them.

## Privacy and limitations

Subscriber lists are deliberately incomplete: only subscribers who made their
subscriptions public are returned, mirroring the privacy behavior described in
[[Subscriptions and Subscribers]]. Member identities are sensitive personal data
and must be handled under the API Services Terms and the storage rules in
[[API Policies and Limits]]. Neither surface exposes payment details.

## How to apply

- To verify a subscription relationship cheaply, use `subscriptions.list` with
  `mine` and `forChannelId` rather than paging an entire subscriber list.
- Budget writes carefully: subscribe and unsubscribe cost 50 units each against
  the shared pool in [[API Quota System]].
- Do not build a product around `members.list` unless you have been allowlisted;
  design for the case where access is denied.
- Treat returned member and subscriber data as personal data with retention and
  deletion obligations.

## Sources

- Subscriptions resource, Google for Developers, retrieved 2026-06-26,
  https://developers.google.com/youtube/v3/docs/subscriptions
- Subscriptions: list, Google for Developers, retrieved 2026-06-26,
  https://developers.google.com/youtube/v3/docs/subscriptions/list
- Members: list, Google for Developers, retrieved 2026-06-26,
  https://developers.google.com/youtube/v3/docs/members/list
- MembershipsLevels: list, Google for Developers, retrieved 2026-06-26,
  https://developers.google.com/youtube/v3/docs/membershipsLevels/list
- Determine quota cost, Google for Developers, retrieved 2026-06-26,
  https://developers.google.com/youtube/v3/determine_quota_cost
- See [[research-pack-2026-06-23]] and [[index]].
