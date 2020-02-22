from turtle import *
color('purple')
speed(-10)
for i in range(90):
    for j in range(45):
        forward(200)
        lt(90)
    lt(2)
    for k in range(45):
        pencolor('white')
        forward(200)
        lt(90)
    lt(2)


shape("turtle")
color("red")

mainloop()
for i in range(3):
    print(i)