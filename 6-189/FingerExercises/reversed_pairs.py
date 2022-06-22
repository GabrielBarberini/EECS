fin = open("../words.txt")

import bisect

word_list = []

for line in fin:
    word = line.strip()
    word_list.append(word)

def in_bisect(word_list, word):
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word

def reverse_pairs(word_list):
    reverse_pairs = []

    for word in word_list:
        reverse_word = word[::-1]

        if word == reverse_word:
            next

        if in_bisect(word_list, reverse_word):
            reverse_pairs.append([word, reverse_word])
    return reverse_pairs

print(reverse_pairs(word_list))
