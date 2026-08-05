employee_count=0

def line():
    print("="*30)

def heading(title=""):
    line()
    print(title.upper())
    line()

def add_employee(name,salary):
    global employee_count
    print(f"Name : {name}")
    print(f"Salary : {salary}")
    
    employee_count+=1

def show_count():
    line()
    print(f"Employee count : {employee_count}")
    line()

employee=int(input("Enter number of employees : "))
for i in range(employee):
    print(f"Employee {i+1}")
    name=input("Enter name of employee  :")
    salary=int(input("Enter salary of employee : "))
    print()
    add_employee(name,salary)
    print()

show_count()