from copy import deepcopy
import json


def sanitize(obj):
    res = deepcopy(obj)
    typ = type(res)
    if typ == type(sanitize):
        func_name = res.__name__ or "lambda"
        return "[func {}]".format(func_name)
    elif typ == type({}):
        for i in res.keys():
            res[i] = sanitize(res[i])
    elif typ == type([]):
        fin = []
        for i in res:
            fin.append(sanitize(i))
        res = fin
    elif typ == type(1) or typ == type("1"):
        return str(res)
    else:
        return "[" + str(type(res)) + "]"
    return res
