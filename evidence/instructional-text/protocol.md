# Protocol: how the pool of sources was built

Every search, count and rule of the instructional-text review, so it can be repeated; all searches ran on 2026-10-29. Shared rules: [evidence README](../README.md#rules-the-four-reviews-share).

## 1. Why grey literature

The seven questions of Garousi 2019, Table 4, for a study text: each answer is yes.

| # | Question | Answer for this topic |
|---|---|---|
| 1 | Complex, not solvable from formal literature alone? | yes: textbook apparatus, lesson templates and course rubrics come from publishers and projects |
| 2 | Lack of volume or quality of evidence? | yes: no experiment was found that removes one aid from a real textbook |
| 3 | Context important? | yes: school, college and workshop lessons carry different apparatus |
| 4 | Corroborate research with practice? | yes |
| 5 | Challenge practice with research, or the reverse? | yes: refutation text and guided notes have meta-analyses and no place in the templates read (position.md) |
| 6 | Would a synthesis serve both communities? | yes |
| 7 | Large practitioner volume? | yes: 4,980 Carpentries workshops since 2012 (Carpentries 2025) |

## 2. Questions

The sub-questions Q1 to Q7 are in [frame](frame.md).

## 3. Existing reviews (Garousi Guideline 2)

- Searched in the first batch of strings (F8, meta-analyses of objectives) and by strings aimed at reviews: F14 refined to titles with "meta-analysis", F32b (glosses), F35 (refutation).
- Found and placed in review.md strand 0: 5 reviews without pooling, 11 meta-analyses, 1 systematic review; 2 further meta-analyses located by title only.
- No systematic review of textbook pedagogical aids as a set, of study guides or of crib sheets was found.

## 4. Formal search

ERIC is primary and phrase-exact (`api.ies.ed.gov/eric/`, field `response.numFound`). Semantic Scholar bulk search is not phrase-exact; its counts are noisy upper bounds. arXiv was not run: no string concerns computing work. OpenAlex was not called; `openalex.tsv` holds every string for the counting script.

| Id | String as run (ERIC syntax) | ERIC | Semantic Scholar | OpenAlex |
| --- | --- | --- | --- | --- |
| F1 | "pedagogical aids" | 25 | 148 | 204 |
| F2 | textbook AND ("study aids" OR "learning aids" OR "textbook features") | 44 | 323 | 595 |
| F3 | "instructional text" AND design | 55 | 266 | 317 |
| F4 | "constructive alignment" | 237 | refused (HTTP 429) | 2,354 |
| F5 | "backward design" | 170 | 1,059 | 1,630 |
| F6 | "instructional alignment" | 70 | 285 | 402 |
| F7 | ("instructional objectives" OR "behavioral objectives" OR "learning objectives") AND (text OR prose OR textbook) AND learning | 887 | 4,552 | 6,735 |
| F8 | "meta-analysis" AND ("learning objectives" OR "instructional objectives" OR "behavioral objectives") | 36 | 260 | 319 |
| F9 | summaries AND recall (Semantic Scholar: summaries + recall + text) | 77 | 1,527 | 11,386 |
| F10 | glossary AND (learning OR comprehension) AND text | 387 | 1,239 | 1,980 |
| F11 | "refutation text" | 61 | 294 | 354 |
| F12 | "refutational text" OR "refutational texts" | 45 | 294 | 354 |
| F13 | "conceptual change text" OR "conceptual change texts" | 86 | 275 | 315 |
| F14 | "guided notes" | 74 | 784 | 918 |
| F15 | ("study guide" OR "study guides") AND ("exam performance" OR "test performance" OR "exam scores") | 25 | 50 | 62 |
| F16 | "crib sheet" OR "cheat sheet" OR "crib sheets" OR "cheat sheets" | 83 | 798 | 1,509 |
| F17 | "Quality Matters" (Semantic Scholar: with + rubric) | 195 | 141 | 2,489 |
| F18 | "course design rubric" OR "online course rubric" | 4 | 10 | 16 |
| F19 | "instructional explanations" | 74 | 271 | 310 |
| F20 | "worked solutions" OR "solutions manual" OR "solution manual" | 21 | 3,074 | 4,717 |
| F21 | "marginal notes" OR "marginal glosses" OR "margin notes" | 73 | 1,939 | 3,204 |
| F22 | textbook AND ("chapter summary" OR "chapter summaries" OR "end-of-chapter") | 49 | 773 | 3,989 |
| F23 | "textbook use" OR "textbook reading" OR "reading compliance" | 300 | 5,920 | 7,724 |
| F24 | "open textbook" OR "open textbooks" | 107 | 938 | 2,234 |
| F25 | "key terms" AND (textbook OR text) AND learning | 52 | 134 | 1,192 |
| F26 | "revision guide" OR "revision guides" | 6 | not run | 1,163 |
| F27 | "textbook" AND "pedagogical features" | 4 | not run | 794 |
| F28 | "chapter summaries" OR "chapter summary" | 77 | not run | 4,729 |
| F29 | "learning objectives" AND textbook AND (students OR use) | 71 | not run | 2,054 |
| F30 | "summaries" AND "textbook" AND (learning OR recall) | 64 | not run | 2,493 |
| F31 | ("sidebar" OR "sidebars" OR "boxed text" OR "text boxes") AND (textbook OR text) AND (learning OR reading) | 44 | not run | 1,283 |
| F32 | "glossary" AND ("vocabulary learning" OR "comprehension") AND ("meta-analysis") | 0 | not run | 4 |
| F32b | (gloss OR glosses OR glossing) AND "meta-analysis" | 18 | not run | 64 |
| F32c | author:Abraham AND glosses | 1 | not run | 0 |
| F32d | "glossed" AND "reading comprehension" | 27 | not run | 197 |
| F33 | "instructional explanations" AND "worked examples" | 5 | not run | 19 |
| F34 | "Quality Matters" AND ("student achievement" OR "student outcomes" OR "final grades" OR "student learning") | 32 | not run | 104 |
| F35 | "refutation" AND "meta-analysis" | 3 | not run | 46 |
| F36 | ("boldface" OR "bold type" OR "typographical cues" OR "typographic cueing") AND text AND (recall OR learning) | 11 | not run | 74 |
| F37 | "chapter objectives" OR "chapter learning objectives" | 28 | not run | 1,440 |
| F38 | glossary AND textbook AND (students OR learning) | 172 | not run | 2,493 |
| F39 | misconceptions AND textbook AND (box OR boxes OR feature OR features) | 17 | not run | 155 |
| F40 | "lesson template" OR "lesson templates" | 18 | not run | 74 |

- Totals: ERIC 3,835 records over 43 strings; Semantic Scholar 25,354 over 24 strings. F1's Semantic Scholar count is from the first call; later calls were refused.
- F32 returned 0 and was rephrased three ways (F32b to F32d): the work is filed under glosses, in second-language reading.
- In `openalex.tsv`, F32c's author field becomes the author's name as a word, since a title-and-abstract search has no author field.
- Screened by title: 668 ERIC titles (the top 20 per string in ERIC's order, fewer where fewer came back) and 435 Semantic Scholar titles (the top 20 by citations). Per string, the Semantic Scholar titles were F1 5, F18 10, F21 none listed.
- Abstracts were then read through the public ERIC service; full texts were read where ERIC holds them (Larwin 2012; Larwin 2013; Clinton 2019; Biggers 2020).
- Lead lookups, not counted as strings: author and title searches in ERIC and Crossref for the leads named in the commission (section 7).
- Snowballing: backward from Marek 1999 (Weiten 1996) and Wilson 2019 (Wiggins 2005); one web search for the numbers of Guzzetti 1993 led to four further meta-analyses, each checked in Crossref or ERIC.

## 5. Grey search

- Types and producers: open textbook publishers (OpenStax), lesson projects (The Carpentries), practitioner books (Wilson 2019; Hartley 1978; Mager 1962), course design rubrics (Quality Matters, SUNY OSCQR). Also: a university teaching centre (CMU), revision-guide and solved-problem publishers, and Q/A sites.
- Engine: a general web search engine, first result page per string (about 10 results, two pages where the tool returned two). Results personalise and change.

| Id | String as run (abridged) | Screened | Included |
|---|---|---|---|
| G1 | OpenStax style guide textbook features learning objectives key terms summary review questions | 20 | 1 (OpenStax 2026b); no standalone style guide found |
| G2 | The Carpentries number of workshops learners instructors since 2012 annual report | 20 | 1 (Carpentries 2025) |
| G3 | study of GCSE revision guides students use CGP effect on exam results research | 19 | 0: no study; the publisher's page refused access |
| G4 | Schaum's Outlines solved problems series sold million copies | 19 | 0: retail listings only |
| P | direct visits: OpenStax preface and impact, Carpentries Workbench, curriculum handbook (deprecated), lesson training index and design episode, Carpentries impact and annual report, Quality Matters about and rubric, OSCQR, Teaching Tech Together, CMU, CGP (refused) | 14 | 10 |

- Searches made only to reach a formal text (Reder 1980, Guzzetti 1993, the Gurung chapter) are not grey strings and are not counted.

### Q/A sites

Strings IT1 to IT13 ran on 2026-10-29, one reviewer, grey tier 2, by the [shared Q/A method](../README.md#rules-the-four-reviews-share). Saturation here: k = 10.

| Id | String as run | Site | Returned = screened | Included | New |
|---|---|---|---|---|---|
| IT1 | `title=study guide` | Academia; Mathematics Educators; Computer Science Educators | 3 | 1 | 1 |
| IT2 | `title=cheat sheet` | Academia; Mathematics Educators; Computer Science Educators | 1 | 0 | 0 |
| IT3 | `title=learning objectives` | Academia; Mathematics Educators; Computer Science Educators | 1 | 0 | 0 |
| IT4 | `q=cheat sheet` | Academia; Mathematics Educators | 38 | 2 | 2 |
| IT5 | `q=learning outcomes` | Academia | 30 | 1 | 1 |
| IT6 | `title=textbook` | Mathematics Educators; Computer Science Educators | 43 | 2 | 2 |
| IT7 | `title=lecture notes` | Academia; Mathematics Educators | 37 | 5 | 5 |
| IT8 | `title=misconception` | Mathematics Educators | 3 | 1 | 1 |
| IT9 | `title=solutions` | Mathematics Educators | 30 | 0 (2 reviewed in exercise-sets) | 0 |
| IT10 | `q=constructive alignment` | Academia | 0 | 0 | 0 |
| IT11 | `title=glossary` | Academia; Mathematics Educators | 15 | 2 | 2 |
| IT12 | `q=study guide` | Academia | 30 | 0 | 0 |
| IT13 | `q=backward design` | Academia; Mathematics Educators | 2 | 0 | 0 |
| Total | 13 strings | | 233 | 14 (distinct) | 14 |

- Excluded after reading: threads of another topic (answer keys, published solutions, practice exams), threads with no answer, and popular threads matched by a word in the body.
- The run ended after IT13, once each field term had been run in one form; the last string that added a thread was IT11.
- The service's daily quota is shared by address; it fell from 154 to 127 calls during this run.

## 6. Stopping rule

- Stated before the first search: effort bounded, the top 20 per formal string; saturation after 5 strings in a row that add no new included source. Grey web: the first result page per string. Q/A: the shared method.
- Formal: saturation was reached at F36 to F40, five strings that added no new included source; the search stopped there.
- Grey web: G3 and G4 added nothing; producer visits ended when each practice form named in the commission had been read.
- Q/A: as above, ended after IT13.

## 7. Selection

- Include: a source on the parts of an explanatory study text (aids, objectives and alignment, summaries, glosses, refutation, notes and guides, explanations in solutions), their use or their effect. The source is in English and readable on the day at least by abstract or, for a book, by its catalogue record.
- Exclude:
  - effects the core already holds, linked instead (frame.md, last table);
  - questions and their format, cards, and the order of exercises and access to their solutions, passed to the sibling reviews (handoff.md);
  - language course books, glossaries of course manuals and other word collisions;
  - sources whose abstract could not be read and whose title does not settle relevance (kept as located only).
- Leads named in the commission and their status:
  - Verified and cited: Hartley 1976, Gurung 2003, Weiten 1996 (located), Marek 1999, Biggs 1996, Cohen 1987, Mager 1962, Reder 1980 (located), Guzzetti 1993. Also cited: Tippett 2010, Schroeder 2022, Konrad 2009, Dickson 2005b, Wilson 2019, the Carpentries template, the Quality Matters rubric;
  - Dickson and Miller 2005 is the core's key Dickson 2005, linked; its DOI in the core bibliography resolves to another item (handoff.md);
  - Hartley's Designing Instructional Text: found as the 1978 book (ERIC record); a 2004 version was not located;
  - Wiggins and McTighe 2005: catalogue record found, book not opened;
  - the taxonomy book by Anderson and Krathwohl (2001): not opened; Krathwohl 2002 cited for the revised taxonomy (title and venue);
  - the lead Gurung and Daniel (2005): a chapter of that title is in Crossref (2006, pp. 59-74) with no authors, and authorship was not verified, so it is not cited;
  - an OpenStax style guide: not found; the preface of one book is used.

## 8. Quality of grey sources (Garousi Guideline 11, Table 7)

- Outlet tier: books (and a book's front matter) = tier 1 (1); project documentation, company and university pages, annual reports and Q/A threads = tier 2 (0.5); blogs = tier 3 (0).
- Scores, with subtotals, are in sources.md.

## 9. Extraction and synthesis

- Extracted per source: kind, year, design, sample, the claim, any number (marked "(secondary)" if read in an abstract), and the sub-question it answers.

## 10. Limits

- One reviewer; no second rater on this topic.
- Most formal sources were read by abstract only; publisher pages of SAGE, Springer, Elsevier and Taylor and Francis refused access without a login, and none was used.
- One Semantic Scholar string was refused three times (F4); Semantic Scholar counts are not phrase-exact.
- The ERIC relevance order and the web engine's ranking are not documented and may change.
- Archived copies exist for six practice pages (references.md); OpenStax, OSCQR and Teaching Tech Together had none on the day.
- This search did not find an experiment that removes one aid from a real textbook; that is not proof none exists.
