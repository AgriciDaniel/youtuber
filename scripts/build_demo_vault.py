#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
PY = sys.executable


def run(args: list[str]) -> None:
    subprocess.run([PY, *args], cwd=REPO, check=True)


def main() -> int:
    demo_parent = REPO / "examples"
    demo = demo_parent / "sample-vault"
    if demo.exists():
        shutil.rmtree(demo)
    run(["scripts/scaffold_vault.py", "--client", "sample-vault", "--client-name", "Sample Client", "--owner", "Sample Owner", "--out-dir", str(demo_parent)])
    run(["scripts/ingest_source.py", "--vault", str(demo), "--file", "tests/fixtures/sample-source.md", "--source-type", "fixture"])
    run(["scripts/synthesize_brain.py", "--vault", str(demo)])
    run(["scripts/generate_vault_visuals.py", "--vault", str(demo)])
    run(["scripts/render_brain_report.py", "--vault", str(demo), "--html-only"])
    run(["scripts/lint_vault.py", "--vault", str(demo)])
    print(demo)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
