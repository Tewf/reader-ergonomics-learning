# Shape: deck

A deck of flashcards shipped with study material, in two files. A header page names the text the cards come from and
how to review them; a file of cards holds one question and one answer each, every card linked to the section it tests.

## Skeleton

The header page, `<deck>.md`:

```markdown
# <The subject of the deck>

> One or two sentences: the text the cards come from, and how many cards.

**Shape:** [deck](<link to this file>). **Cards:** [<deck>.tsv](<deck>.tsv).

## Use                 keep one deck, not small stacks; do not drop a card after one correct recall;
                       add your own cards, written in your words

## Sections            the sections of the source text, each with its concept and its detail cards

## See also            the lesson or notes the deck derives from
```

The cards, `<deck>.tsv`, tab-separated, which Anki imports as it is:

```tsv
front	back	source	tags
<one question>	<one answer>	<lesson.md#section>	<tags; generated and checked when a program wrote it>
```

## The blocks

| Block | Rule | Grade | Evidence |
|---|---|---|---|
| Source text | the deck names the text it derives from; each card links the section it tests | convention, untested (a practitioner rule) | [flashcards](../evidence/flashcards/review.md), strand 1 |
| Invitation | the header invites learners to add cards of their own, in their words | supported with caveat: learner-made cards beat premade ones in five of six experiments, contested for vocabulary | [flashcards](../evidence/flashcards/review.md), strand 3; [against](../evidence/flashcards/against.md) |
| One question, one answer | a short front and a short back; no yes-or-no front; no list as an answer | convention, untested: the practitioner rules agree, no study tests them | [flashcards](../evidence/flashcards/review.md), strand 2 |
| Concept cards | each section has a why or how card beside its detail cards | supported with caveat, two studies read by abstract | [flashcards](../evidence/flashcards/review.md), strand 5 |
| Confusable cards | no two cards with the same front | supported with caveat: related words learned together raise confusion errors, vocabulary only | [flashcards](../evidence/flashcards/review.md), strand 5 |
| Use | one large deck, no card dropped after one correct recall | measured: dropping lowers retention, and small stacks mass the reviews | [flashcards](../evidence/flashcards/review.md), strand 4 |
| Generated cards | tagged `generated`, and `checked` once a person has read them | supported with caveat: one error in 21 after tuning, in one preprint | [flashcards](../evidence/flashcards/review.md), strand 7 |

- Scheduling is left to the review software: the schedulers are compared in the core
  ([learning science](https://github.com/Tewf/reader-ergonomics/blob/e8864477a53d713251ba42a4cf7b7a0d761243a2/evidence/learning-science/review.md), strand 8).
- **The baseline this shape must beat** is a learner-made Anki deck of question-and-answer cards under the default
  scheduler ([baseline](../evidence/flashcards/baseline.md)).

## How it derives from the topic

| Topic block | Here | Change |
|---|---|---|
| Title, summary | the header page's | none |
| Body | Use, Sections | added |
| Contents | the cards file, linked from the Shape line | a data file, not a topic |
| See also | See also | none |

## Checked by

| Check | What it verifies | Kind |
|---|---|---|
| `deck` | every card has a front and a back; no two cards share a front | exact |
| `deck` | every source links a file that exists, and a heading in it | exact |
| `deck` | a card tagged `generated` is also tagged `checked` | exact |
| `deck` | no yes-or-no front, no answer longer than `long_answer` words or listing more than `list_items` items | heuristic, PROVISIONAL thresholds |
| judgment | whether a card tests understanding or the recall of a phrase | judgment |

An example that passes every check: [binary search](examples/binary-search-deck.md).

## See also

[Shapes](README.md), the folder this shape heads; the [lesson](lesson.md) a deck usually derives from.
