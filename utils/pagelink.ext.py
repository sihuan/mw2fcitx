import sys
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

from mw2fcitx.fetch import fetch_as_json


def get_page_link_titles(api: str, page: str):
    link = f"{api}?action=parse&format=json&page={quote_plus(page)}"
    data = fetch_as_json(link)
    html = data["parse"]["text"]["*"]
    bshtml = BeautifulSoup(html, 'html.parser')
    titles = list(filter(lambda x: x, map(
        lambda x: x.text, bshtml.find_all("a"))))
    print("\n".join(titles))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    get_page_link_titles(sys.argv[1], sys.argv[2])
