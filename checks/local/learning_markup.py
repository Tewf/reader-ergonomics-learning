"""The markup the checks of the study shapes read: headings and their sections, folds, quotes, ids and slugs.

Not a check (it has no NAME), so run.py loads it and passes it by; lesson.py, sheet.py and deck.py import it. Its
records are NamedTuples, not dataclasses: run.py loads a local file without registering it as a module, and a
dataclass needs that registration. The
markup is the one shapes/README.md gives. Every function takes the lines of a file whose fenced blocks and inline
code are already blanked (framework.check_api.prose_only), so line numbers match the file and code is never read as
markup. Time O(lines) for each function.
"""
from __future__ import annotations

import re
from typing import NamedTuple

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
DETAILS_OPEN = re.compile(r"<details\b[^>]*>", re.IGNORECASE)
DETAILS_CLOSE = re.compile(r"</details\s*>", re.IGNORECASE)
SUMMARY = re.compile(r"<summary\b[^>]*>(.*?)</summary\s*>", re.IGNORECASE | re.DOTALL)
CALLOUT = re.compile(r"^\s*>\s*\[!([\w-]+)\]([+-]?)\s*(.*)$")  # Obsidian: > [!type]- title; "-" folds it
QUARTO_OPEN = re.compile(r"^\s*(:{3,})\s*\{([^}]*)\}")
QUARTO_CLOSE = re.compile(r"^\s*(:{3,})\s*$")
TITLE_ATTRIBUTE = re.compile(r"""title\s*=\s*["']([^"']*)["']""")
COLLAPSED = re.compile(r"""collapse\s*=\s*["']?true""")
WORD = re.compile(r"[^\W_]+(?:'[^\W_]+)?")
TAG = re.compile(r"<[^>]+>")


class Section(NamedTuple):
    level: int
    title: str
    line: int   # 1-based line of the heading
    start: int  # 0-based index of the first line after the heading
    end: int    # 0-based index one past the section's last line (the next heading of the same or a higher level)


class Fold(NamedTuple):
    label: str  # the summary, the callout's type and title, or the Quarto title, lower case
    line: int   # 1-based line where the fold opens
    words: int  # words inside it, markup removed
    end: int    # 0-based index one past its last line


def sections(lines: list[str]) -> list[Section]:
    """Every heading of the file, with the range of lines it governs."""
    heads = [(index, len(match.group(1)), match.group(2)) for index, line in enumerate(lines)
             if (match := HEADING.match(line))]
    found = []
    for position, (index, level, title) in enumerate(heads):
        end = next((later for later, later_level, _ in heads[position + 1:] if later_level <= level), len(lines))
        found.append(Section(level, title, index + 1, index + 1, end))
    return found


def named(all_sections: list[Section], names: list[str]) -> list[Section]:
    """The sections whose title, stripped of ids and trailing colons, is one of names (case ignored)."""
    wanted = {name.lower() for name in names}
    return [section for section in all_sections if section.title.strip().rstrip(":").lower() in wanted]


def words(text: str) -> int:
    return len(WORD.findall(TAG.sub(" ", text)))


def folds(lines: list[str], start: int, end: int) -> list[Fold]:
    """The folded blocks between start and end: <details>, an Obsidian callout folded with "-", a Quarto callout
    with collapse="true". An unfolded callout (no "-", or "+") is not a fold: its content is in the line of sight."""
    found, index = [], start
    while index < end:
        line = lines[index]
        if DETAILS_OPEN.search(line):
            close = next((later for later in range(index, end) if DETAILS_CLOSE.search(lines[later])), end - 1)
            body = "\n".join(lines[index:close + 1])
            summary = SUMMARY.search(body)
            label = TAG.sub("", summary.group(1)).strip().lower() if summary else ""
            inner = SUMMARY.sub(" ", body)
            found.append(Fold(label, index + 1, words(DETAILS_OPEN.sub(" ", DETAILS_CLOSE.sub(" ", inner))), close + 1))
            index = close + 1
            continue
        callout = CALLOUT.match(line)
        if callout:
            close = index + 1
            while close < end and lines[close].lstrip().startswith(">"):
                close += 1
            if callout.group(2) == "-":
                body = " ".join(text.lstrip()[1:] for text in lines[index + 1:close])
                label = f"{callout.group(1)} {callout.group(3)}".strip().lower()
                found.append(Fold(label, index + 1, words(body), close))
            index = close
            continue
        quarto = QUARTO_OPEN.match(line)
        if quarto:
            fence = quarto.group(1)
            close = next((later for later in range(index + 1, end)
                          if (match := QUARTO_CLOSE.match(lines[later])) and len(match.group(1)) >= len(fence)), end - 1)
            attributes = quarto.group(2)
            if COLLAPSED.search(attributes):
                title = TITLE_ATTRIBUTE.search(attributes)
                classes = " ".join(re.findall(r"\.callout-([\w-]+)", attributes))
                label = f"{classes} {title.group(1) if title else ''}".strip().lower()
                found.append(Fold(label, index + 1, words("\n".join(lines[index + 1:close])), close + 1))
            index = close + 1
            continue
        index += 1
    return found


