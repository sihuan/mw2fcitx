# moegirl.org dictionary for fcitx5-pinyin

[![CircleCI](https://circleci.com/gh/outloudvi/fcitx5-pinyin-moegirl.svg?style=svg)](https://circleci.com/gh/outloudvi/fcitx5-pinyin-moegirl)

[Releases](https://github.com/outloudvi/fcitx5-pinyin-moegirl/releases)

## Installation
### Arch Linux
1. Install the package `fcitx5-pinyin-moegirl` from releases.

### Others
1. Download latest version of "moegirl.dict" from releases.
2. Copy into `/usr/share/fcitx5/pinyin/dictionaries/` (create the folder if it does not exist)

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
