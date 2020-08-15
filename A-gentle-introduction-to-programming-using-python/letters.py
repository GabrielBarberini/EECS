#by gabrielbarberini
import turtle

poro = turtle.Turtle()

def square(l):
    for i in range(4):
        poro.fd(l)
        poro.lt(90)

def polygon(l, n):
    for i in range(n):
        poro.fd(l)
        poro.lt(360/n)

def circle(r):
    polygon(r, 360)

def arc(r, a):
    for i in range(a):
        poro.fd(r)
        poro.lt(1)

def draw_o():
    circle(0.1)

def draw_O():
    arc(0.1, 90)
    poro.fd(6)
    arc(0.1, 180)
    poro.fd(6)
    arc(0.1, 90)

def draw_C():
    poro.lt(180)
    poro.fd(5)
    arc(0.2, 180)
    poro.fd(5)

def draw_D():
    poro.lt(270)
    poro.fd(10)
    poro.lt(90)
    arc(0.1, 180)
   
def draw_d():
    poro.lt(270)
    poro.fd(20)
    poro.lt(180)
    circle(0.1)

def draw_b():
    poro.lt(270)
    poro.fd(20)
    circle(0.1)

def draw_U():
    poro.lt(270)
    poro.fd(20)
    arc(0.1, 180)
    poro.fd(20)

print("I know how to print: O,o,C,D,U,b,d \n")

printLet = input("choose...\n")

if printLet == "O" or\
   printLet == "o" or\
   printLet == "C" or\
   printLet == "D" or\
   printLet == "U" or\
   printLet == "b" or\
   printLet == "d":
    eval('draw_'+printLet)()

else:
    print("I don't know how to print that :(")


