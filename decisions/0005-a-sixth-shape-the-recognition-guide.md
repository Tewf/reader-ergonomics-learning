# 0005: A sixth shape, the recognition guide

**Decision:** the repository holds a sixth shape, the recognition guide, which tells the types a sheet drills apart by their signals and refutes the look-alikes. It defines nothing and links the lesson of each type.

**Status:** accepted, 2026-11-07. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/shapes/decision-record.md).

## Context

- The study guide's error grid names five causes of a miss; one is recognising the type. The lesson teaches a type,
  the sheet drills it and the guide revises it ([0004](0004-five-shapes-and-a-markup.md)); none tells two types apart.
- A vault of course notes needed exactly that on 2026-11-07, for the models of linear programs and flows. A problem
  from either of two courses is a matching, a flow, a cut, an assignment, or none; the courses teach the tools and not
  the telling-apart. The catalogue note written there is the pilot of this shape.
- The field's own books carry such catalogues: an applications chapter, a taxonomy of problem types. No study tests
  one against recognition errors, so the shape enters as a convention, with the grid as the measure to run.

## Decision

- **A shape of its own,** with the headings Types, Signals, Decision, Not one of them, Check yourself and See also,
  checked by the standard's shape-conformance and by `questions` where a repository declares the file.
- **Its types are the sheet's types,** the same ids, so a type has one name across the three documents.
- **It defines nothing:** each type links the lesson that teaches it; a signal that needs a paragraph is a missing
  lesson.
- **One example,** on the subject the others use, binary search: which search a statement asks for.

## Options it rules out

| Option | Why it lost |
|---|---|
| a part of the study guide | the guide prepares one exam; recognition spans courses, and the grid's cause is the same in each |
| a lesson whose parts are the types | a lesson defines and explains; a guide compares, in a table, what is defined elsewhere |
| the sheet's Types list alone | ids and names, no signals; the sheet's job is the drill |

## Consequences

- Good: the recognition cause of the grid has a document to send the learner to, and a table to keep per course.
- Bad: a sixth shape to keep in step with the five; its evidence is the weakest of the six until the grid is counted.
- To keep it true: count, in the study logs, the misses graded "recognition" before and after a guide is written for a
  course, and bring the number here.

## See also

[Decisions](README.md); the [shape](../shapes/recognition-guide.md) and its [example](../shapes/examples/binary-search-recognition.md).
