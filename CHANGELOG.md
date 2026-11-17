# Changelog

Every release of this repository, newest first, in the form of
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/). A move of the standard's pin is one line under Changed, as
the standard's extending.md (Versions) gives it.

## [Unreleased]

### Changed

- Pinned reader-ergonomics v1.24.5 (`030e4f2`), from v1.24.3 (`722cfa4`): a server that refuses the checker (405, 406, or a connection closed without an answer, as ERIC does on GitHub's runner) is a warning, so the weekly online run no longer fails on a reference that exists; v1.24.4 also stops encoding an encoded DOI twice.
- Pinned reader-ergonomics v1.24.3 (`722cfa4`), from v1.24.2 (`65e4247`): a SICI DOI is read whole and a server error is a warning, not an error. The links and version labels of the text move with the pin; several said v1.21.1 beside the commit of v1.24.2.
- Pinned reader-ergonomics v1.24.2 (`65e4247`), from v1.22.1 (`0206e69`): fixes that remove false findings in the sentence, term and figure checks, and `[defined_terms] cues`.

### Fixed

- Three references of `evidence/bibliography.md` that the weekly online run rejected: Sadler 1998's SICI DOI, once percent-encoded inside a doi.org address and so double-encoded by the check, is written as a bare DOI; Parsons and Haden 2006's CRPIT address, whose host `crpit.scem.westernsydney.edu.au` no longer resolves in DNS, points to the Internet Archive's capture of the abstract page (2016-03-19). The third, an ERIC page that dropped one connection, answered 200 on retry and needed no change.

## [1.1.1] - 2026-11-07

### Changed

- Pinned reader-ergonomics v1.22.1 (`0206e69`), from v1.21.1 (`a67087a`): LaTeX maths blanked by the sentence checks, escaped-pipe wikilinks resolved, and `standard-pin` moves a pin.

## [1.1.0] - 2026-11-07

### Added

- A sixth shape, the [recognition guide](shapes/recognition-guide.md): which type a problem is, read off its signals before it is solved ([decision 0005](decisions/0005-a-sixth-shape-the-recognition-guide.md)). Its example asks which search a statement calls for.
- The markup table says that two folds in a row need a blank line between them: the checks read a run of quoted lines as one callout.

### Changed

- Pinned reader-ergonomics v1.21.1 (a67087a), from v1.18.2 (bfbe9f7): the sentence checks skip front matter, `duplication` skips a shape's skeleton lines, `run.py --out`, the `release-version` check. Pinned reader-ergonomics-topic v0.6.1 (86e14fe), from v0.4.0 (1220def): the topic check accepts a remote shape link.

## [1.0.1] - 2026-11-04

### Changed

- The citation file and the Status line now cite the repository as release 1.0.0, no longer work in progress.
- Tag v1.0.1 and a GitHub release of the same name.

## [1.0.0] - 2026-10-29

### Added

- The first release: five shapes of study documents, the checks that read them and a checked example of each, on
  four audited literature reviews, as the [README](README.md) describes them.

### Changed

- Pinned reader-ergonomics v1.18.2 (bfbe9f7), from v1.13.0 (7a76cc6): grades per clause, the changelog form and its check, the Take your own version section, blueprint listed as the sixth extension.
