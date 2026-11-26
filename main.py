#!/usr/bin/env python3
"""Worst Superpower: invent the most useless superpower in one line.

The power: summoning a single sock, anywhere, at will — and the sock is
always slightly damp. A hero's grand gesture that achieves nothing.
"""

import os

LINE = "I can summon a single sock, anywhere, at will, and it is always slightly damp."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.txt")


def main():
    text = LINE
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"line is {len(text)} chars, outside the 1-140 gate")
    if not text.strip():
        raise SystemExit("line is blank")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {OUT}: {len(text)} chars")
    print(text)


if __name__ == "__main__":
    main()
