import json
import sys

MANUAL_FIX_TABLE = {}

try:
    MANUAL_FIX_TABLE = json.loads(open("./manual_fix.json").read())
    print(f"Manual fix table loaded.", file=sys.stderr)
except Exception as e:
    print(f"Error loading manual fix table: {str(e)}", file=sys.stderr)

def manual_fix(text):
    if text in MANUAL_FIX_TABLE:
        return MANUAL_FIX_TABLE[text]
    return None