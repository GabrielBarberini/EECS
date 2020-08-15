"""Exercise 12.2. More anagrams!
1. Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of
words that are anagrams.
Here is an example of what the output might look like:
     ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
     ['retainers', 'ternaries']
     ['generating', 'greatening']
     ['resmelts', 'smelters', 'termless']
Hint: you might want to build a dictionary that maps from a collection of letters to a list of words that can be spelled with those letters. The question is, how can you represent the collection of letters in a way that can be used as a key?
2. Modify the previous program so that it prints the longest list of anagrams first, followed by the second longest, and so on.
3. In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on the board, to form an eight-letter word. What collection of 8 letters forms the most possible bingos?
Solution: http: // thinkpython2. com/ code/ anagram_ sets. py ."""

def makeDict(wordList):
    d = dict()
    for line in wordList:
        d.setdefault(line.strip())
    return d

def readWord(word):
    word = sorted(word)
    return tuple(word)

def groupByLetters(dictionary):
    group = dict()
    for word in dictionary:
        group.setdefault(readWord(word), []).append(word)
    return group

def findAnagrams(dictionary):
    anagrams = list()
    grouped_words = groupByLetters(dictionary)
    for words in grouped_words:
        if len(grouped_words[words]) > 1:
            anagrams.append(grouped_words[words])
    sorted_anagrams = sorted(anagrams, key=len)
    return sorted_anagrams

def filter_length(words, n):
    """Ok I admit, this part I got from the solution, I was actually filtering through the bingo method"""
    n_lettered = dict()
    for word in words:
        if len(word) == n:
            n_lettered.setdefault(word)
    return n_lettered

def bingo(dictionary):
    words = filter_length(dictionary, 8)
    anagrams = findAnagrams(words)
    return anagrams

fin = open("../words.txt")
words = makeDict(fin)

for anagram in bingo(words):
    print(anagram)

#I guess I finally beat the book, my solution seems to run faster, yeeeey ;)
