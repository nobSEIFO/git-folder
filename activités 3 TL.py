def symmetric_browse(L):
    n = len(L)
    result = []
    for i in range(n // 2 + 1):
        if i == n - i - 1:
            result.append(L[i])
        else:
            result.extend([L[i], L[n - i - 1]])
    return result
