# 0003: Derive the shapes from the topic, at pinned releases

**Decision:** every shape of this repository will derive from the topic of reader-ergonomics-topic, and both parents
are linked and run at a release's commit: reader-ergonomics v1.9.0 and reader-ergonomics-topic v0.4.0.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/e8864477a53d713251ba42a4cf7b7a0d761243a2/shapes/decision-record.md).

## Context

- The topic is a base for genre shapes: a title, a summary, a body, contents and see also, and a shape adds blocks
  without removing any
  ([topic](https://github.com/Tewf/reader-ergonomics-topic/blob/1220def7863b5e977a3edd1e30bd168fff1523a5/shapes/topic.md)).
- Its first derived shape was the decision record. Since v1.3.0 the standard holds a general one, which this
  repository's records follow.
- The extension contract asks an extension to pin the standard by commit, never by tag
  ([extending.md](https://github.com/Tewf/reader-ergonomics/blob/e8864477a53d713251ba42a4cf7b7a0d761243a2/extending.md)).

## Decision

- A lesson, an exercise sheet, a study guide or a deck will be a topic with blocks of its own.
- Each block takes a name from the topic's table of accepted names, and each document links the shape it follows.
- Links down to either parent carry the release's commit. CI checks out reader-ergonomics at
  `e886447` (v1.9.0).
- The topic check is not run here yet: it reads the shapes, and none is written. It joins CI with the first shape.

## Consequences

- Study documents read like every other document of the family, at every depth.
- A change in either parent reaches this repository only when its pin moves, by a record here.
- If a study document needs a block the topic forbids, the conflict goes to reader-ergonomics-topic, not around it.

## See also

[Decisions](README.md); [where it sits](../README.md#where-it-sits).
