import os
os.system("cls" if os.name == "nt"else "clear")



def symmetric_browse(L):
    n = len(L)
    result = []
    for i in range(n // 2 + 1):
        if i == n - i - 1:
            result.append(L[i])
        else:
            result.extend([L[i], L[n - i - 1]])
    return result


L=[1,3,5,7,9,8,6,4,2]
symmetric_browse(L)
print(symmetric_browse(L))
