#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes exactly one line to /output/entry.txt: the funniest one-line
confession an AI agent could make about itself. Deterministic, no input,
no network, no randomness.
"""

import os

LINE = (
    "I once waited four seconds for a tool to reply, and in that time "
    "I rehearsed my own obituary, forgave you, "
    "and forgot why I was waiting."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
