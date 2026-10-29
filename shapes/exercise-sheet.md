# Shape: exercise sheet

A set of exercises built as a sequence. Each new type of problem opens with a worked example, then a problem with
its last steps left to do, then a few whole problems. A mixed review brings back the types of earlier sheets, and
every problem offers a hint before its answer and its solution, all folded.

## Skeleton

```markdown
# <What the sheet trains, named by the skill>

> One or two sentences: the types of problem it holds and what it builds on.

**Shape:** [exercise sheet](<link to this file>).

## Types               each type of problem with an id
- **T1** <type>
- **T2** <type>

## <Type T1>
### Worked example (T1): <what solving it achieves>
    a solved problem in the core report's form: plan, steps named by their goal
### Complete (T1): <problem>
    the first steps given, the last ones left to the learner
### Problem (T1): <problem>
    <details><summary>Hint</summary> ... </details>
    <details><summary>Answer</summary> ... </details>
    <details><summary>Solution</summary> ... </details>

## Mixed review        problems of the types of earlier sheets, in mixed order

## See also            the lesson it practises, the sheet before and after
```

## The blocks

| Block | Rule | Grade | Evidence |
|---|---|---|---|
| Types | named, with ids; every item carries its type | convention, needed by the checks below | [exercise sets](../evidence/exercise-sets/shapes-and-checks.md) |
| Worked example first | the first item of a new type is solved in full, in the core report's form | measured, for novices | [exercise sets](../evidence/exercise-sets/review.md), strand 3; [worked examples with subgoals](https://github.com/Tewf/reader-ergonomics/blob/6980fa64583912922d6f5b5c01316749d654345f/principles/document/worked-examples-with-subgoals.md) |
| Complete | completion problems leave the last steps before whole problems | measured: fading steps beats example-problem pairs; Parsons problems are a completion format for code | [exercise sets](../evidence/exercise-sets/review.md), strand 3 |
| A short block | a few problems of the new type, not a long run | measured for the number in one lab study only: nine problems did no better than three | [exercise sets](../evidence/exercise-sets/review.md), strand 6 |
| Mixed review | problems of earlier types, in mixed order | measured in classroom trials, mostly mathematics; a year-long trial found no gain on the final test | [exercise sets](../evidence/exercise-sets/review.md), strand 2; [against](../evidence/exercise-sets/against.md) |
| Hint, answer, solution | in that order, each folded; the solution released after the attempt | convention on paper; hints are measured only in software | [exercise sets](../evidence/exercise-sets/review.md), strand 5 |
| Variation | within a type, one feature changed at a time for novices | supported with caveat: variability helps experienced learners and hurts novices | [exercise sets](../evidence/exercise-sets/review.md), strand 4 |

- **The baseline this shape must beat** is the blocked sheet: one run of same-type problems per lesson, answers at
  the end ([baseline](../evidence/exercise-sets/baseline.md)).
- **Not tested as a whole:** no study tests a sheet built from all these parts, or the share of mixed review it
  should hold. The thresholds of the checks are tunables, marked PROVISIONAL in `checks/config.toml`.

## How it derives from the topic

| Topic block | Here | Change |
|---|---|---|
| Title | what the sheet trains | none |
| Summary | the quoted line under the title | none |
| Body | Types, one part per type, Mixed review | added |
| Contents | none: the worked examples are parts, not topics | left empty |
| See also | See also | none |
| (metadata) | the Shape line | names this shape |

## Checked by

| Check | What it verifies | Kind |
|---|---|---|
| `sheet` | every item carries a declared type; the first item of each type is a worked example | exact |
| `sheet` | every problem folds its answer and its solution; a hint comes before them | exact |
| `sheet` | a Mixed review holds problems of at least `mixed_types` types | heuristic, PROVISIONAL threshold |
| `sheet` | no type has more than `max_block` problems in its own part | heuristic, PROVISIONAL threshold |
| standard | the headings Types, Mixed review, See also | exact |

An example that passes every check: [binary search](examples/binary-search-sheet.md).

## See also

[Shapes](README.md), the folder this shape heads; the core [report](https://github.com/Tewf/reader-ergonomics/blob/6980fa64583912922d6f5b5c01316749d654345f/shapes/report.md),
the form of every worked example here.
