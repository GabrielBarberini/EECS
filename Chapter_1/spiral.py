#Archimedian spiral by gabrielbarberini
import turtle

poro = turtle.Turtle()

def spiral():
    theta = 1
    while True:
        poro.fd(0.001*theta)
        poro.lt(1)
        theta += 1

spiral()
