def display_profile(**details):
    for key,value in details.items():
        print(key,":",value)

def line():
    print("="*30)
def heading():
    line()
    print("EMPLOYEE PROFILE GENERATOR")
    line()
def report(username,**details):
    heading()
    print(f"Username : {username}")

    display_profile(**details)

    line()

username=input("Enter username: ")
name=input("Enter employee name : ")
department=input("Enter employee department  :")
salary=float(input("Enter employee salary : "))
city=input("Enter employee city : ")
experience=int(input("Enter experience"))

if name.replace(" ","").lower().isalpha() and department!="" and salary>0 and city!="" and experience>=0:
    details={
        "employee_name":name,
        "department":department,
        "salary":salary,
        "city":city,
        "Experince":experience
    } 
else:
    print("Invalid input!")
    exit()   

display_profile(**details)
report(username,**details)
