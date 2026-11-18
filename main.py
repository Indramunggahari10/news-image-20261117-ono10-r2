#!/usr/bin/env python3
"""news-image-20261117 entry: write the composed front page to the output dir.

Stdlib only. Deterministic: copies the bundled entry.png byte-for-byte,
so repeated runs produce identical output.
"""
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_NAME = "entry.png"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    if not SOURCE.is_file():
        print(f"missing bundled image: {SOURCE}", file=sys.stderr)
        return 1
    dest = out_dir / OUTPUT_NAME
    shutil.copyfile(SOURCE, dest)
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
