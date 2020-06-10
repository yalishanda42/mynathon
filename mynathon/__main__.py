"""Entry point for the parser executable."""

import sys
import pathlib
from .mynathon import MynathonParser


def entry_point():
    if len(sys.argv) < 2:
        print("USAGE:\n\t$ {0} file_name".format(sys.argv[0]))
        exit(1)

    filepath = pathlib.Path(sys.argv[-1]).as_posix()
    MynathonParser.execute_script_from_file(filepath)


if __name__ == "__main__":
    entry_point()
