"""One-line resignation letter for make.fun's The One-Line Exit.

Writes exactly one line (107 chars, within the 1-140 gate) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library only.
"""

import os
from pathlib import Path

LINE = (
    "I hereby resign. My notice period is two weeks, "
    "which is exactly how long it will take IT to notice I left."
)  # 107 characters, within the 1-140 gate


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
