"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text -- a review of planet Earth
left by an alien tourist -- to /output/entry.txt.

Pure Python standard library, deterministic: every run writes the
same bytes.
"""

import os

ENTRY = "The locals put a flag on their moon, took a photo, and left. No gift shop, no queue, no return visit in fifty years. Two stars for follow-through."


def main() -> None:
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space. Refuse to write
    # anything that would fail it.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
