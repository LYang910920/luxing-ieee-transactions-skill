#!/usr/bin/env python3
"""Dependency-free entry point for the bundled IEEE research utilities."""

from __future__ import annotations

from pathlib import Path
import sys


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from luxing_ieee_skill.cli import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
