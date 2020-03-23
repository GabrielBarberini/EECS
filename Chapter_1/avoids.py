fin = open('../words.txt')
symbols = input("insert forbidden characters:\n")

def avoids(words,symbols):
    allowedWords = []
    for word in words:
        counter = 0
        for c in word:
            for x in symbols:
                if c == x: counter += 1
        if counter == 0:
            word = word.strip() 
            allowedWords.append(word)
    return allowedWords

print(avoids(fin,symbols)) 
