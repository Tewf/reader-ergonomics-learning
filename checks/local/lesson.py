"""Lesson: every objective is tested, every question names an objective and folds its answer, every trap is refuted.

Runs on the files `[lesson] files` names in checks/config.toml: lessons and study guides (shapes/lesson.md,
shapes/study-guide.md), and their question blocks (shapes/question-block.md). The markup is the one shapes/README.md
gives; it is read by learning_markup.py, outside fenced blocks and inline code.

- objectives: a section named in `objective_headings` lists ids as `- **O1** ...`; no id twice (exact);
- tagged: each numbered item of a `check_headings` section opens with an objective id (exact);
- known: that id is listed among the objectives (exact);
- tested: every objective is the id of at least one question (exact): the alignment the shapes ask for;
- folded: each question is followed, before the next one, by a fold (exact);
- explains: the fold holds at least `min_answer_words` words, more than a bare key (heuristic, PROVISIONAL bound);
- options: a question with two or more lettered options has between `options` bounds, and none reads "all of the
  above" or "none of the above" (heuristic: the item-writing rules are a convention, tested for exams, not learning);
- refuted: a trap, a quote opening with a `trap_labels` label or a callout titled with one, holds a `why_labels`
  label (heuristic, a warning: a trap can refute in prose without the label, as all 134 traps of the held-out books
  did, so a program sees the label and not the refutation);
- callout questions: a question written as a callout (`> [!QUESTION]- Check: ...`, the S7 vault's form) is folded
  (exact) and its answer explains (heuristic); in a lesson it also names an objective.

questions.py runs the same rules on notes with `align` off: no objectives are asked for, and questions need no tag.

What a run with no error guarantees, for the declared files: objectives and questions are aligned both ways, and
every question's answer is out of the line of sight. What it does not: that a trap refutes its idea (a warning reads
only the label), that a question tests its objective, that an answer is right, that a trap names the misconception
learners actually hold (judgment).
Time O(lines) per file.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from framework.check_api import MARKDOWN_SUFFIXES, Finding, files_in_scope, matches_any, prose_only

sys.path.insert(0, str(Path(__file__).parent))
import learning_markup as markup  # noqa: E402  (a sibling of this file, not a check)

NAME = "lesson"
EXACT = True

OBJECTIVE = re.compile(r"^\s*[-*+]\s+\*\*(O\d+)\*\*")
QUESTION = re.compile(r"^(\d+)[.)]\s+(.*)$")
QUESTION_ID = re.compile(r"^\*\*(O\d+)\*\*")
OPTION = re.compile(r"^\s+[-*+]\s+(?:[a-z][.)]|\([a-z]\))\s+(.*)$")
ALL_OR_NONE = re.compile(r"\b(all|none) of the above\b", re.IGNORECASE)


def check(root: Path, config: dict) -> list[Finding]:
    return run(root, config.get("lesson", {}), config, align=True, name=NAME)


def run(root: Path, settings: dict, config: dict, align: bool, name: str) -> list[Finding]:
    """The checks over the files settings declares; questions.py calls it for notes, with align False."""
    patterns = settings.get("files", [])
    if not patterns:
        return []
    findings = []
    for path in files_in_scope(root, config, MARKDOWN_SUFFIXES):
        if matches_any(path, patterns) and not matches_any(path, settings.get("exempt", [])):
            text = (root / path).read_text(encoding="utf-8", errors="replace")
            findings += check_text(path, text, settings, align, name)
    return findings


def check_text(path: str, text: str, settings: dict, align: bool = True, name: str = NAME) -> list[Finding]:
    found = check_lines(path, prose_only(text).splitlines(), settings, align)
    return [Finding(name, f.path, f.line, f.message, f.kind) for f in found]


def check_lines(path: str, lines: list[str], settings: dict, align: bool) -> list[Finding]:
    all_sections = markup.sections(lines)
    found = []
    objectives = {}
    for section in markup.named(all_sections, settings.get("objective_headings", ["Objectives"])):
        for index in range(section.start, section.end):
            match = OBJECTIVE.match(lines[index])
            if not match:
                continue
            if match.group(1) in objectives:
                found.append(Finding(NAME, path, index + 1, f"objective {match.group(1)} is listed twice: give each its own id"))
            objectives.setdefault(match.group(1), index + 1)
    if align and not objectives:
        found.append(Finding(NAME, path, 1, "no objective listed as `- **O1** ...` under Objectives: "
                                            "a lesson states what the learner will be able to do"))
    tested = set()
    callouts = markup.callout_questions(lines, settings.get("question_prefixes", ["Check:"]))
    for section in markup.named(all_sections, settings.get("check_headings", ["Check yourself"])):
        questions = [index for index in range(section.start, section.end) if QUESTION.match(lines[index])]
        if not questions and not any(section.start <= line - 1 < section.end for line, *_ in callouts):
            found.append(Finding(NAME, path, section.line, "a Check yourself section with no numbered question"))
        for position, index in enumerate(questions):
            stop = questions[position + 1] if position + 1 < len(questions) else section.end
            found += question(path, lines, index, stop, objectives, tested, settings, align)
    for line, title, folded, answer_words in callouts:
        if align:
            found += aligned(path, line, title, objectives, tested)
        if not folded:
            found.append(Finding(NAME, path, line, "a question callout left open: fold it with `-`, so the answer "
                                                   "stays out of sight until the question is tried"))
        elif answer_words < settings.get("min_answer_words", 8):
            found.append(Finding(NAME, path, line, "the answer is only a key: add why, which teaches more than the "
                                                   "key alone", "warning"))
    for objective, line in (objectives.items() if align else []):
        if objective not in tested:
            found.append(Finding(NAME, path, line, f"objective {objective} is tested by no question: "
                                                   "add a question tagged with it, or drop the objective"))
    found += traps(path, lines, settings)
    return found


def aligned(path: str, line: int, question_text: str, objectives: dict, tested: set) -> list[Finding]:
    """A question names an objective that exists; the objective is then counted as tested."""
    tag = QUESTION_ID.match(question_text)
    if not tag:
        return [Finding(NAME, path, line, "a question that names no objective: open it with `**O1**`")]
    if tag.group(1) not in objectives:
        return [Finding(NAME, path, line, f"the question names {tag.group(1)}, which no objective lists")]
    tested.add(tag.group(1))
    return []


def question(path: str, lines: list[str], index: int, stop: int, objectives: dict, tested: set,
             settings: dict, align: bool = True) -> list[Finding]:
    found = []
    if align:
        found += aligned(path, index + 1, QUESTION.match(lines[index]).group(2), objectives, tested)
    folds = markup.folds(lines, index + 1, stop)
    if not folds:
        found.append(Finding(NAME, path, index + 1, "a question with no folded answer: put the answer in "
                                                    "<details>, a folded callout, or a collapsed Quarto callout"))
    elif max(fold.words for fold in folds) < settings.get("min_answer_words", 8):
        found.append(Finding(NAME, path, folds[0].line, "the answer is only a key: add why, which teaches more "
                                                        "than the key alone", "warning"))
    first_fold = folds[0].line - 1 if folds else stop
    options = [match.group(1) for line in lines[index + 1:first_fold] if (match := OPTION.match(line))]
    low, high = settings.get("options", [3, 4])
    if len(options) >= 2 and not low <= len(options) <= high:
        found.append(Finding(NAME, path, index + 1, f"a multiple-choice item with {len(options)} options, "
                                                    f"outside {low} to {high}", "warning"))
    for option in options:
        if ALL_OR_NONE.search(option):
            found.append(Finding(NAME, path, index + 1, "an option reads all or none of the above, "
                                                        "which the item-writing guidelines rule out", "warning"))
    return found


def traps(path: str, lines: list[str], settings: dict) -> list[Finding]:
    trap_labels = settings.get("trap_labels", ["Trap"])
    why_labels = settings.get("why_labels", ["Why not"])
    return [Finding(NAME, path, line, f"a trap with no {why_labels[0]}: label the refutation, or write it, saying "
                                      "why the idea is wrong and then the accepted one, since refutation is what "
                                      "teaches", "warning")
            for line, body in markup.traps(lines, trap_labels) if not markup.holds_label(body, why_labels)]
