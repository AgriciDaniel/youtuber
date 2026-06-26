---
type: concept
title: "Brand Account and Channel Permissions"
status: mature
created: 2026-06-26
updated: 2026-06-26
tags: [youtube, brand-account, permissions, roles, operations, security]
domain: "Operations"
difficulty: intermediate
related:
  - "[[Channel Page and Branding]]"
  - "[[YouTube Partner Program]]"
  - "[[Studio Analytics]]"
  - "[[Handles and Channel Identity]]"
  - "[[Subscriptions and Subscribers]]"
  - "[[Live Streaming and Premieres]]"
  - "[[Community Guidelines Strikes]]"
source_urls:
  - "https://support.google.com/youtube/answer/9481328"
  - "https://support.google.com/accounts/answer/7001996"
  - "https://support.google.com/accounts/answer/7311601"
  - "https://support.google.com/youtube/answer/4628007"
  - "https://support.google.com/youtube/answer/9367690"
  - "https://support.google.com/youtube/answer/9890437"
---

# Brand Account and Channel Permissions

How a channel is owned and shared is the first thing any team, editor, or agency
must get right, and the first thing to get wrong. A YouTube channel can sit on a
personal Google Account or on a Brand Account, and access can be granted to others
through channel permissions in YouTube Studio. Getting this model right protects
the channel from accidental deletion and from password sharing, and it is the
foundation for safely operating everything else in [[Channel Page and Branding]],
[[Studio Analytics]], and monetization.

## Brand Account versus personal account

A Brand Account is a separate account for a brand that several people can jointly
manage through their own Google Accounts, with no shared username or password. A
channel linked to a Brand Account can therefore have multiple owners and managers.
A Brand Account must have exactly one primary owner. Crucially, a channel can only
be transferred to a new owner if it is on a Brand Account; a channel on a personal
account can change managers but not owners. Moving a channel between accounts is
done in Studio under Settings, Advanced settings, and must be done carefully,
because moving onto a Brand Account that already has a channel can replace and
delete the existing one.

## Channel permissions roles

The current way to share a channel is channel permissions in Studio, under
Settings, Permissions. Invites are by email and expire after 30 days. The roles
are:

- Owner: can do everything, including delete the channel and manage permissions.
- Manager: can view all data, manage permissions, edit details, manage live
  streams, and create, upload, publish, and delete content.
- Editor: can edit everything, upload and publish, manage live streams, and
  moderate live chat, but cannot manage permissions.
- Editor (Limited): same as Editor but cannot access revenue data.
- Subtitle Editor: can add, edit, publish, and delete subtitles only.
- Viewer: can view all details and revenue but not edit.
- Viewer (Limited): same as Viewer but cannot access revenue data.

Only managers and the owner can see who else has access. Apply least privilege:
give editors the Limited variant when revenue should stay hidden.

## Brand Account roles versus channel permissions

Separately, a Brand Account has its own Google-level roles: primary owner, owner,
manager, and communications manager (the last cannot use YouTube). YouTube is
migrating channel sharing away from these Brand Account roles toward Studio channel
permissions for security, so prefer channel permissions for granting channel
access and reserve Brand Account roles for the underlying account.

## Ownership transfer and safety windows

Several actions have a built-in seven-day waiting period: you must have been an
owner for seven days before you can remove other owners or managers, and both the
current and the prospective primary owner must have held an owner or manager role
for at least seven days before primary ownership can transfer. These delays exist
to blunt account takeovers. YouTube also recommends keeping at least one backup
owner so a single compromised or departing account cannot lock everyone out.

## Security and feature access

Monetization through the [[YouTube Partner Program]] requires two-step
verification on the Google Account and advanced-features access on YouTube.
Feature access has three tiers: standard on channel creation, intermediate after
phone verification (which unlocks longer videos, custom thumbnails, live
streaming, and podcasts), and advanced after sufficient channel history or ID and
video verification. A clean record under [[Community Guidelines Strikes]] is a
prerequisite for keeping these features.

## How to apply

- Put any channel with more than one operator on a Brand Account, and name a
  backup owner immediately.
- Grant collaborators channel permissions by email and role rather than sharing
  the login; never share a password.
- Use Editor (Limited) or Viewer (Limited) for contractors who should not see
  revenue.
- Before moving or transferring a channel, confirm the destination account is
  empty and the seven-day windows are satisfied to avoid deleting the wrong
  channel.

## Sources

- Add or remove access to your channel with channel permissions, YouTube Help,
  retrieved 2026-06-26, https://support.google.com/youtube/answer/9481328
- Manage your Brand Account, Google Account Help, retrieved 2026-06-26,
  https://support.google.com/accounts/answer/7001996
- Change who manages your Brand Account, Google Account Help, retrieved
  2026-06-26, https://support.google.com/accounts/answer/7311601
- Change channel owners and managers with a Brand Account, YouTube Help, retrieved
  2026-06-26, https://support.google.com/youtube/answer/4628007
- Migrate from Brand Account user access to channel permissions, YouTube Help,
  retrieved 2026-06-26, https://support.google.com/youtube/answer/9367690
- Learn about feature access for YouTube creators, YouTube Help, retrieved
  2026-06-26, https://support.google.com/youtube/answer/9890437
- See [[research-pack-2026-06-23]] and [[index]].
