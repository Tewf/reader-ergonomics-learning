# Shapes and checks: proposals from the flashcards review

Proposals for the maintainer, not decisions; each names its grade and the line of [review](review.md) it rests on.

## Shape of a deck shipped with study material

| Block, in order | Proposal | Grade | Rests on |
|---|---|---|---|
| deck header | names the text it derives from, and invites the learner to add own cards | supported with caveat (one paper of six experiments, abstract read; the invitation itself untested) | review.md L38, L41 |
| one card per idea | front holds one question, back one answer | convention, untested | review.md L25, L66 |
| source link | each card links to the section it comes from | convention, untested (Wozniak rule 18) | review.md L18 |
| concept cards | each section has at least one why or how card beside its detail cards | supported with caveat | review.md L72, L73 |
| direction | a reversed card only when the text asks for production | supported with caveat, vocabulary only | review.md L28, L107 |
| confusable pairs | marked, and introduced on different days | supported with caveat, vocabulary only | review.md L69, L70 |
| use note | do not drop a card after one correct recall; keep one deck, not small stacks | measured | review.md L52, L54, L55 |

## Checks a program could run on a deck file

| Check | Kind | What it flags | Grade of the rule | Rests on |
|---|---|---|---|---|
| card-two-sides | exact | a card with an empty front or back | convention, untested | review.md L25 |
| card-source | exact | a card whose source link does not resolve to a section | convention, untested | review.md L18 |
| card-duplicate | exact | two cards with the same front | supported with caveat (interference) | review.md L70 |
| card-near-duplicate | heuristic | fronts above a similarity threshold, PROVISIONAL | supported with caveat | review.md L70 |
| card-yes-no | heuristic | a front opening with an auxiliary verb and a back of yes or no | convention, untested | review.md L25 |
| card-list-answer | heuristic | a back with more than N list items, N PROVISIONAL | convention, untested | review.md L18, L25 |
| card-long-answer | heuristic | a back over N words, N PROVISIONAL | convention, untested | review.md L25, L66 |
| deck-concept-share | heuristic | a section with detail cards only (no why or how) | supported with caveat | review.md L72, L73 |
| generated-flag | exact | a generated card not marked as generated, or not checked by a person | supported with caveat (1 error in 21) | review.md L86 |

## Judgment, not a program

- Whether a card tests understanding or only recall of a phrase.
- Whether a cloze hides the part that matters.
- Whether two cards are confusable in meaning, beyond their wording.
