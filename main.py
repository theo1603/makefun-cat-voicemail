#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun bounty
u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443

Writes one voicemail greeting, recorded by a cat, to /output/entry.txt.
Deterministic, standard library only, no network.
"""

import os

ENTRY = "Hi, it's Miso. I'm asleep in the box you threw away. Leave a message after the beep. I'll knock it off a shelf at 4am."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
