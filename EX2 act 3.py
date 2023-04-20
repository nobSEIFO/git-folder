import os
os.system("cls" if os.name == "nt"else "clear")



def shuffle_symbol(word, c):
    count_c = word.count(c)
    interleave = c + ''.join(['']*count_c)
    shuffle_list = [word[:i] + interleave + word[i:] for i in range(len(word)+1)]
    return shuffle_list
    
word = "abba"
c = "c"
print(shuffle_symbol(word, c))