"""Task metrics for KreyolBench."""

from __future__ import annotations

import math
import re
from collections import Counter
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


def multilabel_classification_scores(
    predictions: list[list[str]], references: list[list[str]]
) -> dict[str, float]:
    """Compute set-based multi-label scores without choosing model thresholds."""

    _check_lengths(predictions, references)
    labels = sorted({label for row in predictions + references for label in row})
    per_label_f1 = []
    total_tp = total_fp = total_fn = 0
    sample_f1s = []
    exact = []
    for predicted, reference in zip(predictions, references):
        predicted_set = set(predicted)
        reference_set = set(reference)
        tp = len(predicted_set & reference_set)
        fp = len(predicted_set - reference_set)
        fn = len(reference_set - predicted_set)
        total_tp += tp
        total_fp += fp
        total_fn += fn
        sample_f1s.append(_f1(tp, fp, fn))
        exact.append(float(predicted_set == reference_set))
    for label in labels:
        tp = sum(label in p and label in r for p, r in zip(predictions, references))
        fp = sum(label in p and label not in r for p, r in zip(predictions, references))
        fn = sum(label not in p and label in r for p, r in zip(predictions, references))
        per_label_f1.append(_f1(tp, fp, fn))
    return {
        "subset_accuracy": sum(exact) / len(exact) if exact else 0.0,
        "micro_f1": _f1(total_tp, total_fp, total_fn),
        "macro_f1": sum(per_label_f1) / len(per_label_f1) if per_label_f1 else 0.0,
        "sample_f1": sum(sample_f1s) / len(sample_f1s) if sample_f1s else 0.0,
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


def character_span_scores(
    predictions: list[list[dict[str, Any]]], references: list[list[dict[str, Any]]]
) -> dict[str, float]:
    """Score exact typed character spans, including nested spans."""

    _check_lengths(predictions, references)
    predicted_spans: Counter[tuple[int, int, int, str]] = Counter()
    reference_spans: Counter[tuple[int, int, int, str]] = Counter()
    for row_index, (predicted, reference) in enumerate(zip(predictions, references)):
        predicted_spans.update(
            (row_index, item["start_char"], item["end_char"], item["label"])
            for item in predicted
        )
        reference_spans.update(
            (row_index, item["start_char"], item["end_char"], item["label"])
            for item in reference
        )
    tp = sum((predicted_spans & reference_spans).values())
    fp = sum((predicted_spans - reference_spans).values())
    fn = sum((reference_spans - predicted_spans).values())
    return {
        "span_f1": _f1(tp, fp, fn),
        "precision": _precision(tp, fp),
        "recall": _recall(tp, fn),
    }


def token_classification_scores(
    predictions: list[list[str]], references: list[list[str]]
) -> dict[str, float]:
    """Compute direct token-label scores without BIO span interpretation."""

    _check_lengths(predictions, references)
    flat_predictions: list[str] = []
    flat_references: list[str] = []
    for predicted, reference in zip(predictions, references):
        _check_lengths(predicted, reference)
        flat_predictions.extend(predicted)
        flat_references.extend(reference)
    scores = classification_scores(flat_predictions, flat_references)
    return {
        "token_accuracy": scores["accuracy"],
        "micro_f1": scores["accuracy"],
        "macro_f1": scores["macro_f1"],
        "weighted_f1": scores["weighted_f1"],
    }


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
    judged_rates = []
    bprefs = []
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
        judged_rates.append(
            sum(doc_id in relevant for doc_id in ranked_at_k) / len(ranked_at_k)
            if ranked_at_k
            else 0.0
        )
        judged_nonrelevant = {doc_id for doc_id, rel in relevant.items() if rel == 0}
        denominator = min(len(relevant_docs), len(judged_nonrelevant))
        if not relevant_docs or denominator == 0:
            bprefs.append(0.0)
        else:
            ranked_positions = {doc_id: index for index, doc_id in enumerate(ranked_docs)}
            preferences = []
            for relevant_doc in relevant_docs:
                relevant_rank = ranked_positions.get(relevant_doc, len(ranked_docs))
                nonrelevant_above = sum(
                    ranked_positions.get(doc_id, len(ranked_docs)) < relevant_rank
                    for doc_id in judged_nonrelevant
                )
                preferences.append(1.0 - min(nonrelevant_above, denominator) / denominator)
            bprefs.append(sum(preferences) / len(preferences))
    return {
        f"mrr_at_{k}": sum(mrrs) / len(mrrs) if mrrs else 0.0,
        f"ndcg_at_{k}": sum(ndcgs) / len(ndcgs) if ndcgs else 0.0,
        f"recall_at_{k}": sum(recalls) / len(recalls) if recalls else 0.0,
        f"judged_at_{k}": sum(judged_rates) / len(judged_rates) if judged_rates else 0.0,
        "bpref": sum(bprefs) / len(bprefs) if bprefs else 0.0,
    }


def normalization_scores(predictions: list[str], references: list[str]) -> dict[str, float]:
    return {
        "exact_match": accuracy(predictions, references),
        "token_accuracy": token_accuracy([p.split() for p in predictions], [r.split() for r in references]),
    }


def normalization_reference_scores(
    predictions: list[str], references: list[list[str]]
) -> dict[str, float]:
    """Score normalization against one or more accepted references."""

    _check_lengths(predictions, references)
    exact = []
    closest_token_f1 = []
    for prediction, accepted in zip(predictions, references):
        if not accepted:
            raise ValueError("normalization references must not be empty")
        exact.append(float(prediction in accepted))
        closest_token_f1.append(
            max(_token_f1(prediction.casefold(), reference.casefold()) for reference in accepted)
        )
    return {
        "exact_match_any_reference": sum(exact) / len(exact) if exact else 0.0,
        "closest_reference_token_f1": (
            sum(closest_token_f1) / len(closest_token_f1) if closest_token_f1 else 0.0
        ),
    }


def evaluate_task(task: str, predictions: Any, references: Any) -> dict[str, float]:
    """Dispatch metrics for implemented runtime aliases, not all roadmap tasks."""
    if task == "classification":
        if predictions and isinstance(predictions[0], list):
            return multilabel_classification_scores(predictions, references)
        return classification_scores(predictions, references)
    if task == "sentiment":
        return classification_scores(predictions, references)
    if task == "codeswitch":
        return token_classification_scores(predictions, references)
    if task == "ner":
        first_sequence = predictions[0] if predictions else (references[0] if references else [])
        if first_sequence and isinstance(first_sequence[0], dict):
            return character_span_scores(predictions, references)
        return span_f1(predictions, references)
    if task == "qa":
        return qa_scores(predictions, references)
    if task == "retrieval":
        return retrieval_scores(predictions, references)
    if task == "normalization":
        if references and isinstance(references[0], list):
            return normalization_reference_scores(predictions, references)
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
