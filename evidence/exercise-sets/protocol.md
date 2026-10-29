# Protocol: how the pool of sources was built

Every search, count and rule of the exercise-sets review, so it can be repeated; every search ran on 2026-10-29. The rules the four reviews share are in the [evidence README](../README.md#rules-the-four-reviews-share).

## 1. Why grey literature

Garousi 2019, Table 4, answered for exercise sets: seven yes.

| # | Question | Answer for this topic |
|---|---|---|
| 1 | Complex, not solvable from formal literature alone? | yes: the exercise set as published (textbook sections, answer keys, online homework) comes from practice |
| 2 | Lack of volume or quality of evidence? | yes: the EEF review found 12 classroom studies of interleaving (Perry 2021); none tests a whole set design |
| 3 | Context important? | yes: subject, age and whether homework is graded change what works |
| 4 | Corroborate research with practice? | yes |
| 5 | Challenge practice with research, or the reverse? | yes: 9.7% of textbook problems are interleaved against classroom trials favouring interleaving (Rohrer 2020b) |
| 6 | Would a synthesis serve both communities? | yes: teachers ask for the evidence on Q/A sites and do not find it (MathEd 2021b, example only) |
| 7 | Large practitioner volume? | yes: online homework systems, problem sites and solution sites with millions of users (state-of-the-art.md) |

## 2. Questions

| Id | Question |
|---|---|
| Q1 | Blocked against interleaved or mixed review, at the level of a sheet or homework, in classrooms |
| Q2 | From worked example to problem: fading schedules, completion problems, example-problem pairs, Parsons problems |
| Q3 | Difficulty order and variability across a set |
| Q4 | Hints, answer keys and full solutions: when shown; help seeking and its abuse; copying |
| Q5 | How much practice; homework effects |
| Q6 | Practice and adoption: textbooks, problem books, past exams, online homework, mastery exercises, programming exercise sites |

## 3. Existing reviews (Garousi Guideline 2)

- Searched first, by strings F1 (interleaving reviews), F3 (homework meta-analyses) and the review hits of F2, F10, F15 and F31.
- Found: 13 reviews and meta-analyses, read by abstract except Fan 2017 (title and venue only); and the EEF review, read first-hand in its summary (Perry 2021, grey). They are placed in review.md strand 0.
- No review of the exercise set as a whole was found.

## 4. Formal search

Counts: ERIC (primary, phrase-exact, `numFound`), the Semantic Scholar bulk search (title and abstract, not phrase-exact), arXiv for strings where computing work is plausible. OpenAlex counts are added afterwards by script from `openalex.tsv`, which holds F1 to F35 and X1 to X7; the author strings A1 and A2 have no title-and-abstract form and are left out. No key and no identity were sent.

| Id | String as run (ERIC syntax) | ERIC | Semantic Scholar | OpenAlex | Included (new) |
| --- | --- | --- | --- | --- | --- |
| F1 | ("interleaved practice" OR interleaving) AND ("meta-analysis" OR "systematic review") | 4 | 39 | 53 | 2 |
| F2 | "Parsons problems" OR "Parsons puzzles" OR "Parson's programming puzzles" | 7 | 179 | 199 | 8 |
| F3 | homework AND "meta-analysis" | 32 | 158 | 185 | 3 |
| F4 | "interleaved practice" AND mathematics | 20 | 28 | 44 | 7 |
| F5 | "mixed review" OR "spiral review" OR "mixed practice" | 27 | 1,547 | 2,313 | 3 |
| F6 | "blocked practice" AND (mathematics OR classroom OR homework) | 15 | 38 | 42 | 0 |
| F7 | "backward fading" OR "faded worked examples" OR "faded examples" OR "fading worked" | 15 | 105 | 120 | 6 |
| F8 | "completion problems" OR "completion strategy" | 34 | 3,405 | 4,439 | 2 |
| F9 | "example-problem pairs" OR "problem-example pairs" OR "example-problem sequences" | 14 | 35 | 33 | 6 |
| F10 | "worked examples" AND ("problem solving" OR "practice problems") AND (classroom OR homework) | 47 | 100 | 202 | 1 |
| F11 | "variability of practice" OR "variable practice" OR "variability effect" | 32 | 2,380 | 1,161 | 1 |
| F12 | ("easy-to-hard" OR "difficulty sequencing" OR "problem difficulty") AND (practice OR exercises) AND learning | 13 | 161 | 77 | 1 |
| F13 | "desirable difficulties" AND (mathematics OR practice OR homework) | 17 | 126 | 230 | 2 |
| F14 | "variation theory" AND mathematics AND (exercises OR tasks OR practice) | 26 | 73 | 104 | 0 |
| F15 | "help seeking" AND ("intelligent tutoring" OR "interactive learning environments" OR hints) | 55 | 141 | 166 | 3 |
| F16 | "bottom-out hint" OR "bottom-out hints" OR "on-demand hints" OR "hint abuse" OR "gaming the system" | 58 | 2,884 | 616 | 2 |
| F17 | "homework copying" OR ("copying" AND homework AND (physics OR online)) | 13 | 133 | 159 | 3 |
| F18 | ("solution manual" OR "solutions manual" OR "answer key" OR "worked solutions") AND (students OR learning) | 1,110 | 2,469 | 6,512 | 1 |
| F19 | "online homework" AND (feedback OR "multiple attempts" OR "number of attempts") | 59 | 156 | 192 | 0 |
| F20 | homework AND ("time spent" OR "amount of homework" OR "homework time") AND achievement | 342 | 277 | 321 | 0 |
| F21 | overlearning AND (mathematics OR problems OR practice) | 29 | 223 | 242 | 1 |
| F22 | ASSISTments AND (homework OR "randomized controlled trial" OR efficacy) | 32 | 67,786 (noise: OR across words) | 89,106 | 3 |
| F23 | WeBWorK | 16 | 210 | 269 | 0 |
| F24 | "problem sets" AND (design OR sequencing OR order OR mixed) | 144 | 1,707 | 1,938 | 1 |
| F25 | "programming exercises" AND (practice OR drill OR "problem sets") | 7 | 254 | 291 | 0 |
| F26 | "exercise sets" OR "exercise sheets" OR "practice sets" | 78 | 1,842 | 2,342 | 0 |
| F27 | ("generative AI" OR ChatGPT) AND homework AND (learning OR hints OR performance) | 17 | 153 | 267 | 0 |
| F28 | "Saxon Math" OR "Saxon mathematics" OR "Saxon" (Semantic Scholar without the bare word) | 478 | 41 | 33 | 2 formal, 2 grey |
| F29 | ("textbook exercises" OR "practice problems") AND (textbooks OR analysis) AND mathematics | 44 | 208 | 268 | 2 |
| F30 | ("next-step hints" OR "automated hints" OR "hint generation") AND programming | 10 | 78 | 76 | 1 |
| F31 | ("spaced practice" OR "distributed practice" OR "spaced retrieval practice") AND (homework OR mathematics) AND (course OR classroom) | 17 | 36 | 43 | 4 |
| F32 | "worked examples" AND programming | 41 | 1,081 | 1,637 | 0 |
| F33 | homework AND (frequency OR effort) AND (multilevel OR "two-level" OR "three-level") | 23 | 66 | 69 | 1 |
| F34 | (Chegg OR "contract cheating" OR "homework help websites") AND (STEM OR homework OR mathematics) | 11 | 46 | 53 | 2 |
| F35 | (ChatGPT OR "generative AI" OR "GPT-4") AND (hints OR tutor OR "help") AND mathematics AND learning | 15 | 175 | 353 | 2 |
| A1 | author:"Rohrer, Doug" (ERIC only) | 31 | not run | not counted | 2 |
| A2 | author:"van Gog, Tamara" AND (problems OR problem) (ERIC only) | 36 | not run | not counted | 0 |

- Semantic Scholar refused 12 strings at first (HTTP 429); each was retried after waits of at least 6 seconds and all but F28 answered on the second pass; F28 answered on the third.
- The Semantic Scholar query is the same string in its syntax (`+` for AND, `|` for OR). It matches words, so F5, F8, F11, F16, F18, F22, F24 and F26 return unrelated fields (matrix completion, motor control, vehicle routing).

| Id | arXiv string (all fields) | arXiv | Included (new) |
|---|---|---|---|
| X1 | "Parsons problems" OR "Parsons puzzles" | 15 | 1 |
| X2 | hints AND programming AND ("large language model" OR LLM) AND students | 20 | 0 |
| X3 | ("generative AI" OR GPT) AND mathematics AND students AND learning AND randomized | 2 | 0 |
| X4 | "homework copying" | 1 | 1 |
| X5 | title: "generative AI" AND "harm learning" | 0 | 0 |
| X6 | "optimal learning" AND difficulty AND ("error rate" OR "training accuracy") | 1 | 0 |
| X7 | (ChatGPT OR GPT) AND hints AND mathematics AND learning | 4 | 0 |

- Totals: ERIC 2,969 records over 37 strings; Semantic Scholar 88,340 over 35 strings (20,554 without F22); arXiv 43 over 7 strings.
- Screened by title: the 20 most relevant ERIC records per string (631), the 20 most cited Semantic Scholar records per string (700), every arXiv record (43): 1,374, with repeats across strings.
- Abstracts were read through ERIC, Crossref, arXiv and one Semantic Scholar batch call; full texts were read for Rohrer 2015, Rohrer 2020b and Roschelle 2016 (ERIC copies) and Hou 2025 (arXiv).
- Leads named in the brief and verified: Rohrer 2007, Rohrer 2015, Rohrer 2020 (core), Atkinson 2003, van Merriënboer 1990, van Gog 2011 (core), Sweller 1985. Also verified: Parsons 2006, Ericson 2017, Aleven 2003, Palazzo 2010, Cooper 2006, Bjork 1994 and Saxon mathematics. Two were found only by title: Cooper 2006 (ERIC) and Sweller 1985 (Crossref).
- Snowballing, forward: Cox 2024 from Gulacar 2022 (same first-author group, Crossref); Rieger 2016 from Kontur 2015 (a published comment). Backward: none beyond the strings.

## 5. Grey search

- Types and producers, chosen because the formal search pointed to them: government and charity guidance (IES, What Works Clearinghouse, EEF), a national centre (NCETM), an open textbook (OpenStax). Also: online homework and problem projects (WeBWorK, ASSISTments, Project Euler), a company report (Chegg), and Q/A sites.
- Engine: a general web search engine, first result page per string; results personalise and change. The What Works Clearinghouse reports came through ERIC string F28.

| Id | String as run (abridged) | Screened | Included |
|---|---|---|---|
| G1 | IES practice guide "Organizing Instruction and Study to Improve Student Learning" interleave worked example solutions | 9 | 1 (Pashler 2007) |
| G2 | EEF "Cognitive science approaches in the classroom" systematic review interleaving worked examples | 10 | 1 (Perry 2021) |
| G3 | NCETM "intelligent practice" variation teaching for mastery | 20 | 1 (NCETM 2020) |
| G4 | WeBWorK open source online homework system institutions number | 10 | 1 (WeBWorK 2026) |
| G5 | Chegg annual report number of subscribers | 19 | 1 (Chegg 2025) |
| P | direct visits: Project Euler, Exercism, Runestone (refused, HTTP 403), ASSISTments, OpenStax answer key | 5 | 3 |

- Not used: the MAA WeBWorK page (HTTP 404), so its "700 colleges" claim seen in a search summary stays unverified; Exercism (no counts on the page).

### Q/A sites

Strings ES1 to ES23 ran on 2026-10-29, one reviewer, grey tier 2, by the [shared Q/A method](../README.md#rules-the-four-reviews-share). Threads were read with their bodies (`filter=withbody`).

| Id | String as run | Site | Returned = screened | Included | New |
|---|---|---|---|---|---|
| ES1 | `q=interleaving` | Mathematics Educators | 2 | 1 | 1 |
| ES2 | `q=interleaved` | Mathematics Educators | 2 | 1 | 0 |
| ES3 | `q=spiral review` | Mathematics Educators | 0 | 0 | 0 |
| ES4 | `q=spiral` | Mathematics Educators | 5 | 0 | 0 |
| ES5 | `title=homework` | Mathematics Educators | 30 | 5 | 5 |
| ES6 | `title=solutions` | Mathematics Educators | 30 | 7 | 6 |
| ES7 | `q=worked examples` | Mathematics Educators | 30 | 1 | 1 |
| ES8 | `q=Parsons` | Computer Science Educators | 3 | 1 | 1 |
| ES9 | `title=exercises` | Computer Science Educators | 18 | 2 | 2 |
| ES10 | `q=hints` | Computer Science Educators | 8 | 0 | 0 |
| ES11 | `title=homework` | Computer Science Educators | 7 | 1 | 1 |
| ES12 | `title=practice` | Computer Science Educators | 15 | 0 | 0 |
| ES13 | `title=homework solutions` | Academia | 1 | 1 | 1 |
| ES14 | `title=problem sets` | Academia | 3 | 0 | 0 |
| ES15 | `q=Chegg` | Academia | 19 | 2 | 2 |
| ES16 | `title=homework` | Academia | 30 | 4 | 3 |
| ES17 | `q=answers back of the book` | Academia | 25 | 1 | 0 |
| ES18 | `title=exercises` | Mathematics Educators | 30 | 5 | 3 |
| ES19 | `q=hints` | Mathematics Educators | 30 | 2 | 1 |
| ES20 | `title=practice` | Mathematics Educators | 14 | 0 | 0 |
| ES21 | `q=blocked practice` | Mathematics Educators | 3 | 1 | 0 |
| ES22 | `title=problem sets` | Mathematics Educators | 1 | 0 | 0 |
| ES23 | `title=difficulty` | Mathematics Educators | 14 | 2 | 2 |
| Total | 23 strings | | 320 | 29 (distinct) | 29 |

- Excluded after reading: grading policy, product support (a Chegg tool), tooling how-to (paper Parsons construction), threads of another topic (spaced repetition sites), and unanswered threads that add nothing.
- The run ended after ES23, when each term of the field had been run in at least one form; ES23 added 2 new threads. The daily quota fell from 275 to 235 calls.

## 6. Stopping rule

- Stated before searching (and written first in this file): effort bounded, the 20 most relevant ERIC records and 20 most cited Semantic Scholar records per string. Saturation at k = 5 strings in a row that add no new included source.
- Applied: saturation at k = 5 was not reached; the longest run without a new source was three strings (F25 to F27). The search stopped on the effort bound, once every field name of the brief and every sub-question had been run in at least one string.
- Evidence exhaustion: F1, F2, F6, F7, F9, F12, F13, F17, F25, F30, F31, F34, F35 returned 20 or fewer ERIC records, all screened.
- Grey web: first result page per string. Q/A: as above.

## 7. Selection

- Include: a source on how practice items are ordered, supported, solved, checked or assigned as a set, measured on learners or counted in practice. The source is in English and readable on the day at least by abstract (a title states the result only for Harms 2016).
- Exclude:
  - motor and sport training (variability of practice in its original field), clinical and language-drill studies, matrix completion and other word collisions;
  - feedback content and timing, question format and folded answers to single questions (passed to practice-questions);
  - worked-solution writing as a genre (passed to instructional-text);
  - effects already held by the core, linked instead;
  - sources whose abstract could not be read and whose title does not settle relevance.

## 8. Quality of grey sources (Garousi Guideline 11, Table 7)

- Outlet tier: government and charity reports, standards and textbooks = tier 1 (1); project and company pages, handouts, company reports and Q/A threads = tier 2 (0.5); blogs = tier 3 (0).
- Scores are in sources.md.

## 9. Extraction and synthesis

- Extracted per source: kind, year, sample, design, the outcome and its delay, any number (marked "(secondary)" when read in an abstract), and the question it answers.

## 10. Limits

- One reviewer, no second rater for this topic yet.
- Search engines personalise and change; Semantic Scholar counts are not phrase-exact; OpenAlex counts were taken afterwards by script, title and abstract, phrase search.
- Publisher pages of ACM, APS, Elsevier and PNAS refused automated reading; several computing studies are known by title and abstract only.
- Most formal sources were read by abstract; sources.md says which.
- This search did not find a study of a whole exercise set built from all the measured parts; that is not proof none exists.
