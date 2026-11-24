#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

Writes the final text message a dying phone sends at one percent
battery, to /output/entry.txt. The line is fixed and deterministic:
the same 137-character line on every run.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only white space. The program validates the line
before writing and exits non-zero if it ever violates the gate,
so a bad line can never ship silently.
"""

import os
import sys

# The entry line itself: a fixed, deterministic message. The three
# fragments concatenate into exactly 137 characters — a final text
# from a phone that watched its owner as much as its owner watched it.
# Keep this literal unchanged: the gate validates it on every run.
LINE = (
    "You spent 11 hours a day staring at me. "
    "I spent 11 hours a day staring back. "
    "At 1%, I die knowing your face better than your mother does."
)


OUTPUT_FILENAME = "entry.txt"


def check_line(line: str) -> None:
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)


def main() -> None:
    check_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
