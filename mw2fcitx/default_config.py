from mw2fcitx.tweaks.moegirl import tweaks

exports = {
    "source": {
        "api_path": "https://zh.moegirl.org.cn/api.php",
        "kwargs": {
            "title_limit": 120
        }
    },
    "tweaks": tweaks,
    "converter": {
        "use": "opencc",
        "kwargs": {}
    },
    "generator": {
        "use": "rime",
        "kwargs": {}
    }
}

print("ok")