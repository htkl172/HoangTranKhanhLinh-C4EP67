from random import randint, choice
from calc import calc #1 TEN FILE #2 TEN HAM


score = 0
loop = True
while loop:
    a = randint(0,9)
    b = randint(0,9)
    operator_poll = ['+', '-', '*', '/']
    dau = choice(operator_poll)
    result = calc(a, b, dau)
    random_num = randint(-1,1)
    display_result = result + random_num
    print(f'{a} {dau} {b} = {display_result}')
    ans = input('T/F? ').upper()
    if random_num == 0:
        if ans == 'T':
            score = score + 1
            print(score)
        else:
            score = 0
            print(score)
    else:
        if ans == 'F':
            score = score + 1
            print(score)
        else:
            score = 0
            print(score)
loop = False




