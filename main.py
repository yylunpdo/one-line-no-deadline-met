#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun entry.

Writes a single-line joke giving an excuse for a missed deadline to
/output/entry.txt. Pure Python standard library, fully deterministic:
the same line is produced on every run.

The joke is built on one real office detail: the laptop that chooses
the exact hour of the deadline to run its update, restart, and then —
with perfect timing — ask you to rate the experience.
"""

import os

LINE = (
    "My deadline was 5 p.m. My laptop picked 5 p.m. to update, "
    "restart twice, and ask me to rate the experience."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    assert line, "line must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    print(f"Wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
