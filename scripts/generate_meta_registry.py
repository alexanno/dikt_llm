#!/usr/bin/env python3
"""Generate dikt/meta-registry.json for GitHub Pages.

GitHub Pages does not expose folder listings, so index.html needs a static
manifest listing all run folders and where each folder's registry lives.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIKT_DIR = ROOT / "dikt"
OUTPUT_FILE = DIKT_DIR / "meta-registry.json"


def read_registry(registry_path: Path) -> list[dict]:
    with registry_path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, list):
        raise ValueError(f"Registry must be a list: {registry_path}")

    return data


def newest_id(entries: list[dict]) -> str | None:
    ids = [entry.get("id", "") for entry in entries if isinstance(entry, dict)]
    ids = [value for value in ids if isinstance(value, str) and value]
    if not ids:
        return None
    return max(ids)


def discover_runs() -> list[dict]:
    runs = []

    for folder in sorted(DIKT_DIR.iterdir()):
        if not folder.is_dir() or folder.name.startswith("."):
            continue

        registry_path = folder / "registry.json"
        if not registry_path.exists():
            continue

        entries = read_registry(registry_path)
        runs.append(
            {
                "folder": folder.name,
                "label": folder.name,
                "registry": f"{folder.name}/registry.json",
                "count": len(entries),
                "latestId": newest_id(entries),
            }
        )

    runs.sort(key=lambda run: (run.get("latestId") or ""), reverse=True)
    return runs


def main() -> None:
    if not DIKT_DIR.exists():
        raise FileNotFoundError(f"Missing directory: {DIKT_DIR}")

    runs = discover_runs()

    payload = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "runs": runs,
    }

    OUTPUT_FILE.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Wrote {OUTPUT_FILE} ({len(runs)} runs)")


if __name__ == "__main__":
    main()
