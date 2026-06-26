#!/usr/bin/env python3
"""Adapter tests for the YouTube Brain: importer, synthesis, renderer, and
determinism plus malformed-input handling. Pure-stdlib, no network."""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from youtube_brain.adapters import (
    channel_health,
    load_export,
    normalize_records,
    packaging_audit,
    render_scorecard_markdown,
)

FIXTURE = REPO / "tests" / "fixtures" / "sample-youtube-export.json"


def test_import_normalizes() -> None:
    records = normalize_records(load_export(FIXTURE))
    assert len(records) == 5
    assert [r["video_id"] for r in records] == sorted(r["video_id"] for r in records)
    one = next(r for r in records if r["video_id"] == "sample-001")
    # APV = avd / length = 318 / 612
    assert abs(one["average_percentage_viewed"] - round(318 / 612, 4)) < 1e-9
    # RPM = revenue / views * 1000 = 58.4 / 9200 * 1000
    assert abs(one["rpm_usd"] - round(58.4 / 9200 * 1000, 2)) < 1e-9
    assert one["midroll_eligible"] is True  # 612s >= 480s, long-form


def test_channel_health_flags() -> None:
    records = normalize_records(load_export(FIXTURE))
    health = channel_health(records)
    assert health["video_count"] == 5
    assert health["total_subscribers_gained"] == 240 + 180 + 64 + 410 + 152
    assert 0.0 <= health["avg_impressions_ctr"] <= 1.0
    assert isinstance(health["flags"], list)


def test_packaging_audit_picks_below_median() -> None:
    records = normalize_records(load_export(FIXTURE))
    audit = packaging_audit(records, min_impressions=1000.0)
    # Highest-impression below-median candidate sorts first.
    assert audit["candidate_count"] >= 1
    assert audit["candidates"][0]["impressions"] >= audit["candidates"][-1]["impressions"]


def test_render_is_deterministic_and_sourced() -> None:
    records = normalize_records(load_export(FIXTURE))
    a = render_scorecard_markdown(records, channel_name="Sample Creator")
    b = render_scorecard_markdown(records, channel_name="Sample Creator")
    assert a == b  # deterministic
    assert a.startswith("# Channel Health Scorecard")
    assert "[[Click-Through Rate]]" in a  # carries source wikilinks
    assert "rollback" in a.lower()


def test_malformed_input_raises() -> None:
    for bad in ([{"title": "missing id"}], [{"video_id": "x"}]):
        try:
            normalize_records(bad)
        except ValueError:
            continue
        raise AssertionError("expected ValueError on malformed input")


def test_empty_export_renders() -> None:
    # Empty / over-filtered exports must not crash the headline deliverable.
    health = channel_health([])
    assert health["video_count"] == 0
    assert health["total_views"] == 0.0  # full key set, no KeyError
    md = render_scorecard_markdown([], channel_name="Empty")
    assert md.startswith("# Channel Health Scorecard")


def test_null_and_nonfinite_handled() -> None:
    # null is treated as the field default; bool / NaN / negative are rejected cleanly.
    recs = normalize_records([{"video_id": "v", "title": "T", "length_seconds": None,
                               "impressions": 100, "views": 10}])
    assert recs[0]["length_seconds"] == 0.0
    for bad in (
        [{"video_id": "v", "title": "T", "length_seconds": 60, "impressions": True, "views": 5}],
        [{"video_id": "v", "title": "T", "length_seconds": float("nan"), "impressions": 1, "views": 1}],
        [{"video_id": "v", "title": "T", "length_seconds": -60, "impressions": 1, "views": 1}],
    ):
        try:
            normalize_records(bad)
        except ValueError:
            continue
        raise AssertionError("expected ValueError on bool/NaN/negative numeric field")


def main() -> int:
    test_import_normalizes()
    test_channel_health_flags()
    test_packaging_audit_picks_below_median()
    test_render_is_deterministic_and_sourced()
    test_malformed_input_raises()
    test_empty_export_renders()
    test_null_and_nonfinite_handled()
    print("Adapter tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
