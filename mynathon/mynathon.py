#!python3

"""Mynathon.

The universal language of mainas and manqks.

(c) 2020 AJ & MC Ton4ou
"""

import os
from io import BytesIO
from tokenize import tokenize, untokenize, NAME


class MynathonParser:
    """The class that is capable of converting mynathon to python."""

    KEYWORDS = {
        "трю": "True",
        "бомбок": "False",
        "и": "and",
        "или": "or",
        "не": "not",
        "е": "is",
        "нищо": "None",
        "ако майна": "if",
        "ако пък": "elif",
        "иначе": "else",
        "начи за": "for",
        "пробягващо": "in",
        "начи майна": "while",
        "скандал": "break",
        "дайму още": "continue",
        "маняк искаш да ме направиш": "raise",
        "маняк ти иеш ли са": "assert",
        "пробвай майна": "try",
        "яба гръмна ми": "except",
        "кат цяло": "finally",
        "пас": "pass",
        "клас": "class",
        "нека": "def",
        "готоо майна": "return",
        "метни му": "yield",
        "гърция": "lambda",
        "от": "from",
        "дай ми": "import",
        "като": "as",
        "праскай": "with",
        "мани го тоа бе майна": "del",
        "софия": "nonlocal",
        "кичука": "global",
        "изчакай": "await",
        "многонишково": "async",
    }

    TEMPFILE = "/tmp/mynathontempfile"

    @staticmethod
    def to_python_string(contents):
        """Transform a mynathon code string into a python code string."""
        keyword_dict = MynathonParser.KEYWORDS
        keywords = keyword_dict.keys()
        result = []
        token_stack = []
        tokens_gen = tokenize(BytesIO(contents.encode('utf-8')).readline)
        for toktype, tokval, _, _, _ in tokens_gen:
            if toktype != NAME:  # all keywords are names so ignore other types
                result.append((toktype, tokval))
                continue

            # Mynathon keywords can consist of more than one 'word'
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

    @staticmethod
    def execute_script_from_file(filename, return_output=False):
        """Parse a mynathon script from a file and execute it."""
        with open(filename, "r") as fread:
            contents = fread.read()

        contents = MynathonParser.to_python_string(contents)

        with open(MynathonParser.TEMPFILE, "w+") as fwrite:
            fwrite.write(contents)

        command = "cat {0} | python3".format(MynathonParser.TEMPFILE)

        result = None
        if return_output:
            result = os.popen(command).read()
        else:
            os.system(command)

        os.remove(MynathonParser.TEMPFILE)
        return result
