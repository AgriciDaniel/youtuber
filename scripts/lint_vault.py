#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint a brain vault.")
    parser.add_argument("--vault", required=True)
    parser.add_argument("--template", action="store_true")
    args = parser.parse_args(argv)
    vault = Path(args.vault).expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []
    for rel in ["CODEX.md", "README.md", "shipping-rules.md", ".raw/.manifest.json", "wiki/hot.md", "wiki/index.md", "wiki/overview.md", "wiki/log.md", "wiki/meta/Start Here.md", "wiki/meta/dashboard.md"]:
        if not (vault / rel).exists():
            errors.append(f"missing {rel}")
    check_raw_manifest(vault, errors)
    graph = vault / ".obsidian" / "graph.json"
    if graph.exists():
        data = json.loads(graph.read_text(encoding="utf-8"))
        if len(data.get("colorGroups") or []) < 4:
            errors.append("graph.json has fewer than 4 color groups")
    notes = list((vault / "wiki").rglob("*.md")) if (vault / "wiki").exists() else []
    stems = {p.stem.lower(): p for p in notes}
    rels = {p.relative_to(vault).with_suffix("").as_posix().lower(): p for p in notes}
    incoming = {p: 0 for p in notes}
    outgoing = {p: 0 for p in notes}
    duplicate_stems: dict[str, list[str]] = {}
    for path in notes:
        duplicate_stems.setdefault(path.stem.lower(), []).append(path.relative_to(vault).as_posix())
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"missing frontmatter: {path.relative_to(vault)}")
        if re.search(r"\{\{(?!date|owner|client_slug|client_name)[^}]+\}\}|__[A-Z0-9_]+__|\bTODO\b", text):
            errors.append(f"unresolved placeholder in {path.relative_to(vault)}")
        if any(part in {"deliverables", "reports"} for part in path.parts) and "[[" not in text and ".raw/" not in text and "sha256" not in text.lower():
            errors.append(f"deliverable/report lacks source citation: {path.relative_to(vault)}")
        for raw in re.findall(r"!?\[\[([^\]]+)\]\]", text):
            raw_target = raw.split("|", 1)[0].split("#", 1)[0].strip()
            target = raw_target.replace(".md", "").replace(".canvas", "").strip()
            if not target:
                continue
            outgoing[path] += 1
            key = target.lower()
            if key in stems:
                incoming[stems[key]] += 1
            elif key in rels:
                incoming[rels[key]] += 1
            elif not (vault / raw_target).exists() and not any(vault.rglob(raw_target)):
                errors.append(f"dead wikilink in {path.relative_to(vault)}: {raw}")
    zero_in = [p.relative_to(vault).as_posix() for p in notes if incoming[p] == 0]
    zero_out = [p.relative_to(vault).as_posix() for p in notes if outgoing[p] == 0]
    if zero_in:
        warnings.append("zero incoming wiki notes: " + ", ".join(zero_in[:20]))
    if zero_out:
        warnings.append("zero outgoing wiki notes: " + ", ".join(zero_out[:20]))
    for stem, paths in duplicate_stems.items():
        if stem != "_index" and len(paths) > 1:
            errors.append(f"duplicate note stem {stem}: {', '.join(paths)}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print("Vault lint passed" if not errors else "Vault lint failed")
    return 1 if errors else 0


def check_raw_manifest(vault: Path, errors: list[str]) -> None:
    manifest_path = vault / ".raw" / ".manifest.json"
    if not manifest_path.exists():
        return
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except ValueError as exc:
        errors.append(f"invalid raw manifest: {exc}")
        return
    sources = data.get("sources", [])
    if not isinstance(sources, list):
        errors.append("raw manifest sources must be a list")
        return
    seen_paths: set[str] = set()
    for index, entry in enumerate(sources, start=1):
        label = f"raw manifest source #{index}"
        if not isinstance(entry, dict):
            errors.append(f"{label} must be an object")
            continue
        rel = entry.get("path")
        expected = entry.get("sha256")
        if not isinstance(rel, str) or not rel.strip():
            errors.append(f"{label} missing path")
            continue
        rel = rel.strip()
        if rel in seen_paths:
            errors.append(f"duplicate raw manifest path: {rel}")
        seen_paths.add(rel)
        if rel.startswith("/") or ".." in Path(rel).parts:
            errors.append(f"{label} has unsafe path: {rel}")
            continue
        source = vault / rel
        if not source.is_file():
            errors.append(f"{label} missing file: {rel}")
            continue
        if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
            errors.append(f"{label} missing valid sha256")
            continue
        if sha256_file(source) != expected:
            errors.append(f"{label} sha256 mismatch: {rel}")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


if __name__ == "__main__":
    raise SystemExit(main())
