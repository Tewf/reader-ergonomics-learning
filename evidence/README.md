# Evidence

Four literature reviews, one per kind of study document, each in the steps reader-ergonomics uses for its own
[evidence](https://github.com/Tewf/reader-ergonomics/tree/d17ee8e9bc07e0bd06e8ec7734cecd570b4e3b37/evidence): frame,
review, state of the art, position, the case against, baseline. Written on 2026-10-29; not yet audited.

## Contents

| Review | Question | Sources |
|---|---|---|
| [practice-questions](practice-questions/) | how the questions inside study material are written, placed and answered | 107 |
| [flashcards](flashcards/) | how prompts for spaced review are written, made and kept | 100 |
| [exercise-sets](exercise-sets/) | how a set of exercises is ordered and supported, from worked example to problem | 117 |
| [instructional-text](instructional-text/) | how an explanatory text is built around its content: objectives, terms, summaries, boxes | 96 |

Every work cited is listed once in the [bibliography](bibliography.md): 452 works, with the ones the reviews link in the
standard.

## The pool

| | practice-questions | flashcards | exercise-sets | instructional-text | all |
|---|---|---|---|---|---|
| formal, new | 73 | 69 | 78 | 69 | 289 |
| grey, new | 23 | 31 | 39 | 27 | 120 |
| of which Q/A threads | 15 | 19 | 29 | 14 | 77 |
| grey below 10 of 20, examples only | 0 | 5 | 12 | 8 | 25 |
| carried from a sibling review | 11 | 0 | 0 | 0 | 11 |
| in the review | 107 | 100 | 117 | 96 | 420 |

- Most formal sources were read by abstract; each review's `sources.md` says which were read in full.
- Each review keeps the form most used in practice apart from the best tested one. Practice counts as evidence only
  where a study measured its effect.

## Method

Each review is a **multivocal literature review**: research and **grey literature** (standards, publishers' and
open textbook guides, practitioner books, tools, question-and-answer sites) in one review, built to a written protocol
after Garousi 2019. The rules the four share are those of the reviews of reader-ergonomics-topic, linked rather than
repeated: [its method](https://github.com/Tewf/reader-ergonomics-topic/blob/1220def7863b5e977a3edd1e30bd168fff1523a5/evidence/README.md#method).

Two rules differ here:

- **ERIC.** Education research is indexed first in ERIC, the database of the US Institute of Education Sciences, so
  every formal string is counted there, by phrase, through its public interface. It is the primary count.
- **OpenAlex** counted each formal string afterwards by script, on 2026-10-29, in titles and abstracts, as a phrase
  search. The counts sit in each protocol's formal table; the strings, in OpenAlex syntax, in each `openalex.tsv`.

Each review also holds two files the reviews of the siblings do not:

| File | What it holds |
|---|---|
| `shapes-and-checks.md` | what its evidence implies for the shapes of study documents and for checks, each with a grade: proposals, not decisions |
| `handoff.md` | the works met there that belong to another of the four, passed on rather than reviewed twice |

## Rules the four reviews share

Each protocol links here for these rules and states only what is its own: its questions, strings, counts, stopping
point, outlet tiers and exclusions.

- **Quality of a grey source:** Garousi's 20 criteria, each scored 1, 0.5 or 0, in eight groups: authority (4),
  methodology (6), objectivity (4), date (1). The rest: position among related sources (1), novelty (2), impact (1),
  outlet tier (1). The `sources.md` tables give the subtotals in that order.
- **Threshold: 10 of 20.** Below it a source is an **example of practice** only, never support for a claim. A part
  of a source that was not seen scores 0, so a book known only from its catalogue record scores low for that reason.
- **Question-and-answer threads:** read through the Stack Exchange API, top 30 by votes per string and site
  (`order=desc&sort=votes&pagesize=30`, endpoint `search/advanced`, version 2.3, no key, no login), after the
  [Q/A method](https://github.com/Tewf/reader-ergonomics-software-design/blob/master/evidence/architecture-descriptions/protocol.md#qa-sites)
  of reader-ergonomics-software-design. A thread whose title bears on a question of the review is opened, and its
  question and two top answers are read.
- **Scoring a thread:** authority 0.5 for a moderated, peer-voted site; the top answerer's reputation 1 at 20,000
  and 0.5 at 5,000. Impact 1 at 20,000 views or 30 votes, 0.5 at 3,000 views or 10 votes; outlet 0.5; date 1.
  Display names are not recorded: a thread is cited by site, year and number.
- **Why grey literature:** each protocol answers the seven questions of Garousi 2019, Table 4; one yes suggests
  including it.
- **Synthesis** is narrative, by the review's questions, and every claim traces to a row of its `sources.md`.

## The principles of the standard these reviews serve

Linked here once; a review names them without repeating the links.

| Principle | Served by |
|---|---|
| [retrieval prompts](https://github.com/Tewf/reader-ergonomics/blob/d17ee8e9bc07e0bd06e8ec7734cecd570b4e3b37/principles/document/retrieval-prompts.md) | all four |
| [worked examples with subgoals](https://github.com/Tewf/reader-ergonomics/blob/d17ee8e9bc07e0bd06e8ec7734cecd570b4e3b37/principles/document/worked-examples-with-subgoals.md) | exercise-sets, practice-questions, instructional-text |
| [define before use](https://github.com/Tewf/reader-ergonomics/blob/d17ee8e9bc07e0bd06e8ec7734cecd570b4e3b37/principles/document/define-before-use.md) | instructional-text |
| [overview first](https://github.com/Tewf/reader-ergonomics/blob/d17ee8e9bc07e0bd06e8ec7734cecd570b4e3b37/principles/document/overview-first.md) | instructional-text |
| [signal the structure](https://github.com/Tewf/reader-ergonomics/blob/d17ee8e9bc07e0bd06e8ec7734cecd570b4e3b37/principles/page/signal-the-structure.md) | instructional-text |
| [one place per fact](https://github.com/Tewf/reader-ergonomics/blob/d17ee8e9bc07e0bd06e8ec7734cecd570b4e3b37/principles/collection/one-place-per-fact.md) | instructional-text |

## What these reviews do not repeat

Whether a technique works is reviewed in the standard
([decision 0001](../decisions/0001-take-the-document-not-the-technique.md)). These reviews link it, with one line of
context, and add how the document delivers it.

## Checked so far

- Every DOI in the four reviews resolved on Crossref on 2026-10-29. Where Crossref's year differs from a key's, the
  key gives the year of print and Crossref the year online.
- Every key was checked by script against the five bibliographies of the family: no work here carries a key another
  repository gives a different work. The one exception, Yang 2021, names the standard's work here and another work in
  reader-ergonomics-presentations. That clash is between the two siblings.
- One citation in reader-ergonomics was found wrong here and corrected there, in v1.3.1 (Dickson 2005).
- Not done yet: the audit of every number against its source by agents that did not write it, and a second rater
  on every fifth grey source.

## See also

The [repository's front page](../README.md), the parent of this folder; [decision 0002](../decisions/0002-four-reviews.md)
for why there are four reviews.
