def soustraire(L1, L2):
    res = []
    for x in L1:
        if x not in L2:
            res.append(x)
    return res
