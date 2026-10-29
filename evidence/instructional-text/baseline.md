# Baseline: what the shapes are compared against

This file names the baseline a proposed shape of study text must beat, and says how the two would be compared.

## The named baselines

| Document | Baseline | Why this one |
|---|---|---|
| A section or chapter studied alone | the open-textbook section with its usual apparatus, as OpenStax prints it: objectives first, key terms in bold defined in context, a section summary, a concept check before the exercises, answers in a key at the back (OpenStax 2026b) | it is the apparatus learners meet and value (Weiten 1999; Marek 1999); open textbooks of this kind teach as much as commercial ones (Clinton 2019, k = 22, N = 100,012), so it stands for both |
| A lesson for one sitting | the Carpentries episode: questions and objectives at the top, challenges with nested solutions, key points at the end (Carpentries 2026a) | a template with required parts, used across 45 lessons and 4,980 workshops (Carpentries 2025) |

- The first is the primary baseline: it is what a learner studying alone holds.
- The plain linear text of the core's [learning-science baseline](https://github.com/Tewf/reader-ergonomics/blob/d17ee8e9bc07e0bd06e8ec7734cecd570b4e3b37/evidence/learning-science/baseline.md) is the floor below both.
- The baseline sources score OpenStax 2026b 10.5, Carpentries 2026a 14.5 and Carpentries 2025 11.5 of 20 (sources.md).

## Candidate variant to test

- Each objective is tagged, and every check carries the tag of the objective it tests (alignment made checkable).
- A misconception the text expects is written as a refutation block: the wrong idea stated, marked wrong, the accepted explanation given.
- Each key term is defined where it is first used, beside the text, rather than only in an end glossary.
- The summary closes the part, rather than opening it.
- A guided-notes sheet, generated from the headings and key terms with blanks, is offered with the text.
- Worked solutions keep their steps and leave the explanation of each step to the learner, with a prompt.
- These are hypotheses: each is graded in shapes-and-checks.md by the review line it rests on.

## How a comparison would be measured

| Question | Outcome | Instrument | Prior study to borrow from |
|---|---|---|---|
| Does the variant teach the stated aims? | share correct on items written from the objectives, one week later | objective-tagged test items, the same in both arms | Klauer 1984 (core): targeted and incidental items scored apart |
| Does it teach beyond them? | share correct on untargeted and transfer items | items on content no objective names; new problems | Klauer 1984; Mayer 1996 (transfer) |
| Does the refutation block change the misconception? | misconception items before, at once and four weeks later | a misconception inventory; a four-group design for the pretest | Jin 2025b; Zengilowski 2021 asks for delayed tests and several topics |
| Is the apparatus used? | which parts are opened, and for how long | logs of folds and scrolls in an online text | Gurung 2003 (self-report) as the weaker measure it replaces |
| What does it cost? | time on task; time to write | timed sessions; writer logs | none found for writers of study texts |

- Design: two arms with the same content and time; several topics, at least three, so one topic cannot carry the result (Zengilowski 2021).
- Effect sizes: Hedges' g with its confidence interval, reported against the named baseline, as the meta-analyses do (Schroeder 2022; Larwin 2013).
- Learners: novices and advanced learners analysed apart, since assistance helps novices and can hurt the advanced (core: Tetzlaff 2025).
- Self-reported use is not an outcome: it did not predict scores (Gurung 2004).

## A checklist in the baseline's own terms

Per section, from OpenStax 2026b:

1. Learning objectives open the section, stated so they can be measured.
2. Key terms are in bold and defined in context.
3. Key definitions, concepts and equations are called out.
4. A section summary reduces the section to its key points.
5. A concept check ends the section, before the exercises, with answers in the key.

Per episode, from Carpentries 2026a:

1. The header gives the teaching and exercise times.
2. Questions and objectives open the episode.
3. Challenges carry their solutions nested inside them.
4. Key points close the episode.

A shape may drop a baseline part deliberately; the drop is written where a reviewer looks for the missing part.
