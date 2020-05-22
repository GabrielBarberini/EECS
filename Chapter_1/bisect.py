"""
Exercise 10.10.
To check whether a word is in the word list, you could use the in operator, but it would be slow because it searches through the words in order.
Because the words are in alphabetical order, we can speed things up with a bisection search (also known as binary search), which is similar to what you do when you look a word up in the dictionary (the book, not the data structure). You start in the middle and check to see whether the word you are looking for comes before the word in the middle of the list. If so, you search the first half of the list the same way. Otherwise you search the second half.
Either way, you cut the remaining search space in half. If the word list has 113,809 words, it will take about 17 steps to find the word or conclude that it’s not there."""

fin = open("../words.txt")

def in_bisect(t, word):
    a = 0
    b = 1
    l = []

    for line in t:
        l.append(line.strip())

    while len(l)//2 > 0:
        index = len(l)//2
       
        if word[a:b] > "n":
            #through right
            if word in l[index:]:
                return True
            else:
                l = l[index:]
                a += 1
                b += 1
        else:
            #through left
            if word in l[:index]:
                return True
            else:
                l = l[index:]
                a += 1
                b += 1
    return False

print(in_bisecit(fin, "ameixa"))
