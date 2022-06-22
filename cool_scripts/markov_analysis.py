def markov(d, lenght=2)
''' assumes input is a set of strings, returns a map of prefix to possible suffix naturally weighted by frequency of occurence'''
    mark = {}
    for word in d:
        mark.setdefault(word[:lenght],[]).append(word[lenght:])
    return mark
