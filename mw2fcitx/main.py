from optparse import OptionParser


def get_args():
    parser = OptionParser(
        usage="Fetch titles from online and generate a dictionary.")
    parser.add_option("-i",
                      "--input",
                      dest="url",
                      help="address to api.php of a MediaWiki instance",
                      metavar="URL")
    parser.add_option("-c",
                      "--config",
                      dest="config",
                      default="config.py",
                      help="configuration file location")

    return parser.parse_args()


def main():
    v = get_args()
    print(v)