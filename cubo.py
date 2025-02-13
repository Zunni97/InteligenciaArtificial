"""
Rojas Baldivia Zunni.
Practica 1: Cubo.

"""
import turtle as turtle
from turtle import *

def linea (num_pixeles):
    for pixel in range(num_pixeles):
        dot(3, "black")
        turtle.forward(1)
linea(100)

turtle.teleport(x=-250)
turtle.teleport(y=70)

def cuadrado ():
    forward(100),
    right(90),
    forward(100),
    right(90),
    forward(100),
    right(90),
    forward(100)

cuadrado()

right(45)
forward(50)
right(45)

cuadrado()

right(90)
forward(100)
right(135)
forward(50)
left(45)
forward(100)
left(135)
forward(50)
left(135)
forward(100)
left(45)
forward(50) 

input("Detener tortuga")