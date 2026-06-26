"""Domain adapters for the YouTube Brain.

Pure-stdlib, deterministic transforms over a YouTube Studio style video-level
export. No network, no credentials, no account mutation. Every metric maps to a
sourced concept in the vault (see wiki/concepts and references/source-ledger.json).
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

# Official impressions CTR band: half of channels sit between 2% and 10%
# (YouTube Help 7628154). Used only to flag, never to promise outcomes.
CTR_BAND_LOW = 0.02
CTR_BAND_HIGH = 0.10
# A typical intro keeps 50%+ past 30 seconds; 50% APV is the common "good" line
# (YouTube Help 12942217 / 12340300; vidIQ average-view-duration).
APV_GOOD = 0.50
# Mid-roll ads require an 8 minute runtime (YouTube Help 6175006).
MIDROLL_MIN_SECONDS = 8 * 60

REQUIRED_FIELDS = ("video_id", "title", "length_seconds", "impressions", "views")


def _num(row: dict[str, Any], field: str, index: int, *, default: float = 0.0, allow_negative: bool = False) -> float:
    """Coerce a field to a finite, non-negative float with a clear error.

    Treats a missing value or ``None`` as ``default``; rejects booleans,
    non-numeric strings, lists, and non-finite values (NaN/Infinity) with a
    ``ValueError`` that names the offending video and field. This keeps the
    importer from crashing on the ``null`` cells common in real Studio exports
    and prevents invalid JSON (bare ``NaN``) in the output."""
    value = row.get(field, default)
    if value is None:
        return float(default)
    if isinstance(value, bool):
        raise ValueError(f"video #{index + 1} field {field!r} must be numeric, not a boolean")
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"video #{index + 1} field {field!r} is not numeric: {value!r}") from None
    if not math.isfinite(number):
        raise ValueError(f"video #{index + 1} field {field!r} must be finite, got {value!r}")
    if number < 0 and not allow_negative:
        raise ValueError(f"video #{index + 1} field {field!r} must be non-negative, got {number}")
    return number


def load_export(path: str | Path) -> list[dict[str, Any]]:
    """Load a YouTube export JSON. Accepts {"videos": [...]} or a bare list."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict):
        videos = data.get("videos", [])
    elif isinstance(data, list):
        videos = data
    else:
        raise ValueError("export must be a JSON object with 'videos' or a JSON list")
    if not isinstance(videos, list):
        raise ValueError("'videos' must be a list")
    return videos


