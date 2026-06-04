"""Transformer baseline placeholders.

The concrete training loops are intentionally thin in v0.1 because model training
depends on GPU availability and task-specific annotation scale.
"""

from __future__ import annotations


DEFAULT_MODELS = [
    "bert-base-multilingual-cased",
    "xlm-roberta-base",
    "xlm-roberta-large",
]


def describe_model_plan(task: str, model_name: str) -> dict[str, str]:
    head = "sequence_classification"
    if task in {"ner", "codeswitch"}:
        head = "token_classification"
    if task == "qa":
        head = "question_answering"
    return {"task": task, "model_name": model_name, "head": head, "status": "training_loop_pending"}

