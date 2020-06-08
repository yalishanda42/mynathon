#!python3

"""Mython.

The language of 411.

(c) 2020 AJ & MC Ton4ou
"""

import sys
import os
from io import BytesIO
from tokenize import tokenize, untokenize, NAME


class MythonParser:
    """The class that is capable of converting mython to python."""

    KEYWORDS = {
        "трю": "True",
        "бомбок": "False",
        "изчакай": "await",
        "иначе": "else",
        "дай ми": "import",
        "пас": "pass",
        "нищо": "None",
        "скандал": "break",
        "яба гръмна ми": "except",
        "пробягващо": "in",
        "маняк искаш да ме направиш": "raise",
        "клас": "class",
        "кат цяло": "finally",
        "е": "is",
        "готоо майна": "return",
        "и": "and",
        "дайму още": "continue",
        "начи за": "for",
        "хаскелче": "lambda",
        "пробвай майна": "try",
        "като": "as",
        "нека": "def",
        "от": "from",
        "софия": "nonlocal",
        "начи майна": "while",
        "маняк ти ибеш ли са": "assert",
        "мани го тоа е майна": "del",
        "асеновград": "global",
        "не": "not",
        "праскай": "with",
        "многонишково": "async",
        "ако пък": "elif",
        "начи ако": "if",
        "или": "or",
        "метни му": "yield",
    }

    @staticmethod
    def to_python_string(contents):
        """Transform a mython code string into a python code string."""
        keyword_dict = MythonParser.KEYWORDS
        keywords = keyword_dict.keys()
        result = []
        token_stack = []
        tokens_gen = tokenize(BytesIO(contents.encode('utf-8')).readline)
        for toktype, tokval, _, _, _ in tokens_gen:
            if toktype != NAME:  # all keywords are names so ignore other types
                result.append((toktype, tokval))
                continue

            # Mython keywords can consist of more than one 'word'
            # so use a stack to persist words of possible detected keywords
            # between the generator iterations
            token_stack.append((toktype, tokval))
            stack_stmt = " ".join(map(lambda t: t[1], token_stack))

            if tokval in keywords:
                result.append((NAME, keyword_dict[tokval]))
                token_stack = []
            elif stack_stmt in keywords:
                result.append((NAME, keyword_dict[stack_stmt]))
                token_stack = []
            elif len(list(filter(lambda k: stack_stmt in k, keywords))) == 0:
                result.extend(token_stack)
                token_stack = []

        return untokenize(result).decode('utf-8')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"USAGE:\n\t{sys.argv[0]} FILE_NAME")
        exit(1)

    with open(sys.argv[-1], "r") as fread:
        contents = fread.read()

    contents = MythonParser.to_python_string(contents)

    TEMPFILE = "/tmp/mythontempfile"

    with open(TEMPFILE, "w+") as fwrite:
        fwrite.write(contents)

    os.system(f"cat {TEMPFILE} | python3")
    os.remove(TEMPFILE)
