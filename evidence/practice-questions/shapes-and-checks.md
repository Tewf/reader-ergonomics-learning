# Shapes and checks: proposals for the maintainer

What the evidence implies for the question block of a study document, and for checks a program could run on it. Proposals, not decisions; "review N" is the line of [review](review.md) a proposal rests on.

## The question block, in order, at the end of each part

| Block | What it holds | Grade | Rests on |
|---|---|---|---|
| recall question | one key idea of the part, answered without the text | measured (core) | review 37, 38 |
| higher-order question | an application or inference question on the same idea | measured | review 24, 25, 26, 28 |
| multiple-choice item, if any | three competitive options from known errors, stem first | measured for learning (competitive options); convention for three | review 41, 45, 53, 58 |
| folded answer | the key with an explanation of why, and of each wrong option | measured (explanation); untested (explaining wrong options) | review 63, 65 |
| answer placement | folded beside the question, opened after a written attempt | convention, untested | review 73, 74, 75, 77 |

- No block fixes feedback timing: the pooled evidence shows no average difference (review 67).
- Keep the full answer out of the line of sight before the attempt; the reasons are old studies of peeking (review 73, 74).
- Generated questions enter only after human review; item quality is mixed and learning is untested (review 83 to 95).

## Checks a program could run

| Check | Kind | What it tests | Grade | Rests on |
|---|---|---|---|---|
| `question-present` | exact | each part ends with at least one question block | measured (core) | review 37, 38 |
| `answer-folded` | exact | each question has an answer, inside a fold, not in the visible line | convention, untested | review 73, 77 |
| `answer-explains` | heuristic | a folded answer has more than the key: a sentence of reason | measured | review 63, 65 |
| `no-all-none-of-the-above` | exact | no option reads "all of the above" or "none of the above" | convention (guidelines) | review 57, 59 |
| `option-count` | exact | multiple-choice items have three or four options | supported with caveat (tests, not learning) | review 53 |
| `options-parallel` | heuristic | option lengths within a factor of two; the key not the longest | convention, untested | review 105 |
| `negation-marked` | heuristic | a stem with "not" or "except" marks it in bold | convention, untested | review 105, 117 |
| `level-mix` | judgment | at least one question per part beyond recall | measured | review 24, 25, 26 |
| `distractor-source` | judgment | each wrong option names the error it diagnoses | convention; one lab result | review 41, 58, 102 |

- `level-mix` cannot be exact: a question's level depends on what was taught, so it goes to judgment.
- The exact and heuristic checks are cheap and can run on every push; judgment checks follow the standard's judgment file.

## What the evidence does not support

- A rule preferring short answer over multiple choice, in classrooms (review 38).
- A rule fixing immediate or delayed feedback (review 67).
- A rule that facts must be asked before application (review 24).
