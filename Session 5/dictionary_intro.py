# person = ['Duc', 96, 'Ha Noi', 'Son La', 'dev', False, True]
person = {
    
    'name': 'Duc', 
    'yob': 96, 
    'address': 'Ha Noi'
    }
#key luon phai doc nhat, neu 2 key trung nhau thi phai lay key cuoi cung]
person['gender'] = 'Male' #CREATE
person['address'] = 'Da Lat' #UPDATE

del person['yob']
if 'job' in person:
    print('job' in person)

print(person)
#phia been trai dau : la key ' ', ben phai la value
#{'key1': value1, 'key2': value2}
#dictionary ko co index
# print(person['name'])
# info = {
#     'ten': 'Linh',
#     'tuoi': 22,
#     'dia chi': 'Chua Lang',
#     'ho khau': 'QN',
# }

# print(info)
# print(info['ho khau'])
# for key, value in person.items(): #READ ALL
#     print(key, value)
# key = input()
# print(info[key])
teencode = {
    'clgt': 'con lon goi tinh',
    'hok': 'khong',
    'iu': 'yeu',
    'vk': 'vo',
    'ck': 'chong',
}
loop = True
while loop:
    key = input('Ban muon tra tu gi: ')
    if key in teencode:
        print(teencode[key])
    else:
        word = input('Moi ban dong gop tu: ')
        meaning = input('Moi ban dong gop nghia: ')
        teencode[word] = meaning
        print(word, ":", teencode[word])