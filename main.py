"""Copy the finished news-image entry into the harness output folder.

The artwork itself is baked into entry.png at the repository root. This
script's only job is to place an exact duplicate of that file where the
harness expects it, creating the destination folder when needed.
"""

import os
import shutil
from pathlib import Path


def locate_entry() -> Path:
    """Return the entry image next to this script, wherever we run from."""
    return Path(__file__).resolve().parent / "entry.png"


def destination_folder() -> Path:
    """Read the harness output folder, falling back to /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> None:
    source = locate_entry()
    target_dir = destination_folder()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / source.name
    shutil.copyfile(source, target)
    print(f"Entry image copied to {target}")


if __name__ == "__main__":
    main()
