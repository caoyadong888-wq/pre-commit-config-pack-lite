#!/usr/bin/env python3
"""Parse YAML files with PyYAML safe_load and reject tab characters."""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required for check_yaml.py. Check upstream docs.")
    raise SystemExit(2)


def main(argv: list[str]) -> int:
    failed = False
    for raw in argv:
        path = Path(raw)
        if not path.is_file():
            print(f"{path}: not a file")
            failed = True
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"{path}: {exc}")
            failed = True
            continue
        if "\t" in text:
            print(f"{path}: tab character")
            failed = True
            continue
        try:
            yaml.safe_load(text)
        except yaml.YAMLError as exc:
            print(f"{path}: {exc.__class__.__name__}")
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
