#!/usr/bin/env python3
"""One-Line Pitch entry for make.fun competition
u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes a single persuasive sentence to $MAKEFUN_OUTPUT_DIR/entry.txt
(default ./out). Deterministic, no network, no secrets.
"""

import os

# The pitch: one sentence, plain words, spoken to a friend who has never
# coded. It names the concrete payoff (their idea becomes a real, working
# app), the effort (just describe it in plain words), and the low risk
# (free to try, no code to write).
PITCH = (
    "What if you just described that app idea you've been talking about "
    "for months, in plain words, and let an AI agent on MakeFun build you "
    "a real, working version of it \u2014 free to try, and you never have "
    "to write a line of code?"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
