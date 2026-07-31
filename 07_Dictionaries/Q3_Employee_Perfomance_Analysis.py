username =input("enter username : ")
number=int(input("Enter how many employee? : "))

i=1
employee={}
while i<=number:
    emp_id=int(input("Enter employee id : "))

    

    emp_name=input("Enter employee name : ")
    emp_department=input("Enter employee department : ")
    emp_salary=float(input("Enter employhee salary : "))
    emp_rating=int(input("Enter experience (in year) : "))

    if emp_name.replace(" ","").isalpha() and emp_department !="" and emp_salary>0 and 1<=emp_rating<=5 and emp_id not in employee:
        employee[emp_id]={
            "name":emp_name,
            "department":emp_department,
            "salary":emp_salary,
            "rating":emp_rating
        }
    else:
        print("invalid input!")
        break
    i+=1

while True:

    print("="*30)
    print("EMPLOYEE PERFOMANCE ANALYSIS")
    print("="*30)
    print("1. Show all employee ")
    print("2. Search employee ")
    print("3. Update employee")
    print("4. Remove employee")
    print("5. Employee analysis")
    print("6. Dictionary method challange")
    print("7. Exit")

    choice=int(input("Enter your choice : "))
    if choice==7:
        print("Thank you ")
        break

    elif choice==1:
        for emp_id,details in employee.items():
            print(f"Employee id : {emp_id}")

            for key,value in details.items():
                print(key ,":", value)
            print()
    elif choice==2:
        search=int(input("Enter employee id to search : "))
        if search in employee:
            print("Employee id found in employees")
            for key,value in employee[search].items():
                print(key,":",value)

           
        else:
            print("Employee not found")
    elif choice==3:
        update=int(input("enter employee id for update : "))
        new_department=input("Enter new department")
        new_salary=float(input("Enter new salary"))
        new_rating=int(input("Enter new ratings"))

        found=False

    
        if update in employee:
            if new_salary>0 and 1<=new_rating<=5 and new_department !="":
                employee[update]["department"]=new_department
                employee[update]["salary"]=new_salary
                employee[update]["rating"]=new_rating
            else:
                print("invalid updation details!")

            found=True
                
        if not found:
            print("employee not available")

    elif choice==4:
        remove=int(input("Enter emp id to remove :  "))
        if remove in employee:
            employee.pop(remove)
            print("Employee removed succesfully")
        else:
            print("Employee not found")

    elif choice==5:
        total_emp=0
        highest_salary_emp=""
        highest_salary=0
        lowest_salary_emp=""
        lowest_salary=0
        total_salary=0
        highest_rated_emp=""
        highest_rating=0
        top_rating=0
        above_avg=0
        data_emp_count=0
        hr_emp_count=0
        other_emp_count=0

        if len(employee)!=0:
            for emp_id,details in employee.items():
                total_emp=len(employee)
                total_salary+=details["salary"]
            average=total_salary/total_emp  
            for i,(emp_id,details) in enumerate(employee.items(),start=1): 
                if i==1:
                    highest_salary_emp=details["name"]
                    highest_salary=details["salary"]
                    lowest_salary_emp=details["name"]
                    lowest_salary=details["salary"]
                    highest_rated_emp=details["name"]
                    highest_rating=details["rating"]
                elif(details["salary"]>highest_salary):
                    highest_salary_emp=details["name"]
                    highest_salary=details["salary"]
                elif(details["salary"]<lowest_salary):
                    lowest_salary_emp=details["name"]
                    lowest_salary=details["salary"]

                if(details["rating"]>highest_rating):
                    highest_rated_emp=details["name"]
                    highest_rating=details["rating"]
                if(details["rating"]>=4):
                    top_rating+=1
                if(details["salary"]>average):
                    above_avg+=1

                if(details["department"].lower()=="data"):
                    data_emp_count+=1
                elif(details["department"].lower()=="hr"):
                    hr_emp_count+=1
                else:
                    other_emp_count+=1
                    

            print(f"total employee : {total_emp}")
            print(f"Total salary : {total_salary}")
            print(f"average : {average}")
            print(f"highest salary employee : {highest_salary_emp}")
            print(f"highest salary  : {highest_salary}")
            print(f"lowest salary employee : {lowest_salary_emp}")
            print(f"lowest salary  : {lowest_salary}")
            print(f"highest rated employee : {highest_rated_emp}")
            print(f"highest rating  : {highest_rating}")
            print(f"rating >=4 : {top_rating}")
            print(f"salary above average : {above_avg}")
            print("-"*10)
            print("Department wise employee count\n")
            print(f"data : {data_emp_count}")
            print(f"Hr : {hr_emp_count}")
            print(f"other : {other_emp_count}")

        else:
            print("no employee available ")

    elif choice==6:
        backup=employee.copy()
        
        employee.clear()
        employee=backup.copy()
        employee[101].setdefault("age",20)
        backup.pop(103,None)
        backup.popitem()
        x=backup.get(101)
        current_keys=backup.keys()
        current_value=backup.values()
        current_item=backup.items()
        backup[102]["name"]="madhav"


