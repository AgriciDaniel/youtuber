#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 420" role="img" aria-labelledby="title desc">
<title id="title">YouTube Brain relationship map</title>
<desc id="desc">Source to memory to deliverable operating map.</desc>
<rect width="980" height="420" fill="#f8fafc"/>
<text x="40" y="58" font-size="28" font-family="Inter,Arial" font-weight="700" fill="#172033">YouTube Brain Relationship Map</text>
<g font-family="Inter,Arial" font-size="14" font-weight="700">
<rect x="50" y="130" width="160" height="72" rx="8" fill="#fff" stroke="#586f92" stroke-width="3"/><text x="82" y="172" fill="#172033">Raw Sources</text>
<rect x="290" y="130" width="160" height="72" rx="8" fill="#fff" stroke="#2f7f87" stroke-width="3"/><text x="324" y="172" fill="#172033">Wiki Memory</text>
<rect x="530" y="130" width="160" height="72" rx="8" fill="#fff" stroke="#c85f4d" stroke-width="3"/><text x="560" y="172" fill="#172033">Checks + Gates</text>
<rect x="770" y="130" width="160" height="72" rx="8" fill="#fff" stroke="#f0b33d" stroke-width="3"/><text x="800" y="172" fill="#172033">Deliverables</text>
</g>
<path d="M210 166 H290 M450 166 H530 M690 166 H770" stroke="#64748b" stroke-width="3"/>
</svg>
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate vault visual assets.")
    parser.add_argument("--vault", required=True)
    args = parser.parse_args(argv)
    vault = Path(args.vault).expanduser().resolve()
    out = vault / "_attachments" / "brain-relationship-map.svg"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(SVG, encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
