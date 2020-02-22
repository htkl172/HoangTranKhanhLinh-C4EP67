# # # # # # # #1
# # # # # # # a = int(input("Moi ban nhap chieu cao (cm): "))
# # # # # # # b = int(input("Moi ban nhap can nang (kg): "))
# # # # # # # BMI = b/(a/100)**2
# # # # # # # print(BMI)
# # # # # # # if BMI > 30:
# # # # # # #     print("Obese")
# # # # # # # elif BMI >= 25:
# # # # # # #     print("Overweight")
# # # # # # # elif BMI >= 18.5:
# # # # # # #     print("Normal")
# # # # # # # elif BMI >= 16:
# # # # # # #     print("Underweight")
# # # # # # # else:
# # # # # # #     print("Severely underweight")

# # # # # # #2
# # # # # # a = int(input("Moi ban nhap mot so tu nhien bat ky: "))
# # # # # # giai_thua = 1
# # # # # # if a == 1 or a == 0:
# # # # # #     print("Giai thua cua", a, "la", giai_thua)
# # # # # # else:
# # # # # #     for i in range(2, a + 1):
# # # # # #         giai_thua = giai_thua * i
# # # # # #     print("Giai thua cua", a, "la", giai_thua)

# # # # # #3
# # # # # loop = True
# # # # # count = 0
# # # # # while count <= 19:
# # # # #     print(count)
# # # # #     count = count + 1

# # # # a = int(input("Enter a number: "))
# # # # loop = True
# # # # count = 0
# # # # while count < a:
# # # #     print(count)
# # # #     count = count + 1
# n = int(input("Enter a number: "))
# if n % 2 == 0:
#     for i in range(int(n/2)):
#         print("1")
#         for j in range(1):
#             print("0")
# else:
#     for i in range(int((n-1)/2)):
#         print("1")
#         for j in range(1):
#            print("0")
#     print("1")

#Python Program to Print 1 and 0 in alternative Columns
 
# n = int(input("Please Enter a Number : "))
 
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         for j in range(1, n + 1):
#             if(j % 2 == 0):          
#                 print('1', end = '  ')
#             else:
#                 print('0', end = '  ')
#     else:
#         for j in range(1, n + 1):
#             if(j % 2 == 0):          
#                 print('0', end = '  ')
#             else:
#                 print('1', end = '  ')
#     print()

# n = int(input("Please Enter a Number : "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i*j, end = '  ')
#     print()
