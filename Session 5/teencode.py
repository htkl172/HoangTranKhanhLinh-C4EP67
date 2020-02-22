teencode = {
    'vk': 'vo',
    'ck': 'chong',
    'clgt': 'con lon goi tinh',
    'hok': 'khong',
}
loop = True
while loop:
    word = input('nhap tu teencode ban muon tra: ')
    if word in teencode:
        print(word, 'co nghia la', teencode[word])
    else:
        ans = input("tu tren khong co trong tu dien, ban co muon bo sung khong?(y/n)").lower().strip()
        if ans == 'y':
            new_word = input('moi ban nhap nghia cua tu do:')
            teencode[word] = new_word
        elif ans == 'n':
            print('bye bye')
            loop = False


