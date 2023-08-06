from __future__ import annotations

from pathlib import Path
from typing import Any

import toml


def pdm_scripts(root: Path) -> dict[str, Any]:
    pyproject_toml = root / "pyproject.toml"
    if pyproject_toml.exists():
        pyproject = toml.load(pyproject_toml.open("r"))
        return pyproject.get("tool", {}).get("pdm", {}).get("scripts", {})
    return {}
