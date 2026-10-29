"""Questions: the question-block rules on notes, which state no objectives: every question folds its answer, the
answer explains, a multiple-choice item follows the item rules, and every trap is refuted.

Runs on the files `[questions] files` names in checks/config.toml, with the settings of that table (the same keys as
`[lesson]`). It is the lesson check with alignment off (lesson.py): a note (the core note shape) holds a Check
yourself and traps but no objectives, so neither objectives nor tags are asked for. What a run with no error
guarantees, and what it does not: as lesson.py says, less the alignment. Exact, with the heuristic warnings of
lesson.py. Time O(lines) per file.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lesson  # noqa: E402  (the sibling check whose rules this one reuses)

NAME = "questions"
EXACT = True


def check(root: Path, config: dict):
    return lesson.run(root, config.get("questions", {}), config, align=False, name=NAME)
