import os
os.system("cls" if os.name == "nt"else "clear")


def soustraire(L1, L2):
    res = []
    for x in L1:
        if x not in L2:
            res.append(x)
    return res

L1=[1,3,6,4,7]
L2=[1,2,3,5]
soustraire(L1, L2)
print(soustraire(L1, L2))