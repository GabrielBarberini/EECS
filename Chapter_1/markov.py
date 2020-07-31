"""Exercise 13.8. Markov analysis:
1. Write a program to read a text from a file and perform Markov analysis. The result should be a dictionary that maps from prefixes to a collection of possible suffixes. The collection might be a list, tuple, or dictionary; it is up to you to make an appropriate choice. You can test your program with prefix length two, but you should write the program in a way that makes it easy to try other lengths.
2. AddafunctiontothepreviousprogramtogeneraterandomtextbasedontheMarkovanalysis. Here is an example from Emma with prefix length 2:
He was very clever, be it sweetness or be angry, ashamed or only amused, at such a stroke. She had never thought of Hannah till you were never meant for me?" "I cannot make speeches, Emma:" he soon cut it all himself.
For this example, I left the punctuation attached to the words. The result is almost syntacti- cally correct, but not quite. Semantically, it almost makes sense, but not quite.
What happens if you increase the prefix length? Does the random text make more sense?
132 Chapter 13. Case study: data structure selection
 3. Once your program is working, you might want to try a mash-up: if you combine text from two or more books, the random text you generate will blend the vocabulary and phrases from the sources in interesting ways.
Credit: This case study is based on an example from Kernighan and Pike, The Practice of Pro- gramming, Addison-Wesley, 1999."""

import random
import string

fin = open('../mombo.txt')

def readFile(f):
    d = {}
    for line in f:
        for word in line.split():
            d.setdefault(word.strip(string.punctuation+string.whitespace+string.digits).lower())
    return d

def letterMarkAna(d, length=4):
    marko = {}
    for word in d:
        marko.setdefault(word[:length], []).append(word[length:])
    return marko

def randomGen(d, l, words=15):
    l = []
    for i in range(words):
        word = random.choice(list(d))
        l.append(word+random.choice(d[word]))
    return ' '.join(l)

print(randomGen(letterMarkAna(readFile(fin)), readFile(fin)))
