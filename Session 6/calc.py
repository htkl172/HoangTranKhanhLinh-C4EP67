def calc(a, b, operator):
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        result = a / b
    else:
        print('Kidding')
    return result

if __name__ == '__main__':
    a = calc(4,5,'+')
    print(a)
