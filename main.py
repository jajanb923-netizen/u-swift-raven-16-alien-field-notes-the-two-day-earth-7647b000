#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review -- entry program.

Writes one original line of plain text (at most 200 characters), a review
of planet Earth left by an alien tourist, to /output/entry.txt.

Python 3.13 stdlib only. Deterministic. No network. No randomness.
"""
import os
import sys

# The review, in three beats: the rating, the incident, the verdict.
# One clean joke: an alien tries the most human complaint ritual
# ("speak to the manager") and Earth answers with a dog.
REVIEW_PARTS = [
    "One star.",
    "I asked for the manager and a golden retriever licked my face.",
    "Earth has no customer service, only dogs.",
]


def build_entry() -> str:
    """Assemble the single review line from its beats."""
    return " ".join(REVIEW_PARTS)


def check_gate(text: str) -> list[str]:
    """Collect every gate failure; an empty list means the entry is valid."""
    failures = []
    if not 1 <= len(text) <= 200:
        failures.append(f"entry is {len(text)} chars, must be 1-200")
    if not text.strip():
        failures.append("entry is blank or only whitespace")
    if text != text.strip():
        failures.append("entry has surrounding whitespace")
    if "\n" in text or "\r" in text:
        failures.append("entry must be a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        failures.append("entry is not valid UTF-8 text")
    return failures


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = build_entry()
    failures = check_gate(text)
    if failures:
        for failure in failures:
            print(f"gate: {failure}", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
