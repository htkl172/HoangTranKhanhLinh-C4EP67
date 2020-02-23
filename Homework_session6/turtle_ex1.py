#1
def hello():
    print('Hello world')

hello()
hello()
hello()

#2
def add(a, b):
    print(a + b)

add(1, 2)

#3
from turtle import *
def draw_square(length, square_color):
    color(square_color)
    for i in range(4):
        fd(length)
        lt(90)

#4 
for i in range(30):
    draw_square(i * 5, 'red')
    lt(17)
    penup()
    fd(i * 2)
    pendown()





