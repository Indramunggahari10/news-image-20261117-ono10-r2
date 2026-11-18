#!/usr/bin/env python3
"""news-image-20261117: copy the bundled entry.png to the output dir.

Stdlib only. Deterministic: the output is a byte-for-byte copy of
entry.png sitting next to this script, so repeated runs are identical.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    nbytes = os.path.getsize(dst)
    print(f"wrote {dst}: {nbytes} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
