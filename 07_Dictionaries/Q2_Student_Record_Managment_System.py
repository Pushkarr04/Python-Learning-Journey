username=input("Enter username  : ")
number=int(input("Enetr how many students? : "))
students={}
i=1
while i<=number:
    roll_no=int(input("Enmter roll no.  : "))

    if roll_no in students:
        print("roll no. already exist ! please enter unique roll no.")
        continue

    name=input("Enter student name : ")
    marks=int(input("Enter marks : "))
    branch=input("Enter Branch : ")

    if name.replace(" ","").isalpha() and 0<=marks<=100 and branch !="":
        students.update({
                roll_no:{
                    "name":name,
                    "marks":marks,
                    "branch":branch
                },
                })

    else:
        print("invalid input!")
        break

    
    print("-"*10)
    
    i+=1
    
print(students)


while True:
    print("="*30)
    print("STUDENT RECORD MANAGMENT ")
    print("="*30)
    print("1. Show all student ")
    print("2. Search student ")
    print("3. Update marks")
    print("4. Delete student")
    print("5. Student analytics")
    print("6. Exit")

    choice=int(input("Enter your choicer from above menu : "))

    if(choice==6):
        print("Thank you!")
        break
    elif(choice==1):
        for roll_no,details in students.items():
            print(f"Roll_no : {roll_no}")
            print(f"Name : {details['name']}")
            print(f"Marks : {details['marks']}")
            print(f"Branch : {details['branch']}")
            print("-"*10)

    elif(choice==2):
        search=int(input("enter roll no. to search : "))
        found=False

        for roll_no,details in students.items():
            if search==roll_no:
                print("Student found \n")

                print(f"Name  : {details['name']}")
                print(f"Marks : {details['marks']}")
                print(f"Branch : {details['branch']}")

                found=True
        if not found:
            print("Student not found!")

    elif(choice==3):
        search=int(input("Enter roll no. to update details : "))
        found=False

        
        if search in students:
            new_marks=int(input("enter new marks to update : "))
            if 0<= new_marks<=100:
                students[search]["marks"]=new_marks
            else:
                print("invalid new marks")
                
            found=True
        if not found:
            print("roll no. is not available ")
            

    elif(choice==4):
        delete=int(input("enter roll no. to delete student details : "))
        if delete in students:
            students.pop(delete)
            print("student deleted succesfully!")
        else:
            print("Student not found")

    elif(choice==5):
        print("="*30)
        print("STUDENT ANALYZER")
        print("="*30)

        print(f"Username : {username}\n")
        print(f"Total students : {len(students)}\n")
        highest_scorer=""
        highest_marks=0
        lowest_scorer=""
        lowest_marks=0
        passed=0
        failed=0
        total_marks=0
        for roll_no,details in students.items():
            total_marks+=details["marks"]
        if len(students)==0:
            average=0
        else:
            average=total_marks/len(students)

        for i,( roll_no,details) in enumerate(students.items(),start=1):
            
            if i==1:
                highest_scorer=details["name"]
                highest_marks=details["marks"]
                lowest_scorer=details["name"]
                lowest_marks=details["marks"]
            elif(details["marks"]>highest_marks):
                highest_scorer=details["name"]
                highest_marks=details["marks"]
            elif(details["marks"]<lowest_marks):
                lowest_scorer=details["name"]
                lowest_marks=details["marks"]

            if (details["marks"]>=40):
                passed+=1
            else:
                failed+=1
            

        print(f"Highest scorer : {highest_scorer}")
        print(f"Highest marks  : {highest_marks}\n")

        print(f"Lowest scorer : {lowest_scorer}")
        print(f"Lowest marks : {lowest_marks}\n")

        print(f"average : {average}\n")
        print(f"Passed student : {passed}")
        print(f"Failed student : {failed}")

            
            
                




            

            




