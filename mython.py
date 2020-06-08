#!python3

import sys
import os
import re

TEMPFILE = "/tmp/mythontempfile"

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
    "за": "for",
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
    "или пък": "elif",
    "ако": "if",
    "или": "or",
    "метни му": "yield",
}


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"USAGE:\n\t{sys.argv[0]} FILE_NAME")
        exit(1)

    with open(sys.argv[-1], "r") as fread:
        contents = fread.read()

    for mykeyword, pykeyword in KEYWORDS.items():
        contents = re.sub(r"\b{0}\b".format(mykeyword), pykeyword, contents)

    with open(TEMPFILE, "w+") as fwrite:
        fwrite.write(contents)

    os.system(f"cat {TEMPFILE} | python3")
    os.remove(TEMPFILE)
