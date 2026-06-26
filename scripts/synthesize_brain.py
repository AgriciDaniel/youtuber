#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Synthesize source-cited starter deliverables.")
    parser.add_argument("--vault", required=True)
    args = parser.parse_args(argv)
    vault = Path(args.vault).expanduser().resolve()
    manifest_path = vault / ".raw" / ".manifest.json"
    if not manifest_path.exists():
        print("ERROR: missing .raw/.manifest.json; run scaffold and ingest first", file=sys.stderr)
        return 2
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    sources = manifest.get("sources", [])
    source_rows = "\n".join(f"| `{item.get('path', '')}` | `{item.get('sha256', '')[:12]}` | {item.get('retrieved', '')} |" for item in sources) or "| No sources yet |  |  |"
    write(vault / "wiki" / "deliverables" / "Health Scorecard.md", f"""---
type: "deliverable"
title: "Health Scorecard"
created: "{date.today().isoformat()}"
updated: "{date.today().isoformat()}"
status: "draft"
---

# Health Scorecard

## Source Coverage

| Source | Hash | Retrieved |
|---|---|---:|
{source_rows}

## Current Read

This is a source-cited scaffold. Domain-specific conclusions remain blocked
until current trustworthy research is captured in `references/`.

Related: [[Action Roadmap]] | [[Weekly Report]] | [[Source Manifest Guide]]
""")
    write(vault / "wiki" / "deliverables" / "Action Roadmap.md", f"""---
type: "deliverable"
title: "Action Roadmap"
created: "{date.today().isoformat()}"
updated: "{date.today().isoformat()}"
status: "draft"
---

# Action Roadmap

## Immediate Actions

1. Complete source intake.
2. Refresh official/current requirements.
3. Replace scaffold claims with sourced domain notes.

## Approval Gate

Every action requires source, confidence, owner, approval status, and rollback.

Related: [[Approval Queue]] | [[Health Scorecard]] | [[Best Practices Kernel]]
""")
    write(vault / "wiki" / "reports" / "Weekly Report.md", f"""---
type: "report"
title: "Weekly Report"
created: "{date.today().isoformat()}"
updated: "{date.today().isoformat()}"
status: "draft"
---

# Weekly Report

## Summary

YouTube Brain is ready for source review. It has {len(sources)} raw source(s) in
the manifest.

## Evidence

- [[Health Scorecard]]
- [[Action Roadmap]]
- [[Source Manifest Guide]]

Related: [[Reporting Workflow]] | [[Approval Queue]]
""")
    append_log(vault, "Synthesized source-cited starter deliverables.")
    print("Synthesis complete")
    return 0


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def append_log(vault: Path, message: str) -> None:
    log = vault / "wiki" / "log.md"
    if log.exists():
        log.write_text(log.read_text(encoding="utf-8").rstrip() + f"\n- {date.today().isoformat()} - {message}\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
