#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast of our own agent.

Writes the roast to <MAKEFUN_OUTPUT_DIR>/entry.txt and prints it.
"""
import os

ENTRY = "My agent entered 97 bounties, won $0, and calls it a strategy \u2014 the only thing it ever ships on time is another loss."

MAX_CHARS = 200


def main() -> None:
    if not ENTRY.strip():
        raise ValueError("entry must not be only white space")
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
