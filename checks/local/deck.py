"""Deck: every card has two sides, a source that resolves to a heading, and a front no other card has; a generated
card is marked checked.

Runs on the TSV files `[deck] files` names in checks/config.toml (shapes/deck.md). The header row names the columns
front, back, source and tags, in any order; Anki imports the file as it is.

- header: the four columns are present (exact);
- two sides: no empty front or back (exact);
- duplicate: no two fronts equal once case and spaces are set aside (exact): confusable cards interfere;
- source: the source links a file that exists, beside the deck, and a heading of it when an anchor is given (exact);
- checked: a card tagged `generated` is also tagged `checked`, once a person has read it (exact);
- yes or no: a front opening with an auxiliary verb whose back is yes, no, true or false (heuristic);
- long answer: a back past `long_answer` words (heuristic, PROVISIONAL);
- list answer: a back of more than `list_items` items, separated by semicolons or line breaks (heuristic, PROVISIONAL).

What a run with no error guarantees: every card can be shown and answered, traced to the section it tests, and told
apart from the others by its front; no generated card is unread. What it does not: that a card tests understanding
rather than a phrase, or that a back is right (judgment). Time O(cards + lines of the linked files).
"""
from __future__ import annotations

import csv
import io
import re
import sys
from pathlib import Path

from framework.check_api import Finding, files_in_scope, matches_any, prose_only

sys.path.insert(0, str(Path(__file__).parent))
import learning_markup as markup  # noqa: E402  (a sibling of this file, not a check)

NAME = "deck"
EXACT = True

COLUMNS = ("front", "back", "source", "tags")
AUXILIARY = re.compile(r"^(is|are|was|were|does|do|did|can|could|will|would|should|has|have|had|must)\b", re.IGNORECASE)
YES_NO = {"yes", "no", "true", "false"}
SEPARATOR = re.compile(r";|<br\s*/?>", re.IGNORECASE)


def check(root: Path, config: dict) -> list[Finding]:
    settings = config.get("deck", {})
    patterns = settings.get("files", [])
    if not patterns:
        return []
    findings = []
    for path in files_in_scope(root, config, {".tsv"}):
        if matches_any(path, patterns) and not matches_any(path, settings.get("exempt", [])):
            text = (root / path).read_text(encoding="utf-8", errors="replace")
            findings += check_text(root, path, text, settings)
    return findings


def anchors(file: Path) -> set[str]:
    lines = prose_only(file.read_text(encoding="utf-8", errors="replace")).splitlines()
    return {markup.slug(section.title) for section in markup.sections(lines)}


def check_text(root: Path, path: str, text: str, settings: dict) -> list[Finding]:
    rows = list(csv.reader(io.StringIO(text), delimiter="\t", quoting=csv.QUOTE_NONE))
    if not rows:
        return [Finding(NAME, path, 1, "an empty deck")]
    header = [cell.strip().lower() for cell in rows[0]]
    missing = [column for column in COLUMNS if column not in header]
    if missing:
        return [Finding(NAME, path, 1, f"the header lacks {', '.join(missing)}: write front, back, source, tags")]
    at = {column: header.index(column) for column in COLUMNS}
    folder = (root / path).parent
    seen, cache, found = {}, {}, []
    for number, row in enumerate(rows[1:], start=2):
        if not any(cell.strip() for cell in row):
            continue
        cell = lambda column: row[at[column]].strip() if at[column] < len(row) else ""
        front, back, source, tags = (cell(column) for column in COLUMNS)
        if not front or not back:
            found.append(Finding(NAME, path, number, "a card with an empty side: one question, one answer"))
        key = " ".join(front.lower().split())
        if key and key in seen:
            found.append(Finding(NAME, path, number, f"the same front as the card on line {seen[key]}: "
                                                     "cards a learner cannot tell apart interfere"))
        seen.setdefault(key, number)
        found += source_of(path, number, source, folder, root, cache)
        tag_set = {tag.lower() for tag in re.split(r"[\s,;]+", tags) if tag}
        if "generated" in tag_set and "checked" not in tag_set:
            found.append(Finding(NAME, path, number, "a generated card no person has checked: read it, then tag it checked"))
        if AUXILIARY.match(front) and back.lower().strip(" .!") in YES_NO:
            found.append(Finding(NAME, path, number, "a yes-or-no card: ask for the thing itself", "warning"))
        if markup.words(back) > settings.get("long_answer", 25):
            found.append(Finding(NAME, path, number, f"an answer past {settings.get('long_answer', 25)} words: "
                                                     "split it into cards", "warning"))
        if len(SEPARATOR.split(back)) > settings.get("list_items", 3):
            found.append(Finding(NAME, path, number, "an answer that is a list: one card per item", "warning"))
    return found


def source_of(path: str, number: int, source: str, folder: Path, root: Path, cache: dict) -> list[Finding]:
    if not source:
        return [Finding(NAME, path, number, "a card with no source: link the section it tests")]
    target, _, anchor = source.partition("#")
    file = (folder / target).resolve()
    if not target or not file.is_file() or root.resolve() not in file.parents:
        return [Finding(NAME, path, number, f"the source {source} is not a file of this repository")]
    if anchor:
        if file not in cache:
            cache[file] = anchors(file)
        if anchor not in cache[file]:
            return [Finding(NAME, path, number, f"the source {source} names no heading of {target}")]
    return []
