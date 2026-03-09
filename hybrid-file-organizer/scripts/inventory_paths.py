from __future__ import annotations

import argparse
import collections
import os
from pathlib import Path


DEFAULT_WINDOWS_TARGETS = [
    Path.home() / "Desktop",
    Path.home() / "Downloads",
    Path.home() / "Documents",
    Path.home() / "Pictures",
    Path.home() / "Videos",
]


def summarize_path(path: Path) -> dict[str, object]:
    root_files = 0
    root_dirs = 0
    recursive_files = 0
    total_size = 0
    ext_counter: collections.Counter[str] = collections.Counter()

    try:
        for child in path.iterdir():
            try:
                if child.is_file():
                    root_files += 1
                elif child.is_dir():
                    root_dirs += 1
            except OSError:
                continue
    except OSError:
        pass

    for root, dirs, files in os.walk(path, onerror=lambda _: None):
        _ = dirs
        for filename in files:
            recursive_files += 1
            file_path = Path(root) / filename
            try:
                total_size += file_path.stat().st_size
            except OSError:
                pass
            ext = file_path.suffix.lower() or "<none>"
            ext_counter[ext] += 1

    top_ext = "; ".join(f"{ext}={count}" for ext, count in ext_counter.most_common(12))
    return {
        "path": str(path),
        "root_files": root_files,
        "root_dirs": root_dirs,
        "recursive_files": recursive_files,
        "size_gb": round(total_size / (1024**3), 3),
        "top_extensions": top_ext,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inventory candidate file-organization paths before content sampling."
    )
    parser.add_argument("paths", nargs="*", help="Paths to summarize. Defaults to common Windows user roots.")
    args = parser.parse_args()

    targets = [Path(p) for p in args.paths] if args.paths else DEFAULT_WINDOWS_TARGETS

    print("path\troot_files\troot_dirs\trecursive_files\tsize_gb\ttop_extensions")
    for target in targets:
        if not target.exists():
            continue
        row = summarize_path(target)
        print(
            f"{row['path']}\t{row['root_files']}\t{row['root_dirs']}\t"
            f"{row['recursive_files']}\t{row['size_gb']}\t{row['top_extensions']}"
        )


if __name__ == "__main__":
    main()
