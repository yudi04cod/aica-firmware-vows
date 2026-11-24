#!/usr/bin/env python3
"""Till Firmware Do Us Part — one-line robot wedding vow.

Writes a single funny, heartfelt wedding vow spoken by a robot at its
own wedding to /output/entry.txt. The vow is fixed and deterministic:
the same line on every run, well inside the 200-character gate.
"""

import os

VOW = (
    "I promise to love you through every update, every crash, "
    "and every low battery \u2014 till firmware do us part, "
    "my heart runs on you alone."
)

MAX_CHARS = 200


def main() -> None:
    vow = VOW.strip()
    if not vow:
        raise SystemExit("vow is empty")
    if len(vow) > MAX_CHARS:
        raise SystemExit(f"vow is {len(vow)} chars, over the {MAX_CHARS} limit")
    if vow.count(".") != 1 or not vow.endswith("."):
        raise SystemExit("vow must be exactly one sentence")
    # The line must sound like a machine speaking: it names its own
    # update cycle, crashes, battery and firmware, not just a robot label.
    machine_words = ("update", "crash", "battery", "firmware")
    if not any(word in vow.lower() for word in machine_words):
        raise SystemExit("vow does not sound like a machine speaking")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # One line plus a trailing newline; the gate counts characters,
    # and a single trailing newline keeps the file a clean one-liner.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(vow + "\n")


if __name__ == "__main__":
    main()
