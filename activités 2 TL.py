def repeat_by_list(L1, L2):
    result = []
    for i, x in enumerate(L1):
        sublist = [x] * L2[i]
        result.append(sublist)
    return result
