username=input("Enter username : ")
number=int(input("How many students ? : "))



names=[]
marks=[]
for i in range(number):
    name=input(f"Enter name of student {i} : ")
    mark=int(input(f"Enter marks of student {i} : "))
    if name.replace(" ","").isalpha() and 0<=mark<=100:
        names.append(name)
        marks.append(mark)
    else:
        print("Invalid input!")
    

while True:

    print("="*30)
    print("STUDENTS MARKS ANALYSIS")
    print("="*30)    

    print("\n1.Show all students ")
    print("2.Search student")
    print("3.Update marks")
    print("4.Remove students")
    print("5.Student statistics")
    print("6.Exit")    

    choice=int(input("Enter choice : "))

    if(choice==6):
        print("Thank You For Using Student Marks Analytics System")
        break
    elif(choice==1):
        print("="*5)
        print("STUDENT LIST")
        print("="*5)

        for i in range(len(names)):
            print(names[i],"    ",marks[i])
    elif(choice==2):
        print("SEARCH STUDENT \n")
        search=input("Enter a name to search : ")
        search = search.lower()
        found=False
        for i in range(len(names)):
            if names[i].lower() == search:
                print("Student Found")
                print(names[i], marks[i])
                found=True
                
        if not found:
            print("Student not found")
    elif(choice==3):
        search=input("Enter student matrks  : ")
        new_mark=int(input("Enter new marks for updation : "))
           
        if search in names:
            found_at=names.index(search)
            if 0<=new_mark<=100:
                marks[found_at]=new_mark
                print("Marks updated succesfully!")
            else:
                print("Invalid marks")
        else:
            print("student not found")
    elif(choice==4):
        remove=input("Enter student name to remove : ")
        
        if remove in names:
            found_at=names.index(remove)
            names.pop(found_at)
            marks.pop(found_at)
            print("Student removed succesfully!")
        else:
            print("Student not found!")
    elif(choice==5):
        print("="*15)
        print("STUDENT ANALYTICS REPORT")
        print("="*15)

        print(f"username : {username}\n")
        print(f"Total students  :{len(names)}\n")
        if len(marks)==0:
            print("Student not found")
            continue
        else:
            highest_marks=max(marks)
            lowest_marks=min(marks)
        highest_scorer=names[marks.index(highest_marks)]
        lowest_scorer=names[marks.index(lowest_marks)]

        print(f"Highest marks : {highest_marks}")
        print(f"Highest scorer : {highest_scorer}\n")

        print(f"Lowest marks : {lowest_marks}")
        print(f"Lowest scorer : {lowest_scorer}\n")

        average_marks=sum(marks)/len(marks)
        print(f"Average marks : {average_marks}\n")

        total_passed=0
        total_failed=0
        for mark in marks : 
            
            if mark >=40:
                total_passed+=1
            else:
                total_failed+=1

        print(f"Total passed : {total_passed}")
        print(f"Total field : {total_failed}\n")

        above_average=0
        below_average=0
        for mark in marks:
            
            if mark>=average_marks:
                above_average+=1
            else:
                below_average+=1

        print(f"Students above average : {above_average}")
        print(f"Students below average : {below_average}\n")

        print("="*15)

    else:
        print("Invalid choice!")














    