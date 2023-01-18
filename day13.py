def hello():
    return "How are you"

def math():
    return 6+7


def add_staff():
    staff = input("add staff name ")
    dept = input("dept to be added ")
    if dept in employee:
        d = employee[dept]
        d.append(staff)
        print(employee)
    else:
        print(f"{dept} is not a department")

def check_staff():
    name = input ("Enter Staff Name ")
    for dept, staff in employee.items():
        if name not in staff:
            continue
        elif name in staff:
            d = dept
            print (f'{name} is {d}')
    

def buy_items():
    pass
def verify():
    info = {
        'yul' : '74tgb',
        'bisi' : 'ugbdj34',
        'tolani' : '456gvh'
    }
    
    
def admin():
    global employee
    employee = {
        "cashier" : ['ayo', 'trix'],
        "cleaner" : ['fred', 'tony', 'stark'],
        "accountant" : ['yola']
    }
    task = input("What would you like to do?  ")
    if task == "check":
        check_staff()
    elif task == "add":
        add_staff()
    else:
        print ("Admin can only add staff or check staff")
