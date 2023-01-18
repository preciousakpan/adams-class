#LOOPS - FOR LOOP, WHILE LOOP
'''
for x in range(0,6):
    print (x)

for y in "burger":
    print (y)

for b in range(7):
    print (b * 2)

van = ['rice', 'beans', 'moimoi']

car = [34, 78, 43]

for c in car:
    van.append(c)
    print (van)

for c in car:
    van.append(c)

print(van)

for v in van:
    print (v)

for t in range(0, 11, 2):
    print (t)
else:
    print("Done")
'''

cars = ['bentley', 'benz', 'rolls royce', 'range rover', 'lexus']

# for car in cars:
#     print(car)
#     if car == 'rolls royce':
#         break

# for car in cars:
#     if car == "rolls royce":
#         break
#     print (car)

# for car in cars:
#     print (car)
#     if car == 'range rover':
#         continue

brand = input('brand of car  ')

if brand in cars:

    for car in cars:
        if car == brand:
            continue
        print(car)
else:
    print("Not a luxury car")

cart = ['egg', 'yolk']

item = input("add item  ")

cart.append(item)
print(cart)

for a in cart:
    pass


'''
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
.
.
.
6 x 12 = 72

'''
# creating a new dictionary
my_dict ={"java":100, "python":112, "c":11}

#getting keys from dictionary
value = int(input("enter value "))
for i in my_dict:
    if value == my_dict[i]:
        key = i
        print (key)
