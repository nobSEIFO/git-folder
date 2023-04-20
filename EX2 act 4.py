import os
os.system("cls" if os.name == "nt"else "clear")



def shuffle(w1, w2):
    len_w1, len_w2 = len(w1), len(w2) 
    max_len = max(len_w1, len_w2) 
    idx_w1, idx_w2 = 0, 0
    shuffled = []
    while idx_w1 < len_w1 and idx_w2 < len_w2:
        shuffled.append(w1[idx_w1])
        idx_w1 += 1
        shuffled.append(w2[idx_w2])
        idx_w2 += 1
    if idx_w1 < len_w1:
        shuffled.extend(w1[idx_w1:])
    if idx_w2 < len_w2:
        shuffled.extend(w2[idx_w2:])
    return ''.join(shuffled)
'''
بديل
def shuffle(w1, w2):
    return ''.join([a + b for a, b in zip(w1, w2)]) + w1[len(w2):] + w2[len(w1):]
'''


w1 = input("Entrez le premier mot : ")
w2 = input("Entrez le deuxième mot : ")
print(shuffle(w1, w2))