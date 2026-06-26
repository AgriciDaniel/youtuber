#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path


MAX_BYTES = 10 * 1024 * 1024


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Ingest one raw source into a brain vault.")
    parser.add_argument("--vault", required=True)
    parser.add_argument("--file", required=True)
    parser.add_argument("--source-type", default="manual")
    args = parser.parse_args(argv)
    vault = Path(args.vault).expanduser().resolve()
    source = Path(args.file).expanduser().resolve()
    if not (vault / "CODEX.md").exists():
        print(f"ERROR: not a brain vault: {vault}", file=sys.stderr)
        return 2
    if not source.is_file():
        print(f"ERROR: source file not found: {source}", file=sys.stderr)
        return 2
    if source.stat().st_size > MAX_BYTES:
        print(f"ERROR: source file too large: {source}", file=sys.stderr)
        return 2
    raw_dir = vault / ".raw" / "sources"
    raw_dir.mkdir(parents=True, exist_ok=True)
    source_digest = sha256_file(source)
    target = collision_safe_path(raw_dir, source.name, source_digest)
    shutil.copy2(source, target)
    digest = sha256_file(target)
    update_manifest(vault, target.relative_to(vault).as_posix(), digest, args.source_type)
    source_note = collision_safe_path(vault / "wiki" / "sources", f"{safe_title(source.stem)}.md", digest)
    source_note.parent.mkdir(parents=True, exist_ok=True)
    source_note.write_text(f"""---
type: "source"
title: "{source.stem}"
created: "{date.today().isoformat()}"
updated: "{date.today().isoformat()}"
status: "active"
sources: ["{target.relative_to(vault).as_posix()}"]
---

# {source.stem}

## Source

- Path: `{target.relative_to(vault).as_posix()}`
- Hash: `{digest}`
- Retrieved: {date.today().isoformat()}
- Type: {args.source_type}

## Compiled Truth

Summarize this source without copying it wholesale.

Related: [[Source Manifest Guide]] | [[wiki/sources/_index|Sources Hub]]
""", encoding="utf-8")
    append_log(vault, f"Ingested source [[{source.stem}]] from `{target.relative_to(vault).as_posix()}`.")
    print(json.dumps({"copied": str(target), "sha256": digest}, indent=2))
    return 0


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def collision_safe_path(directory: Path, filename: str, digest: str) -> Path:
    safe_name = safe_filename(filename)
    candidate = directory / safe_name
    if not candidate.exists():
        return candidate
    stem = candidate.stem or "source"
    suffix = candidate.suffix
    digest_name = directory / f"{stem}-{digest[:12]}{suffix}"
    if not digest_name.exists():
        return digest_name
    counter = 2
    while True:
        numbered = directory / f"{stem}-{digest[:12]}-{counter}{suffix}"
        if not numbered.exists():
            return numbered
        counter += 1


def safe_filename(value: str) -> str:
    name = Path(value).name
    cleaned = re.sub(r"[^A-Za-z0-9._ -]+", "", name).strip()
    return cleaned[:120] or "source"


def update_manifest(vault: Path, rel: str, digest: str, source_type: str) -> None:
    path = vault / ".raw" / ".manifest.json"
    data = {"sources": []}
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit(f"ERROR: raw manifest must be an object: {path}")
    sources = data.setdefault("sources", [])
    if not isinstance(sources, list):
        raise SystemExit(f"ERROR: raw manifest sources must be a list: {path}")
    data.setdefault("sources", []).append({
        "path": rel,
        "sha256": digest,
        "retrieved": date.today().isoformat(),
        "source_type": source_type,
    })
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    path.chmod(0o600)


def safe_title(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9 _-]+", "", value).strip() or "Source"
    return cleaned[:90]


def append_log(vault: Path, message: str) -> None:
    log = vault / "wiki" / "log.md"
    if log.exists():
        text = log.read_text(encoding="utf-8").rstrip() + f"\n- {date.today().isoformat()} - {message}\n"
        log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