def labelled(fold: Fold, labels: list[str]) -> bool:
    """True when one of labels, as a word, names the fold: "Answer" names <summary>Answer</summary> and [!answer]-."""
    return any(re.search(rf"\b{re.escape(label.lower())}\b", fold.label) for label in labels)


def quotes(lines: list[str]) -> list[tuple[int, list[str]]]:
    """Runs of consecutive quoted lines, as (1-based first line, the lines without their leading ">")."""
    found, index = [], 0
    while index < len(lines):
        if lines[index].lstrip().startswith(">"):
            first = index
            body = []
            while index < len(lines) and lines[index].lstrip().startswith(">"):
                body.append(lines[index].lstrip()[1:].strip())
                index += 1
            found.append((first + 1, body))
            continue
        index += 1
    return found


def traps(lines: list[str], labels: list[str]) -> list[tuple[int, list[str]]]:
    """Every trap block, as (1-based first line, its lines), in any of three forms: a quote opening with a bold label
    (> **Trap:** ...), an Obsidian callout whose type or title is the label (> [!warning] Trap), and a Quarto callout
    whose title opens with it (::: {.callout-warning title="Trap"}). The explained books of the held-out test wrote
    all 134 of their traps in the last form."""
    found = [(line, body) for line, body in quotes(lines) if body and opens_with_label(body[0], labels)]
    wanted = [label.lower() for label in labels]
    for line, body in quotes(lines):
        callout = CALLOUT.match(">" + body[0]) if body else None
        if callout and (callout.group(1).lower() in wanted or callout.group(3).strip().lower().split(":")[0] in wanted):
            found.append((line, body[1:]))
    index = 0
    while index < len(lines):
        opening = QUARTO_OPEN.match(lines[index])
        if opening:
            fence = opening.group(1)
            close = next((later for later in range(index + 1, len(lines))
                          if (match := QUARTO_CLOSE.match(lines[later])) and len(match.group(1)) >= len(fence)), len(lines))
            title = TITLE_ATTRIBUTE.search(opening.group(2))
            if title and any(title.group(1).strip().lower().startswith(label) for label in wanted):
                found.append((index + 1, lines[index + 1:close]))
            index = close + 1
            continue
        index += 1
    return sorted(found)


def callout_questions(lines: list[str], prefixes: list[str]) -> list[tuple[int, str, bool, int]]:
    """Questions written as Obsidian callouts, the question in the title and the answer inside, as the S7 vault does
    (> [!QUESTION]- Check: <question>): (1-based line, the title after its prefix, folded or not, words of the answer).
    A callout counts when its type is question or its title opens with one of prefixes."""
    found = []
    for line, body in quotes(lines):
        callout = CALLOUT.match(">" + body[0]) if body else None
        if not callout:
            continue
        title = callout.group(3).strip()
        prefix = next((p for p in prefixes if title.lower().startswith(p.lower())), None)
        if callout.group(1).lower() == "question" or prefix:
            question = title[len(prefix):].strip() if prefix else title
            found.append((line, question, callout.group(2) == "-", words(" ".join(body[1:]))))
    return found


def opens_with_label(text: str, labels: list[str]) -> bool:
    """True when text opens with a bold label followed by a colon: **Trap:** or **Trap**:."""
    return any(re.match(rf"\*\*{re.escape(label)}\s*:?\*\*\s*:?", text, re.IGNORECASE) for label in labels)


def holds_label(lines: list[str], labels: list[str]) -> bool:
    return any(re.search(rf"\*\*{re.escape(label)}\s*:?\*\*", line, re.IGNORECASE) for line in lines for label in labels)


def slug(heading: str) -> str:
    """The anchor GitHub gives a heading: lower case, punctuation dropped, spaces as hyphens."""
    text = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return text.replace(" ", "-")
