"""Command-line interface for KreyolBench."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from kreyolbench.evaluation.reporting import results_to_csv
from kreyolbench.evaluation.runner import evaluate_jsonl
from kreyolbench.governance import audit_repository
from kreyolbench.io import read_jsonl
from kreyolbench.registry import load_yaml
from kreyolbench.schemas import validate_row
from kreyolbench.sources import build_source_plan

app = typer.Typer(help="KreyolBench dataset and evaluation tools.")

# Local fixtures for currently implemented adapters, not the project task universe.
SAMPLE_FILES = {
    "classification": Path("data/sample/classification_topic.jsonl"),
    "sentiment": Path("data/sample/sentiment.jsonl"),
    "ner": Path("data/sample/ner.jsonl"),
    "qa": Path("data/sample/qa.jsonl"),
    "normalization": Path("data/sample/normalization.jsonl"),
    "codeswitch": Path("data/sample/codeswitch.jsonl"),
    "translation": Path("data/sample/translation.jsonl"),
    "summarization": Path("data/sample/summarization.jsonl"),
}


@app.command("audit-governance")
def audit_governance(
    root: Path = typer.Option(Path("."), help="KreyolBench repository root."),
    output_format: str = typer.Option(
        "text", "--format", help="Output format for maintainers or CI."
    ),
) -> None:
    """Validate governance configuration and scientific invariants."""

    if output_format not in {"text", "json"}:
        raise typer.BadParameter("--format must be 'text' or 'json'")
    audit = audit_repository(root)
    if output_format == "json":
        typer.echo(audit.as_json())
    else:
        typer.echo(f"status: {audit.status}")
        typer.echo(f"release_eligible: {str(audit.release_eligible).lower()}")
        for field_name in (
            "errors",
            "warnings",
            "blocked_components",
            "unresolved_decisions",
        ):
            values = getattr(audit, field_name)
            typer.echo(f"{field_name}: {len(values)}")
            for value in values:
                typer.echo(f"  - {value}")
    if audit.errors:
        raise typer.Exit(code=1)


@app.command("validate-dataset")
def validate_dataset(
    task: str = typer.Option(..., help="Task name to validate."),
    path: Path = typer.Option(..., help="JSONL dataset path."),
) -> None:
    rows = read_jsonl(path)
    for row in rows:
        validated = validate_row(row)
        if validated.task != task:
            raise typer.BadParameter(f"row {validated.id} has task {validated.task}, expected {task}")
    typer.echo(f"validated {len(rows)} {task} rows from {path}")


@app.command("evaluate")
def evaluate(
    task: str = typer.Option(..., help="Task name."),
    model: str = typer.Option("file-baseline", help="Model or run name."),
    predictions: Optional[Path] = typer.Option(None, help="JSONL predictions or rows with target labels."),
    references: Optional[Path] = typer.Option(None, help="Reference JSONL. Defaults to predictions path."),
    output_dir: Path = Path("eval/results"),
) -> None:
    predictions = predictions or SAMPLE_FILES.get(task)
    if predictions is None:
        raise typer.BadParameter(f"No sample file is registered for task {task}; pass --predictions.")
    result = evaluate_jsonl(task, predictions, references, model=model, output_dir=output_dir)
    typer.echo(result)


@app.command("prepare-data")
def prepare_data(
    source: str = typer.Option(..., help="Source ID."),
    config: Path = typer.Option(..., help="Source YAML config."),
) -> None:
    source_config = load_yaml(config)
    if source_config.get("source_id") != source:
        raise typer.BadParameter(f"{config} source_id does not match {source}")
    plan = build_source_plan(source_config)
    typer.echo(plan)


@app.command("export-hf")
def export_hf(version: str = "v0.1", out: Path = Path("datasets")) -> None:
    out.mkdir(parents=True, exist_ok=True)
    typer.echo(f"Hugging Face export scaffold ready for {version} at {out}")


@app.command("build-leaderboard")
def build_leaderboard(results: Path = Path("eval/results"), out: Path = Path("leaderboard/submissions.csv")) -> None:
    results_to_csv(results, out)
    typer.echo(f"wrote leaderboard table to {out}")


if __name__ == "__main__":
    app()
