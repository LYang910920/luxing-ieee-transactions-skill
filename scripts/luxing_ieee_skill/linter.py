"""Explainable manuscript lint checks for the personalized IEEE workflow."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import re
from typing import Iterable

from .metrics import analyze_text, clean_prose, segment_sections, split_sentences, words


@dataclass(frozen=True)
class Issue:
    severity: str
    code: str
    message: str
    evidence: str = ""
    suggestion: str = ""

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


ABSTRACT_MOVE_PATTERNS = {
    "gap": [r"\bhowever\b", r"\bexisting (?:studies|work|methods|models)\b", r"\blimitations?\b", r"\bgap\b"],
    "proposal": [r"\bwe (?:propose|develop|introduce|present)\b", r"\bthis (?:study|work|article) (?:proposes|develops|introduces|presents)\b"],
    "formalization": [r"\bformulat(?:e|es|ed)\b", r"\boptimization problem\b", r"\bdifferential game\b", r"\boptimal control\b"],
    "theory": [r"\bderiv(?:e|es|ed)\b", r"\bestablish(?:es|ed)?\b", r"\btheorem\b", r"\bnecessary conditions?\b"],
    "algorithm": [r"\balgorithm\b", r"\bnumerical method\b", r"\biterative\b"],
    "evaluation": [r"\bexperiments?\b", r"\bevaluat(?:e|es|ed|ion)\b", r"\bsimulations?\b", r"\bdatasets?\b", r"\bnetworks?\b"],
    "result": [r"\bdemonstrat(?:e|es|ed)\b", r"\bshow(?:s|ed)?\b", r"\breveal(?:s|ed)?\b", r"\bimprov(?:e|es|ed|ement)\b", r"\breduc(?:e|es|ed|tion)\b"],
}

SECTION_REQUIRED_ALIASES = {
    "introduction": {"introduction"},
    "model_or_methods": {"model", "background", "algorithm"},
    "results": {"results", "discussion", "experimental_setup"},
    "conclusion": {"conclusion"},
}

OVERCLAIM_RULES = {
    "novel": "Link the novelty claim to the closest-work matrix and state the non-equivalent mechanism.",
    "innovative": "Replace promotional wording with the exact technical difference unless the novelty audit supports it.",
    "state-of-the-art": "Compare against current relevant baselines under matched conditions.",
    "practical": "Map assumptions and constraints to a realistic operational setting and state limitations.",
    "practicability": "Support with deployment constraints, scale/resource evidence and failure boundaries.",
    "scalable": "Report a problem-size sweep, runtime/memory or complexity, and hardware context.",
    "scalability": "Report a problem-size sweep, runtime/memory or complexity, and hardware context.",
    "robust": "Declare the tested shift or perturbation set, repetitions, uncertainty, and retained failures.",
    "robustness": "Declare the tested shift or perturbation set, repetitions, uncertainty, and retained failures.",
    "real-world": "Require observed outcomes or measured intervention effects; topology or trace realism alone is insufficient.",
    "field-proven": "Require measured field evidence and state the study-design and external-validity boundaries.",
    "causal": "Require a prospective, randomized, quasi-experimental, or otherwise defensible causal design.",
    "causally": "Require a prospective, randomized, quasi-experimental, or otherwise defensible causal design.",
}

MAJOR_OVERCLAIM_TERMS = {
    "novel",
    "innovative",
    "state-of-the-art",
    "robust",
    "robustness",
    "real-world",
    "field-proven",
    "causal",
    "causally",
}


def _extract_abstract(text: str) -> str:
    latex = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", text, flags=re.S | re.I)
    if latex:
        return latex.group(1).strip()

    markdown = re.search(
        r"(?ims)^\s*#{1,6}\s*abstract\s*$\s*(.*?)(?=^\s*#{1,6}\s+|\Z)", text
    )
    if markdown:
        return markdown.group(1).strip()

    ieee = re.search(
        r"(?is)\bAbstract\s*[—-]\s*(.*?)(?=\b(?:Index Terms|Keywords)\s*[—:-]|\n\s*(?:I\.|1\.?\s+)\s*Introduction|\Z)",
        text,
    )
    if ieee:
        return ieee.group(1).strip()

    plain = re.search(
        r"(?ims)^\s*abstract\s*$\s*(.*?)(?=^\s*(?:keywords?|index terms|introduction)\s*$|\Z)",
        text,
    )
    return plain.group(1).strip() if plain else ""


def _nearby_numeric_support(text: str, start: int, radius: int = 220) -> bool:
    window = text[max(0, start - radius) : start + radius]
    return bool(re.search(r"\b\d+(?:\.\d+)?\s*(?:%|ms|s|min|hours?|nodes?|networks?|runs?|times?|×|x)\b", window, flags=re.I))


def _sentence_excerpt(sentence: str, limit: int = 180) -> str:
    compact = re.sub(r"\s+", " ", sentence).strip()
    return compact if len(compact) <= limit else compact[: limit - 1] + "…"


def _containing_sentence(text: str, start: int, end: int) -> str:
    left = max(text.rfind(mark, 0, start) for mark in (".", "!", "?"))
    right_candidates = [position for mark in (".", "!", "?") if (position := text.find(mark, end)) >= 0]
    right = min(right_candidates) + 1 if right_candidates else len(text)
    return text[left + 1 : right]


def lint_text(text: str, source: str | None = None) -> list[Issue]:
    issues: list[Issue] = []
    prose = clean_prose(text)
    lowered = prose.lower()
    sentences = split_sentences(prose)
    metrics = analyze_text(text, source=source)

    abstract = _extract_abstract(text)
    if not abstract:
        issues.append(
            Issue("warning", "ABSTRACT_MISSING", "No abstract section was detected.", suggestion="Add or label the abstract before final preflight.")
        )
    else:
        abstract_words = len(words(abstract))
        if abstract_words < 140:
            issues.append(
                Issue(
                    "warning",
                    "ABSTRACT_SHORT",
                    f"Detected abstract has {abstract_words} words.",
                    suggestion="Check that it contains the gap, model/problem, theory/algorithm, evaluation, result and implication.",
                )
            )
        elif abstract_words > 260:
            issues.append(
                Issue(
                    "warning",
                    "ABSTRACT_LONG",
                    f"Detected abstract has {abstract_words} words.",
                    suggestion="Compress background and preserve verified method/result details; verify the current journal limit.",
                )
            )
        abstract_lower = abstract.lower()
        for move, patterns in ABSTRACT_MOVE_PATTERNS.items():
            if not any(re.search(pattern, abstract_lower) for pattern in patterns):
                issues.append(
                    Issue(
                        "warning",
                        f"ABSTRACT_MOVE_{move.upper()}",
                        f"The abstract does not clearly signal the {move} move.",
                        suggestion=f"Add a concise, evidence-backed {move} sentence or clause if relevant.",
                    )
                )

    section_names = {section.name for section in segment_sections(text)}
    if len(section_names) > 1:
        for label, alternatives in SECTION_REQUIRED_ALIASES.items():
            if not section_names.intersection(alternatives):
                issues.append(
                    Issue(
                        "warning",
                        f"SECTION_{label.upper()}_MISSING",
                        f"No recognizable {label.replace('_', ' ')} section was detected.",
                        suggestion="Confirm the manuscript architecture or add a clear heading.",
                    )
                )

    for sentence in sentences:
        length = len(words(sentence))
        if length > 60:
            issues.append(
                Issue(
                    "major",
                    "SENTENCE_VERY_LONG",
                    f"A sentence contains {length} words.",
                    evidence=_sentence_excerpt(sentence),
                    suggestion="Split independent claims and keep definitions/results close to their evidence.",
                )
            )
        elif length > 45:
            issues.append(
                Issue(
                    "warning",
                    "SENTENCE_LONG",
                    f"A sentence contains {length} words.",
                    evidence=_sentence_excerpt(sentence),
                    suggestion="Check dependency clarity; split if the sentence carries more than one major claim.",
                )
            )

    novelty_first_patterns = [
        r"\bfor the first time\b",
        r"\b(?:is|are|was|were) the first to\b",
        r"\bthe first (?:model|framework|method|algorithm|study|approach) to\b",
        r"\bfirst-of-its-kind\b",
    ]
    for pattern in novelty_first_patterns:
        for match in re.finditer(pattern, lowered):
            issues.append(
                Issue(
                    "major",
                    "CLAIM_GATE_FIRST",
                    "A priority claim requires a dated full-text novelty audit and an exact novelty dimension.",
                    evidence=_sentence_excerpt(prose[max(0, match.start() - 80) : match.end() + 120]),
                    suggestion="Document the closest full texts, negative evidence, search date, and the exact sense in which the work is first.",
                )
            )

    for match in re.finditer(r"\boutperform(?:s|ed|ing)?\b", lowered):
        issues.append(
            Issue(
                "major",
                "CLAIM_GATE_OUTPERFORM",
                "A superiority claim requires matched-budget, relevant-baseline and uncertainty evidence.",
                evidence=_sentence_excerpt(prose[max(0, match.start() - 80) : match.end() + 120]),
                suggestion="Report matched information/resources, tuned baselines, repeated runs or instances, and uncertainty.",
            )
        )

    probability_one_patterns = (
        r"\balmost surely\b",
        r"\bwith probability (?:one|1)\b",
    )
    probability_contract = re.compile(r"\b(?:probability space|probability measure)\b")
    sampling_law = re.compile(
        r"\b(?:sampling distribution|noise distribution|sampled from|random variables?|"
        r"i\.i\.d\.|independent and identically distributed|martingale)\b"
    )
    linked_probability_support = re.compile(
        r"\b(?:theorem|proposition|lemma)(?:\s+(?:\d+(?:\.\d+)*|[A-Z][A-Za-z0-9_-]*))?\b"
        r"[^.!?]{0,180}\b(?:hence|therefore|implies?|yields?|prove[sd]?|establish(?:es|ed)?)\b"
        r"[^.!?]{0,180}\b(?:almost surely|with probability (?:one|1))\b|"
        r"\b(?:almost surely|with probability (?:one|1))\b[^.!?]{0,120}\b(?:by|under|from)\b"
        r"[^.!?]{0,80}\b(?:theorem|proposition|lemma)\b"
    )
    for pattern in probability_one_patterns:
        for match in re.finditer(pattern, lowered):
            context = lowered[max(0, match.start() - 700) : match.end() + 700]
            claim_sentence = _containing_sentence(lowered, match.start(), match.end())
            if (
                probability_contract.search(context)
                and sampling_law.search(context)
                and linked_probability_support.search(claim_sentence)
            ):
                continue
            issues.append(
                Issue(
                    "major",
                    "CLAIM_GATE_ALMOST_SURE",
                    "A probability-one claim appears without a nearby probability space, sampling law, or formal result.",
                    evidence=_sentence_excerpt(prose[max(0, match.start() - 80) : match.end() + 140]),
                    suggestion=(
                        "Define the probability space and distribution and provide a theorem or statistical design; "
                        "otherwise scope the statement to the tested instances."
                    ),
                )
            )

    uniform_sampling_pattern = re.compile(
        r"\b(?:randomly and uniformly|uniformly random(?:ly)?|uniformly sampled)\b"
    )
    functional_object_pattern = re.compile(
        r"\b(?:control|controls|policy|policies|strategy|strategies|function|functions|trajectory|trajectories)\b"
    )
    functional_representation_pattern = re.compile(
        r"\b(?:basis functions?|coefficients?|finite-dimensional|knot points?|grid values?)\b"
    )
    finite_resolution_pattern = re.compile(
        r"\b(?:\d+[- ]?(?:point|dimensional)|dimension(?:\s+of)?\s+\d+|"
        r"(?:time )?grid\s+(?:with|of)\s+\d+\s+(?:points?|values?))\b"
    )
    reconstruction_pattern = re.compile(
        r"\b(?:piecewise[- ]constant|piecewise[- ]linear|linear interpolation|"
        r"spline interpolation|smoothness rule)\b"
    )
    seed_pattern = re.compile(r"\b(?:random seed|seeds?)\b(?:\s*(?:=|:)?\s*\d+)?")
    for match in uniform_sampling_pattern.finditer(lowered):
        context = _containing_sentence(lowered, match.start(), match.end())
        has_contract = all(
            pattern.search(context)
            for pattern in (
                functional_representation_pattern,
                finite_resolution_pattern,
                reconstruction_pattern,
                seed_pattern,
            )
        )
        if not functional_object_pattern.search(context) or has_contract:
            continue
        issues.append(
            Issue(
                "major",
                "BASELINE_RANDOM_FUNCTION_UNDEFINED",
                "A uniform random functional baseline lacks a nearby finite-dimensional sampling contract.",
                evidence=_sentence_excerpt(prose[max(0, match.start() - 80) : match.end() + 160]),
                suggestion=(
                    "Specify the time grid or basis, dimension, coefficient distribution, interpolation or smoothness, "
                    "and random seeds before using the baseline."
                ),
            )
        )

    solved_successfully_pattern = re.compile(
        r"(?:\b(?:solve[sd]?|resolve[sd]?)\b[^.!?]{0,100}\bsuccessfully\b|"
        r"\bsuccessfully\b[^.!?]{0,100}\b(?:solve[sd]?|resolve[sd]?)\b)"
    )
    solution_certificate_pattern = re.compile(
        r"\b(?:certified optimality gap|verification theorem|global optimality theorem)\b|"
        r"\bsufficient conditions?\b[^.!?]{0,100}\b(?:hold|satisf|prove|establish|theorem)\w*\b|"
        r"\b(?:independent solver|direct collocation|direct transcription|exhaustive search)\b"
        r"[^.!?]{0,140}\b(?:agree|match|confirm|verify|certif|residual|gap|within)\w*\b"
    )
    for match in solved_successfully_pattern.finditer(lowered):
        after = lowered[match.end() : match.end() + 360].split(".", 1)[0]
        before = lowered[max(0, match.start() - 260) : match.start()].rsplit(".", 1)[-1]
        linked_prior_certificate = re.compile(
            r"\b(?:as|independently)\s+(?:verified|confirmed|matched)\s+by\b[^.!?]{0,160}|"
            r"\b(?:because|since)\b[^.!?]{0,120}\bsufficient conditions?\b[^.!?]{0,80}\b(?:hold|satisf)\w*\b"
        )
        if solution_certificate_pattern.search(after) or linked_prior_certificate.search(before):
            continue
        issues.append(
            Issue(
                "major",
                "CLAIM_GATE_SOLVED_SUCCESSFULLY",
                "A solved-successfully claim lacks a nearby sufficiency, optimality-gap, or independent-solver certificate.",
                evidence=_sentence_excerpt(prose[max(0, match.start() - 80) : match.end() + 160]),
                suggestion=(
                    "Describe the output as a necessary-condition, stationary, configured numerical, or among-tested "
                    "solution unless stronger evidence is available."
                ),
            )
        )

    for term, suggestion in OVERCLAIM_RULES.items():
        for match in re.finditer(r"\b" + re.escape(term) + r"\b", lowered):
            code_term = {"causally": "causal", "robustness": "robust"}.get(term, term)
            issues.append(
                Issue(
                    "major" if term in MAJOR_OVERCLAIM_TERMS else "warning",
                    "CLAIM_GATE_" + code_term.upper().replace("-", "_"),
                    f"Evidence gate required for the term '{term}'.",
                    evidence=_sentence_excerpt(prose[max(0, match.start() - 80) : match.end() + 120]),
                    suggestion=suggestion,
                )
            )

    recovery_patterns = (
        r"\brecover(?:ed|ing|y)?\s+(?:the\s+)?(?:true\s+)?parameters?\b",
        r"\bparameter\s+recovery\b",
        r"\brecover(?:ed|ing|y)?\s+(?:the\s+)?ground\s+truth\b",
    )
    for pattern in recovery_patterns:
        for match in re.finditer(pattern, lowered):
            context = lowered[max(0, match.start() - 500) : match.end() + 500]
            if not re.search(r"\b(generated|synthetic truth|ground truth|identif|partial identif|independently known)\b", context):
                issues.append(
                    Issue(
                        "major",
                        "CLAIM_GATE_RECOVERY",
                        "A recovery claim lacks nearby generated-truth, independently known truth, or identifiability scope.",
                        evidence=_sentence_excerpt(prose[max(0, match.start() - 80) : match.end() + 120]),
                        suggestion="Use calibration/effective-rate language or document ground truth, identifiability, and independent validation.",
                    )
                )

    for match in re.finditer(r"\boptimal(?:ly|ity)?\b", lowered):
        context = lowered[max(0, match.start() - 500) : match.end() + 500]
        if not re.search(r"\b(theorem|necessary condition|sufficient condition|global|local|stationar|pontryagin|optimality gap)\b", context):
            issues.append(
                Issue(
                    "major",
                    "CLAIM_GATE_OPTIMAL",
                    "An optimality term appears without nearby scope or theoretical/numerical qualification.",
                    evidence=_sentence_excerpt(prose[max(0, match.start() - 80) : match.end() + 120]),
                    suggestion="State global/local/necessary/stationary/among-tested scope and provide the corresponding evidence.",
                )
            )

    for match in re.finditer(r"\bequilibrium\b", lowered):
        context = lowered[max(0, match.start() - 600) : match.end() + 600]
        positive_cue = False
        for cue in re.finditer(r"\b(best response|deviation|residual|nash|stackelberg|saddle|verification)\b", context):
            window = context[max(0, cue.start() - 90) : cue.end()]
            negated = re.search(
                r"\b(no|without|lack(?:s|ed|ing)?|absent)\b[^.!?]{0,70}\b" + re.escape(cue.group(1)) + r"\b",
                window,
            )
            if not negated:
                positive_cue = True
                break
        if not positive_cue:
            issues.append(
                Issue(
                    "major",
                    "CLAIM_GATE_EQUILIBRIUM",
                    "An equilibrium claim lacks a nearby solution concept or independent verification cue.",
                    evidence=_sentence_excerpt(prose[max(0, match.start() - 80) : match.end() + 120]),
                    suggestion="Define the solution concept and report best-response/deviation/residual checks.",
                )
            )

    for match in re.finditer(r"\bsignificant(?:ly)?\b", lowered):
        if not _nearby_numeric_support(prose, match.start()) and not re.search(
            r"\b(p\s*[<=>]|confidence interval|statistical|effect size|anova|t-test|wilcoxon)\b",
            lowered[max(0, match.start() - 300) : match.end() + 300],
        ):
            issues.append(
                Issue(
                    "warning",
                    "CLAIM_GATE_SIGNIFICANT",
                    "'Significant' appears without nearby statistical or explicitly quantified support.",
                    evidence=_sentence_excerpt(prose[max(0, match.start() - 80) : match.end() + 120]),
                    suggestion="Report the test/effect size or replace with a precise numerical description.",
                )
            )

    transition_counts = metrics.get("transitions", {})
    total_words = max(1, int(metrics.get("words", 0)))
    for transition, count in transition_counts.items():
        if count >= 3 and count * 500 / total_words > 3:
            issues.append(
                Issue(
                    "warning",
                    "TRANSITION_REPETITION",
                    f"'{transition}' appears {count} times in {total_words} words.",
                    suggestion="Keep the connector only where it expresses the exact logical relation.",
                )
            )

    adjacent_transition = re.compile(
        r"(?i)(however|furthermore|moreover|therefore|on this basis)[^.!?]*[.!?]\s*"
        r"(?:however|furthermore|moreover|therefore|on this basis)\b"
    )
    if adjacent_transition.search(prose):
        issues.append(
            Issue(
                "warning",
                "ADJACENT_CONNECTORS",
                "Adjacent sentences begin with heavy transition markers.",
                suggestion="Make the causal/comparative relation explicit and vary sentence openings.",
            )
        )

    legacy_patterns = {
        r"\bpresents challenging\b": ("LEGACY_WORD_FORM", "Use 'presents challenges' or 'is challenging'."),
        r"\bthereby evidencing\b": ("LEGACY_EVIDENCING", "Prefer a direct result or 'thereby demonstrating'."),
        r"\bthis article would be helpful\b": ("LEGACY_WEAK_ENDING", "State a bounded operational implication and limitations."),
        r"\bcurrent models do not\b[^.]{0,120}\bit lacks\b": ("LEGACY_AGREEMENT", "Keep plural subject agreement across coordinated clauses."),
    }
    for pattern, (code, suggestion) in legacy_patterns.items():
        match = re.search(pattern, lowered)
        if match:
            issues.append(
                Issue(
                    "major",
                    code,
                    "A known legacy language artifact was detected.",
                    evidence=_sentence_excerpt(prose[max(0, match.start() - 60) : match.end() + 100]),
                    suggestion=suggestion,
                )
            )

    if re.search(r"\[(?:TBD|TODO|CITATION|REF|XX|\?+)\]", text, flags=re.I):
        issues.append(
            Issue(
                "major",
                "PLACEHOLDER_REMAINS",
                "A bracketed placeholder remains in the manuscript.",
                suggestion="Resolve or explicitly retain it as a draft-only blocker before submission.",
            )
        )

    conclusion_sections = [section.text for section in segment_sections(text) if section.name == "conclusion"]
    if conclusion_sections:
        conclusion = " ".join(conclusion_sections).lower()
        if not re.search(r"\b(limit|future work|future research|does not|remains|extension)\b", conclusion):
            issues.append(
                Issue(
                    "warning",
                    "CONCLUSION_LIMITATIONS_MISSING",
                    "The conclusion does not clearly signal limitations or a bounded future direction.",
                    suggestion="Add limitations tied to assumptions, data, information, control implementation or scale.",
                )
            )

    return _deduplicate(issues)


def _deduplicate(issues: Iterable[Issue]) -> list[Issue]:
    seen: set[tuple[str, str, str]] = set()
    result: list[Issue] = []
    for issue in issues:
        key = (issue.code, issue.message, issue.evidence)
        if key not in seen:
            seen.add(key)
            result.append(issue)
    severity_order = {"blocking": 0, "major": 1, "warning": 2, "info": 3}
    result.sort(key=lambda item: (severity_order.get(item.severity, 9), item.code, item.evidence))
    return result


def render_markdown_report(issues: Iterable[Issue], source: str | None = None) -> str:
    issue_list = list(issues)
    counts: dict[str, int] = {}
    for issue in issue_list:
        counts[issue.severity] = counts.get(issue.severity, 0) + 1
    decision = "PASS WITH NO AUTOMATED FLAGS" if not issue_list else "REVIEW REQUIRED"
    lines = ["# Manuscript Preflight Report", "", f"**Source:** `{source or 'in-memory text'}`", f"**Decision:** {decision}", ""]
    if counts:
        lines.append("## Summary")
        lines.append("")
        for severity in ("blocking", "major", "warning", "info"):
            if counts.get(severity):
                lines.append(f"- {severity}: {counts[severity]}")
        lines.append("")
    if not issue_list:
        lines.append("No deterministic flags were raised. This does not replace technical, novelty, citation, statistical or journal review.")
        lines.append("")
        return "\n".join(lines)
    lines.append("## Findings")
    lines.append("")
    for index, issue in enumerate(issue_list, 1):
        lines.append(f"### {index}. [{issue.severity.upper()}] {issue.code}")
        lines.append("")
        lines.append(issue.message)
        lines.append("")
        if issue.evidence:
            lines.append(f"**Evidence:** {issue.evidence}")
            lines.append("")
        if issue.suggestion:
            lines.append(f"**Action:** {issue.suggestion}")
            lines.append("")
    lines.append("## Boundary")
    lines.append("")
    lines.append("The linter flags language and traceability risks. It does not determine whether a theorem is correct, a citation is real, a result is reproducible, or a claim is novel.")
    lines.append("")
    return "\n".join(lines)
