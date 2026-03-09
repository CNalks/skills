from __future__ import annotations

import argparse
import collections
import hashlib
import os
from pathlib import Path


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def collect_files(paths: list[Path], min_size: int) -> list[Path]:
    items: list[Path] = []
    for root in paths:
        if not root.exists():
            continue
        for current_root, _, files in os.walk(root, onerror=lambda _: None):
            for filename in files:
                candidate = Path(current_root) / filename
                try:
                    if candidate.stat().st_size >= min_size:
                        items.append(candidate)
                except OSError:
                    continue
    return items


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find duplicate file candidates by grouping same-size files and hashing only collisions."
    )
    parser.add_argument("paths", nargs="+", help="Paths to scan.")
    parser.add_argument("--min-size", type=int, default=1, help="Minimum file size in bytes.")
    args = parser.parse_args()

    scan_roots = [Path(path) for path in args.paths]
    files = collect_files(scan_roots, args.min_size)

    by_size: dict[int, list[Path]] = collections.defaultdict(list)
    for file_path in files:
        try:
            by_size[file_path.stat().st_size].append(file_path)
        except OSError:
            continue

    print("group_id\tsize_bytes\tsha256\tpath")
    group_id = 1
    for size_bytes, members in sorted(by_size.items(), key=lambda item: (-len(item[1]), item[0])):
        if len(members) < 2:
            continue
        by_hash: dict[str, list[Path]] = collections.defaultdict(list)
        for member in members:
            try:
                by_hash[sha256_file(member)].append(member)
            except OSError:
                continue
        for digest, digest_members in by_hash.items():
            if len(digest_members) < 2:
                continue
            for duplicate in sorted(digest_members):
                print(f"{group_id}\t{size_bytes}\t{digest}\t{duplicate}")
            group_id += 1


if __name__ == "__main__":
    main()
