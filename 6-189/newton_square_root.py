#Newton method for finding square roots. y = ( x + a/x )/2 where 'x' is an initial approximate guess for the square root and 'a' is the number which we want to find the square from.

import math

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

def mysqrt(a):
    """
this function is an encapsulation of the newton_square algorithm in which the approximate guess is taken recursively without any further input""" 
    
    if a <= 1:
        return 1

    else:   
        x = mysqrt(a-1)
        while True:
            y = (x + a/x)/2
            if x == y:
                return x
            x = y

def test_square_root():
    print("a", "mysqrt(a)", "math.sqrt(a)", "diff")
    print("--","---------", "------------", "----")
    print(1,mysqrt(1),math.sqrt(1),abs(mysqrt(1)-math.sqrt(1)))
    print(2,mysqrt(2),math.sqrt(2),abs(mysqrt(2)-math.sqrt(2)))
    print(3,mysqrt(3),math.sqrt(3),abs(mysqrt(3)-math.sqrt(3)))
    print(4,mysqrt(4),math.sqrt(4),abs(mysqrt(4)-math.sqrt(4)))
    print(5,mysqrt(5),math.sqrt(5),abs(mysqrt(5)-math.sqrt(5)))
    print(6,mysqrt(6),math.sqrt(6),abs(mysqrt(6)-math.sqrt(6)))
    print(7,mysqrt(7),math.sqrt(7),abs(mysqrt(7)-math.sqrt(7)))
    print(8,mysqrt(8),math.sqrt(8),abs(mysqrt(8)-math.sqrt(8)))
    print(9,mysqrt(9),math.sqrt(9),abs(mysqrt(9)-math.sqrt(9)))

test_square_root()
