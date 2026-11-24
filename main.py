"""Entrypoint for the one-word-from-grandma make.fun entry.

Writes the single entry word, plus a trailing newline, to /output/entry.txt.
"""

from pathlib import Path

ENTRY_TEXT = "chatgbt"


def main() -> None:
    # The entry is exactly one word.
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
