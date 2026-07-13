name=input("Enter student name : ")
roll_no =input("Enter Roll No. : ")
subjects=int(input("Enter number of subjets : "))

total_marks=0
maximum=0
minimum=0
result="PASS"
valid=True


if(subjects>0):
    for i in range(1,subjects+1):
        marks=int(input(f"enter marks of subject {i}: "))
        if(marks>=0 and marks <=100):
            if(marks <35):
                result="FAIL"
        
            if i==1:
                minimum=marks
                maximum=marks
            total_marks=total_marks+marks
            if(marks>maximum):
                maximum=marks
            if(marks<minimum):
                minimum=marks
        else:
            print("Invalid marks!")
            valid=False
            break
        
            
    
    if valid:
        print("="*30)
        print("STUDENTS MARKS SUMMARY ")
        print("="*30)
        print(f"Student name : {name}")
        print(f"Roll NO. : {roll_no}\n")
    
        print(f"Subjects : {subjects}")
    
        average=total_marks/subjects
        percentage=(total_marks/(subjects*100))*100
        print(f"Total marks : {total_marks}")
        print(f"Average of marks : {average}")
        print(f"Highest marks : {maximum}")
        print(f"Lowest marks : {minimum}")
        print(f"Percentage : {percentage}\n")
    
        print(f"Result : {result}")
else:
    print("Invalid input!")

print("="*30)
        


