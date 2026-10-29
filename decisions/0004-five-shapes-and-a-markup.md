# 0004: Five shapes, and one markup the checks read

**Decision:** the repository holds five shapes (lesson, question block, exercise sheet, deck, study guide), built on
the core's note and report, and one plain Markdown markup for objectives, questions, folds, traps and types.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/c08433c4d868d9b38ac1441f58ae7602c399db6d/shapes/decision-record.md).

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
