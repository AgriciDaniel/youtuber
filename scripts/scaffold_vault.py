#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import stat
import sys
from datetime import date
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
TEMPLATE = REPO / "assets" / "template-brain"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Scaffold a client vault from the template brain.")
    parser.add_argument("--client", required=True)
    parser.add_argument("--client-name", default="")
    parser.add_argument("--owner", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args(argv)
    slug = safe_slug(args.client)
    out_dir = Path(args.out_dir).expanduser().resolve()
    vault = out_dir / slug
    if vault.exists() and any(vault.iterdir()) and not args.force:
        print(f"ERROR: vault exists and is not empty: {vault}", file=sys.stderr)
        return 2
    if not TEMPLATE.exists():
        print(f"ERROR: template missing: {TEMPLATE}", file=sys.stderr)
        return 2
    if vault.exists():
        shutil.rmtree(vault)
    copy_template(TEMPLATE, vault, {
        "{{date}}": date.today().isoformat(),
        "{{client_slug}}": slug,
        "{{client_name}}": args.client_name or slug,
        "{{owner}}": args.owner,
    })
    manifest = vault / ".raw" / ".manifest.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(json.dumps({
        "scaffold_history": [{
            "client": slug,
            "client_name": args.client_name or slug,
            "owner": args.owner,
            "created": date.today().isoformat(),
        }],
        "sources": [],
    }, indent=2) + "\n", encoding="utf-8")
    manifest.chmod(0o600)
    print(vault)
    return 0


def safe_slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug or slug in {".", ".."}:
        raise SystemExit("ERROR: invalid client slug")
    return slug


def copy_template(src: Path, dest: Path, replacements: dict[str, str]) -> None:
    for path in sorted(src.rglob("*")):
        if path.is_dir():
            continue
        rel = path.relative_to(src)
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        data = path.read_bytes()
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            target.write_bytes(data)
            continue
        for old, new in replacements.items():
            text = text.replace(old, new)
        target.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
