#7
def remove_dollar_sign(s):
    result = s.replace('$', '')
    return result

a = remove_dollar_sign('$100')

#8
string_with_no_dollars = remove_dollar_sign('$80% percent of $life is to show $up')
if string_with_no_dollars == '80% percent of life is to show up':
    print('Your function is correct')
else: 
    print("Oops, there's a bug")

#9
def get_even_list(l): 
    even_num = []   
    for n in l:
        if n % 2 == 0:
            even_num.append(n)
    return even_num

#10
even_list = get_even_list([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
    print('Your function is correct')
else:
    print('Oops, bugs detected')

#11

def is_inside(list_point, list_rec):
    if list_point[0] > list_rec[0]:
        if list_point[0] < list_rec[0] + list_rec[2]:
            if list_point[1] > list_rec[1]:
                if list_point[1] < list_rec[1] + list_rec[3]:
                    return True
                else:
                    return False
            else: 
                return False
        else:
            return False
    else:
        return False

#12
test_case = is_inside([150, 70], [140, 60, 100, 200])
if test_case == True:
    print('Your function is correct')
else: 
    print("Oops, there's a bug")


    


    


