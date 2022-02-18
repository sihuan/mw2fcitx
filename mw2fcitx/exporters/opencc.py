import json
import re
from pypinyin import lazy_pinyin
import opencc
from ..utils import console


def manual_fix(text, table):
    if text in table:
        return table[text]
    return None


def export(words, **kwargs):
    result = ""
    converter = opencc.OpenCC('t2s.json')
    fixfile = kwargs.get("fixfile")
    if fixfile is not None:
        table = json.load(open(fixfile, "r", encoding="utf-8"))
    HANZI_RE = re.compile('^[\u4e00-\u9fa5]+$')
    count = 0
    last_word = None
    for line in words:
        line = line.rstrip("\n")
        if not HANZI_RE.match(line):
            continue

        pinyin = "'".join(lazy_pinyin(line))
        if pinyin == line:
            # print("Failed to convert, ignoring:", pinyin, file=sys.stderr)
            continue

        if fixfile is not None:
            fixed_pinyin = manual_fix(line, table)
            if fixed_pinyin is not None:
                pinyin = fixed_pinyin
                console.debug(f"Fixing {line} to {pinyin}")

        last_word = line

        result += "\t".join((converter.convert(line), pinyin, "0"))
        result += "\n"
        count += 1
        if count % 1000 == 0:
            console.debug(str(count) + " converted")

    if count % 1000 != 0 or count == 0:
        console.debug(str(count) + " converted")
    return result
