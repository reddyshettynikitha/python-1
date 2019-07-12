# undo() function will undo the turtle last action
from turtle import *
pencolor('blue')
for i in range(15):
    forward(100)
    left(90)
    forward(10)
    left(90)
    forward(100)
    right(90)
    forward(10)
    right(90)
pencolour('red')
for i in range(90):
    undo()
