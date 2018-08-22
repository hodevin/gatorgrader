"""GatorGrader checks the files of programmers and writers"""

import sys

from gator import arguments
from gator import display
from gator import invoke
from gator import leave
from gator import orchestrate


DEFAULT_COUNT = 0
DEFAULT_LANGUAGE = "Java"
INCORRECT_ARGUMENTS = 2
NONEXISTENT_CHECKING = 3
JAVA = "Java"
PYTHON = "Python"

SINGLE = "single-line"
MULTIPLE = "multiple-line"

REPOSITORY = "."


if __name__ == "__main__":
    # orchestrate check(s) of the specified deliverable(s)
    exit_code = orchestrate.check(sys.argv[1:])
    # exit the program with the correct code
    # error code: one aspect of the checks failed
    # normal code: all aspects of the checks passed
    sys.exit(exit_code)
