# moegirl.org dictionary for fcitx5-pinyin (or any MediaWiki instance!)

## tl;dr

### Releases
* **Update monthly on 15th**
* Build status: [![CircleCI](https://circleci.com/gh/outloudvi/fcitx5-pinyin-moegirl.svg?style=svg)](https://circleci.com/gh/outloudvi/fcitx5-pinyin-moegirl)
* [Download the latest version](https://github.com/outloudvi/fcitx5-pinyin-moegirl/releases/latest) for fcitx5-pinyin, fcitx5-rime, as well as pre-built packages for Arch Linux users

### [archlinuxcn]
Thanks for [@imlonghao](https://github.com/imlonghao) ([archlinuxcn/repo@6ca3779](https://github.com/archlinuxcn/repo/commit/6ca3779c99fc1115dc1e9b1cfdf9ffbc67825b96)), this dictionary is available packaged at the [archlinuxcn](https://github.com/archlinuxcn/repo) repository.

## Installation
### Arch Linux
1. Install the package `fcitx5-pinyin-moegirl` / `fcitx5-pinyin-moegirl-rime` from releases (or [[archlinuxcn]](https://github.com/archlinuxcn/repo)!).

### Others
1. Download latest version of `moegirl.dict` (for fcitx5-pinyin) / `moegirl.dict.yaml` (for RIME) from releases.
2. Copy it to `/usr/share/fcitx5/pinyin/dictionaries/` (for fcitx5-pinyin) / `/usr/share/rime-data/` (for RIME).
3. (for RIME) Add this dictionary to your config.

## Build Requirements
* libime (https://github.com/fcitx/libime/)

Python modules:
* opencc (https://pypi.org/project/OpenCC/)
* pypinyin (https://pypi.org/project/pypinyin/)

Manual Build & Installation:
```
make
sudo make install
```

## License
Unlicense

Note that the generated dictionary follows Moegirl.org's license: <https://zh.moegirl.org/萌娘百科:版权信息>
