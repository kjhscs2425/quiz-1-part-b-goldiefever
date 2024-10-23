from turtle import *
from math import *

f=forward
b=backward
r=right
l=left
right_angle=90

def isosceles_right_triangle():
    f(50)
    r(right_angle)
    f(50)
    r(135)
    f(71)
    b(71)
    l(135)

for i in range(4):
    isosceles_right_triangle()
    
exitonclick()