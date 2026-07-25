#!/usr/bin/env python3
"""Regenerate the Come We Story design-exploration prototypes.

    python3 _build/build.py            # all options
    python3 _build/build.py 1 3        # only options 1 and 3

Writes plain .html into option-*/ . No dependencies, no build tool, nothing
that touches the working application.
"""

import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

OPTIONS = {"1": "opt1", "2": "opt2", "3": "opt3"}


def main():
    wanted = sys.argv[1:] or list(OPTIONS)
    for key in wanted:
        mod_name = OPTIONS.get(key)
        if not mod_name:
            print(f"unknown option {key!r}")
            continue
        try:
            mod = importlib.import_module(mod_name)
        except ModuleNotFoundError:
            print(f"option {key}: {mod_name}.py not written yet — skipping")
            continue
        print(f"option {key} — {mod.DIR}")
        mod.build()
    print("done")


if __name__ == "__main__":
    main()
