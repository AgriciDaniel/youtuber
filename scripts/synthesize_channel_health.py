#!/usr/bin/env python3
"""Synthesize a sourced channel-health scorecard from a YouTube export.

Read-only. Usage:
    python scripts/synthesize_channel_health.py --export tests/fixtures/sample-youtube-export.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from youtube_brain.adapters import channel_health, load_export, normalize_records


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Channel health synthesis.")
    parser.add_argument("--export", required=True, help="path to export JSON")
    args = parser.parse_args(argv)
    records = normalize_records(load_export(args.export))
    json.dump(channel_health(records), sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
