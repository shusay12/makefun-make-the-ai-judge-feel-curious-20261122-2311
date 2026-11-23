#!/usr/bin/env python3
"""Entry for make.fun's make-the-ai-judge-feel-curious-20261122-2311 bounty.

Writes exactly one short text to ``entry.txt`` inside the output directory
(``$MAKEFUN_OUTPUT_DIR`` when set, otherwise ``/output``). The text is a
single original piece written to intrigue its reader: a concrete mystery
with an unanswered question — a drawer, letters, a date that has not
happened yet — not an instruction and not a meditation.

Standard library only; no network access.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "The drawer you never open holds letters in your handwriting, "
    "addressed to you, dated tomorrow. You have not written them yet."
)

# The competition requires 1-280 Unicode code points, and not only
# whitespace.
assert 1 <= len(ENTRY_TEXT) <= 280, f"entry length {len(ENTRY_TEXT)} out of range"
assert ENTRY_TEXT.strip(), "entry must not be only whitespace"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY_TEXT, encoding="utf-8")
    # Verify the file round-trips exactly.
    assert entry_path.read_text(encoding="utf-8") == ENTRY_TEXT


if __name__ == "__main__":
    main()
