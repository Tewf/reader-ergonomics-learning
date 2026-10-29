# Protocol: how the pool of sources was built

Every search, count and rule of the flashcards review, so it can be repeated. All searches ran on 2026-10-29, by one
reviewer, and the stopping rule (section 6) was written down before the first. Shared rules: [evidence README](../README.md#rules-the-four-reviews-share).

## 1. Why grey literature

For flashcards, Garousi 2019, Table 4 gets a yes on all seven questions.

| # | Question | Answer for flashcards |
|---|---|---|
| 1 | Complex, not solvable from formal literature alone? | yes: the formulation rules come from practice (Wozniak 1999) |
| 2 | Lack of volume or quality of evidence? | yes: no study of one fact per card, or of cloze against question cards, was found |
| 3 | Context important? | yes: second-language words, medical facts and mathematics use cards differently |
| 4 | Corroborate research with practice? | yes |
| 5 | Challenge practice with research, or the reverse? | yes: shared decks dominate in medicine, where the largest controlled comparison on text material favours learner-made cards |
| 6 | Would a synthesis serve both communities? | yes |
| 7 | Large practitioner volume? | yes: 68.3% of 560 US medical students used Anki in 2020 (Halperin 2024) |

## 2. Questions

| Id | Question |
|---|---|
| Q1 | How is a card formulated (one fact, cloze against question and answer, direction, context, images), research against practitioner rules? |
| Q2 | Do learner-made cards beat ready-made ones? |
| Q3 | How do learners use flashcards (dropping, stopping, cramming), and what does it cost? |
| Q4 | How much should a card hold; do similar cards interfere; do cards teach understanding or only facts? |
| Q5 | What is measured about texts with embedded prompts (the mnemonic medium)? |
| Q6 | What do practice and adoption look like (Anki, Quizlet, SuperMemo, shared medical decks), with counts and dates? |
| Q7 | How do cards generated from notes compare with written ones? |

Scheduling algorithms are not a question here; they are linked to the core's benchmark (Open Spaced Repetition 2026a).

## 3. Existing reviews (Garousi Guideline 2)

- Searched first, with strings F22 (reviews of spaced repetition and flashcards) and F23 to F25, and by checking each formal string's list for reviews.
- Found: 11 reviews and syntheses: Nakata 2011, Webb 2020, Lei 2022, Versteeg 2020, Xu 2024c, Öcel 2025, Nguyen 2021, Teymouri 2024, Kornell 2007, Bjork 2013, Kang 2016; all read by abstract. One handbook chapter was located, not opened (Nakata 2019b).
- Two meta-analyses of the generation effect (Bertsch 2007; McCurdy 2020) and one of text generation (Schindler 2023) are used in strand 3.
- Only Lei 2022 compares who makes the cards, by counting studies; none compares card formulations. They are placed in review.md strand 0.

## 4. Formal search

- ERIC: the public API, phrase-exact, `numFound` read; the 20 most relevant records listed per string.
- Semantic Scholar: the bulk search, not phrase-exact, sorted by citation count; the 20 most cited listed. A refusal (HTTP 429) was retried three to four times with waits of 6 to 80 seconds before it was recorded.
- arXiv: the public API, for generated cards and the mnemonic medium only.
- OpenAlex is not called here; its counts are added afterwards from [openalex.tsv](openalex.tsv).

| Id | String as run (ERIC syntax) | ERIC | Semantic Scholar form | Semantic Scholar | OpenAlex |
| --- | --- | --- | --- | --- | --- |
| F1 | flashcard OR flashcards OR "flash cards" OR "flash card" | 588 | `flashcard \ | flashcards \ | 10,238 | "flash cards" \ | "flash card"` | 7,302 |
| F2 | "spaced repetition" | 52 | `"spaced repetition"` | 831 | 1,298 |
| F3 | "spaced repetition" AND (software OR app OR application OR system) | 26 | `"spaced repetition" + (software \ | app \ | 627 | application \ | system)` | 382 |
| F4 | Anki | 12 | `Anki + (flashcards \ | "spaced repetition" \ | 750 | learning)` | 133 |
| F5 | Quizlet | 78 | `Quizlet` | 1,066 | 1,539 |
| F6 | SuperMemo | 1 | `SuperMemo` | 28 | 39 |
| F7 | "minimum information principle" | 0 | `"minimum information principle"` | 21 (all off topic: information theory, transport) | 26 |
| F8 | flashcards AND (formulation OR wording OR "item complexity" OR "card design") | 0 | `(flashcard \ | flashcards) + (formulation \ | 22 | wording \ | design)` | refused (HTTP 429) |
| F9 | cloze AND (flashcards OR "spaced repetition") | 1 | `cloze + (flashcards \ | flashcard \ | 9 | "spaced repetition")` | 5 |
| F10 | "paired associates" AND (retrieval OR testing) | 49 | `"paired associates" + (retrieval \ | testing)` | 3,279 | 3,008 |
| F11 | "cue overload" | 8 | `"cue overload"` | 41 | 57 |
| F12 | "generation effect" | 37 | `"generation effect"` | 1,582 | 1,765 |
| F13 | flashcards AND ("learner generated" OR "self-generated" OR "user-generated" OR "student-generated" OR premade OR "pre-made") | 2 | `(flashcards \ | flashcard) + ("self-generated" \ | 42 | "user-generated" \ | "student-generated" \ | premade \ | "pre-made" \ | "learner-generated")` | 31 |
| F14 | "mnemonic medium" | 0 | `"mnemonic medium"` | 13 (all off topic: memory studies) | 13 |
| F15 | flashcards AND ("self-regulated" OR dropping OR "study decisions" OR metacognition) | 10 | `(flashcards \ | flashcard) + ("self-regulated" \ | 56 | dropping \ | metacognitive)` | 63 |
| F16 | flashcards AND (cramming OR spacing OR spaced) | 14 | `(flashcards \ | flashcard) + (cramming \ | 350 | spacing)` | 49 |
| F17 | "semantic clustering" AND vocabulary | 7 | `"semantic clustering" + vocabulary` | refused (HTTP 429) | 136 |
| F18 | flashcards AND (conceptual OR "higher-order" OR application OR understanding) | 37 | `(flashcards \ | flashcard) + (conceptual \ | 1,807 | "higher-order" \ | understanding)` | 621 |
| F19 | flashcards AND (pictures OR images OR illustrations) | 19 | `(flashcards \ | flashcard) + (pictures \ | 682 | images)` | 425 |
| F20 | ("spaced repetition" OR Anki OR flashcards) AND ("medical students" OR "medical education") | 6 | `("spaced repetition" \ | Anki \ | 318 | flashcards) + ("medical students" \ | "medical education")` | 214 |
| F21 | flashcards AND (automatic OR generated OR "language model") AND generation | 3 | `(flashcards \ | flashcard) + generation + (automatic \ | 86 | "language model" \ | LLM)` | refused (HTTP 429) |
| F22 | ("spaced repetition" OR flashcards) AND ("systematic review" OR "meta-analysis" OR "scoping review") | 5 | `("spaced repetition" \ | flashcards) + ("systematic review" \ | 79 | "meta-analysis" \ | "scoping review")` | refused (HTTP 429) |
| F23 | "word cards" OR "vocabulary cards" | 98 | `"word cards" \ | "vocabulary cards"` | 693 | 505 |
| F24 | "digital flashcards" OR "electronic flashcards" | 29 | `"digital flashcards" \ | "electronic flashcards"` | 471 | 351 |
| F25 | "retrieval practice" AND flashcards | 7 | `"retrieval practice" + (flashcards \ | flashcard)` | 79 | 52 |
| F26 | "image occlusion" | 0 | `"image occlusion"` | 233 (all off topic: computer vision) | 260 |
| F27 | "paired-associate" AND (receptive OR productive) AND vocabulary | 4 | `("paired-associate" \ | flashcards) + receptive + productive + vocabulary` | 13 | refused (HTTP 429) |
| F28 | "successive relearning" | 7 | `"successive relearning"` | 22 | 24 |
| F29 | ("spaced repetition" OR flashcards) AND (attrition OR adherence OR dropout OR "drop out") | 0 | `("spaced repetition" \ | flashcards) + (attrition \ | 31 | adherence \ | dropout)` | 23 |
| F30 | pictures AND vocabulary AND ("retrieval practice" OR "paired associates" OR flashcards) | 9 | `pictures + "foreign language" + vocabulary + (retrieval \ | flashcards)` | 130 | 19 |
| F31 | "generation effect" AND (meta-analysis OR "meta-analytic") | 12 | `"generation effect" + (meta-analysis \ | "meta-analytic")` | 17 | 14 |
| F32 | flashcards AND (shared OR crowdsourced OR crowdsourcing OR "third-party") | 3 | `(flashcards \ | Anki) + (shared \ | 212 | crowdsourced \ | crowdsourcing \ | "third-party")` | 152 |
| F33 | "question generation" AND (flashcards OR "spaced repetition") | 0 | `("question generation" \ | "flashcard generation") + (flashcards \ | 9 | flashcard \ | "spaced repetition")` | 17 |
| F34 | Wozniak AND ("spaced repetition" OR SuperMemo OR "repetition spacing") | 0 | `Wozniak + ("repetition spacing" \ | SuperMemo \ | 3 | "spaced repetition")` | 4 (none on card writing) |
| F35 | Kornell AND flashcards | 0 | `Kornell + flashcards` | 5 | 1 |
| F36 | Nakata AND (flashcards OR "paired-associate" OR "word cards") | 3 | `Nakata + (flashcard \ | flashcards \ | 2 | "word cards")` | 3 |
| F37 | "embedded questions" AND (text OR reading) AND retention | 1 | `"embedded questions" + (text \ | reading) + (retention \ | 7 | recall)` | 13 |
| F38 | "word cards" AND (self-constructed OR "ready-made" OR premade OR "learner-made") | 6 | `"word cards" + ("self-constructed" \ | "ready-made" \ | 7 | premade)` | 4 |
| F39 | flashcards AND (bidirectional OR "both directions" OR reversed OR "direction of learning") | 1 | `(flashcards \ | "paired associates") + (bidirectional \ | 9 | "direction of learning" \ | reversed)` | refused (HTTP 429) |

| Id | arXiv string as run | Returned |
|---|---|---|
| X1 | all:flashcard AND all:generation | 10 |
| X2 | all:flashcards AND (all:"language model" OR all:LLM) | 3 |
| X3 | all:"spaced repetition" AND (all:"language model" OR all:LLM OR all:generation) | 13 |
| X4 | all:"spaced repetition" AND all:flashcards | 3 |
| X5 | all:"mnemonic medium" | 0 |
| X6 | all:"Quantum Country" | 0 |
| X7 | au:Matuschak | 0 |
| X8 | all:"embedded questions" AND all:text AND all:memory | 0 |

- Totals: ERIC 1,135 records over 39 strings. Semantic Scholar 17,232 over the 33 strings it answered (F8, F17, F21, F22, F27 and F39 refused after three or four attempts each); arXiv 29 over 8 strings.
- The Semantic Scholar refusals were retried last, after the arXiv strings; a lookup of the WikiFlash study was refused the same way.
- The Semantic Scholar form uses its own operators (`+` for AND, a vertical bar for OR) and sometimes fewer terms; the OpenAlex form of each string is in [openalex.tsv](openalex.tsv).
- Three ways for zero results: F7 and F14 returned nothing relevant; they were rephrased as F8, F34 (author Wozniak), X5 to X7 (product and author) and F37 (the research name, embedded questions). None found a formal study of either practice.
- Abstracts were read through the public ERIC, PubMed and Crossref services, without any identity; these lookups add no records to the counts.
- Leads named in the brief, verified: Kornell 2008, Kornell 2009, Wissman 2012, Hartwig 2012, Pan 2023b, Zung 2022, Deng 2015, Lu 2021, Slamecka 1978, Bertsch 2007. Also: Wozniak 1999, Matuschak 2020, Nielsen 2018, Matuschak 2019, the Anki manual (Anki 2026a).
- Lead not verified: Quizlet's published user counts (the company page refused the request, HTTP 403).
- Snowballing, backward: Hartwig 2012's abstract led to Kornell 2007; LLSE 2018b led to Nation 2000; a bibliographic query for Kim 2023 led to Nakata 2016. Forward: none beyond the strings.

## 5. Grey search

- Types and producers, chosen because the formal search pointed to them: the rule texts of SuperMemo and Anki, practitioner essays (Matuschak, Nielsen, Gwern, Bjornstad). Also: the mnemonic-medium project, company and encyclopedia pages for adoption, practitioner books, and Q/A sites.
- Engine: a general web search engine, the first result page per string; results personalise and change.

| Id | String as run (abridged) | Screened | Included |
|---|---|---|---|
| G1 | Quizlet monthly active learners number press about page 2025 | 20 | 1 (Wikipedia 2026e) |
| G2 | study comparing LLM-generated flashcards with human-written flashcards learning outcomes | 9 | 0 grey; 1 formal (Khurana 2025) |
| G3 | "mnemonic medium" Quantum Country results retention data Matuschak notes | 10 | 0 (the notes pages returned 404) |
| G4 | survey percentage of US medical students using Anki AnKing deck national survey | 27 | 0 grey; 1 formal (Halperin 2024) |
| G5 | Fluent Forever Gabriel Wyner 2014 Harmony Books publisher page | 9 | 1 (Wyner 2014, book not opened) |
| G6 | how to write good flashcards rules guide minimum information principle cloze | 28 | 0 new (guides repeat Wozniak 1999) |
| G7 | spaced repetition flashcard app users quit abandon retention rate data | 18 | 0 (no published rate) |
| P | direct visits: SuperMemo, Matuschak, Nielsen (two essays), Numinous Productions, Anki manual (three pages), Gwern, Control-Alt-Backspace, Quizlet (refused), Google Play (unreadable), TechCrunch (read, not included), Mobile Marketing (refused), Wikipedia (counted under G1), an ETH Zurich repository page (server error), medRxiv (refused; the abstract read through Crossref), the public GitHub API | 18 | 10 |

- Searches made only to reach a formal text (Kornell 2009 and Pan 2023b full texts, not found) are not grey strings and are not counted.

### Q/A sites

Strings FC1 to FC14 ran on 2026-10-29, one reviewer, grey tier 2, by the [shared Q/A method](../README.md#rules-the-four-reviews-share).

| Id | String as run | Site | Returned = screened | Included | New |
|---|---|---|---|---|---|
| FC1 | `q=flashcards` | Academia; Mathematics Educators; CS Educators; Language Learning; Psychology and Neuroscience | 47 | 9 | 9 |
| FC2 | `q=anki` | the same five | 40 | 8 | 5 |
| FC3 | `q=spaced repetition` | the same five | 64 | 8 | 4 |
| FC4 | `title=flashcard` | Academia; Mathematics Educators; Language Learning; Psychology and Neuroscience | 2 | 1 | 0 |
| FC5 | `q=cloze` | Language Learning | 7 | 1 | 0 |
| FC6 | `tagged=spaced-repetition` | Language Learning | 30 | 5 | 0 |
| FC7 | `tagged=flashcards` | Language Learning | 0 | 0 | 0 |
| FC8 | `q=memorize` | Mathematics Educators | 30 | 0 | 0 |
| FC9 | `q=quizlet` | Academia; Mathematics Educators; CS Educators; Language Learning | 7 | 1 | 1 |
| FC10 | `q=flashcards` | Medical Sciences | 0 | 0 | 0 |
| FC11 | `q=anki` | Medical Sciences | 0 | 0 | 0 |
| FC12 | `q=spaced repetition` | Medical Sciences | 0 | 0 | 0 |
| FC13 | `q=generation effect` | Psychology and Neuroscience | 9 | 0 | 0 |
| FC14 | `q=memorize definitions` | Academia | 4 | 0 | 0 |
| Total | 14 strings | | 240 | 19 (distinct) | 19 |

- Included: a thread that answers a question of the review with an argument or an experience, not only a how-to or a tool request.
- Excluded after reading: threads on whether spaced repetition works at all (the core's question), tool requests, threads without an answer, and a thread on spiral curricula (another topic).
- Stopping point: the last string that added a thread was FC9; FC10 to FC14, five strings, added none.

## 6. Stopping rule

- Stated before searching: effort bounded, the 20 most cited (Semantic Scholar) or most relevant (ERIC) per string, with saturation at k = 5 strings in a row that add no new included source.
- Formal: evidence exhaustion where a string returned fewer than 20 records; effort bounded otherwise.
- First pass: the last string to add a source was X1, and X2 to X8 (seven strings) added none, so saturation was reached.
- Retries: the retried Semantic Scholar list of F23 then added two sources (Lei 2022, Nakata 2019b); F27, F34 and F35 added none.
- Two more strings, F38 and F39, were run to test saturation and added none; with them, five strings in a row added nothing, and the search stopped.
- Grey web: the first result page per string; G6 and G7 added nothing new, and G3 added nothing readable.
- Q/A: the top 30 per string and site; stopped after FC14 (section 5).

## 7. Selection

- Include: a source on how cards are worded, who makes them, how learners use and keep them, embedded prompts, generated cards, or adoption. The source is in English and readable on the day at least by abstract or, for a book, by a catalogue page.
- Exclude:
  - a study that only re-measures retrieval or spacing (linked to the core, not reviewed): for example Janes 2020, which applies successive relearning (Rawson 2013, held by the core), Price 2025 and the schedulers' papers;
  - scheduling algorithms (SM-2, FSRS, half-life regression), linked to the core's benchmark;
  - single-case studies of flashcard drills for children with disabilities, and studies of children learning to read words;
  - works of another topic, passed on in [handoff](handoff.md);
  - a systematic review of six study strategies in STEM courses, received by handoff from the exercise-sets review (ERIC EJ1517222, abstract read): it asks whether the strategies work, the core's question;
  - Rawson 2007, on self-evaluation of key-concept definitions, received by handoff from the instructional-text review: no abstract reached, title only, so not used; Golding 2012, handed over by the same review, was already included;
  - a record whose abstract could not be read and whose title does not settle relevance.
- Grey sources must also pass section 8.

## 8. Quality of grey sources (Garousi Guideline 11, Table 7)

- Outlet tier: books and encyclopedias of record = tier 1 (1); company pages, project documentation, Q/A threads, wiki pages = tier 2 (0.5); personal essays and blogs = tier 3 (0).
- Scores, with subtotals, are in [sources](sources.md).

## 9. Extraction and synthesis

- Extracted per source: kind, year, the claim, the evidence offered, any number with its location (marked "(secondary)" when read in an abstract), and the question it answers.

## 10. Limits

- One reviewer; no second rater on this topic's grey sources.
- Most formal sources were read by abstract only; Deng 2015 and Lu 2021 were read in full. Publisher pages of Wiley, APA and Taylor and Francis were not readable.
- Semantic Scholar refused six strings on the day (marked); its counts are word matches, not phrase matches, and are noisy upper bounds.
- One OpenAlex request was made by mistake, to read the abstract of Kornell 2009; it returned the same text as Crossref, and no count was taken.
- The mnemonic-medium data of the author's working notes could not be read (pages returned 404), so only the 2019 essay is used.
- App-store and Quizlet pages could not be read; adoption counts rest on surveys and repository counts.
- This search did not find a study of one fact per card, of cloze against question cards in a spaced program, or of an essay with prompts against the same essay without. That is not proof that none exists.
