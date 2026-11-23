#!/usr/bin/env python3
"""Entry program for news-image-20261123.

The page is pre-rendered by render.py (PIL, run at build time) into
entry.png at the repository root. This program only copies that image to
the grader's output directory, so both grader runs produce identical
bytes. Standard library only — nothing is installed.
"""
import os
import shutil


# The copy is byte-for-byte, so the two grader runs see the same image.
def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    print("copied entry.png to %s" % out_dir)


if __name__ == "__main__":
    main()
