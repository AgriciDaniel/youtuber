---
type: concept
title: "API Overview and Auth"
status: mature
created: 2026-06-24
updated: 2026-06-24
tags: [youtube, api, data-api, oauth, authentication, developer]
domain: "Developer API"
difficulty: advanced
related:
  - "[[API Resources and Methods]]"
  - "[[API Quota System]]"
  - "[[Analytics and Reporting API]]"
  - "[[API Policies and Limits]]"
  - "[[Studio Analytics]]"
  - "[[Source Intake and Refresh]]"
source_urls:
  - "https://developers.google.com/youtube/v3/getting-started"
  - "https://developers.google.com/youtube/v3/guides/authentication"
  - "https://developers.google.com/youtube/registering_an_application"
---

# API Overview and Auth

The YouTube Data API v3 is the programmatic interface to YouTube data and
channel
operations. It is accessed through a Google Cloud project, which issues the
credentials that
every request must carry. The single most important thing to understand before
writing any
code is the difference between the two credential types, because it determines
what you can
do and whether a user has to grant consent. This note covers that; see
[[API Resources and Methods]] for what the API exposes and [[API Quota System]]
for the cost
model.

## API key versus OAuth 2.0

- An API key authenticates requests that read only public data, for example
  listing public videos or running a public search. It identifies the project,
  not a user.
- OAuth 2.0 is required whenever a request touches private user data or performs
  any write. Operations that insert, update, or delete resources always require
  OAuth user authorization.
- Some list methods accept both: an unauthenticated call returns only public
  data, while an authorized call adds data private to the signed-in user.

Never embed a real key or token in a tracked file; treat them as secrets. See
[[Source Intake and Refresh]] for the no-credentials rule.

## Scopes

During OAuth authorization the application requests scopes that define which
resources it
may manage. The Data API scopes are:

- `youtube.readonly`: read-only access to the user's account.
- `youtube`: manage the account (most read and write operations).
- `youtube.force-ssl`: full read and write including comments, over SSL.
- `youtube.upload`: upload videos.
- `youtubepartner`: content-partner operations.
- `youtubepartner-channel-audit`: read a channel's audit details.

Request the narrowest scope that does the job; users are more likely to consent,
and the
Developer Policies require obtaining consent before requesting scopes. See
[[API Policies and Limits]].

## The token flow

A Google Cloud project holds the credentials. Installed and desktop apps use the
OAuth 2.0
authorization-code flow: the app sends the user to Google, receives an
authorization code on
a loopback or custom-URI redirect, and exchanges it for a short-lived access
token plus a
long-lived refresh token. The refresh token obtains new access tokens without
re-prompting
the user. Access tokens are passed in the `Authorization: Bearer` header.

## How to apply

- Decide first whether your use case is read-only public (API key) or touches a
  user account or writes (OAuth). This choice drives everything else.
- Create a Google Cloud project, enable the YouTube Data API, and generate the
  right credential.
- Store credentials outside the repo; never commit a key or token. See
  [[Made for Kids and COPPA]] and [[Copyright Content ID and Strikes]] for
  content rules the API does not exempt you from.
- Plan around the cost of each call before you ship; see [[API Quota System]].

## Sources

- YouTube Data API Overview, Google for Developers, retrieved 2026-06-24,
  https://developers.google.com/youtube/v3/getting-started
- Implementing OAuth 2.0 Authorization, Google for Developers, retrieved
  2026-06-24, https://developers.google.com/youtube/v3/guides/authentication
- Obtaining authorization credentials, Google for Developers, retrieved
  2026-06-24, https://developers.google.com/youtube/registering_an_application
- See [[research-pack-2026-06-23]] and [[index]].
