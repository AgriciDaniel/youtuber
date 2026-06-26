---
type: flow
title: "Channel Health Audit"
status: mature
created: 2026-06-23
updated: 2026-06-23
tags: [youtube, flow, audit, analytics, workflow]
domain: "Analytics"
difficulty: intermediate
related:
  - "[[Studio Analytics]]"
  - "[[Click-Through Rate]]"
  - "[[Audience Retention]]"
  - "[[RPM and CPM]]"
  - "[[Monthly Optimization Roadmap]]"
  - "[[Source Intake and Refresh]]"
source_urls:
  - "https://support.google.com/youtube/answer/12220281"
  - "https://support.google.com/youtube/answer/9314355"
  - "https://support.google.com/youtube/answer/9314416"
---

# Channel Health Audit

The channel health audit is a repeatable read of a channel's
[[Studio Analytics]] that turns
raw numbers into a prioritized list of fixes. It follows the official funnel,
impressions to
CTR to views to watch time to subscribers, and localizes the weakest link. The
brain's
adapter scripts automate the export side of this flow; see
`scripts/synthesize_channel_health.py` and `scripts/render_channel_report.py`.

## Inputs

- A YouTube Studio video-level export (see
  `schemas/youtube-export-schema.json`), or direct access to Studio.
- A 28 to 90 day window for stable signals.
- The current [[Source Intake and Refresh]] facts for any monetization figure.

## Steps

1. Intake. Load the export with `scripts/import_youtube_export.py`, or open
   Reach, Engagement, Audience, and Revenue in Studio.
2. Top of funnel. Read impressions and impressions [[Click-Through Rate]] by
   traffic source. Weak impressions point to topic or demand; strong impressions
   with weak CTR point to [[Packaging]].
3. Retention. Read [[Audience Retention]] and [[Watch Time and AVD]]. A weak
   first 30 seconds points to the hook; mid video dips point to pacing.
4. Audience. Read returning versus new viewers and watch time from subscribers.
   Few returning viewers means the content does not build a habit; work on
   series and [[Publishing Cadence]].
5. Revenue. Read [[RPM and CPM]] and the active [[Revenue Streams]]. Low RPM
   points to geography, length, suitability, or undiversified income.
6. Synthesize. Produce a scorecard with the single weakest link flagged first;
   `scripts/render_channel_report.py` emits one with sourced wikilinks and a
   rollback note.

## Output

A channel health scorecard: headline metrics, flags, and packaging A/B
candidates, every
claim tied to a source. It feeds directly into the
[[Monthly Optimization Roadmap]].

## Guardrails

- Read every metric against the channel's own typical performance and the
  relevant traffic source, never in isolation.
- Make no monetization claim without a current source; see
  [[Source Intake and Refresh]].
- Recommend, do not mutate. The brain is advisory and read only toward any real
  account.

## Sources

- Understand your YouTube content performance, YouTube Help, retrieved
  2026-06-23, https://support.google.com/youtube/answer/12220281
- Understand your YouTube video reach, YouTube Help, retrieved 2026-06-23,
  https://support.google.com/youtube/answer/9314355
- Understand your YouTube audience, YouTube Help, retrieved 2026-06-23,
  https://support.google.com/youtube/answer/9314416
- See [[research-pack-2026-06-23]] and [[index]].
