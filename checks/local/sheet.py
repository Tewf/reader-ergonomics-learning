"""Sheet: every item names a declared type, each type opens with a worked example, every problem folds its answer
after its hint, and a mixed review brings the types back.

Runs on the files `[sheet] files` names in checks/config.toml (shapes/exercise-sheet.md). Items are headings that
open with one of `item_kinds` and name a type: `### Problem (T1): ...`. The markup is read by learning_markup.py,
outside fenced blocks and inline code.

- types: a `types_headings` section lists ids as `- **T1** ...` (exact);
- typed: every item names a type, and the type is listed (exact);
- example first: the first item of each type is a worked example (exact): the order measured for novices;
- faded: each type has a completion problem in its own part (heuristic, a warning: fading is measured for novices
  and reverses for experts, so a sheet for experts may leave it out);
- folded: every problem and completion problem folds an answer or a solution (exact);
- hint first: in a problem that has both, the hint fold comes before the answer and the solution (exact);
- hinted: a problem has a hint (heuristic: a hint on paper is a convention; hints are measured only in software);
- mixed: a `mixed_headings` section holds problems of at least `mixed_types` types (heuristic, PROVISIONAL);
- short block: outside the mixed review, no type has more than `max_block` problems (heuristic, PROVISIONAL).

What a run with no error guarantees, for the declared files: every type opens with a solved example before any
problem of it, and no answer of a problem is in the line of sight before its hint. What it does not: that the worked
example is solved well, that the completion problem leaves the last steps, that problems vary (judgment).
Time O(lines) per file.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from framework.check_api import MARKDOWN_SUFFIXES, Finding, files_in_scope, matches_any, prose_only

sys.path.insert(0, str(Path(__file__).parent))
import learning_markup as markup  # noqa: E402  (a sibling of this file, not a check)

NAME = "sheet"
EXACT = True

TYPE = re.compile(r"^\s*[-*+]\s+\*\*(T\d+)\*\*")
ITEM_TYPE = re.compile(r"\((T\d+)\)")
KINDS = {"example": "Worked example", "complete": "Complete", "problem": "Problem"}


def check(root: Path, config: dict) -> list[Finding]:
    settings = config.get("sheet", {})
    patterns = settings.get("files", [])
    if not patterns:
        return []
    findings = []
    for path in files_in_scope(root, config, MARKDOWN_SUFFIXES):
        if matches_any(path, patterns) and not matches_any(path, settings.get("exempt", [])):
            text = (root / path).read_text(encoding="utf-8", errors="replace")
            findings += check_text(path, text, settings)
    return findings


def kind_of(title: str, kinds: dict) -> str | None:
    lowered = title.lower()
    return next((kind for kind, word in kinds.items() if lowered.startswith(word.lower())), None)


def check_text(path: str, text: str, settings: dict) -> list[Finding]:
    lines = prose_only(text).splitlines()
    all_sections = markup.sections(lines)
    kinds = {**KINDS, **settings.get("item_kinds", {})}
    found = []
    types = {}
    for section in markup.named(all_sections, settings.get("types_headings", ["Types"])):
        for index in range(section.start, section.end):
            if match := TYPE.match(lines[index]):
                types.setdefault(match.group(1), index + 1)
    if not types:
        found.append(Finding(NAME, path, 1, "no type listed as `- **T1** ...` under Types: name each type of problem"))
    mixed = markup.named(all_sections, settings.get("mixed_headings", ["Mixed review"]))
    in_mixed = lambda section: any(m.start <= section.line - 1 < m.end for m in mixed)
    first_item, block_problems, mixed_types, completed = {}, {}, set(), set()
    for section in all_sections:
        kind = kind_of(section.title, kinds)
        if not kind:
            continue
        tag = ITEM_TYPE.search(section.title)
        if not tag:
            found.append(Finding(NAME, path, section.line, f"an item with no type: write `{kinds[kind]} (T1): ...`"))
            continue
        item_type = tag.group(1)
        if item_type not in types:
            found.append(Finding(NAME, path, section.line, f"the item names {item_type}, which Types does not list"))
        if in_mixed(section):
            mixed_types.add(item_type)
        else:
            first_item.setdefault(item_type, (kind, section.line))
            if kind == "complete":
                completed.add(item_type)
            if kind == "problem":
                block_problems[item_type] = block_problems.get(item_type, 0) + 1
        if kind in ("problem", "complete"):
            found += folds_of(path, lines, section, kind, settings)
    for item_type, (kind, line) in first_item.items():
        if kind != "example":
            found.append(Finding(NAME, path, line, f"type {item_type} opens without a worked example: solve its "
                                                   "first problem in full before asking for one"))
    for item_type, (kind, line) in first_item.items():
        if kind == "example" and item_type not in completed:
            found.append(Finding(NAME, path, line, f"type {item_type} goes from its worked example to whole problems "
                                                   "with no completion problem: fading the steps helps novices",
                                 "warning"))
    for item_type, line in types.items():
        if item_type not in first_item and item_type not in mixed_types:
            found.append(Finding(NAME, path, line, f"type {item_type} is listed and has no item", "warning"))
    max_block = settings.get("max_block", 4)
    for item_type, count in block_problems.items():
        if count > max_block:
            found.append(Finding(NAME, path, types.get(item_type, 1), f"type {item_type} has {count} problems in "
                                 f"its own part, past {max_block}: move some to the mixed review", "warning"))
    if not mixed:
        found.append(Finding(NAME, path, 1, "no Mixed review: bring back the types of earlier sheets", "warning"))
    elif len(mixed_types) < settings.get("mixed_types", 2):
        found.append(Finding(NAME, path, mixed[0].line, f"the mixed review holds {len(mixed_types)} type(s), fewer "
                             f"than {settings.get('mixed_types', 2)}", "warning"))
    return found


def folds_of(path: str, lines: list[str], section, kind: str, settings: dict) -> list[Finding]:
    folds = markup.folds(lines, section.start, section.end)
    hints = [fold for fold in folds if markup.labelled(fold, settings.get("hint_labels", ["Hint"]))]
    keys = [fold for fold in folds if markup.labelled(fold, settings.get("answer_labels", ["Answer"]) +
                                                      settings.get("solution_labels", ["Solution"]))]
    found = []
    if not keys:
        found.append(Finding(NAME, path, section.line, "no folded answer or solution: fold it, so it stays out of "
                                                       "sight until the problem is tried"))
    if hints and keys and min(fold.line for fold in keys) < min(fold.line for fold in hints):
        found.append(Finding(NAME, path, keys[0].line, "the answer comes before the hint: put the hint first"))
    if kind == "problem" and not hints:
        found.append(Finding(NAME, path, section.line, "a problem with no hint before its answer", "warning"))
    return found
