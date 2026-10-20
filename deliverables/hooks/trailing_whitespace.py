#!/usr/bin/env python3
"""Report trailing spaces or tabs. This hook checks. It does not rewrite.

The upstream trailing-whitespace hook can rewrite files. This local hook
only reports. Check upstream docs before you swap in a remote hook.
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
        if b"\0" in data:
            continue
        text = data.decode("utf-8", errors="replace")
        for number, line in enumerate(text.splitlines(keepends=True), start=1):
            body = line[:-1] if line.endswith("\n") else line
            if body.endswith("\r"):
                body = body[:-1]
            if body.rstrip(" \t") != body:
                print(f"{path}:{number}: trailing whitespace")
                failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
