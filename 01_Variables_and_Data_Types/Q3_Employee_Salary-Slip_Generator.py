e_name=input("Employee name: ")
e_id=input("Employee id :")
department=input("Department :")
salary=float(input("Basic Salary :"))
hra=salary*20/100
da=salary*10/100
tax=salary*5/100
gross_salary=salary+hra+da
net_salary=gross_salary-tax
print("="*30)
print("EMPLOYEE SALARY SLIP")
print("="*30)
print(f"Employee name:{e_name}")
print(f"Employee ID  :{e_id}")
print(f"department   :{department}")
print(f"Basic salary :{salary}")
print(f"HRA(20%)     : {hra}")
print(f"da(10%)      : {da}")
print(f"tax(5%)      : {tax}")
print(f"Gross salary : {gross_salary}")
print(f"Net salary   : {net_salary}")
print("="*30)






