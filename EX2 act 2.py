import os
os.system("cls" if os.name == "nt"else "clear")


def factors(word):
    factor_list = []
    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            factor_list.append(word[i:j])
    return factor_list
    
   
word = "aaabbbccc"
print(factors(word))
