#!/usr/bin/env python3
"""Report a missing final newline on non-empty files.

The upstream end-of-file-fixer hook rewrites files. This local hook only
reports. Check upstream docs before you swap in a remote hook.
"""

from __future__ import annotations

import sys
from pathlib import Path


def main(argv: list[str]) -> int:
    failed = False
    for raw in argv:
        path = Path(raw)
        if not path.is_file():
            print(f"{path}: not a file")
            failed = True
            continue
        data = path.read_bytes()
        if b"\0" in data or data == b"":
            continue
        if not data.endswith(b"\n"):
            print(f"{path}: missing newline at end of file")
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
