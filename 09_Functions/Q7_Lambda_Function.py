annual=lambda salary:salary*12

tax=lambda salary:salary*0.1

net_salary=lambda salary,tax: salary-tax

def line():
    print("="*30)
def heading(title=""):
    line()
    print(title.upper())
    line()

def process_salary(salary,operations):
    return operations(salary)

def display(username,employees,salaries,annual_salaries,tax_amounts,net_salary_amounts):
    heading()

    print(f"username : {username}\n")
    for i  in range((len(salaries))):
    
        print(f"employee name  : {employees[i]}")
        print(f"monthly salary : {salaries[i]:.2f}")
        print(f"annual salary  : {annual_salaries[i]:.2f}")
        print(f"tax            : {tax_amounts[i]:.2f}")
        print(f"net salary     :{net_salary_amounts[i]:.2f}")
        print()

    line()

username=input("enter username : ")
number=int(input("Enter number of employee : "))
salaries=[]
employees=[]
annual_salaries=[]
tax_amounts=[]
net_salary_amounts=[]
for i in range(number):

    print(f"employee {i+1}: ")
    employee=input("Enter name of employee : ")
    salary=int(input("Enter salary  : "))
    employees.append(employee)
    salaries.append(salary)

for i in range(len(salaries)):
    annual_salary=process_salary(salaries[i],annual)
    tax_amount=process_salary(salaries[i],tax)
    net_salary_amount=net_salary(salaries[i],tax_amount)
    annual_salaries.append(annual_salary)
    tax_amounts.append(tax_amount)
    net_salary_amounts.append(net_salary_amount)
    
display(username,employees,salaries,annual_salaries,tax_amounts,net_salary_amounts)
