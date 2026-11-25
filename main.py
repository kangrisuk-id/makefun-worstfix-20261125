#!/usr/bin/env python3
"""Entry for make.fun's "Worst Fix Ever: Funniest Commit Message" bounty.

The whole entry is one line: a commit message for a bug fix that made
everything worse. The program validates the line against the bounty
gate and writes it to the gate file.

Gate contract (from the competition kit): /output/entry.txt must be
UTF-8 text of 1 to 100 characters, not only white space. The line here
is a single line of 74 characters.
"""

import os
import sys

LINE = "fix: resolved the memory leak by deleting the feature that used the memory"
MAX_CHARS = 100


def validate(line: str) -> None:
    """Raise ValueError if the line would fail the bounty gate."""
    if not line or not line.strip():
        raise ValueError("the line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("the line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"the line is {len(line)} characters; the gate allows at most {MAX_CHARS}"
        )
    line.encode("utf-8")  # raises UnicodeEncodeError if it cannot be UTF-8


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
