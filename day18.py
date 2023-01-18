import json

filename = 'day18.json'

item = input("Item name ")

with open(filename, 'r') as file:
    content = json.load(file)
    if item in content:
        qty = content[item]
        print (qty)
    else:
        print (f"{item} not in json")
    print (content)

data = {"boxes":1}
content.update(data)

with open(filename, 'w') as file:
    json.dump(content, file)