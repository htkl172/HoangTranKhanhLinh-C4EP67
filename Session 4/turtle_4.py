# colors = ['red', 'blue', 'brown', 'yellow', 'grey']
# from turtle import *
# a = 3
# for i in range(len(colors)):
#     color(colors[i])
#     for j in range(a):
#         fd(90)
#         lt(360/a)
#     a = a + 1

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
from turtle import *
for i in range(len(colors)):
    fillcolor(colors[i])
    begin_fill() 
    fd(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    end_fill()



        

           
                


done()