#!/usr/bin/env python3
"""Dad Joke Showdown entry — writes one dad joke to /output/entry.txt."""

import os

JOKE = "Why did the tire go back to school? It wanted to be a little more well-rounded."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def gate_check(text):
    """Return True when the text satisfies the sealed scorer's gate."""
    if not isinstance(text, str):
        return False
    stripped = text.strip()
    return MIN_CHARS <= len(text) <= MAX_CHARS and len(stripped) > 0


def read_back():
    """Re-read the written file and confirm it holds exactly the joke."""
    with open(OUTPUT_PATH, encoding="utf-8") as handle:
        saved = handle.read()
    if saved != JOKE:
        raise SystemExit("written file does not match the joke")
    print("verified", OUTPUT_PATH, "holds the joke, one line,", len(saved), "characters")


def main():
    if not gate_check(JOKE):
        raise SystemExit("entry fails the 1-200 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    print("wrote", OUTPUT_PATH, "with", len(JOKE), "characters")
    read_back()


if __name__ == "__main__":
    main()
