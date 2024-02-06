'''draw a square grid with columns and width provided by the user using only string operators (proposed by me based on printing exercise 1.2)'''

import math

def grid(x,y):   
    n = int(math.sqrt(y**2))
    m = int(math.sqrt(x**2))

    horizontal = ("+ ") + ("- "*m)
    base = (horizontal*n) + ("+\n")

    vertical = (n+1) * ("| " + ("  "*m))
    column = (vertical + ("\n")) * n

    print((base+column) * n + base)

width = int(input("Grid's width: "))
column = int(input("Grid's column number: "))

grid(width,column)
