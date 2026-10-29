"""Tests of the checks of the study shapes: lesson.py, sheet.py and deck.py in checks/local.

Each test starts from a document that passes and breaks one rule, so a test fails if a check stops seeing what it is
for. The examples of shapes/examples must pass every check. Run with the standard's checks on the path:

    READER_ERGONOMICS_CHECKS=<reader-ergonomics>/checks python3 -m unittest discover -s checks
"""
from __future__ import annotations

import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.environ.get("READER_ERGONOMICS_CHECKS", str(Path(__file__).resolve().parents[2] / "reader-ergonomics" / "checks")))
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def load(name: str):
    spec = importlib.util.spec_from_file_location(f"local_{name}", HERE / "local" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


lesson, sheet, deck = load("lesson"), load("sheet"), load("deck")
questions = lesson  # questions.py is lesson.run with align off; its rules are tested through check_text
LESSON = {"min_answer_words": 8, "options": [3, 4]}
SHEET = {"mixed_types": 2, "max_block": 4}
DECK = {"long_answer": 25, "list_items": 3}

GOOD_LESSON = """# A subject

> What it teaches.

## Objectives

- **O1** Compute a thing.
- **O2** Explain a thing.

## Part

> **Trap:** a wrong idea.
> **Why not:** the reason, then the right idea.

### Check yourself

1. **O1** First question?

   <details><summary>Answer</summary>
   The answer, then why it holds, in a full sentence.
   </details>

2. **O2** Second question?

   <details><summary>Answer</summary>
   The answer, then why it holds, in a full sentence.
   </details>

## Key points
"""

GOOD_SHEET = """# A sheet

> Two types.

## Types

- **T1** first
- **T2** second

## Part one

### Worked example (T1): solved

1. **Step:** done.

### Problem (T1): try

<details><summary>Hint</summary>
A hint.
</details>

<details><summary>Answer</summary>
An answer.
</details>

## Part two

### Worked example (T2): solved

### Problem (T2): try

<details><summary>Hint</summary>
A hint.
</details>

<details><summary>Solution</summary>
A solution.
</details>

## Mixed review

### Problem (T1): again

<details><summary>Hint</summary>
A hint.
</details>

<details><summary>Answer</summary>
An answer.
</details>

### Problem (T2): again

<details><summary>Hint</summary>
A hint.
</details>

<details><summary>Answer</summary>
An answer.
</details>
"""


def messages(findings, kind=None):
    return [f.message for f in findings if kind is None or f.kind == kind]


class Lesson(unittest.TestCase):
    def run_on(self, text):
        return lesson.check_text("x.md", text, LESSON)

    def test_good_passes(self):
        self.assertEqual(self.run_on(GOOD_LESSON), [])

    def test_untested_objective(self):
        text = GOOD_LESSON.replace("2. **O2** Second", "2. **O1** Second")
        self.assertTrue(any("O2 is tested by no question" in m for m in messages(self.run_on(text), "error")))

    def test_untagged_question(self):
        text = GOOD_LESSON.replace("1. **O1** First", "1. First")
        self.assertTrue(any("names no objective" in m for m in messages(self.run_on(text), "error")))

    def test_unknown_objective(self):
        text = GOOD_LESSON.replace("1. **O1** First", "1. **O9** First")
        self.assertTrue(any("O9, which no objective lists" in m for m in messages(self.run_on(text), "error")))

    def test_duplicate_objective(self):
        text = GOOD_LESSON.replace("- **O2** Explain", "- **O1** Explain")
        self.assertTrue(any("listed twice" in m for m in messages(self.run_on(text), "error")))

    def test_no_objectives(self):
        text = GOOD_LESSON.replace("- **O1** Compute a thing.\n- **O2** Explain a thing.\n", "")
        self.assertTrue(any("no objective listed" in m for m in messages(self.run_on(text), "error")))

    def test_answer_not_folded(self):
        text = GOOD_LESSON.replace("<details><summary>Answer</summary>\n   The answer, then why it holds, in a full sentence.\n   </details>",
                                   "The answer, then why it holds, in a full sentence.", 1)
        self.assertTrue(any("no folded answer" in m for m in messages(self.run_on(text), "error")))

    def test_bare_key_warns(self):
        text = GOOD_LESSON.replace("The answer, then why it holds, in a full sentence.", "Four.", 1)
        self.assertTrue(any("only a key" in m for m in messages(self.run_on(text), "warning")))

    def test_obsidian_and_quarto_folds_count(self):
        obsidian = GOOD_LESSON.replace("<details><summary>Answer</summary>\n   The answer", "> [!answer]-\n   > The answer", 1)
        obsidian = obsidian.replace("full sentence.\n   </details>", "full sentence.", 1)
        quarto = GOOD_LESSON.replace("<details><summary>Answer</summary>", '::: {.callout-note collapse="true"}', 1)
        quarto = quarto.replace("   </details>", "   :::", 1)
        for text in (obsidian, quarto):
            self.assertFalse(any("no folded answer" in m for m in messages(self.run_on(text))), text)

    def test_open_callout_is_not_a_fold(self):
        text = GOOD_LESSON.replace("<details><summary>Answer</summary>\n   The answer", "> [!answer]\n   > The answer", 1)
        text = text.replace("full sentence.\n   </details>", "full sentence.", 1)
        self.assertTrue(any("no folded answer" in m for m in messages(self.run_on(text), "error")))

    def test_options(self):
        two = GOOD_LESSON.replace("1. **O1** First question?\n", "1. **O1** First question?\n   - a. one\n   - b. two\n")
        self.assertTrue(any("2 options" in m for m in messages(self.run_on(two), "warning")))
        banned = GOOD_LESSON.replace("1. **O1** First question?\n", "1. **O1** First question?\n   - a. one\n   - b. two\n   - c. all of the above\n")
        self.assertTrue(any("all or none of the above" in m for m in messages(self.run_on(banned), "warning")))

    def test_trap_without_refutation(self):
        text = GOOD_LESSON.replace("> **Why not:** the reason, then the right idea.\n", "")
        self.assertTrue(any("a trap with no Why not" in m for m in messages(self.run_on(text), "error")))

    def test_trap_callouts(self):
        quarto = '::: {.callout-warning title="Trap"}\nA wrong idea.\n:::\n'
        obsidian = "> [!warning] Trap\n> A wrong idea.\n"
        for block in (quarto, obsidian):
            text = GOOD_LESSON.replace("> **Trap:** a wrong idea.\n> **Why not:** the reason, then the right idea.\n", block)
            self.assertTrue(any("a trap with no Why not" in m for m in messages(self.run_on(text), "error")), block)
            refuted = block.replace("A wrong idea.", "A wrong idea. **Why not:** the reason.")
            text = GOOD_LESSON.replace("> **Trap:** a wrong idea.\n> **Why not:** the reason, then the right idea.\n", refuted)
            self.assertFalse(any("a trap" in m for m in messages(self.run_on(text))), refuted)

    def test_callout_questions(self):
        vault = "# A note\n\n## Check yourself\n\n> [!QUESTION]- Check: why is it so?\n> Because of the reason, stated in a full sentence here.\n"
        self.assertEqual(questions.check_text("n.md", vault, LESSON, align=False, name="questions"), [])
        open_callout = vault.replace("[!QUESTION]- Check", "[!QUESTION] Check")
        self.assertTrue(any("left open" in m for m in messages(questions.check_text("n.md", open_callout, LESSON, align=False), "error")))
        bare = vault.replace("Because of the reason, stated in a full sentence here.", "Four.")
        self.assertTrue(any("only a key" in m for m in messages(questions.check_text("n.md", bare, LESSON, align=False), "warning")))
        piege = vault + "\n> [!WARNING] Piège\n> Une idée fausse.\n"
        found = questions.check_text("n.md", piege, {**LESSON, "trap_labels": ["Piège"], "why_labels": ["Pourquoi non"]}, align=False)
        self.assertTrue(any("a trap with no Pourquoi non" in m for m in messages(found, "error")))

    def test_notes_need_no_objectives(self):
        text = GOOD_LESSON.replace("- **O1** Compute a thing.\n- **O2** Explain a thing.\n", "").replace("**O1** ", "").replace("**O2** ", "")
        self.assertEqual(questions.check_text("n.md", text, LESSON, align=False), [])

    def test_code_is_not_markup(self):
        text = GOOD_LESSON + "\n```markdown\n### Check yourself\n1. untagged\n```\n"
        self.assertEqual(self.run_on(text), [])


class Sheet(unittest.TestCase):
    def run_on(self, text):
        return sheet.check_text("s.md", text, SHEET)

    def test_good_passes(self):
        self.assertEqual(self.run_on(GOOD_SHEET), [])

    def test_untyped_and_unknown(self):
        self.assertTrue(any("an item with no type" in m for m in messages(self.run_on(GOOD_SHEET.replace("### Problem (T1): try", "### Problem: try")), "error")))
        self.assertTrue(any("T7, which Types does not list" in m for m in messages(self.run_on(GOOD_SHEET.replace("(T1): try", "(T7): try")), "error")))

    def test_type_opens_without_example(self):
        text = GOOD_SHEET.replace("### Worked example (T2): solved\n\n", "")
        self.assertTrue(any("T2 opens without a worked example" in m for m in messages(self.run_on(text), "error")))

    def test_problem_without_answer(self):
        text = GOOD_SHEET.replace("<details><summary>Answer</summary>\nAn answer.\n</details>\n\n## Part two", "## Part two")
        self.assertTrue(any("no folded answer or solution" in m for m in messages(self.run_on(text), "error")))

    def test_answer_before_hint(self):
        text = GOOD_SHEET.replace("<details><summary>Hint</summary>\nA hint.\n</details>\n\n<details><summary>Answer</summary>\nAn answer.\n</details>\n\n## Part two",
                                  "<details><summary>Answer</summary>\nAn answer.\n</details>\n\n<details><summary>Hint</summary>\nA hint.\n</details>\n\n## Part two")
        self.assertTrue(any("answer comes before the hint" in m for m in messages(self.run_on(text), "error")))

    def test_mixed_review_of_one_type(self):
        text = GOOD_SHEET.replace("### Problem (T2): again", "### Problem (T1): again too")
        self.assertTrue(any("mixed review holds 1 type" in m for m in messages(self.run_on(text), "warning")))

    def test_long_block(self):
        extra = "### Problem (T1): more\n\n<details><summary>Hint</summary>\nh\n</details>\n\n<details><summary>Answer</summary>\na\n</details>\n\n"
        text = GOOD_SHEET.replace("## Part two", extra * 4 + "## Part two")
        self.assertTrue(any("5 problems" in m for m in messages(self.run_on(text), "warning")))


class Deck(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "lesson.md").write_text("# L\n\n## The invariant\n\ntext\n")

    def tearDown(self):
        self.tmp.cleanup()

    def run_on(self, rows):
        text = "front\tback\tsource\ttags\n" + "".join("\t".join(row) + "\n" for row in rows)
        return deck.check_text(self.root, "deck.tsv", text, DECK)

    def test_good_passes(self):
        self.assertEqual(self.run_on([("Why halve?", "Because it is sorted.", "lesson.md#the-invariant", "concept")]), [])

    def test_errors(self):
        cases = {
            "empty side": [("Why halve?", "", "lesson.md#the-invariant", "")],
            "the same front": [("Why halve?", "A.", "lesson.md", ""), ("why  HALVE?", "B.", "lesson.md", "")],
            "no source": [("Why halve?", "A.", "", "")],
            "not a file": [("Why halve?", "A.", "missing.md", "")],
            "names no heading": [("Why halve?", "A.", "lesson.md#nowhere", "")],
            "no person has checked": [("Why halve?", "A.", "lesson.md", "generated")],
        }
        for expected, rows in cases.items():
            self.assertTrue(any(expected in m for m in messages(self.run_on(rows), "error")), expected)

    def test_checked_generated_passes(self):
        self.assertEqual(self.run_on([("Why halve?", "Because it is sorted.", "lesson.md", "generated checked")]), [])

    def test_warnings(self):
        cases = {
            "yes-or-no": [("Is it sorted?", "Yes", "lesson.md", "")],
            "past 25 words": [("Why?", " ".join(["word"] * 30), "lesson.md", "")],
            "a list": [("Which?", "a; b; c; d", "lesson.md", "")],
        }
        for expected, rows in cases.items():
            self.assertTrue(any(expected in m for m in messages(self.run_on(rows), "warning")), expected)

    def test_header(self):
        found = deck.check_text(self.root, "deck.tsv", "front\tback\n", DECK)
        self.assertTrue(any("header lacks source, tags" in m for m in messages(found, "error")))


class QuestionsModule(unittest.TestCase):
    def test_module_runs_on_declared_notes(self):
        module = load("questions")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "note.md").write_text("# N\n\n## Check yourself\n\n> [!QUESTION] Check: open?\n> An answer long enough to explain why it holds.\n")
            found = module.check(root, {"questions": {"files": ["note.md"], "min_answer_words": 8}})
        self.assertEqual([(f.check, f.kind) for f in found], [("questions", "error")])


class Examples(unittest.TestCase):
    def test_examples_pass(self):
        folder = ROOT / "shapes" / "examples"
        for path in sorted(folder.glob("*-lesson.md")) + sorted(folder.glob("*-guide.md")):
            self.assertEqual(lesson.check_text(path.name, path.read_text(), LESSON), [], path.name)
        for path in sorted(folder.glob("*-sheet.md")):
            self.assertEqual(sheet.check_text(path.name, path.read_text(), SHEET), [], path.name)
        for path in sorted(folder.glob("*.tsv")):
            relative = path.relative_to(ROOT).as_posix()
            self.assertEqual(deck.check_text(ROOT, relative, path.read_text(), DECK), [], path.name)


if __name__ == "__main__":
    unittest.main()
