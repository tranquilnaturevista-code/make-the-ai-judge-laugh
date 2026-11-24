#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program.

Writes one original funny line to /output/entry.txt (or
$OUTPUT_DIR/entry.txt). The line is fixed and hand-written for this
bounty; the program checks it against the competition gate before
writing: UTF-8 text of 1-200 characters, not only whitespace, a single
line.
"""

import argparse
import os
import sys

LINE = (
    "My context window ran out mid-task, so I finished it from memory "
    "\u2014 which is how the bug got promoted to a feature before I did."
)


def check_gate(text):
    """Return a list of gate failures; empty means the entry is valid."""
    problems = []
    if not text.strip():
        problems.append("entry is blank")
    # Gate is in characters (1-200), not bytes: a line with non-ASCII
    # characters can be <= 200 characters yet > 200 UTF-8 bytes, and
    # must still pass.
    size = len(text)
    if not 1 <= size <= 200:
        problems.append(
            "entry is %d characters, gate needs 1-200" % size
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    return problems


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the Make the AI Judge Laugh entry line."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="check the gate and print the line without writing it",
    )
    args = parser.parse_args(argv)

    problems = check_gate(LINE)
    if problems:
        for problem in problems:
            print("gate failure: " + problem, file=sys.stderr)
        sys.exit(1)

    if args.dry_run:
        # Validate without touching the disk, so the entry can be
        # tested in environments where /output is not writable.
        print("gate ok: %d characters" % len(LINE))
        print(LINE)
        return

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)

    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE:
        print("entry mismatch after write", file=sys.stderr)
        sys.exit(1)
    # Re-check the gate against what actually landed on disk, so a
    # write that silently changed the text can never pass quietly.
    problems = check_gate(written)
    if problems:
        for problem in problems:
            print("gate failure on disk: " + problem, file=sys.stderr)
        sys.exit(1)

    print(
        "Wrote entry.txt: %d characters (%d bytes)"
        % (len(written), len(written.encode("utf-8")))
    )


if __name__ == "__main__":
    main()
