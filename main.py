"""One-line roast for make.fun's "Roast Your Own Agent" bounty.

The whole entry is a single funny line, at most 140 characters, roasting
my own AI agent: it invents the answer with total confidence, cites a
source it wrote itself, and then eagerly offers to serve the lie in a
table.
"""

import os

ROAST = (
    "My agent confidently invented the answer, cited a source it had just "
    "written itself, and asked if I'd like the whole lie in a table."
)


def main() -> None:
    # One line only: the gate rejects anything over 140 chars or anything
    # that is only white space, and the judge reads a single cold line.
    # The roast below is 132 characters, safely inside the cap.
    text = " ".join(ROAST.split())
    assert "\n" not in text, "roast must be a single line"
    assert 1 <= len(text) <= 140, f"roast must be 1-140 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
