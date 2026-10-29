# Shapes and checks: proposals for the maintainer

What the exercise-sets evidence implies for the shape of an exercise set and for checks a program could run. Proposals, not decisions. "review N" is the line of [review](review.md) the proposal rests on.

## Blocks of an exercise set, in order

| # | Block | Grade | Rests on |
|---|---|---|---|
| 1 | For each new type: a worked example, then a problem of the same type | measured, for novices | review 48 (van Gog 2011, linked) |
| 2 | Then completion problems that leave the last steps, before whole problems | measured, lab and tutor | review 52, 53, 58 |
| 3 | A short block of same-type problems; a few are enough | measured, one lab study for the number | review 88, 35 |
| 4 | Interleaved review: problems of earlier types, from several earlier sets | measured, classroom trials, mathematics | review 31 to 35, 38; against.md for null results |
| 5 | Per problem: a hint, then the answer, then the worked solution, each folded | convention, untested on paper; hints measured only in software | review 76 to 80 |
| 6 | Solutions released after the attempt, not printed beside the problem | supported with caveat (one two-cohort study, practitioner consensus) | review 81, 82 |
| 7 | Variation within a type: one feature changed at a time for novices; more variety once a type is known | supported with caveat (variability reverses with expertise) | review 66, 71 |

## Checks a program could run

| Check | What it tests | Kind | Grade of the rule behind it |
|---|---|---|---|
| `type-tagged` | every problem carries a type tag | exact | convention (needed by the checks below) |
| `example-before-type` | the first problem of each type is preceded by a worked example of that type | exact | measured (review 48) |
| `interleaved-share` | the share of problems whose type was introduced in an earlier set is above a threshold, PROVISIONAL at one half | exact, threshold PROVISIONAL | measured for the direction (review 31, 34); the threshold untested (position.md) |
| `spaced-types` | each type appears in at least two sets after its own | exact | measured (review 10, 39, 88) |
| `max-run` | no run of same-type problems longer than N, PROVISIONAL at 4 | exact, threshold PROVISIONAL | supported with caveat (review 35, 88) |
| `help-ladder` | each problem with a solution also has a hint, placed before it | exact | convention, untested on paper (review 76) |
| `solution-folded` | answers and solutions are folded or in a separate file, never inline | exact | supported with caveat (review 81) |
| `type-balance` | no type is far rarer than the others without a reason given | heuristic | supported with caveat (review 69) |
| `fading-steps` | whether completion problems remove steps from the end | judgment | measured (review 53) |
| `variation-purpose` | whether the varied feature is the one the type is about | judgment | convention (review 71) |

- Thresholds marked PROVISIONAL go in config, not in code, until a study sets them.
- Every check reads type tags; a set without them can only get the judgment checks.
