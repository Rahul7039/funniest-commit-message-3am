#!/usr/bin/env python3
"""3 AM Hotfix: The Funniest Commit Message.

Writes one commit message to /output/entry.txt. The line is validated
against the competition gate before it is written: UTF-8 text, 1 to 179
characters, and not only white space.
"""

import os
import sys

ENTRY = "Revert the Friday deploy: prod died at 3 AM and the pager has filed for divorce"

MAX_CHARS = 179


def main() -> int:
    text = ENTRY
    if not text or not text.strip():
        print("error: entry is blank", file=sys.stderr)
        return 1
    # The competition is one line: reject any embedded newline outright.
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if text != text.strip():
        print("error: entry has leading or trailing white space", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"error: entry is {len(text)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    # Must be valid UTF-8 text; the gate counts characters, not bytes.
    text.encode("utf-8")

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
