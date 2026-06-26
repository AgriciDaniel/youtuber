---
type: concept
title: "Ad Bidding and Budget"
status: mature
created: 2026-06-24
updated: 2026-06-24
tags: [youtube, ads, advertising, bidding, cpv, cpm, budget]
domain: "Advertising"
difficulty: advanced
related:
  - "[[Ad Formats]]"
  - "[[Ad Campaign Types]]"
  - "[[Ad Targeting]]"
  - "[[Ad Measurement]]"
  - "[[RPM and CPM]]"
  - "[[Connected TV and Shorts Ads]]"
source_urls:
  - "https://support.google.com/google-ads/answer/2472735"
  - "https://support.google.com/google-ads/answer/13982458"
  - "https://support.google.com/google-ads/answer/12400225"
---

# Ad Bidding and Budget

Bidding is where the advertiser tells Google what an outcome is worth, and the
single fact
that trips people up is that a "view" means different things by format and
campaign, so you
can pay for very different things under similar-looking buys. This note maps bid
strategies
to outcomes. The format definitions are in [[Ad Formats]] and the campaigns that
use them in
[[Ad Campaign Types]]. Note the contrast with creator-side [[RPM and CPM]],
which is what
the creator earns, not what the advertiser pays.

## What counts as a view

- In-stream: a view counts when someone watches 30 seconds, or the full ad if it
  is shorter than 30 seconds, or interacts, whichever comes first.
- In-feed: a view counts on a thumbnail click or a 10-second autoplay.
- Shorts: a view counts at 10 seconds, the full ad, a call-to-action click, or
  an engagement.

Bumper and non-skippable in-stream do not generate TrueView views; they generate
public
views and bill on impressions.

## The bid strategies

- CPV (cost per view): you set a Target CPV, the average you pay per TrueView
  view. This powers consideration and video views campaigns.
- CPM (cost per mille): you pay per 1,000 impressions, used by bumper,
  non-skippable, and reach campaigns via Target CPM.
- Conversion bidding: Maximize Conversions, Target CPA, Maximize Conversion
  Value, and Target ROAS bill toward actions, used by Demand Gen; see
  [[Ad Campaign Types]].
- Maximize Clicks for traffic.

## Frequency as a budget lever

Target frequency optimizes to a set weekly or monthly impression count per user
(2 to 7
weekly or 4 to 12 monthly for multi-format) and is an average target, not a hard
cap; some
users see more and some fewer. See [[Connected TV and Shorts Ads]].

## How to apply

- Pick the bid that matches the goal: CPV for paid views, CPM for impressions
  and reach, conversion bidding for actions.
- Know which "view" definition applies before you read a CPV report, or you will
  misjudge efficiency.
- Use frequency targets to control how often the same person sees the ad,
  balancing reach and waste.
- Measure outcomes, not just views; see [[Ad Measurement]].

## Sources

- About cost-per-view (CPV) bidding, Google Ads Help, retrieved 2026-06-24,
  https://support.google.com/google-ads/answer/2472735
- About Video views, Google Ads Help, retrieved 2026-06-24,
  https://support.google.com/google-ads/answer/13982458
- About Target frequency, Google Ads Help, retrieved 2026-06-24,
  https://support.google.com/google-ads/answer/12400225
- See [[research-pack-2026-06-23]] and [[index]].
