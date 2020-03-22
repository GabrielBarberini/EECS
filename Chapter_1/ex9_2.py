fin = open('../words.txt')

def has_no_e(word):
    count = 0
    for c in word:
        if c == 'e': return False
    return True

def percentage(part, total):
    return part/total*100

wordcount = 0
no_e_count = 0

for word in fin:
    wordcount += 1
    if has_no_e(word):
        print(word)
        no_e_count += 1

print(percentage(no_e_count, wordcount))


