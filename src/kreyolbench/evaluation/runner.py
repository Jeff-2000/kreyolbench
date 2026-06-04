"""Simple file-based evaluation runner."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from kreyolbench.evaluation.metrics import evaluate_task
from kreyolbench.evaluation.reporting import build_result, save_result_json
from kreyolbench.io import read_jsonl, sha256_file


def extract_references(task: str, rows: list[dict[str, Any]]) -> Any:
    if task in {"classification", "sentiment"}:
        return [row["target"]["label"] for row in rows]
    if task == "ner":
        return [row["target"]["tags"] for row in rows]
    if task == "codeswitch":
        return [row["target"].get("sentence_lang") for row in rows]
    if task == "qa":
        return [[answer["text"] for answer in row["target"]["answers"]] for row in rows]
    if task == "retrieval":
        return [
            {item["doc_id"]: int(item["relevance"]) for item in row["target"]["relevant_docs"]}
            for row in rows
        ]
    if task == "normalization":
        return [row["target"]["normalized_text"] for row in rows]
    if task in {"translation", "summarization"}:
        return [row["target"].get("summary") or row["target"]["references"][0] for row in rows]
    raise ValueError(f"Unsupported task: {task}")


def extract_predictions(task: str, rows: list[dict[str, Any]]) -> Any:
    if rows and "prediction" in rows[0]:
        return [row["prediction"] for row in rows]
    return extract_references(task, rows)


def evaluate_jsonl(
    task: str,
    predictions_path: str | Path,
    references_path: str | Path | None = None,
    model: str = "file-baseline",
    output_dir: str | Path = "eval/results",
) -> dict[str, Any]:
    prediction_rows = read_jsonl(predictions_path)
    reference_rows = read_jsonl(references_path or predictions_path)
    predictions = extract_predictions(task, prediction_rows)
    references = extract_references(task, reference_rows)
    metrics = evaluate_task(task, predictions, references)
    result = build_result(task=task, model=model, metrics=metrics, data_hash=sha256_file(references_path or predictions_path))
    output_path = Path(output_dir) / f"{result['run_id'].replace(':', '').replace('+', 'Z')}.json"
    save_result_json(output_path, result)
    return result

