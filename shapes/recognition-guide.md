# Shape: recognition guide

A guide to telling which type a problem is before solving it. Each named type gets its signals in the statement and in
the model, its tool, and the signs that a problem is none of them; then come statements to place, answers folded. It
serves the learner who knows every method and still picks the wrong one.

## Skeleton

```markdown
# <What the guide tells apart>

> One or two sentences: the types it covers, and what the learner can do after it.

**Shape:** [recognition guide](<link to this file>).

## Types               the same ids the exercise sheet and the study guide use
- **T1** <type>
- **T2** <type>

## Signals             one row per type
| Type | In the statement | In the model | Tool | Not when |
|---|---|---|---|---|

## Decision            the questions in order, each ending on a type or on "none"; a list, or a figure
1. <question>: yes, <next question or type>; no, <next question or type>

## Not one of them     what looks like a type and is not, with the witness
| Looks like | Why not | What it is |
|---|---|---|

## Check yourself      statements to place, the type folded
1. <a statement>
   <details><summary>Answer</summary> T1: <the signal that decides> </details>

## See also            the lesson, sheet and guide that use these types
```

## The blocks

| Block | Rule | Grade | Evidence |
|---|---|---|---|
| Types | named, with the ids the sheet and the guide use, so a type has one name across the three | convention, needed by the checks | the [exercise sheet](exercise-sheet.md), Types |
| Signals | one row per type: the words of a statement and the shape of a model that announce it, the tool, and the case that defeats it | convention, untested: the field's catalogues (an applications chapter, a taxonomy of problem types) are written this way, and no study tests a catalogue against recognition | [instructional text](../evidence/instructional-text/position.md), on what is not measured |
| Decision | the questions in the order a learner can ask them, each ending on a type or on none | convention, untested | none found |
| Not one of them | a refuted look-alike per trap, with the witness that settles it | measured for refutation text, g = 0.36, as the lesson's Trap | [instructional text](../evidence/instructional-text/review.md), strand 5 |
| Check yourself | statements to place before the answer is unfolded | measured (core): practice testing beats rereading | [question block](question-block.md) |

- **What it is for.** The one cause of a miss the other shapes leave alone, recognising the type
  ([decision 0005](../decisions/0005-a-sixth-shape-the-recognition-guide.md)); this shape does only that.
- **Not a lesson.** It defines nothing: every type links the note that teaches it. A signal that needs a paragraph is a
  sign the type needs a lesson first.
- **Untested as a whole.** The test it should face is whether a guide written this way lowers the recognition errors
  in the grid. The first one was written for a vault's notes on linear programs and flows, on 2026-11-07, and the
  count is still to run.

## How it derives from the topic

| Topic block | Here | Change |
|---|---|---|
| Title, summary | what the guide tells apart, and for whom | none |
| Body | Types, Signals, Decision, Not one of them, Check yourself | added |
| Contents | none: its parts are sections, not topics | left empty |
| See also | See also | none |
| (metadata) | the Shape line | names this shape, as the topic asks |

## Checked by

| Check | What it verifies | Kind |
|---|---|---|
| standard | the headings Types, Signals, Decision, Not one of them, Check yourself, See also | exact |
| `questions`, when the repository declares the file | every item of Check yourself folds its answer, and the answer is more than a key | exact, and a heuristic for the key |
| judgment | whether each Signals row names a signal a learner can see before solving, and whether every type of the sheet has a row | judgment |

An example that passes every check: [which search](examples/binary-search-recognition.md).

## See also

[Shapes](README.md), the folder this shape heads; the [exercise sheet](exercise-sheet.md) and the
[study guide](study-guide.md) whose types it tells apart; the [lesson](lesson.md) each type links.
