"""Configuration registry helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_yaml(path: str | Path) -> dict[str, Any]:
    with Path(path).open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return data


def load_registry(directory: str | Path) -> dict[str, dict[str, Any]]:
    registry: dict[str, dict[str, Any]] = {}
    for path in sorted(Path(directory).glob("*.yaml")):
        item = load_yaml(path)
        key = item.get("source_id") or item.get("task") or path.stem
        registry[str(key)] = item
    return registry

