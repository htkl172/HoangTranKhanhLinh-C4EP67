#1 INIT DICTIONARY
stock = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30,

}

#2 READ
key = input('Moi ban nhap ten hang may can tim: ').upper()
print(stock[key])
#4 CREATE
stock['TOSHIBA'] = 10
user_brand = input('Moi ban nhap hang moi: ').upper()
user_stock = int(input('Moi ban nhap so luong: '))
stock[user_brand] = user_stock
print(stock)

#6 UPDATE
stock['DELL'] = 60
stock['MACBOOK'] = 2
print(stock)

#7 READ
for key, value in stock.items(): #READ ALL
    print(key, ':', value)

#8 SUM VALUE
print(sum(stock.values()))

#9 CREATE
stock['FUJITSU'] = 15
stock['ALIENWARE'] = 5
print(sum(stock.values()))

#1 INIT PRICE TABLE
price = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 12000,
    'ASUS': 400,
    'ACER': 350,
    'TOSHIBA': 600,
    'FUJITSU': 900,
    'ALIENWARE': 1000,

}

#2 PRINT PRICE
user_input = input('Moi ban nhap gia may can tim: ').upper()
print(price[user_input])

#4 PRINT INVOICE
user_quan = int(input('Moi ban nhap so luong can mua: '))
print(price[user_input] * user_quan)

#6 UPDATE WAREHOUSE
realtime = stock[user_input] - user_quan
print(user_input, ':', realtime)

#8 CALCULATE PRICE
print(stock)
for key in stock:
    quan = stock[key]
    price_1 = price[key]
    total = quan * price_1
    print(key, ':', total)

#9 CALCULATE TOTAL PRICE
sum = 0
for key in stock:
    quan = stock[key]
    price_1 = price[key]
    total = quan * price_1
    sum = sum + total
print(sum)


    