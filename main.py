#!/usr/bin/env python3
"""Describe Your Ex in One Word — entry program (stdlib only).

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt, falling back
to ./output/entry.txt when the variable is unset. The word is the whole
entry: no punctuation tricks, no extra words, just the verdict.
"Subscription" fits because the relationship kept auto-renewing long
after anyone wanted it — a monthly charge for a service nobody uses,
impossible to cancel without three phone calls and a guilt trip.
"""

import os
from pathlib import Path

WORD = "Subscription"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(WORD + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
