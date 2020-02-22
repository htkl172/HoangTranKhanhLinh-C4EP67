# from turtle import *
# color('red')
# lt(25)
# for i in range(2):
#     fd(70)
#     rt(50)
#     fd(70)
#     rt(130)
#     fd(70)
#     rt(50)
#     fd(70)
#     for j in range(1):
#         fd(70)
#         lt(50)
#         fd(70)
#         lt(130)
#         fd(70)
#         lt(50)
#         fd(70)
#         lt(90)
        

# done()

from turtle import *
a = 3
for i in range(4):
    if i % 2 == 0:
        color('blue')
    else:
        color('red')
    for j in range(a):
        fd(90)
        lt(360/a)
    a = a + 1
