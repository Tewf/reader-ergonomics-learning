# 0004: Five shapes, and one markup the checks read

**Decision:** the repository holds five shapes (lesson, question block, exercise sheet, deck, study guide), built on
the core's note and report, and one plain Markdown markup for objectives, questions, folds, traps and types.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/shapes/decision-record.md).

## Context

- The four reviews each ended in proposals for blocks and checks, graded and traced to their lines.
- The core already holds a note with a Check yourself and folded answers. Its report is a worked example, with its
  plan, its steps named by their goal, its traps and its fading.
- The documents these shapes serve are written in three places: Quarto books, an Obsidian vault and Anki decks. A
  program can check alignment, folds and order only if they are marked the same way in all three.

## Decision

- **Five shapes, one per kind of study document,** each a topic of reader-ergonomics-topic. The lesson extends the
  core note; every worked example is a core report; the question block is a part, not a document; the study guide
  composes the other four.
- **One markup:** bold ids for objectives (`**O1**`) and types (`**T1**`), and the id at the head of each question.
  Folds are `<details>`, an Obsidian callout or a Quarto callout; a trap is a quote labelled Trap holding a Why not.
  Items of a sheet name their type in their heading, and cards are rows of a TSV.
- **A rule enters a shape only with its grade.** Where no study exists, the shape says convention, and its threshold
  is a tunable marked PROVISIONAL.
- **One example per shape,** on one subject, binary search, checked in CI.

## Options it rules out

None was weighed in a table when this record was written; these are the options its context argues against.

| Option | Why it lost |
|---|---|
| shapes of their own, apart from the core's note and report | the core already holds a note with a Check yourself and folded answers, and a report that is a worked example; one place per fact |
| a markup per tool, each read by its own check | alignment, folds and order are checkable only if they are marked the same way in Quarto, Obsidian and Anki; the one markup reads each tool's own fold and callout instead |
| a shape per technique: a retrieval shape, a spacing shape | [decision 0001](0001-take-the-document-not-the-technique.md) takes the document, not the technique |

## Consequences

- Alignment, folds, traps and the order of a sheet become checks a program runs on every push. The topic check of
  reader-ergonomics-topic runs in CI from now on, as decision 0003 announced, on the front page, shapes and decisions.
- The markup is a convention no study tested; a document written otherwise passes the standard and fails these
  checks, and the labels are tunables for that reason.
- What no program can decide (whether a question goes beyond recall, whether a card tests understanding) stays with
  the judgment file.
- The shapes have not been tested on learners; the baselines each must beat are in the reviews.

## See also

[Decisions](README.md); the [shapes](../shapes/README.md).
