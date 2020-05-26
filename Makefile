MEDIAWIKI_API_ENDPOINT="https://zh.moegirl.org/api.php"

all: build

build: moegirl.dict

titles.txt:
	./fetch.py $(MEDIAWIKI_API_ENDPOINT) titles.txt

results.txt: titles.txt
	node collate.js

moegirl.raw: results.txt
	./convert.py results.txt > moegirl.raw

moegirl.dict: moegirl.raw
	libime_pinyindict moegirl.raw moegirl.dict

install: moegirl.dict
	install -Dm644 moegirl.dict -t $(DESTDIR)/usr/share/fcitx5/pinyin/dictionaries/
