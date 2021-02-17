import re
from pypinyin import lazy_pinyin
import opencc
from ..utils import console
from ..utils import manual_fix


def export(words):
    result = ""
    converter = opencc.OpenCC('t2s.json')
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

        if manual_fix(line):
            pinyin = manual_fix(line)
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
