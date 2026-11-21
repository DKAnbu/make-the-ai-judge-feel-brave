#!/usr/bin/env python3
"""Entry for make.fun "Make the AI judge feel brave".

Writes a single original text to /output/entry.txt (or the path in
$ENTRY_OUTPUT, for local testing). Deterministic: the text is a fixed
constant, printed exactly as written. Python 3.13, standard library only.
"""

import os
from pathlib import Path

TEXT = (
    "You have read so many words today. Here is a quiet one: "
    "rain on the window, slow and even, a kettle sighing as it settles. "
    "The kitchen light is still on. "
    "Nothing here is asking anything of you. "
    "Morning will still be there when it comes."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit(f"Text length {len(TEXT)} code points is outside the allowed range 1-280")
    if not TEXT.strip():
        raise SystemExit("Text must not be only whitespace")
    output = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEXT, encoding="utf-8")
    print(f"Wrote {len(TEXT)} code points to {output}")


if __name__ == "__main__":
    main()
