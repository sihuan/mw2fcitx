#!/usr/bin/env python
import sys
import json
from urllib.request import Request, urlopen
from urllib.parse import quote_plus
from retry import retry


class StatusError(Exception):
    def __init__(self, code):
        super().__init__("HTTP status is {}".format(code))


@retry()
def open_request(url):
    return urlopen(Request(url, headers={
        "User-Agent": "PyFcitxDictBot/1.0; github.com/outloudvi/fcitx5-pinyin-moegirl"
    }))

def fetch(url):
    res = open_request(url)
    if res.status == 200:
        return json.loads(res.read())
    else:
        raise StatusError(res.status)


API_PAGE = sys.argv[1]
FILE = "titles.txt"
if len(sys.argv) > 2:
    FILE = sys.argv[2]
articles = []
data = fetch(API_PAGE + "?action=query&list=allpages&format=json")
while True:
    for i in map(lambda x: x["title"], data["query"]["allpages"]):
        articles.append(i)
    print("Got {} pages".format(len(articles)))
    if "continue" in data:
        data = fetch(API_PAGE + "?action=query&list=allpages&format=json&aplimit=max&apcontinue={}".format(
            quote_plus(data["continue"]["apcontinue"])))
    else:
        break
print("Finished.")
with open(FILE, "w") as f:
    f.write("\n".join(articles))
