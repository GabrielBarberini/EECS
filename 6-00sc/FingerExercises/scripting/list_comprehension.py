print([ x for x in range (2, 100) if all(x % y != 0 for y in range (2, x-1))])
