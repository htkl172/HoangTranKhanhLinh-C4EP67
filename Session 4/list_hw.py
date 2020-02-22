#1 FILTER EVEN
number = [5, 1, 8, 92, 7, 30]
even_n = [i for i in number if i % 2 == 0]
print('All even numbers: ', even_n)

#2 SEQUENCE INPUT
user_list = []
n = int(input('Enter the list size: '))
for i in range(0, n):
    print('Enter the number at location', i, ': ')
    item = int(input())
    user_list.append(item)
print("User's List is: ", user_list)
even_input = [i for i in user_list if i % 2 == 0]
print('All even numbers: ', even_input)

#3 