fin = open('../words.txt')

for word in fin:
    if len(word) > 20:
        print(word)
