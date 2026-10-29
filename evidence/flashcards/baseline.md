# Baseline: what a deck's shape must beat

This file names the baseline that a proposed shape for flashcards must beat, and how the two would be compared.

## The named baseline

| Role | Baseline | Why this one |
|---|---|---|
| Primary | a **learner-made deck** of basic question-and-answer cards in Anki, under its default scheduler, written from the same study text | the stronger arm of the largest controlled comparison on text material (Pan 2023b, six experiments; word-card studies lean the other way, Lei 2022); the form the Anki manual recommends for complex subjects (Anki 2026a) |
| Secondary | a **ready-made shared deck** of the same content, used as downloaded | the most adopted form in medicine: at least 80% of respondents in Lu 2021 |

- A shape proposed here is a ready-made deck by definition: it ships with the study material.
- It must therefore beat the secondary baseline, and should not fall below the primary one.
- Falling below a learner-made deck would repeat the gap Pan 2023b found, d = 0.45 for memory (secondary).
- The scheduler is held constant at Anki's default; scheduler choice belongs to the core's benchmark (Open Spaced Repetition 2026a).

## Candidate variant to test

- A deck derived from the study text, each card linked to its section, written to the converging rules: one idea, one answer, no yes or no prompt, no list answer, context named.
- A share of cards on concepts and application, not only details, after Senzaki 2017 and Lin 2018.
- Confusable items introduced on different days, after Nakata 2019.
- An instruction to the learner to add their own cards and not to drop cards early, after Pan 2023b and Kornell 2008.
- These are hypotheses, graded **convention, untested**, except where the cited study measured them.

## How a comparison would be measured

| Reader task | Outcome | Instrument | Prior study to borrow from |
|---|---|---|---|
| Remember what the text holds | share correct on cued recall, 48 hours and 1 week or more after study | questions on definitions from the text | Pan 2023b (48-hour criterial test) |
| Use it | share correct on application questions not shown on any card | new problems or cases | Pan 2023b (application questions); Senzaki 2017 |
| Keep the deck | days of review until abandonment; share of learners still reviewing at 4 weeks | the app's review log | Seibert Hanson 2020 (days studied); Ingebrigtsen 2025 (uptake) |
| Cost | review minutes per retained item; lapses per card; leeches per 100 cards | the app's review log | Nakata 2017 (gain per time); Anki 2026c (leech count) |
| Confusion | interference errors between paired items | final test coding | Nakata 2019 |

- Design: within-subject over matched text passages, counterbalanced, total time matched, as in Pan 2023b.
- Subjects: novices in the domain, since the core holds that support helps novices more (core review, strand 3).
- Report effect sizes with confidence intervals and the control used, as the core asks.
- A trial in a course should randomise at the level of the course or campus, as Senzaki 2017 and Ingebrigtsen 2025 did.

## A checklist for a card in the baseline's own terms

Per card, from Wozniak 1999 and Matuschak 2020:

1. The learner understands the material before the card is made (rule 1).
2. One idea per card (rule 4); a list becomes several cards or a cloze per item (rules 9 and 10).
3. One correct answer; the prompt rules out other correct answers.
4. No yes or no prompt; ask why or how instead.
5. Enough context named on the front to make the question unambiguous (rule 16).
6. The card cites its source (rule 18).
7. Two cards that the learner confuses are rewritten to differ, or separated in time (rule 11; Anki 2026c).

A rule may be broken deliberately; the deck then says why, where a reviewer looks for it.
