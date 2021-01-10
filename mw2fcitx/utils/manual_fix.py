import json
from os import path

from .logger import console

MANUAL_FIX_TABLE = {}
JSON_PATH = path.join(path.dirname(path.realpath(__file__)), "manual_fix.json")

try:
    MANUAL_FIX_TABLE = json.loads(open(JSON_PATH).read())
    console.debug("Manual fix table loaded.")
except Exception as e:
    console.debug(f"Error loading manual fix table: {str(e)}")


def manual_fix(text):
    if text in MANUAL_FIX_TABLE:
        return MANUAL_FIX_TABLE[text]
    return None
