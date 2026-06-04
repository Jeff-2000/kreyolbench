"""Evaluation result persistence."""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def build_result(
    task: str,
    model: str,
    metrics: dict[str, float],
    dataset_version: str = "v0.1",
    setting: str = "unspecified",
    data_hash: str = "unknown",
    seed: int = 42,
) -> dict[str, Any]:
    created_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    safe_model = model.replace("/", "_")
    return {
        "run_id": f"{created_at}_{task}_{safe_model}",
        "task": task,
        "dataset_version": dataset_version,
        "model": model,
        "setting": setting,
        "metrics": metrics,
        "confidence_intervals": {},
        "data_hash": data_hash,
        "code_commit": "unknown",
        "seed": seed,
        "created_at": created_at,
    }


def save_result_json(path: str | Path, result: dict[str, Any]) -> None:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def results_to_csv(results_dir: str | Path, output_csv: str | Path) -> None:
    rows = []
    for path in sorted(Path(results_dir).glob("*.json")):
        result = json.loads(path.read_text(encoding="utf-8"))
        for metric_name, metric_value in result.get("metrics", {}).items():
            rows.append(
                {
                    "run_id": result["run_id"],
                    "model_name": result["model"],
                    "task": result["task"],
                    "primary_metric": metric_name,
                    "metric_value": metric_value,
                    "training_setting": result.get("setting", "unspecified"),
                    "dataset_version": result.get("dataset_version", "unknown"),
                    "date_submitted": result.get("created_at", ""),
                    "verified": False,
                }
            )
    output = Path(output_csv)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()) if rows else ["run_id"])
        writer.writeheader()
        writer.writerows(rows)

