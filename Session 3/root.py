from getpass import getpass
username = "mindx"
password = "xdnim"

loop = True
count = 0
while loop:
    count += 1
    print(count)
    if count == 7:
        print("spam vua thoi T_T")
        loop = False
    else:
        input_username = input("username?")
        if input_username == username:
        
            input_password = getpass()
            print(input_password)
            if input_password == password:
                print("Welcome to mindx")
                loop = False
            else:
                print("Sai mat khau")
        else:
            print("Sai username")
        