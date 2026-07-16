#!/usr/bin/env python3
"""Build a deterministic, privacy-safe ZIP of the installed skill."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_skill import validate  # noqa: E402


EXCLUDED_PARTS = {
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    ".git",
    ".venv",
    "private",
    "raw",
    "checkpoints",
}
EXCLUDED_SUFFIXES = {".pyc", ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".zip", ".pcap", ".pcapng", ".pt", ".pth", ".ckpt"}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _files(root: Path):
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise RuntimeError(f"Refusing to package symlink: {path}")
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if any(part in EXCLUDED_PARTS or part.endswith(".egg-info") for part in relative.parts):
            continue
        if path.suffix.lower() in EXCLUDED_SUFFIXES or path.name == ".DS_Store":
            continue
        yield path, relative


def build(root: Path, output_dir: Path) -> tuple[Path, Path, int]:
    errors, _, _ = validate(root, run_smoke=True)
    if errors:
        raise RuntimeError("Skill validation failed:\n" + "\n".join(errors))

    manifest = json.loads((root / "references/project_manifest.json").read_text(encoding="utf-8"))
    version = manifest.get("version", "0.0.0")
    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / f"luxing-ieee-transactions-skill-v{version}.zip"
    prefix = str(manifest.get("name") or root.name)
    count = 0
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for path, relative in _files(root):
            info = zipfile.ZipInfo(f"{prefix}/{relative.as_posix()}", date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, path.read_bytes(), compresslevel=9)
            count += 1

    checksum = output_dir / f"{archive.name}.sha256"
    checksum.write_text(f"{_sha256(archive)}  {archive.name}\n", encoding="utf-8")
    return archive, checksum, count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    try:
        archive, checksum, count = build(args.root.resolve(), args.output_dir.resolve())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps({"archive": str(archive), "checksum": str(checksum), "files": count}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
