def dedup(arr: [str]):
    ret = []
    for i in arr:
        if i not in ret:
            ret.append(i)
    return ret