from random import randint
a = randint(0,9)
b = randint(0,9)
c = randint(a + b - 1, a + b + 1)
print(a, '+', b, '=', c)
print(a + b == c)

print(f'{a} + {b} = {c}')
ans = print(input('Moi ban chon T/F: ').upper())
score = 0
d = a + b
loop = True
while loop:
    if d == c:
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





