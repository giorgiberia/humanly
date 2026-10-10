#!/usr/bin/env python3
"""Check Humanly HUMANLY.md declaration text, not product compliance.

Usage: python check_declaration.py [repo-directory] [--strict]
Exit codes: 0 valid, 1 invalid/incomplete, 2 missing HUMANLY.md.
"""

import argparse
from datetime import date
from pathlib import Path
import re

LEVELS = {"unassessed": -1, "H0": 0, "H1": 1, "H2": 2, "H3": 3}
REQUIRED = {"H1": 2, "H2": 3, "H3": 3}


def check(root: Path, strict: bool = False) -> int:
    target = root / "HUMANLY.md"
    if not target.is_file():
        print(f"ERROR: HUMANLY.md not found in {root}")
        return 2

    content = target.read_text(encoding="utf-8")
    found = re.search(r"```(?:yaml|yml)\s*\n(.*?)\n```", content, re.I | re.S)
    if not found:
        print("ERROR: HUMANLY.md must contain a fenced YAML declaration. See assets/HUMANLY-template.md.")
        return 1
    yaml_text = found.group(1)
    errors, warnings = [], []

    if not re.search(r"^humanly:\s*$", yaml_text, re.M):
        errors.append("Missing `humanly:` YAML root key")

    def scalar(key: str):
        match = re.search(r"^\s{2,}" + re.escape(key) + r":\s*(.*?)\s*(?:#.*)?$", yaml_text, re.M)
        return match.group(1).strip().strip("\"'") if match else None

    version, level = scalar("version"), scalar("level")
    scope, reviewed = scalar("scope"), scalar("reviewed")
    if version != "0.3-draft":
        warnings.append(f"Version {version!r} differs from 0.3-draft; review against the project's declared version")
    if level not in LEVELS:
        errors.append(f"Unknown level {level!r}; use unassessed, H0, H1, H2 or H3")
    if not scope or "[" in scope:
        warnings.append("Scope is missing or a placeholder")
    if not reviewed or "[" in reviewed:
        warnings.append("Reviewed date is missing or a placeholder")
    else:
        try:
            date.fromisoformat(reviewed)
        except ValueError:
            errors.append("Reviewed date must be YYYY-MM-DD")

    checks = {"H1": 0, "H2": 0, "H3": 0}
    for line in content.splitlines():
        match = re.match(r"\s*- \[([ xX])\].*\((H[123])\)\s*$", line)
        if match and match.group(1).lower() == "x":
            checks[match.group(2)] += 1

    if level in LEVELS and LEVELS[level] >= 1:
        for category, needed in REQUIRED.items():
            if LEVELS[category] <= LEVELS[level] and checks[category] < needed:
                errors.append(f"{level} needs {needed} checked {category} items; found {checks[category]}")

    if level == "unassessed":
        warnings.append("Level is unassessed (correct for an unverified template)")
    if any(marker in content for marker in ["[Link", "[Describe", "[Product", "[YYYY", "[Team", "[How", "[Where", "[Explain", "[Keyboard", "[UI", "[URLs", "[Team or", "[Location", "[Process", "[State"]):
        warnings.append("Template placeholders remain; replace before publishing")

    print(f"Humanly text check: version={version or 'missing'} level={level or 'missing'}")
    for error in errors:
        print("ERROR:", error)
    for warning in warnings:
        print("WARN:", warning)
    print("NOTE: Static text checks cannot validate accessibility, functionality, authorization, or certification.")
    return 1 if errors or (strict and warnings) else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--strict", action="store_true", help="Fail on placeholders, missing fields and unassessed level")
    args = parser.parse_args()
    return check(Path(args.repo).resolve(), strict=args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
