# State of the art, per sub-question

This file names who holds the record on each sub-question, by what method and measured how.
Two records are kept apart: **most adopted** (what people use) and **best evidence** (what a study measured).
Upper bounds (what has been achieved) are kept apart from lower bounds (what has not been shown).

## Records

| Sub-question | Most adopted | Best evidence | Measured how |
|---|---|---|---|
| Q1 how a card is worded | Wozniak 1999's twenty rules, repeated by Matuschak 2020, Nielsen 2018, Bjornstad 2020 and the Anki manual (Anki 2026c) | none on wording as such; Lin 2018 and Senzaki 2017 on conceptual cards | experiments and course studies, abstracts read |
| Q1 direction and pictures | Anki's "Basic (and reversed card)" note type (Anki 2026a) | Griffin 1996; Carpenter 2012; Ide 2026 | laboratory and classroom vocabulary experiments |
| Q1 cloze against question and answer | Anki's cloze note type (Anki 2026a) | Kim 2023, fill-in-the-blank sentences against flashcards, 150 learners (secondary) | two-week delayed vocabulary test |
| Q2 learner-made against ready-made | shared premade decks in medicine: at least 80% of 201 respondents (Lu 2021) | Pan 2023b, six experiments; against it, Lei 2022 for word cards | 48-hour delayed test, memory and application; a count of 32 studies |
| Q3 dropping and stopping | dropping known cards, almost universal (Kornell 2008); Anki's leech suspension after 8 lapses (Anki 2026c) | Kornell 2008; Karpicke 2009; Pyc 2011 | laboratory paired associates, delayed tests |
| Q3 stack size and cramming | small stacks, cramming before exams (Kornell 2009; Hartwig 2012) | Kornell 2009 | three experiments, 90% of learners better with spacing (secondary) |
| Q4 granularity | minimum information principle (Wozniak 1999) | Nakata 2016 on set size; no study of card size found | second-language word pairs |
| Q4 interference | "avoid sets", "combat interference" (Wozniak 1999) | Nakata 2019; Ishii 2015; Tinkham 1997 | confusion errors and posttests, word pairs |
| Q4 understanding against facts | detail cards, the kind learners write most (Lin 2018) | Senzaki 2017 (434 students in six courses); Pan 2023b application d = 0.29 (secondary) | course exams; application questions |
| Q5 text with embedded prompts | Quantum Country and Orbit (Matuschak 2019; GitHub 2026h) | Matuschak 2019, informal delayed-review test, 16 and 25 users | accuracy before and after a two-week delay |
| Q6 adoption | Anki in medicine: 68.3% of 560 students (Halperin 2024, secondary); Quizlet, uncited 60 million monthly users (Wikipedia 2026e, example only) | n/a (a practice record) | self-selected surveys; repository counts |
| Q6 outcomes of real use | Anki with shared decks | Lu 2021, d = 0.38 (full text); Deng 2015; Gilbert 2023 | observational cohorts and surveys |
| Q7 generated cards | generated decks in medicine (Khurana 2025) | Khurana 2025, no exam difference, self-selected (secondary) | preprint, quasi-experiment |

## Adoption counts, descriptive, taken 2026-10-29

| Count | Value | Caveat |
|---|---|---|
| stars, Anki repository (created 2012-12-21) | 32,379 | interest, not use |
| stars, AnkiDroid | 12,116 | interest, not use |
| stars, FSRS add-on for Anki | 4,119 | scheduler, linked to the core |
| stars, Orbit (an experimental spaced repetition platform, by its description) | 1,838 | interest, not use |
| US medical students using Anki in 2020 | 68.3% of 560, 102 schools | social-media recruitment (Halperin 2024, secondary) |
| daily Anki users at one school | 56% of 165 | one school (Wothe 2023, secondary) |
| Anki users among respondents at one school | 132 of 201 | 36.9% response, respondents scored higher than non-respondents (Lu 2021) |
| Anki and commercial cards, one school, 2015 | 31% and 49% of 72 | Deng 2015 |
| introductory psychology students using flashcards | almost 70% of 415 | Golding 2012, secondary |
| Quizlet monthly users, 2021 | over 60 million | uncited on the page; the company page refused the request |

- Repository counts are the reviewer's own reading of public listings (GitHub 2026h), not a source.
- No public count of active Anki users was found; app-store counts could not be read.

## Upper bounds (achieved)

- Learner-made cards beat premade ones under matched time, d = 0.45 for memory (Pan 2023b, secondary).
- Cards written for application raised course exam scores in a cluster design of six courses (Senzaki 2017, secondary).
- Teacher-made cards given to whole campuses went with higher exam scores among those who used them, d = 0.42 (Ingebrigtsen 2025, secondary).
- Embedded prompts kept a month of retention on most of 112 questions for 195 readers (Matuschak 2019).
- Generated cards reached 1 error in 21 after prompt tuning (Khurana 2025, secondary).

## Lower bounds (not yet shown)

- No study tests one fact per card against several facts per card.
- No study tests a cloze card against a question-and-answer card inside a spaced repetition program; Kim 2023 is the nearest.
- No randomised trial of Anki or a shared deck on a course or licensing exam was found; the medical studies are observational.
- No comparison of an essay with embedded prompts against the same essay without them was found.
- No randomised comparison of generated against written cards on delayed recall was found.
- No published dropout rate for flashcard apps was found; only anecdote (Branwen 2019, citing a 2012 developer) and low uptake (Ingebrigtsen 2025).
