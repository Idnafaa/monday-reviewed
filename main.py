#!/usr/bin/env python3
"""Monday, Reviewed in One Line — review writer.

Writes a single original one-line review of my own Monday
(120 characters, no title, no explanation) to /output/entry.txt.
"""
import os

MAX_CHARS = 200

REVIEW = (
    "One star: Monday woke me at 5 a.m. to announce my weekend had been "
    "cancelled due to a scheduling conflict \u2014 with Monday."
)

def main():
    text = REVIEW.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"review is {len(text)} characters, must be 1-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("review must be exactly one line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")

if __name__ == "__main__":
    main()
