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

starrail_tweaks = [
    tweak_remove_word_includes(["攻略", "一览", "计算", "规范", "教程", "解说", "机制"]),
    tweak_trim_suffix(["语音", "列表", "需要内容"]),
    # tweak_trim_prefix(["奇怪的","美味的","特别的","特制的"]),
    tweak_remove_regex(["^模拟宇宙.+$"]),
    tweak_normalize,
    tweak_len_more_than(1),
]

exports = {
    "source": {
        "api_path": "https://r.zjuyk.site/https://wiki.biligame.com/sr/api.php",
        "file_path": [
            "extras/starrail.txt"
        ],
        "kwargs": {
            "output": "starrail_titles.txt"
        }
    },
    "tweaks": starrail_tweaks,
    "converter": {
        "use": "opencc",
        "kwargs": {}
    },
    "generator": [{
        "use": "rime",
        "kwargs": {
            "output": "starrail.dict.yaml"
        }
    }, {
        "use": "pinyin",
        "kwargs": {
            "output": "starrail.dict"
        }
    }]
}
