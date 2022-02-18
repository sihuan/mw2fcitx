from http.client import HTTPException
import json
import sys
from os import access, R_OK, W_OK
from urllib.error import URLError
from urllib.request import Request, urlopen
from urllib.parse import quote_plus

from .utils import console
from .retry import retry


class StatusError(Exception):

    def __init__(self, code):
        super().__init__("HTTP status is {}".format(code))


@retry()
def open_request(url):
    return urlopen(
        Request(
            url,
            headers={
                "User-Agent":
                    "MW2Fcitx/1.0; github.com/outloudvi/fcitx5-pinyin-moegirl"
            }))


def fetch_as_json(url):
    res = open_request(url)
    if res.status == 200:
        return json.loads(res.read())
    console.error("Error fetching URL {}".format(url))
    raise StatusError(res.status)


def save_to_partial(partial_path, titles, apcontinue):
    ret = {
        "apcontinue": apcontinue,
        "titles": titles
    }
    try:
        with open(partial_path, "w", encoding="utf-8") as fp:
            fp.write(json.dumps(ret, ensure_ascii=False))
        console.debug("Partial session saved to {}".format(partial_path))
    except Exception as e:
        console.error(str(e))


def resume_from_partial(partial_path):
    if not access(partial_path, R_OK):
        console.warn("Cannot read partial session: {}".format(partial_path))
        return [[], None]
    try:
        partial_data = json.load(open(partial_path, "r", encoding="utf-8"))
        titles = partial_data.get("titles", [])
        apcontinue = partial_data.get("apcontinue", None)
        return [titles, apcontinue]
    except Exception as e:
        console.error(str(e))
        console.error("Failed to parse partial session")
        return [[], None]


def fetch_all_titles(api_url, **kwargs):
    limit = kwargs.get("api_title_limit") or kwargs.get("title_limit") or -1
    console.debug("Fetching titles from {}".format(api_url) +
                  (" with a limit of {}".format(limit) if limit != -1 else ""))
    titles = []
    partial_path = kwargs.get("partial")
    initial_url = api_url + "?action=query&list=allpages&format=json"
    if partial_path is not None:
        console.info(
            "Partial session will be saved/read: {}".format(partial_path))
        [titles, apcontinue] = resume_from_partial(partial_path)
        if apcontinue is not None:
            initial_url = api_url + \
                "?action=query&list=allpages&format=json&aplimit=max&apcontinue={}".format(
                    quote_plus(apcontinue))
            console.info("{} titles found. Continuing from {}".format(
                len(titles), apcontinue))
    data = fetch_as_json(initial_url)
    breakNow = False
    while True:
        for i in map(lambda x: x["title"], data["query"]["allpages"]):
            titles.append(i)
            if limit != -1 and len(titles) >= limit:
                breakNow = True
                break
        console.debug("Got {} pages".format(len(titles)))
        if breakNow:
            break
        if "continue" in data:
            try:
                apcontinue = data["continue"]["apcontinue"]
                data = fetch_as_json(
                    api_url +
                    "?action=query&list=allpages&format=json&aplimit=max&apcontinue={}"
                    .format(quote_plus(apcontinue)))
            except (HTTPException, TimeoutError, URLError) as e:
                console.error(str(e))
                if partial_path:
                    save_to_partial(partial_path, titles, apcontinue)
                sys.exit(1)
            except KeyboardInterrupt as e:
                console.error("Keyboard interrupt received. Stopping.")
                if partial_path:
                    save_to_partial(partial_path, titles, apcontinue)
                sys.exit(1)
        else:
            break
    console.info("Finished.")
    return titles
