from mw2fcitx.pipeline import MWFPipeline


def build(config):
    config["source"] = config["source"] or {}
    config["tweaks"] = config["tweaks"] or []
    config["converter"] = config["converter"] or {}
    config["generator"] = config["generator"] or {}
    pipeline = MWFPipeline(config["source"].get("api_path"))
    pipeline.fetch_titles(**config["source"].get("kwargs"))
    pipeline.convert_to_words(config["tweaks"])
    pipeline.export_words(config["converter"].get("use"),
                          **config["converter"].get("kwargs"))
    pipeline.generate_dict(config["generator"].get("use"),
                           **config["generator"].get("kwargs"))
    return pipeline.dict