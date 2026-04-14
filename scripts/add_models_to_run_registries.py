#!/usr/bin/env python3
"""Backfill phase model metadata into each run registry.

For each run folder in dikt/, this script reads README.md to extract:
- Phase 1 model
- Phase 2 model

Then it writes those values onto every entry in that folder's registry.json.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIKT_DIR = ROOT / "dikt"

PHASE1_RE = re.compile(r"###\s*Phase\s*1[\s\S]*?\|\s*Model\s*\|\s*(.*?)\s*\|", re.IGNORECASE)
PHASE2_RE = re.compile(r"###\s*Phase\s*2[\s\S]*?\|\s*Model\s*\|\s*(.*?)\s*\|", re.IGNORECASE)


def extract_models(readme_text: str) -> tuple[str, str]:
    phase1_match = PHASE1_RE.search(readme_text)
    phase2_match = PHASE2_RE.search(readme_text)

    if not phase1_match or not phase2_match:
        raise ValueError("Could not find both Phase 1 and Phase 2 model values in README.md")

    phase1_model = phase1_match.group(1).strip().strip("`")
    phase2_model = phase2_match.group(1).strip().strip("`")
    return phase1_model, phase2_model


def update_registry(registry_path: Path, phase1_model: str, phase2_model: str) -> int:
    with registry_path.open("r", encoding="utf-8") as f:
        registry = json.load(f)

    if not isinstance(registry, list):
        raise ValueError(f"Expected list in {registry_path}")

    changed = 0
    for entry in registry:
        if not isinstance(entry, dict):
            continue

        if entry.get("phase1Model") != phase1_model:
            entry["phase1Model"] = phase1_model
            changed += 1

        if entry.get("phase2Model") != phase2_model:
            entry["phase2Model"] = phase2_model
            changed += 1

    with registry_path.open("w", encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)
        f.write("\n")

    return changed


def main() -> None:
    if not DIKT_DIR.exists():
        raise FileNotFoundError(f"Missing dikt directory: {DIKT_DIR}")

    scanned = 0
    updated_files = 0
    skipped = 0

    for run_dir in sorted(DIKT_DIR.iterdir()):
        if not run_dir.is_dir() or run_dir.name.startswith("."):
            continue

        registry_path = run_dir / "registry.json"
        readme_path = run_dir / "README.md"

        if not registry_path.exists():
            continue

        scanned += 1

        if not readme_path.exists():
            skipped += 1
            print(f"Skip {run_dir.name}: missing README.md")
            continue

        try:
            phase1_model, phase2_model = extract_models(readme_path.read_text(encoding="utf-8"))
        except Exception as exc:
            skipped += 1
            print(f"Skip {run_dir.name}: {exc}")
            continue

        update_registry(registry_path, phase1_model, phase2_model)
        updated_files += 1
        print(f"Updated {run_dir.name}: phase1Model={phase1_model}, phase2Model={phase2_model}")

    print(
        f"Done. scanned={scanned}, updated={updated_files}, skipped={skipped}"
    )


if __name__ == "__main__":
    main()
