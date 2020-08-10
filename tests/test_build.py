from mw2fcitx.pipeline import MWFPipeline


def test_pipeline_basic():
    SNAPSHOT_1 = "测试\tce'shi\t0\n百科\tbai'ke\t0\n"
    pipeline = MWFPipeline()
    pipeline.load_titles(["测试", "百科"])
    pipeline.convert_to_words([])
    pipeline.export_words()
    assert (pipeline.exports == SNAPSHOT_1)
    pipeline.generate_dict(output="test.dict")
    pipeline.generate_dict(generator="rime",
                           output="test.dict.yml",
                           name="test",
                           version="1.0")


if __name__ == "__main__":
    test_pipeline_basic()