import tempfile
import subprocess
import logging


def gen(text, **kwargs):
    file = tempfile.NamedTemporaryFile("w+")
    file.write(text)
    logging.info("Running libime_pinyindict...")
    subprocess.run(["libime_pinyindict", file.name, kwargs["output"]])
    logging.info("Dictionary generated.")