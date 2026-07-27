employees = (
    ("Rahul", "Data Analyst", 50000, "Delhi"),
    ("Neha", "Data Scientist", 70000, "Mumbai"),
    ("Amit", "Data Analyst", 55000, "Pune"),
    ("Riya", "Business Analyst", 60000, "Delhi"),
    ("Karan", "Data Engineer", 75000, "Bangalore")
)




for employee in employees:
    print(employee[0])
    

for i,(name,department,salary,city)in enumerate(employees,start=1):
    print("="*10)
    print(f"Employee {i}")
    print("="*10)

    print(f"name : {name}")
    print(f"department : {department}")
    print(f"salary : {salary}")
    print(f"city : {city}\n")
    print()
total_salary=0
highest_salary=0
minimum_salary=0
highest_paid_employee=""
lowest_paid_employee=""



for i ,(name,department,salary,city) in enumerate(employees,start=1):
    total_salary+=salary
    if i==1:
        highest_salary=salary
        highest_paid_employee=name
        minimum_salary=salary
        lowest_paid_employee=name
    elif(salary>highest_salary):
        highest_salary=salary
        highest_paid_employee=name
    elif(minimum_salary>salary):
        minimum_salary=salary
        lowest_paid_employee=name

print("Total salary : ",total_salary)
average_salary=total_salary/len(employees)
print("Average salary : ",average_salary)
print("Highest salary : ",highest_salary)
print(f"Minimum salary: {minimum_salary}\n")

print("Highest paid employee")
print("-"*15)

print(f"Name : ",highest_paid_employee)
print(f"Salary : {highest_salary}\n")
da_count=0
ds_count=0
ba_count=0
de_count=0
print("DEPARTMENT ANALYSIS")
for i ,(name,department,salary,city) in enumerate(employees,start=1):
    if department.lower()=="data analyst":
        da_count+=1
    elif department.lower()=="data scientist":
        ds_count+=1
    elif department.lower()=="buSIness analyst":
        ba_count+=1
    elif department.lower()=="data engineer":
        de_count+=1

print(f"Data analyst : {da_count}")
print(f"Data science : {ds_count}")
print(f"Business analyst : {ba_count}")
print(f"Data Engineer  :{de_count}\n")

print("Employee from delhi")
print("-"*15)

for i ,(name,department,salary,city) in enumerate(employees,start=1):
    if city=="Delhi":
        print(name)

# print()
new_tuple=()

print("Employee name tuples")
print("-"*15)
new_tuple=list(new_tuple)
for employee in employees:
    new_tuple.append(employee[0])
new_tuple=tuple(new_tuple)
print(new_tuple)

new_tuple=list(new_tuple)
new_tuple.append("pushkar")
new_tuple=tuple(new_tuple)
print(f"updated tuple : {new_tuple}")

found=False
for name in new_tuple:
    if  name.lower()=="neha":
        print("Employee found")
        found=True
if not found:
    print("Employee not found")






