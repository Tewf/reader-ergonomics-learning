# Exercise sets: how a set of exercises is ordered and supported

Question: how is a set of exercises ordered and supported, so that working through it builds a method the learner can apply to a new problem? And what does the evidence say about sequence, fading, hints and solutions?

- It is a multivocal literature review (Garousi 2019) by one reviewer, searched on 2026-10-29.
- It holds 78 new formal sources and links 13 more already reviewed in the core repository.
- It scores 39 grey sources out of 20 (10 from the web and the What Works Clearinghouse, 29 Q/A threads); 12 fall below the threshold of 10 and are used as examples only.
- It is not a standard, a new result, or a claim to the state of the art. A number read only in an abstract is marked "(secondary)".

## Files

| File | Role |
|---|---|
| [protocol](protocol.md) | how the pool was built: questions, strings with ERIC and Semantic Scholar counts, stopping rule, scoring |
| [sources](sources.md) | the flow of the pool, then one row per source with its quality |
| [frame](frame.md) | step 1: the problem in one sentence, the terms, what research and practice call it |
| [review](review.md) | step 2: existing reviews, seminal work, one strand per sub-question, practice, Q/A sites |
| [state of the art](state-of-the-art.md) | step 3: most adopted against best evidence, adoption counts, upper and lower bounds |
| [position](position.md) | step 4: known, not known, where practice and evidence part |
| [against](against.md) | null classroom results, contested orders, the Saxon case, the limits |
| [baseline](baseline.md) | step 5: the blocked sheet the shapes must beat, and how to measure it |
| [shapes and checks](shapes-and-checks.md) | proposals for the blocks of a set and the checks a program could run |
| [bibliography](../bibliography.md) | every cited work: key, citation, link |
| [handoff](handoff.md) | works met here that belong to the sibling reviews |
| `flow.json`, `openalex.tsv` | the flow as data; the formal strings in OpenAlex syntax, for counting by script |

## Claims

| Claim | Grade | Where |
|---|---|---|
| Interleaving the problem types of homework raised delayed classroom test scores: d = 0.79 at 30 days, 1.05 at two weeks | measured, classroom trials in mathematics (one read in full, one secondary) | review.md 2 |
| A full year of interleaved sets raised short-term scores (0.29 SD) and not a cumulative test | measured, one cluster trial, working paper (secondary) | against.md |
| Spacing a type across sets beats massing it in mathematics, less inside courses (g = 0.28; 0.24) | measured, meta-analysis (secondary) | review.md 0 |
| 9.7% of 13,505 problems in six mathematics textbooks are interleaved | measured, descriptive | review.md 7 |
| Most students judge the least spaced, least interleaved schedules most effective | measured, descriptive (secondary) | review.md 2 |
| Nine problems of one type in one session did no better than three at one and four weeks | measured, one study (secondary) | review.md 6 |
| Fading worked steps beats example-problem pairs on near transfer; adaptive fading beats fixed fading | measured (secondary) | review.md 3 |
| Example-problem order beats problem-example in some studies and not in others | measured, contested | review.md 3; against.md |
| Parsons problems are as effective as writing the equivalent code, and faster | measured, one research group (abstracts) | review.md 3 |
| Variability helps experienced learners and hurts novices | measured, one paper (secondary) | review.md 4 |
| Training help seeking changed help use, not learning | measured (secondary) | review.md 5 |
| Open model access during practice lowered later exam grades by 17%; a hint-only tutor avoided most of the loss | measured, one field experiment (secondary) | review.md 5 |
| Homework copying rises toward deadlines and goes with lower exam scores | measured, descriptive (secondary) | review.md 5 |
| Online homework with hints and teacher reports raised an end-of-year standardised test, g = 0.18 | measured, one randomised field trial (read in full) | review.md 6 |
| Online and paper homework do not differ | measured, meta-analysis of 18 studies (secondary) | review.md 0 |
| Odd-numbered answers only, solutions released after submission, variation sets, starred problems | convention, untested | review.md 7, 8 |
| A set built from all the measured parts beats the blocked textbook set | convention, untested (a hypothesis to test) | position.md; baseline.md |

## Named baseline

- To beat: **B1, the blocked sheet**, one run of same-type problems per lesson with answers to half the items at the end (Rohrer 2020b; OpenStax 2026).
- To match on the opening of a type: **B2, the example-problem pair** (van Gog 2011, linked; Pashler 2007).
- Comparison: classes randomised, same problems, unannounced mixed tests at one and 30 days and at the end of the year; strategy choice, transfer, time and help use logged; d or g per outcome ([baseline](baseline.md)).

## Linked, not reviewed again

- Principles of the standard an exercise set serves: listed in the [evidence README](../README.md#the-principles-of-the-standard-these-reviews-serve).
- The effects themselves (interleaving, spacing, worked examples, fading): the core's [learning science](https://github.com/Tewf/reader-ergonomics/blob/c08433c4d868d9b38ac1441f58ae7602c399db6d/evidence/learning-science/review.md).
