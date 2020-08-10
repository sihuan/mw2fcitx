import tempfile
import subprocess
from mw2fcitx.utils import console
import re


def gen(text, **kwargs):
    name = kwargs.get("name") or "moegirl"
    version = kwargs.get("version") or "0.1"
    text = re.sub(r'[ ][ ]*', '\t', text)
    text = text.replace("\t0", "")
    text = text.replace("'", " ")
    text = '---\nname: {}\nversion: "{}"\nsort: by_weight\n...\n'.format(
        name, version) + text
    if kwargs.get("output"):
        with open(kwargs.get("output"), "w", encoding="utf-8") as file:
            file.write(text)
    else:
        print(text)
    console.info("Dictionary generated.")
    return text