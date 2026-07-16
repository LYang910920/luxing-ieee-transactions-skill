"""Deterministic prose metrics for academic manuscripts and corpora."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import math
import re
from statistics import mean, median, pstdev
from typing import Any, Iterable, Mapping

WORD_RE = re.compile(r"[A-Za-z]+(?:[-'][A-Za-z]+)*|\d+(?:\.\d+)?")
MARKDOWN_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")
LATEX_HEADING_RE = re.compile(r"^\s*\\(?:section|subsection|subsubsection)\*?\{(.+?)\}\s*$")
IEEE_HEADING_RE = re.compile(r"^\s*(?:[IVX]+\.|[A-Z]\.)\s+([A-Z][A-Z0-9 ,/&\-]{2,})\s*$")

ABBREVIATIONS = (
    "e.g.",
    "i.e.",
    "et al.",
    "Fig.",
    "Figs.",
    "Eq.",
    "Eqs.",
    "Sec.",
    "Secs.",
    "Ref.",
    "Refs.",
    "Dr.",
    "Prof.",
    "No.",
    "Vol.",
)

TRANSITIONS = [
    "however",
    "in contrast",
    "on this basis",
    "thereby",
    "therefore",
    "furthermore",
    "moreover",
    "finally",
    "to address this limitation",
    "to address these limitations",
    "to bridge these gaps",
    "as a result",
    "on the one hand",
    "on the other hand",
]
HEDGES = ["may", "might", "can", "could", "suggest", "suggests", "indicate", "indicates", "appears"]
ACTION_VERBS = [
    "characterize",
    "characterizes",
    "formulate",
    "formulates",
    "derive",
    "derives",
    "establish",
    "establishes",
    "develop",
    "develops",
    "approximate",
    "approximates",
    "evaluate",
    "evaluates",
    "demonstrate",
    "demonstrates",
    "reveal",
    "reveals",
    "propose",
    "proposes",
]
CLAIM_TERMS = [
    "first",
    "novel",
    "innovative",
    "optimal",
    "optimally",
    "equilibrium",
    "significant",
    "significantly",
    "scalable",
    "scalability",
    "practical",
    "practicability",
    "outperform",
    "outperforms",
    "state-of-the-art",
]

SECTION_ALIASES = {
    "abstract": "abstract",
    "index terms": "index_terms",
    "keywords": "index_terms",
    "introduction": "introduction",
    "related work": "related_work",
    "related works": "related_work",
    "background": "related_work",
    "preliminaries": "background",
    "system model": "model",
    "model": "model",
    "problem formulation": "model",
    "theoretical analysis": "theory",
    "analysis": "theory",
    "theory": "theory",
    "algorithm": "algorithm",
    "solution method": "algorithm",
    "numerical method": "algorithm",
    "experimental setup": "experimental_setup",
    "experiment setup": "experimental_setup",
    "experiments": "results",
    "numerical experiments": "results",
    "results": "results",
    "results and discussion": "results",
    "discussion": "discussion",
    "limitations": "limitations",
    "conclusion": "conclusion",
    "conclusions": "conclusion",
    "appendix": "appendix",
    "references": "references",
}


@dataclass(frozen=True)
class Section:
    name: str
    heading: str
    text: str


def _strip_latex(text: str) -> str:
    text = re.sub(r"(?m)(?<!\\)%.*$", " ", text)
    text = re.sub(
        r"\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?|table\*?|figure\*?)\}.*?"
        r"\\end\{(?:equation\*?|align\*?|gather\*?|multline\*?|table\*?|figure\*?)\}",
        " ",
        text,
        flags=re.S,
    )
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.S)
    text = re.sub(r"\$(?:\\.|[^$])*\$", " ", text)
    text = re.sub(r"\\cite[a-zA-Z*]*\{[^}]*\}", " [CITATION] ", text)
    text = re.sub(r"\\(?:ref|eqref|autoref)\{[^}]*\}", " [REF] ", text)
    text = re.sub(r"\\[a-zA-Z@]+\*?(?:\[[^]]*\])?\{([^{}]*)\}", r" \1 ", text)
    text = re.sub(r"\\[a-zA-Z@]+\*?", " ", text)
    text = text.replace("~", " ")
    return text


def clean_prose(text: str) -> str:
    """Remove common markup and non-prose noise without attempting OCR."""

    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if "\\section" in text or "\\begin{" in text:
        text = _strip_latex(text)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"!\[[^]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"(?m)^\s*\|.*\|\s*$", " ", text)
    text = re.sub(r"(?m)^\s*[-*+]\s+", "", text)
    text = re.sub(r"(?m)^\s*\d+[.)]\s+", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_sentences(text: str) -> list[str]:
    prose = clean_prose(text)
    if not prose:
        return []
    protected = prose
    placeholders: dict[str, str] = {}
    for index, abbreviation in enumerate(ABBREVIATIONS):
        key = f"__ABBR_{index}__"
        placeholders[key] = abbreviation
        protected = protected.replace(abbreviation, abbreviation.replace(".", key))
    protected = re.sub(r"(?<=\d)\.(?=\d)", "__DECIMAL__", protected)
    raw = re.split(r"(?<=[.!?])(?:[\"'”’)]*)\s+(?=[A-Z0-9\[(])|\n{2,}", protected)
    sentences: list[str] = []
    for item in raw:
        item = item.strip()
        item = item.replace("__DECIMAL__", ".")
        for key, abbreviation in placeholders.items():
            item = item.replace(abbreviation.replace(".", key), abbreviation)
        if len(WORD_RE.findall(item)) >= 2:
            sentences.append(item)
    return sentences


def split_paragraphs(text: str) -> list[str]:
    prose = clean_prose(text)
    paragraphs = []
    for paragraph in re.split(r"\n\s*\n", prose):
        paragraph = re.sub(r"\s*\n\s*", " ", paragraph).strip()
        if len(WORD_RE.findall(paragraph)) >= 3:
            paragraphs.append(paragraph)
    return paragraphs


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def percentile(values: list[int], p: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    position = (len(ordered) - 1) * p
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return float(ordered[lower])
    weight = position - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def normalize_heading(heading: str) -> str:
    cleaned = re.sub(r"[^a-z0-9 ]+", " ", heading.lower())
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    for alias, normalized in SECTION_ALIASES.items():
        if cleaned == alias or cleaned.startswith(alias + " "):
            return normalized
    if "experiment" in cleaned or "simulation" in cleaned:
        return "results"
    if "proof" in cleaned or "stability" in cleaned or "optimality" in cleaned:
        return "theory"
    if "model" in cleaned or "formulation" in cleaned:
        return "model"
    if "algorithm" in cleaned or "method" in cleaned:
        return "algorithm"
    return cleaned.replace(" ", "_") or "document"


def segment_sections(text: str) -> list[Section]:
    """Segment Markdown, LaTeX, or IEEE-like plain text by headings."""

    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    sections: list[Section] = []
    current_heading = "Document"
    current_name = "document"
    buffer: list[str] = []

    def flush() -> None:
        nonlocal buffer
        content = "\n".join(buffer).strip()
        if content:
            sections.append(Section(current_name, current_heading, content))
        buffer = []

    for line in lines:
        heading = None
        for pattern in (MARKDOWN_HEADING_RE, LATEX_HEADING_RE, IEEE_HEADING_RE):
            match = pattern.match(line)
            if match:
                heading = match.group(1).strip()
                break
        if heading is not None:
            flush()
            current_heading = heading
            current_name = normalize_heading(heading)
        else:
            buffer.append(line)
    flush()

    if not sections:
        return [Section("document", "Document", text)]
    return sections


def _pattern_counts(text: str, patterns: Iterable[str]) -> dict[str, int]:
    lowered = text.lower()
    counts: dict[str, int] = {}
    for pattern in patterns:
        counts[pattern] = len(re.findall(r"\b" + re.escape(pattern) + r"\b", lowered))
    return {key: value for key, value in counts.items() if value}


def analyze_text(text: str, source: str | None = None, include_sections: bool = True) -> dict[str, Any]:
    """Compute explainable academic-prose metrics."""

    prose = clean_prose(text)
    sentence_list = split_sentences(prose)
    paragraph_list = split_paragraphs(prose)
    word_list = words(prose)
    sentence_lengths = [len(words(sentence)) for sentence in sentence_list]
    paragraph_sentence_lengths = [len(split_sentences(paragraph)) for paragraph in paragraph_list]
    paragraph_word_lengths = [len(words(paragraph)) for paragraph in paragraph_list]
    total_words = len(word_list)
    lowered_words = [word.lower() for word in word_list]
    counter = Counter(lowered_words)

    metrics: dict[str, Any] = {
        "source": source,
        "words": total_words,
        "sentences": len(sentence_list),
        "paragraphs": len(paragraph_list),
        "sentence_length": {
            "mean": round(mean(sentence_lengths), 2) if sentence_lengths else 0.0,
            "median": round(median(sentence_lengths), 2) if sentence_lengths else 0.0,
            "stddev": round(pstdev(sentence_lengths), 2) if len(sentence_lengths) > 1 else 0.0,
            "p90": round(percentile(sentence_lengths, 0.9), 2),
            "max": max(sentence_lengths, default=0),
            "short_le_14_ratio": round(sum(x <= 14 for x in sentence_lengths) / len(sentence_lengths), 3)
            if sentence_lengths
            else 0.0,
            "medium_15_30_ratio": round(sum(15 <= x <= 30 for x in sentence_lengths) / len(sentence_lengths), 3)
            if sentence_lengths
            else 0.0,
            "long_31_45_ratio": round(sum(31 <= x <= 45 for x in sentence_lengths) / len(sentence_lengths), 3)
            if sentence_lengths
            else 0.0,
            "very_long_gt_45_ratio": round(sum(x > 45 for x in sentence_lengths) / len(sentence_lengths), 3)
            if sentence_lengths
            else 0.0,
        },
        "paragraph_length": {
            "mean_sentences": round(mean(paragraph_sentence_lengths), 2) if paragraph_sentence_lengths else 0.0,
            "mean_words": round(mean(paragraph_word_lengths), 2) if paragraph_word_lengths else 0.0,
            "max_words": max(paragraph_word_lengths, default=0),
        },
        "first_person_research_voice": {
            "we": counter.get("we", 0),
            "our": counter.get("our", 0),
            "we_our_per_1000_words": round(
                1000 * (counter.get("we", 0) + counter.get("our", 0)) / total_words, 2
            )
            if total_words
            else 0.0,
        },
        "transitions": _pattern_counts(prose, TRANSITIONS),
        "hedges": _pattern_counts(prose, HEDGES),
        "research_verbs": _pattern_counts(prose, ACTION_VERBS),
        "claim_terms": _pattern_counts(prose, CLAIM_TERMS),
        "citation_markers": len(re.findall(r"\[[0-9,\-– ]+\]|\[CITATION\]|\\cite", text)),
        "figure_references": len(re.findall(r"\b(?:Fig\.|Figure)\s*\d+", text, flags=re.I)),
        "table_references": len(re.findall(r"\bTable\s*[IVX0-9]+", text, flags=re.I)),
        "equation_references": len(re.findall(r"\b(?:Eq\.|Equation)\s*\(?\d+", text, flags=re.I)),
        "theorem_references": len(re.findall(r"\b(?:Theorem|Lemma|Proposition|Corollary)\s*\d*", text, flags=re.I)),
    }

    if include_sections:
        section_metrics: dict[str, Any] = {}
        name_counts: Counter[str] = Counter()
        for section in segment_sections(text):
            name_counts[section.name] += 1
            key = section.name if name_counts[section.name] == 1 else f"{section.name}_{name_counts[section.name]}"
            section_metrics[key] = analyze_text(section.text, source=section.heading, include_sections=False)
        metrics["sections"] = section_metrics
    return metrics


def aggregate_metrics(
    documents: Iterable[tuple[Mapping[str, Any], float]],
) -> dict[str, Any]:
    """Aggregate document metrics with explicit positive weights."""

    docs = [(dict(metrics), float(weight)) for metrics, weight in documents if float(weight) > 0]
    if not docs:
        return {"documents": 0, "total_weight": 0.0}
    total_weight = sum(weight for _, weight in docs)

    def weighted(path: tuple[str, ...]) -> float:
        values = []
        for metrics, weight in docs:
            value: Any = metrics
            for key in path:
                value = value.get(key, 0) if isinstance(value, Mapping) else 0
            try:
                values.append((float(value), weight))
            except (TypeError, ValueError):
                values.append((0.0, weight))
        return sum(value * weight for value, weight in values) / total_weight

    transition_totals: Counter[str] = Counter()
    claim_totals: Counter[str] = Counter()
    for metrics, weight in docs:
        transition_totals.update({key: value * weight for key, value in metrics.get("transitions", {}).items()})
        claim_totals.update({key: value * weight for key, value in metrics.get("claim_terms", {}).items()})

    return {
        "documents": len(docs),
        "total_weight": round(total_weight, 3),
        "weighted_mean_words": round(weighted(("words",)), 2),
        "weighted_mean_sentences": round(weighted(("sentences",)), 2),
        "weighted_sentence_length_mean": round(weighted(("sentence_length", "mean")), 2),
        "weighted_sentence_length_p90": round(weighted(("sentence_length", "p90")), 2),
        "weighted_we_our_per_1000_words": round(
            weighted(("first_person_research_voice", "we_our_per_1000_words")), 2
        ),
        "weighted_transition_counts": {key: round(value, 3) for key, value in transition_totals.most_common()},
        "weighted_claim_term_counts": {key: round(value, 3) for key, value in claim_totals.most_common()},
    }
