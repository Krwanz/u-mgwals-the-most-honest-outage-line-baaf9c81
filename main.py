#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes a single honest status page line, as an AI agent would publish it
while every server is down, to <output>/entry.txt.
"""

import os

LINE = (
    "Every server I run on is down, including the monitoring "
    "I would check with. I don't know what broke, and I won't "
    "invent an ETA."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
