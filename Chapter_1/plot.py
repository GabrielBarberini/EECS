#by gabrielbarberini
import turtle
import os

'''
Disclaimer
* Here, 'n' is equal to the number of angles we want, not the number of sides, it just matches the number of sides in case of polygons
* The polygons are regular
'''

poro = turtle.Turtle()

def square(t, l):
    for i in range(4):
        t.fd(l)
        t.lt(90)

def polygon(t, l, n): 
    for i in range(n):
        t.fd(l)
        t.lt(360/n)

def circle(t, r):
    '''
    Inception thoughs: Since 360 = 2pi and l = r so polygon(t, l 360) is moving forward 360 times with a lenght of r, in the end we have a circumference of 2*pi*r.
    ''' 
    polygon(t, r, 360)

def arc(t, r, a):
    for i in range(a):
        t.fd(r)
        t.lt(1)

def dash():
    os.system('clear')
    user = input("What you want me to draw?... \nsquare, polygon, circle, arc\n")

    if user == "square":
       l = input("Square side lenght? \n")
       square(poro, int(l))
       exit()     
     
    elif user == "polygon":
       l = input("Polygon side lenght? \n")
       n = input("Polygon side number? \n")
       polygon(poro, int(l), int(n))
       exit()       

    elif user == "circle":
       r = input("Circle radius? \n")
       circle(poro, int(r))
       exit()          

    elif user == "arc":
       r = input("Arc radius? \n")
       a = input("Arc angle? \n")
       arc(poro, int(r), int(a))
       exit()          

    else:
       print("Not a valid option!")
       exit()   
dash()
