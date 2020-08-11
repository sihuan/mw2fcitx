from mw2fcitx.fetch import fetch_all_titles
from mw2fcitx.utils import dedup
from mw2fcitx.utils import console
import os
import sys


class MWFPipeline():

    def __init__(self, api_path=""):
        self.api_path = api_path
        self.titles = []
        self.words = []
        self.exports = ""
        self.dict = ""

    def load_titles(self, titles):
        if type(titles) == type(""):
            titles = titles.split("\n")
        self.titles = titles
        console.debug("{} title(s) imported.".format(len(titles)))
        self.words = self.titles

    def write_titles_to_file(self, filename):
        try:
            with open(filename, "w") as file:
                file.write("\n".join(self.titles))
        except Exception as e:
            console.error("File {} is not writable: {}".format(
                filename, str(e)))
            sys.exit(1)

    def post_load(self, **kwargs):
        if kwargs.get("output"):
            self.write_titles_to_file(kwargs.get("output"))

    def load_titles_from_file(self, filename, **kwargs):
        if not os.access(filename, os.R_OK):
            console.error("File {} is not readable".format(filename))
            sys.exit(1)
        self.load_titles(open(filename, "r").read())
        self.post_load(**kwargs)

    def fetch_titles(self, **kwargs):
        titles = fetch_all_titles(self.api_path, **kwargs)
        self.load_titles(titles)
        self.post_load(**kwargs)

    def reset_words(self):
        self.words = self.titles

    def convert_to_words(self, pipelines=[]):
        console.debug("Running {} pipelines".format(len(pipelines)))
        cnt = 0
        if type(pipelines) == type(self.convert_to_words):
            pipelines = [pipelines]
        titles = self.titles
        for i in pipelines:
            cnt += 1
            console.debug("Running pipeline {}/{} ({})".format(
                cnt, len(pipelines), i.__name__ or "anonymous function"))
            titles = i(titles)
        self.words = dedup(titles)

    def export_words(self, converter="opencc", **kwargs):
        if converter == "opencc":
            console.debug("Exporting {} words with OpenCC".format(
                len(self.words)))
            from mw2fcitx.exporters.opencc import export
            self.exports = export(self.words, **kwargs)
        elif type(converter) == type(self.export_words):
            console.debug("Exporting {} words with custom converter".format(
                len(self.words)))
            self.exports = converter(self.words, **kwargs)
        else:
            console.error("No such exporter: {}".format(converter))

    def generate_dict(self, generator="pinyin", **kwargs):
        if generator == "pinyin":
            from mw2fcitx.dictgen import pinyin
            dest = kwargs.get("output")
            if not dest:
                console.error(
                    "Dictgen 'pinyin' can only output to files. Please give the file path in the 'output' argument."
                )
                return
            pinyin(self.exports, **kwargs)
        elif generator == "rime":
            from mw2fcitx.dictgen import rime
            self.dict = rime(self.exports, **kwargs)
        else:
            console.error("No such dictgen: {}".format(generator))