# Protocol: how the pool of sources was built

Every search, count and rule of the practice-questions review; all searches ran on 2026-10-29, one reviewer. Terms are defined in [frame](frame.md); shared rules in the [evidence README](../README.md#rules-the-four-reviews-share).

## 1. Why grey literature

Garousi 2019, Table 4, answered for practice-questions: all seven questions get a yes.

| # | Question | Answer for this review |
|---|---|---|
| 1 | Complex, not solvable from formal literature alone? | yes: item-writing rules come from textbooks and testing bodies, not from studies (Haladyna 1989) |
| 2 | Lack of volume or quality of evidence? | yes: no study compares where answers sit in a study text |
| 3 | Context important? | yes: classroom and lab results on format disagree (Yang 2021; Rowland 2014) |
| 4 | Corroborate research with practice? | yes |
| 5 | Challenge practice with research, or the reverse? | yes: textbook questions stay at low levels (Momsen 2010) |
| 6 | Would a synthesis serve both communities? | yes |
| 7 | Large practitioner volume? | yes: 12,654,431,762 quiz questions on registered Moodle sites (Moodle 2026) |

## 2. Questions

Q1 to Q7, as in [frame](frame.md): kinds and levels; format; item writing; feedback; where answers sit; practice; generated questions.

## 3. Existing reviews (Garousi Guideline 2)

- Searched first, by strings F13 (feedback meta-analyses), F18b (transfer meta-analyses), F7 (item-writing guidelines), F15 (AQG reviews) and F23 (distractor reviews).
- Found: 20 new reviews and meta-analyses, plus the core's Rowland 2014 and Yang 2021, whose moderator sections were read in full. New ones read in full: Pan 2018, Wisniewski 2020, Hattie 2007. By abstract: 16. Through a news release: Butler 2018.
- Located, not used: a survey of AQG and answer assessment (ERIC EJ1288621; 2021) and a meta-analysis of retrieval against elaborative encoding (ERIC EJ1492680; 2025). Also: a 1985 review of adjunct questions and objectives (reviewed in the instructional-text review).
- They are placed in review.md strand 0.

## 4. Formal search

Count sources: ERIC (phrase-exact, field `response.numFound`), the Semantic Scholar bulk search (not phrase-exact; most cited first), and the arXiv API for generated questions. OpenAlex is counted afterwards from `openalex.tsv`. Semantic Scholar refused many calls (HTTP 429); each refused string was retried three times, about 20 s apart.

| Id | String as run (ERIC syntax) | ERIC | Semantic Scholar | OpenAlex |
| --- | --- | --- | --- | --- |
| F1 | "test-enhanced learning" | 32 | 209 | 260 |
| F2 | "retrieval practice" AND ("multiple-choice" OR "short-answer") | 36 | 128 | 161 |
| F3 | "testing effect" AND ("question format" OR "test format") | 8 | 30 | 44 |
| F4 | "adjunct questions" | 111 | 206 | 204 |
| F5 | ("higher-order questions" OR "higher order questions" OR "higher-level questions") AND (text OR reading OR quiz) | 53 | 138 | 174 |
| F6 | "retrieval practice" AND Bloom | 2 | refused (HTTP 429) | 14 |
| F7 | "item writing" AND (guidelines OR rules) | 61 | 152 | 213 |
| F8 | "item-writing flaws" OR "item writing flaws" OR "flawed items" | 20 | 167 | 195 |
| F9 | "multiple-choice" AND ("number of options" OR "three-option" OR "three options") | 39 | 180 | 191 |
| F10 | distractors AND misconceptions AND "multiple-choice" | 23 | refused (HTTP 429) | 173 |
| F11 | "elaborated feedback" OR "elaborative feedback" | 83 | 302 | 357 |
| F12 | "delayed feedback" AND (test OR quiz OR testing) | 58 | 694 | 861 |
| F13 | feedback AND "meta-analysis" AND (achievement OR learning) | 209 | 315 | 1,191 |
| F14 | "answer-until-correct" OR "answer until correct" | 42 | 94 | 98 |
| F15 | "automatic question generation" OR "automated question generation" | 26 | 588 | 692 |
| F16 | "question generation" AND ("large language model" OR "large language models" OR ChatGPT OR GPT-4) AND "multiple-choice" | 0 | 89 | 118 |
| F16b | ChatGPT AND "multiple-choice questions" AND (generated OR generation) | 6 | 281 | 396 |
| F16c | ("large language model" OR "large language models" OR GPT) AND ("generated questions" OR "question generation") | 18 | refused (HTTP 429) | 1,180 |
| F16d | "automatically generated questions" OR "machine-generated questions" OR "AI-generated questions" OR "AI-generated multiple-choice" | 12 | 366 | 456 |
| F17 | "review questions" AND (textbook OR textbooks) | 38 | 356 | 1,028 |
| F18 | "testing effect" AND transfer AND "meta-analysis" | 0 | refused (HTTP 429) | 3 |
| F18b | ("testing effect" OR "retrieval practice" OR "test-enhanced learning") AND transfer AND (meta-analysis OR "meta-analytic") | 11 | 5 | 11 |
| F19 | "multiple-choice" AND ("negative suggestion" OR lures) AND testing | 2 | 31 | 39 |
| F20 | feedback AND ("programmed instruction" OR "written instruction") AND (peeking OR "presearch availability" OR "answer availability") | 0 | 1 | 1 |
| F20b | Kulhavy AND feedback | 12 | 15 | 21 |
| F20c | feedback AND ("programmed instruction" OR "written instruction") AND (peek OR peeking OR "answers available" OR "answer availability" OR prompting) | 4 | refused (HTTP 429) | 42 |
| F21 | "practice quizzes" OR "practice quiz" OR "online quizzes" | 177 | 1,293 | 1,652 |
| F22 | "Bloom's taxonomy" AND (textbook OR "exam questions" OR "test questions") AND (biology OR science OR chemistry) | 27 | 148 | 219 |
| F23 | distractors AND "multiple-choice" AND (review OR guidelines) AND (development OR writing) | 20 | 90 | 145 |
| F24 | "multiple-choice" AND ("competitive alternatives" OR "plausible alternatives") AND (learning OR retention) | 1 | 2 | 8 |
| F25 | ("covert retrieval" OR "overt retrieval") AND practice | 12 | 31 | 37 |
| F26 | ("free recall" OR "cued recall") AND ("retrieval practice" OR "testing effect") AND (format OR "multiple-choice") | 13 | 58 | 63 |
| F27 | "automatic item generation" OR "automated item generation" | 55 | 279 | 386 |
| F28 | feedback AND ("multiple-choice" OR quiz OR quizzes) AND ("correct answer" OR "explanation feedback" OR "knowledge of correct response") | 46 | 24 | 235 |
| F29 | ("end-of-chapter questions" OR "end of chapter questions" OR "textbook questions") AND (cognitive OR Bloom OR level) | 16 | 131 | 269 |
| F30 | ("practice questions" OR "practice tests") AND (exam OR examination) AND (performance OR learning) AND (university OR college OR medical) | 25 | 112 | 376 |

| Id | arXiv string as run (all abstracts) | arXiv |
|---|---|---|
| X1 | abs:"question generation" AND abs:education AND abs:students | 31 |
| X2 | abs:"multiple-choice" AND abs:"question generation" AND (abs:GPT OR abs:"language model") | 22 |
| X3 | abs:"distractor generation" | 41 |
| X4 | abs:"generated questions" AND abs:"learning gains" | 1 |

- Totals: ERIC 1,298 records over 36 strings; Semantic Scholar 6,515 over 31 strings; arXiv 95 over 4 strings; 7,908 in all, with repeats.
- Zero results (F16, F18, F20 in ERIC) were rephrased (F16b to F16d, F18b, F20b and F20c), and the rephrased strings returned records.
- Screened by title: the 20 most relevant ERIC records per string (517), 8 to 12 of the most cited Semantic Scholar records per string (254). Also the first 20 arXiv records per string (61): 832 with repeats.
- Abstracts were then read through the public ERIC, PubMed and Crossref services, and three full texts through open copies; these lookups add no records.
- Snowballing, backward: the reference lists of Pan 2018 (Butler 2010, Kang 2007), Yang 2021 (Adesope 2017, McDermott 2014) and Hattie 2007 (Kulhavy 1977, Kulik 1988, Bangert-Drowns 1991) were read for this topic. Forward: none beyond the strings.
- Leads named in the brief and verified: Haladyna 2002, Rodriguez 2005, Downing 2005, Tarrant 2008, Butler 2018, Little 2012, McDaniel 2007, Smith 2013c (the brief's Smith and Karpicke, printed 2014). Also: Agarwal 2019, Jensen 2014, Pan 2018, Hattie 2007, Shute 2008, Van der Kleij 2015, Wisniewski 2020, Butler 2007, Kurdi 2020, Sadler 1998.
- Leads from the reviewer's earlier reading, each checked on Crossref and read by abstract or full text: Mertens 2022, McDaniel 2013, Momsen 2010, Little 2014, Marsh 2007, Fazio 2010, Masters 2001. Also: Butler 2013, Pashler 2005, Metcalfe 2009, Lefevre 2016, Laupichler 2023, Van Campenhout 2021.
- Leads located but not read: McDaniel 2007 and Kang 2007 (title, venue and DOI only; no abstract reachable), so no result of theirs is claimed.

## 5. Grey search

- Types and producers, chosen because the formal search pointed to them: open textbooks (OpenStax), lesson templates and instructor training (The Carpentries), quiz tools (Moodle). Also: item-writing guides of testing bodies (NBME), university teaching centres, federal practice guides (IES), and Q/A sites.
- Engine: a general web search engine, first result page per string. Searches made only to reach a formal text (Pan 2018, Yang 2021, Hattie 2007, Van Campenhout 2021) are not grey strings and are not counted.

| Id | String as run (abridged) | Screened | Included |
|---|---|---|---|
| G1 | Carpentries instructor training multiple choice "diagnostic power" distractors misconceptions formative assessment | 19 | 1 (Carpentries 2025p, reached through the episode list) |
| G2 | Butler 2018 multiple-choice testing in education best practices pdf | 20 | 1 (WashU 2018) |
| P | direct visits: NBME, OpenStax (impact, two question pages, a table of contents, a book record), Moodle (documentation, statistics), The Carpentries (training index and two episodes, Workbench guide), IES, Vanderbilt (archived page) | 15 | 8 |

- One OpenStax answer-key page returned 404; the Vanderbilt guide had moved and was read in an archived copy of 2023-12-19.
- OpenStax 2026c (reach) is the same page as in the instructional-text review; it is scored there.

### Q/A sites

Strings PQ1 to PQ11 ran on 2026-10-29, one reviewer, grey tier 2, by the [shared Q/A method](../README.md#rules-the-four-reviews-share). Sites: Mathematics Educators (MathEd), Computer Science Educators (CSEd), Academia.

| Id | String as run | Site | Returned = screened | Included | New |
|---|---|---|---|---|---|
| PQ1 | `q=multiple choice` | MathEd; CSEd; Academia | 73 | 9 | 9 |
| PQ2 | `title=multiple choice` | Academia | 11 | 3 | 2 |
| PQ3 | `title=quiz` | MathEd; CSEd | 12 | 0 | 0 |
| PQ4 | `title=answers` | MathEd | 11 | 3 | 2 |
| PQ5 | `q=retrieval practice` | MathEd; CSEd; Academia | 6 | 0 | 0 |
| PQ6 | `title=quiz` | Academia | 12 | 1 | 1 |
| PQ7 | `q=ChatGPT questions exam` | Academia; MathEd; CSEd | 5 | 0 | 0 |
| PQ8 | `q=Bloom taxonomy` | Academia; MathEd; CSEd | 9 | 1 | 1 |
| PQ9 | `title=generate questions` (Academia); `q=generate questions AI` (MathEd) | Academia; MathEd | 4 | 0 | 0 |
| PQ10 | `q=immediate feedback` | MathEd; CSEd | 7 | 1 | 0 |
| PQ11 | `q=distractors` | MathEd | 22 | 0 | 0 |
| Total | 11 strings | | 172 | 15 (distinct) | 15 |

- Excluded after reading: cheating, grading, exam logistics and policy threads, and threads of other topics.
- Thread 16741 ("What's the point of exercises without answers?") was met in PQ4 and is already reviewed in the exercise-sets review; it is not counted here. Threads on homework solutions went to handoff.md.
- Included: 15, scored on the 20 criteria (section 8) with the shared rules for Q/A threads; none falls below 10 of 20.
- The run ended after PQ11; the last string that added a new thread was PQ8, and PQ9 to PQ11 added none.
- The shared daily quota of the service fell from 123 to 99 calls during this run, so strings were kept few.

## 6. Stopping rule

- Stated before the first search (2026-10-29): effort bounded, the 20 most relevant ERIC records and the 20 most cited Semantic Scholar records per string. Saturation at 5 strings in a row that add no new included source.
- Formal: saturation was not reached; the run ended when every sub-question had been searched in three forms. The last two strings, F29 and F30, added 1 and 0. Fewer than 20 Semantic Scholar titles were printed per string (8 to 12), a departure from the stated N.
- Grey web: first result page per string.
- Q/A: the shared rule, top 30 per string and site; saturation inside a string never cut a list short.

## 7. Selection

- Include: a source on how a question in study material is written, placed, answered or fed back. Also a source on what practice does, with an outcome on learning, on the item, or on adoption. The source is in English and readable on the day at least by abstract or, for a guide, by its page.
- Exclude:
  - studies that only re-measure the testing effect, held in the core (learning-science);
  - assessment design with no bearing on questions as learning (equating, scoring rules, adaptive testing), including most answer-until-correct scoring studies of F14;
  - question generation for machine reading benchmarks, with no learner (most of X1 to X3);
  - live classroom questioning and clickers (presentations review);
  - works of another topic, passed to handoff.md.

## 8. Quality of grey sources (Garousi Guideline 11, Table 7)

- Outlet tier: books, standards, government guides = tier 1 (1); project documentation, teaching-centre pages, news releases, Q/A threads = tier 2 (0.5); blogs = tier 3 (0).
- The NBME guide, read only by its landing page, scores low on the parts not seen.
- Scores, with subtotals, are in sources.md.

## 9. Extraction and synthesis

- Extracted per source: kind, year, the claim, the evidence offered, any number (marked "(secondary)" if not read in the primary), and which question it answers.

## 10. Limits

- One reviewer, no inter-rater agreement; no second rater has scored the grey sources yet.
- Search engines personalise and change; counts will differ on a repeat. Semantic Scholar refused five strings and is not phrase-exact.
- Most formal sources were read by abstract only; sources.md says which. Publisher pages of APA, Elsevier, Taylor and Francis and SAGE were not readable without access, and a request that would have needed a changed client identity was not made.
- No archived copy was made of the practice pages; Moodle, OpenStax and NBME pages may move.
- This search found no study comparing answer placements in a study text; that is not proof none exists.
