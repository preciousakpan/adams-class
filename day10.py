shop = {
    'mango' : 100,
    'pawpaw' : 300,
    'apple' : 200,
    'pear' : 500,
    'banana' : 100,
    'food' : ['beans', 'rice', 'ogi']
}

#SIMPLE ASSIGNMENT1: APPEND TO A LIST IN A DICTIONARY
#SIMPLE ASSIGNMENT2: PRACTICE HOW TO USE DICT.UPDATE()

amount = 0

while True:
    add = input ("add items  ")
    if add == 'end':
        break
    else:
        if add in shop:
            price = shop[add]
#            print (price)
            amount = amount + price
#            print (amount)
        else:
            print(f'{add} is not in the shop')

print (f'Your total cost is {amount}')



cart = {
    'mango' : 3,
    'pawpaw' : 4,
    'apple' : 1,
    'pear' : 6,
    'banana' : 2
}


while True:
    add = input("add item  ")
    qty = cart[add]
    if qty > 1:
        qty = qty - 1
        cart[add] = qty
        print (f"{qty} remaining")
    else:
        print(f"{add} is out of stock")

