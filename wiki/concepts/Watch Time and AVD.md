---
type: concept
title: "Watch Time and AVD"
status: mature
created: 2026-06-23
updated: 2026-06-23
tags: [youtube, watch-time, avd, apv, metrics, retention]
domain: "Retention"
difficulty: basic
related:
  - "[[Audience Retention]]"
  - "[[Recommendation System]]"
  - "[[Studio Analytics]]"
  - "[[Click-Through Rate]]"
  - "[[Shorts]]"
  - "[[Hook in the First 30 Seconds]]"
source_urls:
  - "https://support.google.com/youtube/answer/9313698"
  - "https://support.google.com/youtube/answer/12942217"
  - "https://vidiq.com/blog/post/average-view-duration/"
---

# Watch Time and AVD

Watch time is the total time viewers spend watching your content. Average view
duration
(AVD) is the average minutes watched among those who stayed to watch, that is
total watch
time divided by views. Average percentage viewed (APV) is the relative version,
AVD divided
by the video length. These three metrics, together with the retention graph,
tell you
whether a video keeps the promise its [[Packaging]] made. They are inputs to the
[[Recommendation System]], not the target themselves, because the system weights
them by
satisfaction.

## AVD versus APV

- AVD is absolute. A 4 minute AVD on a 20 minute video is very different from a
  4 minute AVD on a 5 minute video.
- APV is relative and comparable across lengths. APV = AVD / length.
- Use both. AVD shows raw holding power; APV shows efficiency. A long video with
  a moderate APV can still produce more watch time than a short video with a
  high APV.

## Benchmarks that hold up

There is no universal ideal length; YouTube explicitly says to avoid filler and
artificial
stretching. Practitioner data offers rough APV tiers: 50 to 60 percent is good,
60 to 70
percent very good, and 70 percent or higher excellent. A consistent APV above 50
percent is
a strong signal, and consistently below 40 percent is the first thing to fix.
For
[[Shorts]], the target is higher, often 60 percent or more, because the format
is short and
looping. See [[Audience Retention]] for the graph-level view.

## Why it feeds discovery indirectly

The system uses AVD and APV as retention signals, but it weights them by
satisfaction
surveys and session continuation. This is the key nuance: maximizing minutes by
padding a
video can raise AVD while lowering satisfaction, which is self defeating. The
goal is a
video that is as long as it deserves to be and no longer. See
[[Chasing Views Over Satisfaction]].

## Shorts watch behavior

For Shorts, AVD is calculated from engaged views. Since 2025-03-31 a view counts
on every
play or replay, while the older sustained metric is renamed engaged views and
still governs
monetization. Loops can push APV above 100 percent of a single play. See
[[Shorts]] and
[[Shorts Monetization]].

## How to apply

- In [[Studio Analytics]], compare AVD and APV against your own typical
  performance, not against strangers.
- If APV is low, fix the opening with a [[Hook in the First 30 Seconds]] and
  tighten pacing.
- If AVD is low but APV is high, the video may simply be short; consider whether
  the topic supports more depth.
- Never inflate watch time with filler; it lowers the satisfaction signal that
  actually drives [[Recommendation System]] reach.

## Sources

- Understand audience engagement, YouTube Help, retrieved 2026-06-23,
  https://support.google.com/youtube/answer/9313698
- Content tab analytics tips, YouTube Help, retrieved 2026-06-23,
  https://support.google.com/youtube/answer/12942217
- Understanding YouTube Average View Duration, vidIQ, 2025-02-07,
  https://vidiq.com/blog/post/average-view-duration/
- See [[research-pack-2026-06-23]] and [[index]].
