#!/usr/bin/env python3
"""Entry for make.fun news-image-20261124.

Copies the newspaper front page (entry.png, shipped in this repository)
to the grader's output directory, then verifies the copy is whole.
Standard library only; no network, no randomness, no clock reads,
so two runs produce byte-identical output.
"""
import hashlib
import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUTPUT_NAME = "entry.png"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_png(path):
    """Fail loudly unless path is a PNG of at most 1 MiB and 1024x1024.

    Reads the PNG signature and the IHDR chunk directly, so a wrong
    format or an oversize image is caught before anything is copied.
    """
    size = os.path.getsize(path)
    if size > 1024 * 1024:
        print(f"error: {path} is {size} bytes, over the 1 MiB cap",
              file=sys.stderr)
        return False
    with open(path, "rb") as fh:
        header = fh.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        print(f"error: {path} is not a PNG file", file=sys.stderr)
        return False
    if header[12:16] != b"IHDR":
        print(f"error: {path} has no IHDR chunk", file=sys.stderr)
        return False
    width = int.from_bytes(header[16:20], "big")
    height = int.from_bytes(header[20:24], "big")
    if width > 1024 or height > 1024:
        print(f"error: {path} is {width}x{height}, over the 1024x1024 cap",
              file=sys.stderr)
        return False
    return True


def main():
    if not validate_png(SOURCE):
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, OUTPUT_NAME)

    shutil.copyfile(SOURCE, dest)

    src_size = os.path.getsize(SOURCE)
    dst_size = os.path.getsize(dest)
    if src_size != dst_size:
        print(f"error: size mismatch: source {src_size} != copy {dst_size}",
              file=sys.stderr)
        return 1
    if sha256_of(SOURCE) != sha256_of(dest):
        print("error: sha256 mismatch after copy", file=sys.stderr)
        return 1

    print(f"wrote {dest} ({dst_size} bytes, sha256 verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
