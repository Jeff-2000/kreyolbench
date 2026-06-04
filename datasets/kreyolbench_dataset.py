"""Hugging Face Datasets loader for local KreyolBench JSONL files."""

from __future__ import annotations

import json
from pathlib import Path

import datasets


_TASKS = [
    "classification",
    "sentiment",
    "ner",
    "qa",
    "retrieval",
    "summarization",
    "normalization",
    "translation",
    "codeswitch",
    "orthography_robustness",
]


class KreyolBenchConfig(datasets.BuilderConfig):
    def __init__(self, task: str, **kwargs):
        super().__init__(name=task, version=datasets.Version("0.1.0"), **kwargs)
        self.task = task


class KreyolBench(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [KreyolBenchConfig(task=task, description=f"KreyolBench {task}") for task in _TASKS]
    DEFAULT_CONFIG_NAME = "classification"

    def _info(self):
        return datasets.DatasetInfo(
            description="Kreyol-first Haitian Creole NLP benchmark.",
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "task": datasets.Value("string"),
                    "language": datasets.Value("string"),
                    "split": datasets.Value("string"),
                    "domain": datasets.Value("string"),
                    "source": datasets.Value("string"),
                    "input": datasets.Value("string"),
                    "target": datasets.Value("string"),
                    "metadata": datasets.Value("string"),
                }
            ),
            homepage="https://github.com/REPLACE_ME/kreyolbench",
            license="Code: Apache-2.0; data: per-subset licenses.",
        )

    def _split_generators(self, dl_manager):
        data_dir = Path(self.config.data_dir or "data/processed")
        paths = {
            split: data_dir / f"{self.config.task}_{split}.jsonl"
            for split in ["train", "validation", "test_public"]
        }
        return [
            datasets.SplitGenerator(name=getattr(datasets.Split, split.upper(), split), gen_kwargs={"path": path})
            for split, path in paths.items()
            if path.exists()
        ]

    def _generate_examples(self, path):
        with Path(path).open(encoding="utf-8") as handle:
            for index, line in enumerate(handle):
                row = json.loads(line)
                yield index, {
                    "id": row["id"],
                    "task": row["task"],
                    "language": row.get("language", "hat"),
                    "split": row["split"],
                    "domain": row["domain"],
                    "source": json.dumps(row.get("source", {}), ensure_ascii=False),
                    "input": json.dumps(row.get("input", {}), ensure_ascii=False),
                    "target": json.dumps(row.get("target", {}), ensure_ascii=False),
                    "metadata": json.dumps(row.get("metadata", {}), ensure_ascii=False),
                }

