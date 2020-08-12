from mw2fcitx.pipeline import MWFPipeline
from os.path import getsize


def test_pipeline_basic():
    pipeline = MWFPipeline()
    pipeline.load_titles(["测试", "百科", "朝之琉璃"])
    pipeline.convert_to_words([])
    pipeline.export_words()
    assert (pipeline.exports != "")
    pipeline.generate_dict(generator="rime",
                           output="test.dict.yml",
                           name="test",
                           version="1.0")
    assert (getsize("test.dict.yml") > 0)
    pipeline.generate_dict(
        generator="pinyin",
        output="test.dict",
    )
    assert (getsize("test.dict") > 0)


if __name__ == "__main__":
    test_pipeline_basic()