---
type: index
title: "API Index"
status: evergreen
created: 2026-06-24
updated: 2026-06-26
tags: [meta, index, api]
domain: "Meta"
---

# Developer API

The YouTube developer APIs pillar. See [[index]] and [[YouTube Brain Home]].

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
  compliance audit, Live Streaming API.

These describe the developer surface, distinct from the creator-growth and
advertising
pillars. The brain's own adapters (`youtube_brain/adapters.py`) operate on
exported data and
do not call the live API.
