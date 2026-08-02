def calc_salary(basic_salary):
    hra=basic_salary*20/100
    da=basic_salary*10/100
    gross_salary=basic_salary+hra+da

    return hra,da,gross_salary
    



def calc_tax(gross_salary):
    if gross_salary<300000:
        return gross_salary*0
    elif 300000<=gross_salary<=600000:
        return gross_salary*0.05
    else:
        return gross_salary*0.1

def calc_net_salary(gross_salary,tax):
    net_salary=gross_salary-tax
    return net_salary

def line():
    print("-"*30)

def heading():
    line()
    print("EMPLOYEE SALARY REPORT ")
    line()

def report(username,name,department,basic_salary,hra,da,gross_salary,tax,net_salary):
    heading()
    print(f"username     : {username}")
    print(f"name         : {name}")
    print(f"department   : {department}")
    print(f"Basic salary : {basic_salary}")

    print(f"HRA          : {hra:.2f}")
    print(f"DA           : {da:.2f}")
    print(f"Gross salary : {gross_salary:.2f}")
    print(f"Tax          : {tax:.2f}")
    print(f"Net salary   : {net_salary:.2f}")

    line()


username=input("enter username : ")
name =input("Enter employee name : ")
department=input("Enetr department : ")
basic_salary=float(input("enter basic salary : "))
if basic_salary<=0:
    print("invalid input!")
    exit()

hra,da,gross_salary=calc_salary(basic_salary)
tax=calc_tax(gross_salary)
net_salary=calc_net_salary(gross_salary,tax)

report(username,name,department,basic_salary,hra,da,gross_salary,tax,net_salary)
