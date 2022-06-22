"""
Write a function called most_frequent that takes a string and prints the let- ters in decreasing order of frequency. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at http: // en. wikipedia. org/ wiki/ Letter_ frequencies . Solution: http: // thinkpython2. com/ code/ most_ frequent. py
"""

def most_frequent(string):
    d = dict()
    for letter in string:
        d.setdefault(letter.lower(), 0)
        d[letter.lower()] += 1
    
    frequencies = list()
    for letter, frequency in d.items():
        frequencies.append( (frequency, letter) )
    
    frequencies.sort(reverse=True)
    return frequencies 

string = input("Insira um texto...\n")

for frequency in most_frequent(string):
    print(frequency)
