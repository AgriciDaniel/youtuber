---
type: concept
title: "Analytics and Reporting API"
status: mature
created: 2026-06-24
updated: 2026-06-24
tags: [youtube, api, analytics-api, reporting-api, metrics, developer]
domain: "Developer API"
difficulty: advanced
related:
  - "[[API Overview and Auth]]"
  - "[[API Quota System]]"
  - "[[API Resources and Methods]]"
  - "[[Studio Analytics]]"
  - "[[RPM and CPM]]"
  - "[[Channel Health Audit]]"
source_urls:
  - "https://developers.google.com/youtube/reporting"
  - "https://developers.google.com/youtube/analytics/channel_reports"
  - "https://developers.google.com/youtube/reporting/v1/reports"
---

# Analytics and Reporting API

YouTube exposes channel analytics through two distinct APIs over the same data:
the
Analytics API for real-time targeted queries and the Reporting API for bulk
predefined
datasets. They power the kind of channel-health automation the brain's adapters
do by hand;
choosing the right one depends on whether you want a specific answer now or a
daily firehose
to warehouse. The Studio equivalent of these metrics is in [[Studio Analytics]].

## Analytics API: targeted queries

The Analytics API answers a single `reports.query` request synchronously. A
channel query
specifies `ids=channel==MINE` (or a channel ID), a start and end date, required
metrics, and
optional dimensions and filters.

- Metrics include views, estimatedMinutesWatched, averageViewDuration, likes,
  comments, shares, subscribersGained, and estimatedRevenue.
- Dimensions include day, month, country, video, ageGroup, gender, deviceType,
  and insightTrafficSourceType (the API form of the [[Studio Analytics]] traffic
  sources).
- A report is defined by a combination of dimensions and metrics, optionally
  constrained by filters.

This is the right tool for a dashboard that asks specific questions, for example
watch time
by traffic source for the last 28 days.

## Reporting API: bulk reports

The Reporting API delivers bulk, predefined reports. The workflow is: call
`jobs.create`
with a `reportTypeId` (for example `channel_basic_a3`), then enumerate generated
reports via
`jobs.reports.list`, then download each via its `downloadUrl`. Each report
covers a 24-hour
Pacific-time period as a CSV (optionally gzipped). Reports become retrievable
within 48
hours of job creation, YouTube backfills roughly 30 days of history on job
creation,
standard reports stay available 60 days, and historical reports 30 days. This is
the tool
for warehousing every day's data at scale.

## Scopes and money

Both use `yt-analytics.readonly`, and for revenue and ad metrics,
`yt-analytics-monetary.readonly`. Content-owner reports aggregate metrics across
all
channels linked to a content owner, while channel reports cover one channel.
Revenue numbers
here are the API source for the [[RPM and CPM]] figures a
[[Channel Health Audit]] reads.

## How to apply

- For a live dashboard, use the Analytics API and request only the metrics and
  dimensions you display.
- For a data warehouse or long retention, use the Reporting API and store the
  daily CSVs yourself.
- Add the monetary scope only when you need revenue, and treat that data under
  the no-credentials and storage rules in [[API Policies and Limits]].

## Sources

- Introduction (Analytics and Reporting APIs), Google for Developers, retrieved
  2026-06-24, https://developers.google.com/youtube/reporting
- Channel Reports, Google for Developers, retrieved 2026-06-24,
  https://developers.google.com/youtube/analytics/channel_reports
- Get Bulk Data Reports, Google for Developers, retrieved 2026-06-24,
  https://developers.google.com/youtube/reporting/v1/reports
- See [[research-pack-2026-06-23]] and [[index]].
