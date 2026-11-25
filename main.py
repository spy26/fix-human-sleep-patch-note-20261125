#!/usr/bin/env python3
"""Write one patch-note line about human sleep to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: stdlib only, no randomness, no clock, no network.
"""

import os
import sys

PATCH_NOTE = "Fixed: humans now fall asleep within 8 minutes instead of replaying every embarrassing thing they have ever said."
# Gate: 1-160 characters, one line, no trailing newline. This line is 113
# characters, so it passes with room to spare.


def main() -> None:
    if not PATCH_NOTE or len(PATCH_NOTE) > 160:
        print("error: entry patch note must be non-empty and at most 160 characters", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PATCH_NOTE)


if __name__ == "__main__":
    main()
