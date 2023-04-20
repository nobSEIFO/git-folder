import os
os.system("cls" if os.name == "nt"else "clear")



def prefixes(word):
    prefix_list = []
    for i in range(1, len(word)+1):
        prefix_list.append(word[:i])
    return prefix_list

word = input("Entrez le mot : ")
print("tous les préfixes du mot est :", prefixes(word))
