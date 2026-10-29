# Shape: lesson

A lesson or a course chapter, written to be studied alone. It states what the learner will be able to do, explains it
and corrects the usual wrong idea; then it checks each aim with a question whose answer stays folded until tried.

## Skeleton

```markdown
# <The subject, named as the field names it>

> One or two sentences that stand for the lesson: what it teaches and why it matters.

**Shape:** [lesson](<link to this file>).

## Objectives          few, each with an id and an observable verb
- **O1** Compute ...
- **O2** Explain why ...

## Terms               each term bold where it is defined, with its definition

## <Part 1>            the explanation, figure first when the content is a relation;
                       a Trap box where learners hold a known wrong idea
> **Trap:** <the wrong idea, as learners hold it>
> **Why not:** <why it is wrong, then the accepted idea>

### Check yourself     the question block of this part, each item tagged by an objective
1. **O1** <question>
   <details><summary>Answer</summary> the answer, then why </details>

## Key points          the objectives restated as what the learner can now do

## See also            the notes, sheets and decks that go with it
```

## The blocks

| Block | Rule | Grade | Evidence |
|---|---|---|---|
| Title, summary | the topic's two first blocks; the summary is the overview read before any detail | measured for an overview; the form is a convention | [topic](https://github.com/Tewf/reader-ergonomics-topic/blob/1220def7863b5e977a3edd1e30bd168fff1523a5/shapes/topic.md); [overview first](https://github.com/Tewf/reader-ergonomics/blob/d48ffbe96aed32dd63e1974ee60f69472fe36932/principles/document/overview-first.md) |
| Objectives | few, each with an id and a verb a test can observe | measured that objectives direct study to what they name; the verb rule is a convention | [instructional text](../evidence/instructional-text/review.md), strand 3 |
| Terms | defined at first use, bold | supported with caveat | the core note; [define before use](https://github.com/Tewf/reader-ergonomics/blob/d48ffbe96aed32dd63e1974ee60f69472fe36932/principles/document/define-before-use.md) |
| Trap | the wrong idea stated, marked wrong, then the accepted idea | measured: refutation text beats expository text, g = 0.36 over 30 comparisons; whether it lasts is unsettled | [instructional text](../evidence/instructional-text/review.md), strand 5 |
| Check yourself | per part, items tagged by objective, answers folded | measured for retrieval (core); the tagging is a convention | [question block](question-block.md) |
| Key points | at the end, restating the objectives | supported with caveat: an end summary beat an opening one on the same page in two small studies | [instructional text](../evidence/instructional-text/review.md), strand 4 |
| See also | links, never copies | convention | [topic](https://github.com/Tewf/reader-ergonomics-topic/blob/1220def7863b5e977a3edd1e30bd168fff1523a5/shapes/topic.md) |

- **Alignment** is the rule that ties the blocks: every objective is tested by at least one question, and every
  question tests a stated objective. It is the practice of every template read (OpenStax, the Carpentries, course
  rubrics), and no controlled trial of it was found ([position](../evidence/instructional-text/position.md)).
- **Not in the shape:** a glossary at the end (the weakest gloss form, in second-language studies), and a crib sheet
  as a learning aid (making one does not teach): [against](../evidence/instructional-text/against.md).

## How it derives from the topic

| Topic block | Here | Change |
|---|---|---|
| Title | the subject | none |
| Summary | the quoted line under the title | none |
| Body | Objectives, Terms, the parts, Key points | Objectives, Trap and Key points added to the core note |
| Contents | none: a lesson holds no topics | left empty |
| See also | See also | none |
| (metadata) | the Shape line | names this shape, as the topic asks |

## Checked by

| Check | What it verifies | Kind |
|---|---|---|
| `lesson` | every objective is tested; every question names an objective that exists | exact |
| `lesson` | every question has a folded answer | exact |
| `lesson` | every Trap, a quote or a callout titled Trap, holds a Why not | exact |
| `lesson` | an answer gives a reason, not only the key; multiple-choice items follow the [question block](question-block.md) | heuristic |
| standard | the headings Objectives, Check yourself, Key points, See also | exact |

An example that passes every check: [binary search](examples/binary-search-lesson.md).

## See also

[Shapes](README.md), the folder this shape heads; the [question block](question-block.md) it holds.
