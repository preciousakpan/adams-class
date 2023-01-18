#FOR UDOLU: 41I0GF82074370R8$


school = {
    "primary1" : {"Abdul":"maths",
                    "Femi":"Lit-in-eng"},
    "primary2" : {"Ola":"maths",
                    "Femi":"music"}
}

name = input("Student's name ")
# a = school["primary1"].keys()
#print (a)

for i in school:
    a = school[i].keys()
#    print(a)
    if name in a:       
        print(i)


size = ['small', 'medium', 'large']
item = ['bag', 'shoes', 'watch', 'phone']

for a in size:
    for b in item:
        print(b)


