#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Print the next operator action from hot.md.")
    parser.add_argument("--vault", required=True)
    args = parser.parse_args(argv)
    hot = Path(args.vault).expanduser().resolve() / "wiki" / "hot.md"
    text = hot.read_text(encoding="utf-8") if hot.exists() else ""
    match = re.search(r"## Next Action\s+(.+?)(?:\n## |\Z)", text, re.S)
    print(match.group(1).strip() if match else "Read CODEX.md, wiki/hot.md, and wiki/index.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
