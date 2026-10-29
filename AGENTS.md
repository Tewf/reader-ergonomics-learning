# Contributing to this repository

For anyone changing this repository, person or language model. To apply the reader-ergonomics standard elsewhere,
read its [standard.md](https://github.com/Tewf/reader-ergonomics/blob/adb53c52fa8eefe0e621e520365157bbbcad1a1a/standard.md);
this file is about this repository only.

## Before writing

1. Read the standard at the release this repository checks against (v1.12.0), then its
   [learning-science review](https://github.com/Tewf/reader-ergonomics/tree/adb53c52fa8eefe0e621e520365157bbbcad1a1a/evidence/learning-science),
   then the [topic](https://github.com/Tewf/reader-ergonomics-topic/blob/1220def7863b5e977a3edd1e30bd168fff1523a5/shapes/topic.md)
   every shape here derives from.
2. Ask of every new claim whether it is about the document or about the technique. A claim about whether a technique
   works belongs to the standard; here it is linked, with one line of context
   ([decision 0001](decisions/0001-take-the-document-not-the-technique.md)).
3. A new file is listed by the README of its folder, with its summary. A new folder gets a README.md, listed by the
   README above it, and a one-line `index.qmd` that includes it, because the site generator skips README files.
4. This repository has no principles of its own yet, so it has no `standard.md` card: the standard's card is the one
   to follow.

## Rules for claims

- Every claim carries a grade: **measured**, **supported with caveat**, **convention** or **not supported**. A grade
  moves only with a cited source.
- Cite as `Author Year`; the entry goes once into [evidence/bibliography.md](evidence/bibliography.md), with a DOI,
  an arXiv id, an ERIC id or a stable URL. A key names one work across the six repositories of the family: check it
  against their bibliographies before adding it.
- Evidence against a rule goes into the review's `against.md`, never deleted to make a rule look stronger.
- A number read in a summary rather than in the source is marked "(secondary)".

## Links

- Down to reader-ergonomics and reader-ergonomics-topic: pinned to the release's commit, as CI is, so a rename there
  cannot break them silently.
- Up: none. Nothing here is linked from the repositories below it.

## Before handing back

Run the checks against the release CI uses, not a checkout that may have moved on: extract it once with
`git -C ../reader-ergonomics archive adb53c5 | tar -x -C ../re-v1.12.0`.

```sh
git -C ../reader-ergonomics-topic show 1220def:checks/local/topic.py > checks/local/topic.py   # as CI does; never committed
python3 ../re-v1.12.0/checks/run.py . --tiers program,meaning --judge flag   # the repository, as CI runs it
READER_ERGONOMICS_CHECKS=../re-v1.12.0/checks python3 -m unittest discover -s checks   # the checks of the shapes
```

- Fix every error. Read every warning.
- A key names one work across the family: `bibliography-keys` compares
  [evidence/bibliography.md](evidence/bibliography.md) with each repository its config names, cloned beside this one
  as CI does; a sibling not found is a warning, never a pass.
- Answer the questions in `checks/out/needs-judgment.md` in `checks/judgments.toml`. A model does not review its own
  text in place of the checks; its answers are advice until the maintainer has read them.
- Keep [llms.txt](llms.txt) in step when a page is added, moved or removed: nothing generates it.
- Keep [README.md](README.md) and [README.fr.md](README.fr.md) in step.

## House conventions

- No em dash or en dash in prose; use a comma, a colon, parentheses, or a hyphen for ranges.
- Commit messages follow the standard's commit shape: a subject of at most 72 characters, then why.
- A choice that shapes the repository gets a record in [decisions/](decisions/).
- The maintainer decides every push.
