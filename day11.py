shop = {
    'banana':{'price':350, 'qty': 3},
    'apple':{'price': 200, 'qty': 1},
    'pineapple':{'price':170, 'qty': 2},
}

amount = 0
while True:
    add = input("add items ")
    if add == "end":
        break
    else:
        if add in shop:
            qty = shop[add]['qty']
            if qty > 0:
                qty = qty -1
                shop[add]['qty'] = qty
                print (f"{qty} remaining")
                price = shop[add]['price']
                amount = amount + price
            else:
                print (f"{add} is out of stock")
        else:
            print (f'{add} is not in the shop')

print (f"your total amount is {amount}")
