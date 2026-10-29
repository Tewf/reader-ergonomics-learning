# Shapes and checks: proposals for the maintainer

What the instructional-text evidence implies for a study text's blocks and for checks a program could run. Proposals, not decisions; "review N" is the line of review.md the proposal rests on.

## Shape of a section, in order

| # | Block | Grade | Rests on |
|---|---|---|---|
| 1 | objectives, few, each with an observable verb and an id | measured for objectives in general; the verb rule is convention, untested | review 51, 53; review 28 |
| 2 | explanation, each key term bold and defined where first used | convention, untested for first-language texts; glossaries ranked weakest in a second language | review 70 |
| 3 | misconception block: the wrong idea, marked wrong, the accepted explanation | measured (two meta-analyses), durability unsettled | review 14, 15, 16 |
| 4 | side boxes only when the main text points to them | supported with caveat, one study | review 43 |
| 5 | summary at the end of the part, short | supported with caveat (small, old studies) | review 66, 67, 69 |
| 6 | checks, each tagged with an objective id, answers folded | convention, untested for the tagging; checks themselves are the practice-questions review's | review 55, 117 |
| 7 | key points restating the objectives | convention, untested | review 115 |
| 8 | offered with it: a guided-notes sheet with blanks for the key terms | measured (college meta-analysis) | review 90 |
| 9 | worked solutions with steps and a self-explanation prompt in place of a printed explanation | measured (meta-analysis; three experiments) | review 105, 106 |

- Not proposed: a study guide or concept list handed out before a test (contested, review 94, 95); a crib sheet as a learning aid (review 97).

## Checks a program could run

| Check | What it tests | Kind | Grade of the rule | Rests on |
|---|---|---|---|---|
| `objective-has-check` | every objective id is tagged by at least one check | exact | convention, untested (alignment) | review 55, 60 |
| `check-has-objective` | every check carries an objective id that exists | exact | convention, untested | review 117 |
| `objective-verb` | an objective does not open with "understand", "know", "learn" or "appreciate" | heuristic | convention, untested | review 28 |
| `term-defined-in-place` | a bold term has a definition in the same paragraph or a margin note | heuristic | convention, untested | review 70 |
| `glossary-matches-text` | every glossary entry is bold in the text, and the reverse | exact | convention (one place per fact) | review 70 |
| `misconception-parts` | a misconception block holds a stated idea, a refutation marker and an explanation | exact on structure | measured for the structure; wording is judgment | review 14, 15 |
| `summary-at-end` | a part with a summary places it after the body | exact | supported with caveat | review 66 |
| `summary-ratio` | summary length under a share of the part, PROVISIONAL threshold in config | exact | convention, untested | review 67 |
| `box-referenced` | each side box is referred to from the main text | exact | supported with caveat | review 43 |
| `notes-sheet-generated` | a guided-notes sheet can be built from headings and bold terms | exact | measured for the sheet's use | review 90 |

- Judgment only: whether an objective is measurable, whether a refutation names the learner's actual misconception, whether a summary is faithful.
