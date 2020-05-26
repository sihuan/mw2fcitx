all: build

build: moegirl.dict

titles.txt: prepare
	node fetch.js

results.txt: titles.txt
	node collate.js

moegirl.raw: results.txt
	./convert.py results.txt > moegirl.raw

moegirl.dict: moegirl.raw
	libime_pinyindict moegirl.raw moegirl.dict

install: moegirl.dict
	install -Dm644 moegirl.dict -t $(DESTDIR)/usr/share/fcitx5/pinyin/dictionaries/

prepare:
	npm install axios
