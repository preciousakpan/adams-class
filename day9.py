cart = ['cars', 'house', 'clothes', 'shoes']
'''
while True:
    add = input("add item  ")
    if add == "end":
        break
    else:
        if add in cart:
            print(f"{add} already exists")
        else:
            cart.append(add)
print(cart)  
'''

while True:
    add = input("add item  ")
    if add == "end":
        break
    if add in cart:
        print(f"{add} already exists")
        continue
    cart.append(add)
print(cart)

