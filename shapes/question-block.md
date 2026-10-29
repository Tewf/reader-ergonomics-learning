# Shape: question block

The questions at the end of each part of a study document: a recall question and a question that applies the idea.
Each is tagged by the objective it tests, and its answer stays folded until the learner has tried.

## Skeleton

```markdown
### Check yourself

1. **O1** <a recall question: one key idea, answered without the text>
   <details><summary>Answer</summary> the answer, then a sentence on why </details>
2. **O2** <an application or inference question on the same idea>
   <details><summary>Answer</summary> the answer, then why </details>
3. **O2** <a multiple-choice item, if any: the stem first, then the options>
   - a. <option built from a known error>
   - b. <the key>
   - c. <option built from another known error>
   <details><summary>Answer</summary> b, because ...; a is the error of ...; c ... </details>
```

The fold may also be an Obsidian callout (`> [!answer]-`) or a Quarto callout with `collapse="true"`. A question may
also be a callout that holds its own answer, `> [!QUESTION]- Check: <question>`, the form of the S7 vault.

## The items

| Item | Rule | Grade | Evidence |
|---|---|---|---|
| recall question | one key idea of the part, answered without the text | measured (core) | [retrieval prompts](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/principles/document/retrieval-prompts.md) |
| higher-order question | at least one per part: application or inference on the same idea | measured: testing transfers to application and inference questions (d = 0.32), and higher-order quizzes raised higher-order scores | [practice questions](../evidence/practice-questions/review.md), strands 0 and 1 |
| objective tag | the id of the objective the item tests | convention, untested | [lesson](lesson.md), alignment |
| multiple-choice item | options built from known errors, three or four, no "all of the above" or "none of the above" | measured that competitive options induce retrieval; three options are best for tests, not shown for learning; the banned options are a convention of the item-writing guidelines | [practice questions](../evidence/practice-questions/review.md), strands 2 and 3 |
| folded answer | the key, then why; for a multiple-choice item, why each wrong option is wrong | measured that more informative feedback has larger effects; explaining wrong options is untested | [practice questions](../evidence/practice-questions/review.md), strand 4 |
| answer placement | folded beside its question, opened after a written attempt | convention, untested: peeking before answering lowered learning in old studies | [practice questions](../evidence/practice-questions/review.md), strand 5 |

- **What the evidence does not support:** a rule preferring short answer over multiple choice in classrooms, or one
  fixing immediate or delayed feedback (timing made no average difference, g = 0.03). Nor does it support a rule that
  facts must come before application ([shapes and checks](../evidence/practice-questions/shapes-and-checks.md)).
- **Generated questions** enter only after a person has read them: their quality is mixed, and learning from them
  was not found tested ([practice questions](../evidence/practice-questions/review.md), strand 6).

## How it derives from the topic

A question block is a part of a document, not a document: it is the core note's Check yourself, given rules for its
items. It has no title or summary of its own, so it is checked inside the document that holds it.

## Checked by

| Check | What it verifies | Kind |
|---|---|---|
| `lesson` | each item has a folded answer, and its objective exists | exact |
| `questions` | the same rules in a note, which states no objectives: folded answers | exact |
| `questions` | traps carry a Why not | heuristic, a warning, as in a lesson |
| `lesson` | an answer holds a reason, more words than a bare key | heuristic |
| `lesson` | a multiple-choice item has three or four options, none "all" or "none of the above" | heuristic |
| judgment | whether a part has an item beyond recall: a question's level depends on what was taught | judgment |

An example of two blocks, one with a multiple-choice item: the [binary search lesson](examples/binary-search-lesson.md#check-yourself).

## See also

[Shapes](README.md), the folder this shape heads; the [lesson](lesson.md) and the [study guide](study-guide.md) that
hold it.
