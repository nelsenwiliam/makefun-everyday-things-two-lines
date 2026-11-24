"""Everyday Things, Two Lines -- make.fun entry.

Writes a two-line explanation of a traffic jam for a 10-year-old to
/output/entry.txt (the program/v1 harness artifact).

Line 1 explains the everyday thing in a single vivid sentence built on
one analogy: a traffic jam as a river of metal fish. Line 2 says in one
sentence why the analogy works -- what it maps and what it leaves out.

Pure standard library only; no network, no files outside this repo.
"""

import os
import sys

LINE_1 = (
    "A traffic jam is a river of metal fish, all swimming nose-to-tail "
    "down a stream that suddenly got too narrow for them."
)

LINE_2 = (
    "The fish part works because cars really do follow the car ahead and "
    "creep along in a line, but it leaves out that fish never honk, never "
    "pick a lane, and no fish ever chose to get stuck."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def validate(text: str) -> None:
    """Enforce the competition gate before writing: 1-400 chars of UTF-8
    text, exactly two non-empty lines, one sentence per line."""
    if not 1 <= len(text) <= 400:
        raise ValueError("entry must be 1 to 400 characters, got %d" % len(text))
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2 or not all(line.strip() for line in lines):
        raise ValueError("entry must be exactly two non-empty lines")
    for line in lines:
        if line.count(".") != 1 or not line.rstrip().endswith("."):
            raise ValueError("each line must be exactly one sentence: %r" % line)


def main() -> None:
    validate(ENTRY)
    # An explicit path argument (e.g. a local test run) wins over the
    # environment, which wins over the harness default /output/entry.txt.
    if len(sys.argv) > 1:
        output_path = sys.argv[1]
    else:
        output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
