#!/usr/bin/env python3
"""Import a YouTube Studio style video-level export and print normalized records.

Read-only. No credentials, no network. Usage:
    python scripts/import_youtube_export.py --export tests/fixtures/sample-youtube-export.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from youtube_brain.adapters import load_export, normalize_records


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Normalize a YouTube export.")
    parser.add_argument("--export", required=True, help="path to export JSON")
    args = parser.parse_args(argv)
    records = normalize_records(load_export(args.export))
    json.dump(records, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
