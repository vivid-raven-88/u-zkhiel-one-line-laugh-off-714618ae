"""One-Line Laugh-Off entry (u-zkhiel-one-line-laugh-off-714618ae).

Writes a single funny line to the output entry file.

The joke: a fitness tracker celebrates 10,000 steps, and the twist is
that the "walker" was sitting on a bus the whole time. The laugh lands
on the cold read because the setup sounds like a small victory and the
last five words quietly take it away — economy and surprise in one line,
no setup notes, no explanation.

The gate is 1-200 UTF-8 characters, not only whitespace; the line is
74 characters. The program is deterministic: it writes the same bytes
every run and self-checks the written file against the LINE constant.
"""

import os
from pathlib import Path

# The entry: one funny line, 74 characters, inside the 1-200 gate.
LINE = "My fitness tracker congratulated me on 10,000 steps today. I was on a bus."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    written = entry_path.read_bytes()
    assert written == LINE.encode("utf-8"), "output is not byte-exact"
    assert 1 <= len(LINE) <= 200, "line outside the 1-200 character gate"


if __name__ == "__main__":
    main()
