# mw2fcitx

Build fcitx5 libraries from MediaWiki sites.

[![PyPI](https://img.shields.io/pypi/v/mw2fcitx)](https://pypi.org/project/mw2fcitx/)
[![PyPI - License](https://img.shields.io/pypi/l/mw2fcitx)](https://github.com/outloudvi/mw2fcitx/blob/master/LICENSE)
[![CircleCI](https://circleci.com/gh/outloudvi/mw2fcitx.svg?style=svg)](https://circleci.com/gh/outloudvi/mw2fcitx)

```sh
pip install mw2fcitx
# or if you want to just install for current user
pip install mw2fcitx --user
```

For the old `fcitx5-pinyin-moegirl`, see [branch v1](https://github.com/outloudvi/mw2fcitx/tree/v1).

For the pre-build moegirl dictionary info, see [the wiki](https://github.com/outloudvi/mw2fcitx/wiki/fcitx5-pinyin-moegirl).

## CLI Usage

```
mw2fcitx -c config_script.py
```

## Configuration Script Format

```python
# By default we assume the configuration is located at a variable
#     called "exports".
# You can change this with `-n any_name` in the CLI.

exports = {
    # Source configurations.
    "source": {
        # MediaWiki api.php path, if to fetch titles from online.
        "api_path": "https://zh.moegirl.org.cn/api.php",
        # Title file path, if to fetch titles from local file. (optional)
        # Only works if api_path is absent.
        "file_path": "titles.txt",
        "kwargs": {
            # Title number limit for online fetching. (optional)
            # Only works if api_path is provided.
            "title_limit": 120,
            # Title list export path. (optional)
            "output": "titles.txt"
        }
    },
    # Tweaks configurations as an list.
    # Every tweak function accepts a list of titles and return
    #     a list of title.
    "tweaks":
        tweaks,
    # Converter configurations.
    "converter": {
        # opencc is a built-in converter.
        # For custom converter functions, just give the function itself.
        "use": "opencc",
        "kwargs": {}
    },
    # Generator configurations.
    "generator": [{
        # rime is a built-in generator.
        # For custom generator functions, just give the function itself.
        "use": "rime",
        "kwargs": {
            # Destination dictionary filename. (optional)
            "output": "moegirl.dict.yml"
        }
    }, {
        # pinyin is a built-in generator.
        "use": "pinyin",
        "kwargs": {
            # Destination dictionary filename. (mandatory)
            "output": "moegirl.dict"
        }
    }]
}
```

A sample config file is here: [`sample_config.py`](https://github.com/outloudvi/mw2fcitx/blob/master/mw2fcitx/sample_config.py)

## License

[The Unlicense](https://github.com/outloudvi/mw2fcitx/blob/master/LICENSE)
