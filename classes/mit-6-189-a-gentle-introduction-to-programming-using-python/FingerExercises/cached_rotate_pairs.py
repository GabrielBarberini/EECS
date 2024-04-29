"""Exercise 11.5. Two words are “rotate pairs” if you can rotate one of them and get the other (see rotate_word in Exercise 8.5).
Write a program that reads a wordlist and finds all the rotate pairs. Solution: http:// thinkpython2. com/ code/ rotate_ pairs. py ."""

fin = open("../words.txt")
words = {}

for line in fin:
    words.setdefault(line.strip())

def rotate(phrase, shift):
    encoded_phrase = []
    for letter in phrase:
        if ord(letter) >= 97\
        and (ord(letter) - 97) <= 25:
            cipher = ord(letter)+shift

            while cipher%122 > 0\
            and cipher%122 != cipher:
                cipher = ((96+cipher)%122)
            encoded_phrase.append(chr(cipher))

        elif ord(letter) >= 65\
        and (ord(letter) - 65) <= 25:
            cipher = ord(letter)+shift

            while cipher%90 > 0\
            and cipher%90 != cipher:
                cipher = ((64+cipher)%90)
            encoded_phrase.append(chr(cipher))

        else:
            encoded_phrase.append(letter)
            
    return ''.join(encoded_phrase)

def find_rotate_words(words):
    rotate_words = []
    cache = {}
    for word in words:
        for i in range(1,26):
            rotated = rotate(word, i)
            if rotated in words:
                cache.setdefault(rotated)
                rotate_words.append(word)
                break
    return rotate_words

print(find_rotate_words(words))
