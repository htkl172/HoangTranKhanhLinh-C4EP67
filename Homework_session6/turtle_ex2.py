from turtle import *
#5
def draw_star(x, y, length):    
    pendown()
    for i in range(5):
        fd(length)
        rt(144)
    penup()
    goto(x, y)

#6
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)