"""Task metrics for KreyolBench."""

from __future__ import annotations

import math
import re
from collections import Counter, defaultdict
from typing import Any


def accuracy(predictions: list[Any], references: list[Any]) -> float:
    _check_lengths(predictions, references)
    if not references:
        return 0.0
    return sum(pred == ref for pred, ref in zip(predictions, references)) / len(references)


def classification_scores(predictions: list[str], references: list[str]) -> dict[str, float]:
    _check_lengths(predictions, references)
    labels = sorted(set(predictions) | set(references))
    per_label = {}
    weighted_total = 0.0
    for label in labels:
        tp = sum(p == label and r == label for p, r in zip(predictions, references))
        fp = sum(p == label and r != label for p, r in zip(predictions, references))
        fn = sum(p != label and r == label for p, r in zip(predictions, references))
        support = sum(r == label for r in references)
        f1 = _f1(tp, fp, fn)
        per_label[label] = f1
        weighted_total += f1 * support
    support_total = len(references) or 1
    return {
        "accuracy": accuracy(predictions, references),
        "macro_f1": sum(per_label.values()) / len(per_label) if per_label else 0.0,
        "weighted_f1": weighted_total / support_total,
    }


def token_accuracy(predictions: list[list[str]], references: list[list[str]]) -> float:
    _check_lengths(predictions, references)
    total = 0
    correct = 0
    for pred_seq, ref_seq in zip(predictions, references):
        _check_lengths(pred_seq, ref_seq)
        total += len(ref_seq)
        correct += sum(pred == ref for pred, ref in zip(pred_seq, ref_seq))
    return correct / total if total else 0.0


def span_f1(predictions: list[list[str]], references: list[list[str]]) -> dict[str, float]:
    _check_lengths(predictions, references)
    pred_spans: Counter[tuple[int, int, int, str]] = Counter()
    ref_spans: Counter[tuple[int, int, int, str]] = Counter()
    for row_index, (pred_tags, ref_tags) in enumerate(zip(predictions, references)):
        _check_lengths(pred_tags, ref_tags)
        pred_spans.update((row_index, start, end, label) for start, end, label in bio_spans(pred_tags))
        ref_spans.update((row_index, start, end, label) for start, end, label in bio_spans(ref_tags))
    tp = sum((pred_spans & ref_spans).values())
    fp = sum((pred_spans - ref_spans).values())
    fn = sum((ref_spans - pred_spans).values())
    return {"span_f1": _f1(tp, fp, fn), "precision": _precision(tp, fp), "recall": _recall(tp, fn)}


def bio_spans(tags: list[str]) -> list[tuple[int, int, str]]:
    spans = []
    start = None
    label = None
    for index, tag in enumerate(tags + ["O"]):
        if tag == "O" or tag in {"PUNCT", "NUM", "OTHER"}:
            if start is not None and label is not None:
                spans.append((start, index, label))
            start = None
            label = None
            continue
        prefix, _, current_label = tag.partition("-")
        if prefix == "B" or current_label != label:
            if start is not None and label is not None:
                spans.append((start, index, label))
            start = index
            label = current_label
    return spans


def qa_scores(predictions: list[str], references: list[list[str]]) -> dict[str, float]:
    _check_lengths(predictions, references)
    exact = []
    f1s = []
    for pred, refs in zip(predictions, references):
        normalized_pred = _normalize_answer(pred)
        normalized_refs = [_normalize_answer(ref) for ref in refs]
        exact.append(float(normalized_pred in normalized_refs))
        f1s.append(max((_token_f1(normalized_pred, ref) for ref in normalized_refs), default=0.0))
    return {"exact_match": sum(exact) / len(exact) if exact else 0.0, "f1": sum(f1s) / len(f1s) if f1s else 0.0}


def retrieval_scores(
    rankings: list[list[str]], qrels: list[dict[str, int]], k: int = 10
) -> dict[str, float]:
    _check_lengths(rankings, qrels)
    mrrs = []
    ndcgs = []
    recalls = []
    for ranked_docs, relevant in zip(rankings, qrels):
        ranked_at_k = ranked_docs[:k]
        relevant_docs = {doc_id for doc_id, rel in relevant.items() if rel > 0}
        first_rank = next((i + 1 for i, doc_id in enumerate(ranked_at_k) if doc_id in relevant_docs), 0)
        mrrs.append(1 / first_rank if first_rank else 0.0)
        gains = [relevant.get(doc_id, 0) for doc_id in ranked_at_k]
        dcg = sum((2**gain - 1) / math.log2(index + 2) for index, gain in enumerate(gains))
        ideal = sorted(relevant.values(), reverse=True)[:k]
        idcg = sum((2**gain - 1) / math.log2(index + 2) for index, gain in enumerate(ideal))
        ndcgs.append(dcg / idcg if idcg else 0.0)
        recalls.append(len(set(ranked_at_k) & relevant_docs) / len(relevant_docs) if relevant_docs else 0.0)
    return {
        f"mrr_at_{k}": sum(mrrs) / len(mrrs) if mrrs else 0.0,
        f"ndcg_at_{k}": sum(ndcgs) / len(ndcgs) if ndcgs else 0.0,
        f"recall_at_{k}": sum(recalls) / len(recalls) if recalls else 0.0,
    }


def normalization_scores(predictions: list[str], references: list[str]) -> dict[str, float]:
    return {
        "exact_match": accuracy(predictions, references),
        "token_accuracy": token_accuracy([p.split() for p in predictions], [r.split() for r in references]),
    }


def evaluate_task(task: str, predictions: Any, references: Any) -> dict[str, float]:
    if task in {"classification", "sentiment", "codeswitch"}:
        if predictions and isinstance(predictions[0], list):
            return {"token_accuracy": token_accuracy(predictions, references), **span_f1(predictions, references)}
        return classification_scores(predictions, references)
    if task == "ner":
        return span_f1(predictions, references)
    if task == "qa":
        return qa_scores(predictions, references)
    if task == "retrieval":
        return retrieval_scores(predictions, references)
    if task == "normalization":
        return normalization_scores(predictions, references)
    if task in {"translation", "summarization"}:
        return normalization_scores(predictions, references)
    raise ValueError(f"Unsupported task: {task}")


def _check_lengths(predictions: list[Any], references: list[Any]) -> None:
    if len(predictions) != len(references):
        raise ValueError("predictions and references must have equal length")


def _precision(tp: int, fp: int) -> float:
    return tp / (tp + fp) if tp + fp else 0.0


def _recall(tp: int, fn: int) -> float:
    return tp / (tp + fn) if tp + fn else 0.0


def _f1(tp: int, fp: int, fn: int) -> float:
    precision = _precision(tp, fp)
    recall = _recall(tp, fn)
    return 2 * precision * recall / (precision + recall) if precision + recall else 0.0


def _normalize_answer(text: str) -> str:
    text = text.casefold()
    text = re.sub(r"[^\w\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _token_f1(prediction: str, reference: str) -> float:
    pred_counts = Counter(prediction.split())
    ref_counts = Counter(reference.split())
    common = sum((pred_counts & ref_counts).values())
    if not pred_counts and not ref_counts:
        return 1.0
    if not common:
        return 0.0
    precision = common / sum(pred_counts.values())
    recall = common / sum(ref_counts.values())
    return 2 * precision * recall / (precision + recall)

