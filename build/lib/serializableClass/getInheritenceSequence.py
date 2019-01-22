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
        res += str(s)[8:-2] + "|"
    res = res[0:-2]
    return res