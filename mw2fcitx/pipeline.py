from mw2fcitx.fetch import fetch_all_titles
from mw2fcitx.utils import dedup
from mw2fcitx.utils import console


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

    def fetch_titles(self, **kwargs):
        titles = fetch_all_titles(self.api_path, **kwargs)
        self.load_titles(titles)

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
            console.debug("Exporting words with OpenCC")
            from mw2fcitx.exporters.opencc import export
            self.exports = export(self.words, **kwargs)
        elif type(converter) == type(self.export_words):
            console.debug("Exporting words with custom converter")
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