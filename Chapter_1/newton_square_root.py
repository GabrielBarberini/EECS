#Newton method for finding square roots. y = ( x + a/x )/2 where 'x' is an initial approximate guess for the square root and 'a' is the number which we want to find the square from.

def newton_square(a,x):    
    """
'a' is the number you want to determine the square root
'x' is the initial guess 
"""
    while True:
        print(x)
        y = (x + a/x)/2
        if x == y:
            break
        x = y

newton_square(180, 13) 