def normalize_records(videos: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Validate and enrich raw rows with derived APV and RPM. Deterministic."""
    out: list[dict[str, Any]] = []
    for index, row in enumerate(videos):
        if not isinstance(row, dict):
            raise ValueError(f"video #{index + 1} is not an object")
        for field in REQUIRED_FIELDS:
            if field not in row:
                raise ValueError(f"video #{index + 1} missing required field: {field}")
        length = _num(row, "length_seconds", index)
        views = _num(row, "views", index)
        impressions = _num(row, "impressions", index)
        avd = _num(row, "average_view_duration_seconds", index)
        revenue = _num(row, "estimated_revenue_usd", index)
        ctr = _num(row, "impressions_ctr", index, default=(views / impressions) if impressions else 0.0)
        apv = (avd / length) if length else 0.0
        rpm = (revenue / views * 1000.0) if views else 0.0
        watch_hours = _num(row, "watch_time_hours", index, default=avd * views / 3600.0)
        subs = round(_num(row, "subscribers_gained", index, allow_negative=True))
        fmt = str(row.get("format", "long")).lower()
        out.append(
            {
                "video_id": str(row["video_id"]),
                "title": str(row["title"]),
                "published": str(row.get("published", "")),
                "format": "short" if fmt == "short" else "long",
                "length_seconds": round(length, 2),
                "impressions": round(impressions, 2),
                "impressions_ctr": round(ctr, 4),
                "views": round(views, 2),
                "average_view_duration_seconds": round(avd, 2),
                "average_percentage_viewed": round(apv, 4),
                "watch_time_hours": round(watch_hours, 2),
                "subscribers_gained": subs,
                "estimated_revenue_usd": round(revenue, 2),
                "rpm_usd": round(rpm, 2),
                "midroll_eligible": bool(length >= MIDROLL_MIN_SECONDS and fmt != "short"),
            }
        )
    out.sort(key=lambda r: r["video_id"])
    return out


def _weighted_mean(pairs: list[tuple[float, float]]) -> float:
    total_w = sum(w for _, w in pairs)
    if total_w <= 0:
        return 0.0
    return sum(v * w for v, w in pairs) / total_w


def channel_health(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate a sourced channel-health scorecard from normalized records."""
    if not records:
        return {
            "video_count": 0,
            "total_views": 0.0,
            "total_watch_hours": 0.0,
            "total_subscribers_gained": 0,
            "total_estimated_revenue_usd": 0.0,
            "avg_impressions_ctr": 0.0,
            "avg_percentage_viewed": 0.0,
            "blended_rpm_usd": 0.0,
            "flags": ["no videos in export"],
        }
    total_views = sum(r["views"] for r in records)
    total_watch_hours = round(sum(r["watch_time_hours"] for r in records), 2)
    total_subs = sum(r["subscribers_gained"] for r in records)
    total_revenue = round(sum(r["estimated_revenue_usd"] for r in records), 2)
    avg_ctr = round(_weighted_mean([(r["impressions_ctr"], r["impressions"]) for r in records]), 4)
    avg_apv = round(_weighted_mean([(r["average_percentage_viewed"], r["views"]) for r in records]), 4)
    blended_rpm = round((total_revenue / total_views * 1000.0) if total_views else 0.0, 2)
    flags: list[str] = []
    if avg_ctr < CTR_BAND_LOW:
        flags.append("avg CTR below the official 2 percent band floor; review packaging")
    if avg_apv < APV_GOOD:
        flags.append("avg percentage viewed below 50 percent; review hooks and pacing")
    long_form = [r for r in records if r["format"] == "long"]
    short_long_under_8 = [r for r in long_form if not r["midroll_eligible"]]
    if short_long_under_8:
        flags.append(
            f"{len(short_long_under_8)} long-form videos under 8 minutes forgo mid-roll ad revenue"
        )
    return {
        "video_count": len(records),
        "total_views": round(total_views, 2),
        "total_watch_hours": total_watch_hours,
        "total_subscribers_gained": total_subs,
        "total_estimated_revenue_usd": total_revenue,
        "avg_impressions_ctr": avg_ctr,
        "avg_percentage_viewed": avg_apv,
        "blended_rpm_usd": blended_rpm,
        "flags": flags,
    }


def packaging_audit(records: list[dict[str, Any]], min_impressions: float = 1000.0) -> dict[str, Any]:
    """Flag long-form videos with enough reach but below-median CTR as A/B test
    candidates. Winner is decided by watch-time share, not raw CTR
    (YouTube Help 13861714)."""
    long_form = [r for r in records if r["format"] == "long" and r["impressions"] >= min_impressions]
    if not long_form:
        return {"candidate_count": 0, "median_ctr": 0.0, "candidates": []}
    ctrs = sorted(r["impressions_ctr"] for r in long_form)
    mid = len(ctrs) // 2
    median_ctr = ctrs[mid] if len(ctrs) % 2 else round((ctrs[mid - 1] + ctrs[mid]) / 2, 4)
    candidates = [
        {
            "video_id": r["video_id"],
            "title": r["title"],
            "impressions": r["impressions"],
            "impressions_ctr": r["impressions_ctr"],
            "gap_to_median": round(median_ctr - r["impressions_ctr"], 4),
        }
        for r in long_form
        if r["impressions_ctr"] < median_ctr
    ]
    candidates.sort(key=lambda c: (-c["impressions"], c["video_id"]))
    return {"candidate_count": len(candidates), "median_ctr": round(median_ctr, 4), "candidates": candidates}


def render_scorecard_markdown(records: list[dict[str, Any]], *, channel_name: str = "Sample Channel") -> str:
    """Render a sourced markdown channel-health scorecard. Every claim links to a
    vault concept; advisory only, with a rollback reminder."""
    health = channel_health(records)
    packaging = packaging_audit(records)
    lines = [
        f"# Channel Health Scorecard: {channel_name}",
        "",
        "Advisory only. Verify every monetization figure against the official source before acting; keep a rollback note. See [[YouTube Partner Program]] and [[RPM and CPM]].",
        "",
        "## Headline metrics",
        "",
        f"- Videos analyzed: {health['video_count']}",
        f"- Total views: {health['total_views']}",
        f"- Total watch time (hours): {health['total_watch_hours']}",
        f"- Subscribers gained: {health['total_subscribers_gained']}",
        f"- Avg impressions CTR: {health['avg_impressions_ctr']} (official band 2-10 percent, see [[Click-Through Rate]])",
        f"- Avg percentage viewed: {health['avg_percentage_viewed']} (50 percent is a healthy floor, see [[Audience Retention]])",
        f"- Blended RPM (USD): {health['blended_rpm_usd']} (see [[RPM and CPM]])",
        f"- Estimated revenue (USD): {health['total_estimated_revenue_usd']}",
        "",
        "## Flags",
        "",
    ]
    lines.extend([f"- {flag}" for flag in health["flags"]] or ["- none"])
    lines += [
        "",
        "## Packaging A/B test candidates",
        "",
        f"Median long-form CTR: {packaging['median_ctr']}. Candidates are below-median videos with reach; test titles and thumbnails (see [[Packaging]] and [[Title-Thumbnail A-B Test Loop]]).",
        "",
    ]
    if packaging["candidates"]:
        lines.append("| Video | Impressions | CTR | Gap to median |")
        lines.append("|---|---:|---:|---:|")
        for c in packaging["candidates"]:
            lines.append(f"| {c['title']} | {c['impressions']} | {c['impressions_ctr']} | {c['gap_to_median']} |")
    else:
        lines.append("No below-median candidates with sufficient impressions.")
    lines += [
        "",
        "## Sources",
        "",
        "- [[research-pack-2026-06-23]] and `references/source-ledger.json` back every benchmark above.",
        "",
    ]
    return "\n".join(lines) + "\n"
