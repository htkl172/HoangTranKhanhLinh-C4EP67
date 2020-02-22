from turtle import * # * = all
speed(-5)
shapesize(3)
shape("turtle")
#i=index
for i in range(360):
    for a in range(4):
        color("tomato")
        forward(200)
        left(90)
    left(1)
    for b in range(4):
        color("crimson")
        forward(200)
        left(90)
    left(1)
mainloop()