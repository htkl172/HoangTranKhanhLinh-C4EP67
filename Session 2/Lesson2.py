# # # age = 18
# # # name = "Linh"
# # # print(age == 18)
# # # print (bool(age))
# # # if age >= 18 and name == "Mai": 
# # #     print("Welcome to xxx")
# # # elif age == 18:
# # #     print("Chúc bạn may mắn lần sau")
# # # else:
# # #     print("Cút đi!")
# # number = input()
# # print(int(number)**2)
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# delta = b**2 - 4*a*c

# if delta > 0:
#     print("x1 =",(-b+delta**0.5)/(2*a),"x2 =",(-b-delta**0.5)/(2*a))
# elif delta == 0:
#     print("x =",-b/(2*a))
# else:
#     print("Vô nghiệm")

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b+delta**0.5)/(2*a)
    x2 = (-b-delta**0.5)/(2*a)
    print(f"x1 = {x1} x2 = {x2}") #f = format, {} = variables
elif delta == 0:
    x = -b/(2*a)
    print(f"x = {x}")
else:
    print("PT vo nghiem")