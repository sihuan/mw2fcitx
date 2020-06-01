MEDIAWIKI_API_ENDPOINT="https://zh.moegirl.org/api.php"

all: build

build: moegirl.dict

.INTERMEDIATE: titles.txt

titles.txt:
	python ./fetch.py $(MEDIAWIKI_API_ENDPOINT) titles.txt

results.txt: titles.txt
	python ./collate_moegirl.py titles.txt

moegirl.raw: results.txt
	python ./convert.py results.txt > moegirl.raw

moegirl.dict: moegirl.raw
	libime_pinyindict moegirl.raw moegirl.dict

install: moegirl.dict
	install -Dm644 moegirl.dict -t $(DESTDIR)/usr/share/fcitx5/pinyin/dictionaries/

moegirl.dict.yaml: moegirl.raw
	sed 's/[ ][ ]*/\t/g' moegirl.raw > moegirl.rime.raw
	sed -i 's/\t0//g' moegirl.rime.raw
	sed -i "s/'/ /g" moegirl.rime.raw
	echo -e '---\nname: moegirl\nversion: "0.1"\nsort: by_weight\n...\n' >> moegirl.dict.yaml
	cat moegirl.rime.raw >> moegirl.dict.yaml

install_rime_dict: moegirl.dict.yaml
	install -Dm644 moegirl.dict.yaml -t $(DESTDIR)/usr/share/rime-data/