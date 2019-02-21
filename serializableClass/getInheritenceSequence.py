def getInheritenceSequence(cls):
    sequence = [cls]
    pos = 0
    while pos < len(sequence):
        parents = sequence[pos].__bases__
        for parent in parents:
            sequence.append(parent)
        pos += 1
    res = ""
    for s in sequence:
        className = str(s).split("'")[1]
        if className == "object":
            continue
        res += className.split(".")[1] + "_"
    res = res[0:-1]
    return res