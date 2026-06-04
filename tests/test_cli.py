from typer.testing import CliRunner

from kreyolbench.cli import app


def test_validate_dataset_cli():
    result = CliRunner().invoke(
        app, ["validate-dataset", "--task", "ner", "--path", "data/sample/ner.jsonl"]
    )
    assert result.exit_code == 0
    assert "validated 1 ner rows" in result.output


def test_prepare_data_cli():
    result = CliRunner().invoke(
        app, ["prepare-data", "--source", "cmu_haitian", "--config", "configs/sources/cmu.yaml"]
    )
    assert result.exit_code == 0
    assert "cmu_haitian" in result.output


def test_evaluate_cli_uses_sample_default(tmp_path):
    result = CliRunner().invoke(
        app, ["evaluate", "--task", "ner", "--model", "file-baseline", "--output-dir", str(tmp_path)]
    )
    assert result.exit_code == 0
    assert "span_f1" in result.output
