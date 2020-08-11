from optparse import OptionParser
from importlib import import_module
from mw2fcitx import config_parser
from mw2fcitx.build_dict import build
from mw2fcitx.utils import console, sanitize
import json
import sys


def get_args():
    parser = OptionParser(
        usage="Fetch titles from online and generate a dictionary.")
    parser.add_option("-c",
                      "--config",
                      dest="config",
                      default="config.py",
                      help="configuration file location")
    parser.add_option("-n",
                      "--name",
                      dest="name",
                      default="exports",
                      help="configuration object name")

    return parser.parse_args()


def main():
    (options, _) = get_args()
    filename = options.config
    objname = options.name
    console.debug("Parsing config file: {}".format(filename))
    config_file = import_module(filename)
    if objname not in dir(config_file):
        console.error(
            "Exports not found. Please make sure your config in in a object called '{}'."
            .format(objname))
        sys.exit(1)
    config_object = getattr(config_file, objname)
    console.debug("Config load:")
    displayable_config_object = sanitize(config_object)
    console.debug(
        json.dumps(displayable_config_object, indent=2, sort_keys=True))
    build(config_object)


if __name__ == "__main__":
    main()