# Changelog

Every release of this repository, newest first, in the form of
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/). A move of the standard's pin is one line under Changed, as
the standard's extending.md (Versions) gives it.

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
