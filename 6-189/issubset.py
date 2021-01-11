'''
MIT OCW - A Gentle Introduction to programming using python - january iap 2011
Exercise 2.4.
Now, see if you can, first, explain, and then improve this example!

def issubset(a,b):
    i = 0
    j = 0
    while i < len(a):
        c = False
        while j < len(b):
            if a[i] == b[j]:
                c = True
                j = j+1
            if c:
                c = False
            else:
                return False
        j = 0
        i = i+1
    return True
'''

#by gabrielbarberini

''' 
    (i) In the example above, the variable c is a flag used for nothing, so It can be removed.

    (ii) After (i), the second issue is that the code doesn't work.
        (a) If the first element in list a is asserted with the first element in list b, j is increased, then the next element in b will fail to assert since the index of a hasn't changed, therefore returning False and invalidating the entire flow.
        (b) If the first element in the list a is not asserted with the first lement in the list b, then it returns False and all the rest of the elements in b are discarded, which means a premature end of the function.

    (iii) Given (ii), some modifications were necessary. I could not solve ii-a by increasing the index of 'a' inside the inner loop without loosing some of the assertions or maintaining the current algorithm complexity, so I opted for increasing j in case the assertion fails and breaking for the next iteration of 'a' in case it passes, returning false if all the elements in 'b' has failed the assertion

Please, if you have any feedbacks or think there might be a better way of solving it maintaining the initial algorithm core-structure, just write me an email, I'm willing to know: gabrielbarberinirc@gmail.com '''

def issubset(a,b):
    i = 0
    j = 0 
    while i < len(a):
        while j <= len(b):
            if j == len(b):
                return False
            if a[i] == b[j]:
                break
            else:  
                j += 1
        j = 0
        i = i+1
    return True

x = input("insert anything for A \n")
y = input("insert anything for B \n")

print("\nIs the things provided for A inside the ones provided for B ?\n")
print(issubset(x,y))
