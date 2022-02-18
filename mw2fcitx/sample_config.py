from .tweaks.moegirl import tweaks

exports = {
    "source": {
        "api_path": "https://zh.moegirl.org.cn/api.php",
        "kwargs": {
            "api_title_limit": 120,
            "file_title_limit": 60,
            "title_limit": 240,
            "partial": "partial.json",
            "output": "titles.txt"
        }
    },
    "tweaks":
        tweaks,
    "converter": {
        "use": "opencc",
        "kwargs": {
            "fixfile": "sample_fixfile.json"
        }
    },
    "generator": [{
        "use": "rime",
        "kwargs": {
            "output": "moegirl.dict.yml"
        }
    }, {
        "use": "pinyin",
        "kwargs": {
            "output": "moegirl.dict"
        }
    }]
}
