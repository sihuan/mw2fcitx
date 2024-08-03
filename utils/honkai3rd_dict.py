from mw2fcitx.tweaks.moegirl import tweak_remove_word_includes, tweak_len_more_than, tweak_remove_regex, tweak_trim_suffix, tweak_normalize
from typing import List

def tweak_trim_prefix(prefixes):
    def cb(items: List[str]):
        ret = []
        for i in items:
            for j in prefixes:
                i = i.removeprefix(j)
            ret.append(i)
        return ret

    return cb

honkai3rd_tweaks = [
    tweak_remove_word_includes(["攻略", "规范"]),
    tweak_trim_suffix(["语音", "列表", "需要内容"]),
    tweak_trim_prefix(["官方"]),
    tweak_normalize,
    tweak_len_more_than(1),
]

exports = {
    "source": {
        "api_path": "https://r.zjuyk.site/https://wiki.biligame.com/bh3/api.php",
        "file_path": [
            "extras/honkai3rd.txt"
        ],
        "kwargs": {
            "output": "honkai3rd_titles.txt"
        }
    },
    "tweaks": 
        [],
    "converter": {
        "use": "opencc",
        "kwargs": {}
    },
    "generator": [{
        "use": "rime",
        "kwargs": {
            "output": "honkai3rd.dict.yaml"
        }
    }, {
        "use": "pinyin",
        "kwargs": {
            "output": "honkai3rd.dict"
        }
    }]
}
