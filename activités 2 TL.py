import os
os.system("cls" if os.name == "nt"else "clear")



def repeat_by_list(L1, L2):
    result = []
    for i, x in enumerate(L1):
        sublist = [x] * L2[i]
        result.append(sublist)
    return result

L1=[1,3,6,]
L2=[2,2,3]
repeat_by_list(L1, L2)
print(repeat_by_list(L1, L2))