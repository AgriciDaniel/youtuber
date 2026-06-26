#!/usr/bin/env python3
"""Synthesize packaging A/B test candidates from a YouTube export.

Flags long-form videos with reach but below-median CTR. Read-only. Usage:
    python scripts/synthesize_packaging_audit.py --export tests/fixtures/sample-youtube-export.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from youtube_brain.adapters import load_export, normalize_records, packaging_audit


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Packaging A/B audit.")
    parser.add_argument("--export", required=True, help="path to export JSON")
    parser.add_argument("--min-impressions", type=float, default=1000.0)
    args = parser.parse_args(argv)
    records = normalize_records(load_export(args.export))
    json.dump(packaging_audit(records, min_impressions=args.min_impressions), sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
