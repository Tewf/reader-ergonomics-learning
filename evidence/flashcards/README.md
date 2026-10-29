# Flashcards: how a set of prompts for spaced review is written, made and kept

Question: how is a set of prompts for spaced review written and kept, so that reviewing it makes the learner retain and use what it holds? And what does the evidence say about card formulation, granularity and who makes the cards?

- This is a multivocal literature review (Garousi 2019) by one reviewer, searched on 2026-10-29.
- It holds 69 formal sources, all new to the reader-ergonomics repositories.
- It scores 31 grey sources out of 20 (12 from the web, 19 threads from Q/A sites); 6 are used as examples only, one of them after the second rater scored it below 10.
- A number read only in an abstract or a summary is marked "(secondary)".
- Whether retrieval and spacing work, and how a scheduler is chosen, is not reviewed here: see the [core learning-science review](https://github.com/Tewf/reader-ergonomics/blob/adb53c52fa8eefe0e621e520365157bbbcad1a1a/evidence/learning-science/review.md).

## Files

| File | Role |
|---|---|
| [protocol](protocol.md) | how the pool was built: questions, strings, counts, stopping rule, scoring |
| [sources](sources.md) | the flow of the pool, and one row per source with its quality |
| [frame](frame.md) | step 1: the problem in one sentence, and what research and practice call it |
| [review](review.md) | step 2: existing reviews, seminal rules, formulation, who makes cards, use, granularity, embedded prompts, generated cards, practice |
| [state of the art](state-of-the-art.md) | step 3: most adopted against best evidence, per question; upper and lower bounds |
| [position](position.md) | step 4: known, not known, where practice runs ahead of the evidence |
| [against](against.md) | null results, contradictions, failed replications, limits |
| [baseline](baseline.md) | step 5: the deck a shape must beat, and how to measure it |
| [bibliography](../bibliography.md) | every cited work: key, citation, link |
| [shapes and checks](shapes-and-checks.md) | proposals for the maintainer: deck blocks and checks a program could run |
| [handoff](handoff.md) | works met here that belong to another topic |
| `flow.json`, `openalex.tsv` | the flow as data; the formal strings in OpenAlex syntax |

## Claims

| Claim | Grade | Where |
|---|---|---|
| Learners drop a card once they can recall it, and dropping lowers retention | measured (laboratory experiments; abstracts read) | review.md 4 |
| One large stack beats several small ones, which mass the reviews; 72% of learners believed the opposite | measured (three experiments; secondary) | review.md 4 |
| Learner-made cards beat premade cards under matched time: d = 0.45 for memory, 0.29 for application | measured, one paper of six experiments (secondary) | review.md 3 |
| Premade word cards matched or beat self-made ones in two vocabulary studies and in a count of 32 word-card studies | supported with caveat (abstracts read; the count is not pooled) | review.md 0, 3; against.md |
| Generating beats reading by about 0.40 (secondary), depending on how constrained the generation is; for texts it failed to replicate in seven experiments | measured (meta-analyses), contested | review.md 3; against.md |
| Medical students who use Anki score higher | supported with caveat (observational, self-selected) | review.md 3, 8 |
| Related words learned together raise confusion errors, without always lowering scores | measured, second-language words only | review.md 5 |
| With spacing equal, set size matters little | measured, one study (secondary) | review.md 5 |
| Cards on concepts or application help some learners more than detail cards | supported with caveat (two studies, abstracts) | review.md 5 |
| Pictures on cards help concrete words, and only once overconfidence is checked | supported with caveat (vocabulary experiments) | review.md 2 |
| One idea per card, one answer, no yes or no prompt, no list answer | convention, untested (practitioner rules agree; no study found) | review.md 1, 2 |
| Fill-in-the-blank sentences and flashcards showed no overall difference at two weeks, massed or spaced (secondary); cloze against question cards inside a spaced repetition app was not found tested | supported with caveat (one study) | review.md 2 |
| Readers of an essay with embedded prompts showed long retention | convention, untested (the authors' own data in an essay, no control) | review.md 6 |
| Generated cards held 1 error in 21 after tuning, with no exam difference (secondary) | supported with caveat (preprint, self-selected) | review.md 7 |
| 68.3% of 560 US medical students used Anki in 2020 (secondary) | measured, descriptive (self-selected survey) | review.md 8 |
| Students self-test to check, not to learn, and space too little | measured, descriptive (surveys) | review.md 4 |

## Named baseline

- Primary: a learner-made deck of question-and-answer cards in Anki under its default scheduler, from the same text (Pan 2023b's stronger arm).
- Secondary: a ready-made shared deck of the same content, the most adopted form in medicine (Lu 2021).
- Comparison: matched time, delayed recall and application, adherence and review cost from the app's log ([baseline](baseline.md)).

## Linked, not reviewed again

- Retrieval, spacing and successive relearning: [learning science](https://github.com/Tewf/reader-ergonomics/blob/adb53c52fa8eefe0e621e520365157bbbcad1a1a/evidence/learning-science/review.md), strand 2.
- Schedulers and the FSRS benchmark: the same file, strand 8.
- Folded answers: [progressive disclosure](https://github.com/Tewf/reader-ergonomics-topic/blob/1220def7863b5e977a3edd1e30bd168fff1523a5/evidence/progressive-disclosure/README.md).
- The principles of the standard this review serves: [the list](../README.md#the-principles-of-the-standard-these-reviews-serve).
