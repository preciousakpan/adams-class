# car =  {
#     "name" : "Hyundai",
#     "brand"  : "Toyota",
#     "year" : 2008
# }


# creating a new dictionary
my_dict ={"java":100, "python":112, "c":11}

#getting keys from dictionary
value = int(input("enter value "))
for i in my_dict:
    if value == my_dict[i]:
        key = i
        print (key)




person = {
    "name" : "karen",
    "gender" : "female",
    "race" : "white",
    "age" : 54,
    "is_married" : False,
    "friends" : ['Mitch', 'yomi']
}

#print (person.get("gender"))

# print (person.keys())
# print (person.values())
print (person["race"])
#print(person.get("race"))


rando = {
    "jordan" : "SQL",
    "conor" : "Excel",
    "mike" : "java",
    "coleman" : "Azure",
    "onana" : "javascript",
    "gordon" : "C++",
    "alex" : ["python", "React"]
}


'''
player = input("What Player  ")
if player in rando:
    course = input("What Course  ")
    if course == rando[player]:
        print ("successful")
    else:
        print("Unsussessful")
else:
    print("Not a player")
'''

player1 = input("What Player  ")
if player1 in rando:
    course = rando[player1]
    print (f"{player1} offers {course}")
else:
    print (f"{player1} is not a player")