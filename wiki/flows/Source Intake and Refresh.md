---
type: flow
title: "Source Intake and Refresh"
status: mature
created: 2026-06-23
updated: 2026-06-23
tags: [youtube, flow, sources, refresh, provenance, workflow]
domain: "Operations"
difficulty: intermediate
related:
  - "[[YouTube Partner Program]]"
  - "[[Advertiser-Friendly Guidelines]]"
  - "[[Mid-Roll Ads]]"
  - "[[Shorts Monetization]]"
  - "[[Channel Health Audit]]"
  - "[[overview]]"
source_urls:
  - "https://support.google.com/youtube/answer/1311392"
  - "https://support.google.com/youtube/answer/72851"
---

# Source Intake and Refresh

YouTube's rules move fast, so the brain stays trustworthy only if its sources
are dated and
refreshed on a schedule. This flow defines how new sources enter the brain and
how stale
ones are caught. It is the operational backbone behind the refusal rule that no
growth,
revenue, or policy claim ships without a current official or primary source. The
ledger
lives in `references/source-ledger.json` and the dated pack in
[[research-pack-2026-06-23]].

## Refresh cadence

- Monthly: YouTube Help Center pages and Studio analytics references, the
  fastest moving facts.
- On changelog: recommendation and monetization policy changes, for example the
  inauthentic content policy or a mid-roll update.
- Quarterly: practitioner benchmarks such as vidIQ and TubeBuddy data.

## Intake steps

1. Capture. File the raw source under `.raw/research/` with its URL and
   retrieval date. Deep-research reports land here.
2. Record. Add a ledger entry to `references/source-ledger.json` with id, title,
   url, source_type, retrieved, a future refresh_due, confidence, and specific
   claims.
3. Cite. Add the source to [[research-pack-2026-06-23]] so the dated pack stays
   complete.
4. Synthesize. Update the affected concept notes and their Sources sections,
   then update [[index]] and the changelog.

## Refresh steps

1. Find due sources: any entry whose refresh_due has passed.
2. Re-verify the claim against the live page; update retrieved, refresh_due, and
   the claim if it changed.
3. Propagate changes to the concept notes that cite the source.
4. Record the refresh in the changelog with the date and what changed.

## Fast-moving facts to watch

The highest risk facts are monetization thresholds and mechanics:
[[YouTube Partner Program]] eligibility, the 45 and 55 percent splits,
[[Mid-Roll Ads]]
rules, [[Shorts Monetization]] mechanics, and the
[[Advertiser-Friendly Guidelines]].
Re-verify these before any monetization recommendation, including inside the
[[Channel Health Audit]].

## Guardrails

- No credentials, tokens, cookies, or private audience data enter the repo,
  ever.
- No claim without a dated source; an undated claim is a defect.
- Recommend, do not mutate; the brain is read only toward any real account.

## Sources

- YouTube channel monetization policies, YouTube Help, 2025-07-15,
  https://support.google.com/youtube/answer/1311392
- YouTube Partner Program overview and eligibility, YouTube Help, retrieved
  2026-06-23, https://support.google.com/youtube/answer/72851
- See [[research-pack-2026-06-23]] and [[index]].
