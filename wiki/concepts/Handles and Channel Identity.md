---
type: concept
title: "Handles and Channel Identity"
status: mature
created: 2026-06-26
updated: 2026-06-26
tags: [youtube, handles, channel-url, identity, branding]
domain: "Operations"
difficulty: basic
related:
  - "[[Channel Page and Branding]]"
  - "[[Brand Account and Channel Permissions]]"
  - "[[Video SEO and Metadata]]"
  - "[[Collaborations and Cross-Promotion]]"
  - "[[Community Guidelines Strikes]]"
  - "[[API Resources and Methods]]"
  - "[[Subscriptions and Subscribers]]"
source_urls:
  - "https://support.google.com/youtube/answer/11585688"
  - "https://support.google.com/youtube/answer/6180214"
  - "https://support.google.com/youtube/answer/15920820"
  - "https://support.google.com/youtube/answer/2657968"
  - "https://support.google.com/youtube/answer/9637404"
  - "https://support.google.com/youtube/answer/2801947"
---

# Handles and Channel Identity

A handle is a channel's short, unique identifier that starts with @, such as
@youtubecreators. It is distinct from the channel name: the name is the display
title, while the handle is the unique address used in mentions, comments, live
chat, Shorts, and the channel URL. Every channel has exactly one handle, and that
handle automatically becomes the channel's primary URL. Handles are the canonical
identity layer that ties together [[Channel Page and Branding]] and how other
creators reference you.

## What a handle is and how it is formatted

Choosing or changing a handle automatically creates a handle URL in the form
youtube.com/@handle. Standard handles are 3 to 30 characters, with different
limits for some scripts, and may use letters or numbers from YouTube's supported
languages plus underscores, hyphens, periods, and middle dots, though not at the
start or end. Handles are not case sensitive, must be unique, cannot look like a
URL or phone number, and cannot violate Community Guidelines. If a handle is
unavailable it is usually already taken; adding a period, number, or underscore
often resolves it.

## Changing a handle

You can change your handle twice within a 14-day period. When you change it,
YouTube holds your previous handle for 14 days in case you switch back, and during
that window both the old and new handle URLs work. After the hold expires, the old
handle becomes available to others, so a careless change can hand your former URL
to someone else. Treat the handle as durable infrastructure and change it rarely.

## Handles versus legacy custom URLs

Older channels may still have legacy custom URLs such as youtube.com/c/Name or
username URLs such as youtube.com/user/Name. New custom URLs can no longer be
created and existing ones can no longer be changed, and all legacy URLs now
redirect to the handle-based URL. The handle has effectively replaced the old
vanity-URL system, so new branding and links should always use the @handle form.

## Mentions and discovery

Typing @ in a video title, description, comment, or post lets you mention another
channel by name or handle, which is a core mechanic for
[[Collaborations and Cross-Promotion]]. Not every mention triggers a notification,
but meaningful ones often do, and tapping a mention opens a creator info panel.
Creators can find mentions under Notifications and can toggle whether others may
mention them in privacy settings.

## Impersonation and conflicts

YouTube's impersonation policy prohibits handles or names that are phonetically
identical or visually similar to an established entity, deceptive misspellings, and
posing as an official or backup channel. Fan channels must say so in the name or
handle. Trademark disputes are handled through a separate complaint process, and
YouTube reserves the right to reclaim or change a handle. Staying clear of these
rules protects you from action under [[Community Guidelines Strikes]].

## Handles in the Data API

The Data API exposes handles through the channels resource: channels.list accepts
a forHandle parameter to look up a channel by its handle, with or without the
leading @, which is the cleanest way for a tool to resolve a handle to a channel
ID. See [[API Resources and Methods]] for the broader resource map.

## How to apply

- Pick a handle that matches your brand and is easy to say aloud, since it is your
  spoken and written address everywhere on YouTube.
- Lock it in early and avoid changing it; if you must, do it deliberately within
  the twice-per-14-days limit and update external links promptly.
- Use @mentions to credit collaborators and guests, which aids cross-promotion and
  discovery.
- For tools, resolve handles to channel IDs via the API forHandle lookup rather
  than scraping URLs.

## Sources

- Learn about YouTube handles, YouTube Help, retrieved 2026-06-26,
  https://support.google.com/youtube/answer/11585688
- Understand your YouTube channel's URLs, YouTube Help, retrieved 2026-06-26,
  https://support.google.com/youtube/answer/6180214
- Change, view, or hide your handle, YouTube Help, retrieved 2026-06-26,
  https://support.google.com/youtube/answer/15920820
- Custom URL overview, YouTube Help, retrieved 2026-06-26,
  https://support.google.com/youtube/answer/2657968
- Mention channels in titles and descriptions, YouTube Help, retrieved 2026-06-26,
  https://support.google.com/youtube/answer/9637404
- Impersonation policy, YouTube Help, retrieved 2026-06-26,
  https://support.google.com/youtube/answer/2801947
- See [[research-pack-2026-06-23]] and [[index]].
