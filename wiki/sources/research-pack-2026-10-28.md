---
type: source
title: "Research Pack 2026-10-28"
status: evergreen
created: 2026-10-28
updated: 2026-10-28
tags: [sources, research-pack, verification, youtube]
domain: "Sources"
---

# Research Pack 2026-10-28

Verification refresh of the source pack first gathered on 2026-06-23. This pass
re-requested every ledger URL, compared each article against the title recorded
in `references/source-ledger.json`, re-read the claims where the page had moved,
and corrected claims whose supporting text had changed. Structured record:
`references/source-ledger.json` (`last_refresh`). Initial research pack:
[[research-pack-2026-06-23]]. Related: [[index]], [[YouTube Brain Home]],
[[Source Intake and Refresh]].

Scope: 156 sources. 154 resolved on 2026-10-28; 113 YouTube Help pages answered
HTTP 429 to this network and were read from the Wayback capture instead. Two
sources needed a non-origin citation:

- RetentionRabbit benchmark (404 at origin) -> 2026-07-25 capture; the archived
  text still carries the 23.7% average retention and 16.8% above-50% figures.
- Search Engine Land VRC article (HTTP 403 to automated clients) -> March 2026
  capture; confirms global launch on 2026-03-03 with 6s, 15s, and 30s CTV
  formats.

## URL changes

All 19 redirects are recorded in the ledger. The largest group is the YouTube
Data API documentation, which moved from `/youtube/v3/` to `/youtube/data/`:

- `developers.google.com/youtube/v3/docs` -> `/youtube/data/reference/rest`
- `developers.google.com/youtube/v3/getting-started` -> `/youtube/data/getting-started`
- `developers.google.com/youtube/v3/determine_quota_cost` -> `/youtube/data/determine_quota_cost`
- `developers.google.com/youtube/v3/guides/...` -> `/youtube/data/guides/...`
- `developers.google.com/youtube/v3/live/getting-started` -> `/youtube/data/live/getting-started`
- `developers.google.com/youtube/v3/revision_history` -> `/youtube/data/revision_history`

Three Help Center article IDs now serve a different article and were remapped:

- Video chapters: 12948449 (now "Tips for video descriptions") -> 9884579
- Playlists: 6327615 (now "Autoplay videos") -> 57792
- Copyright strikes: 7002106 (now "What is a claim?") -> 2814000

Two article paths moved in place:

- `youtube.com/intl/ALL_en/howyoutubeworks/product-features/recommendations/`
  -> `.../howyoutubeworks/recommendations/`
- `blog.google/products/youtube/made-on-youtube-2024/`
  -> `blog.google/products-and-platforms/products/youtube/made-on-youtube-2024/`

## Claim changes

- View counting: from 2026-08-24 public views across all formats count from the
  first frame; the previous definition is now an engaged view. YPP qualification
  still uses qualified views, and CTR, AVD, retention, and recommendations are
  unchanged. Source: YouTube Blog, "What are 'Engaged' Views on YouTube?",
  2026-08-19.
- YouTube Partner Program: Help Center now says 4,000 *qualified* watch hours and
  10 million *qualified* Shorts views; Shorts Feed watch time does not count
  toward the 4,000 hours.
- Shopping affiliate: Help Center now states YPP membership plus the YPP
  subscriber threshold rather than a 500-subscriber figure.
- CPM Masthead: access is requested through a Google representative or Account
  Manager for allowlisting; the recorded Programmatic Guaranteed / Reservation
  wording is no longer on the page.
- Video Action Campaigns: the page lists April 2025 (no new VACs) and July 2025
  (automatic upgrade to Demand Gen) only; the recorded April 2026 completion date
  is not supported.
- Content performance: the subscribers report breaks subscribers gained out by
  content type.

## Verified unchanged

Exact-string checks confirmed: 55% / 45% / 70% revenue splits; 8-minute mid-roll
threshold; 1,000 subscribers with 4,000 hours or 10 million Shorts views; 500 / 3
uploads / 3,000 hours or 3 million Shorts views; three-minute Shorts from
2024-10-15 with 90-second music limits; 100,000 / 1,000,000 / 10,000,000 /
100,000,000 Creator Awards; impressions counted after one second at 50% visible;
membership pricing $0.99-$499.99; Super Chat spend caps of $500/day and
$2,000/week; handles of 3-30 characters; Maximum / Moderate / Limited inventory
modes from September 2024.

## Open item

`yt-hype-leaderboard`: the page describes the bonus rule only directionally, so
the ledger claim is kept hedged rather than quantified.
