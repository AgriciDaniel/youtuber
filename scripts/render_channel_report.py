#!/usr/bin/env python3
"""Render a sourced channel-health scorecard (markdown) from a YouTube export.

Read-only. Usage:
    python scripts/render_channel_report.py --export tests/fixtures/sample-youtube-export.json --channel "Sample Channel"
    python scripts/render_channel_report.py --export <path> --out wiki/deliverables/Channel Scorecard.md
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from youtube_brain.adapters import load_export, normalize_records, render_scorecard_markdown


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render channel-health report.")
    parser.add_argument("--export", required=True, help="path to export JSON")
    parser.add_argument("--channel", default="Sample Channel")
    parser.add_argument("--out", default="", help="optional output markdown path")
    args = parser.parse_args(argv)
    records = normalize_records(load_export(args.export))
    md = render_scorecard_markdown(records, channel_name=args.channel)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(md, encoding="utf-8")
        print(args.out)
    else:
        sys.stdout.write(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
