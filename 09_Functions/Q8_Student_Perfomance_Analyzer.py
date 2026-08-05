def line():
    print("="*30)

def heading(title="Student perfomance"):
    line()
    print(title.upper())
    line()

def calc_marks(*marks):
    total=sum(marks)
    average=total/len(marks)
    highest=max(marks)
    lowest=min(marks)
    passed=0
    failed=0
    for mark in marks:
        if mark>=40:
            passed+=1
        else:
            failed+=1

    return total,average,highest,lowest,passed,failed
def calc_grade(average,):
    
    if average>90:
        grade="A+"
    elif average>80:
        grade="A"
    elif average>70:
        grade="B"
    elif average>60:
        grade="C"
    elif average>50:
        grade="D"
    elif average>40:
        grade="E"
    else:
        grade="F"
    
    return grade

def calc_percentage(total,subjects):
    percentage=total/(subjects*100)*100
    return percentage

def student_status(average,failed):
    if failed>0:
        return "Fail"
    else:
        if average>=75:
            return "DISTINCTION"
        elif average>=60:
            return "FIRST DIVISON"
        elif average>=50:
            return "SECOND DIVISON"
        else:
            return "PASS"


def student_profile(**details):
    for key,value in details.items():
        print(key,":",value)
def report (username,total,average,percentage,highest,lowest,passed,failed,grade,status,marks,**details,):
    heading("student perfomance report")
    print(f"username: {username}")

    student_profile(**details)
    print(f"marks : {marks}")

    print(f"Total : {total}")
    print(f"Average : {average}")
    print(f"percentage : {percentage}%")
    print(f"Highest : {highest}")
    print(f"Lowest : {lowest}\n")

    print(f"Pass : {passed}")
    print(f"failed : {failed}\n")

    print(f"Grade : {grade}")
    print(f"Status : {status}")

username=input("Enter username : ")
subjects=int(input("Enter how many subjects : "))
marks=[]

if subjects>0:
    for i in range(subjects):
        mark=int(input(f"Enetr mark of subject {i+1} : "))
        if 0<=mark<=100:
            marks.append(mark)
        else:
            print("Invalid input!")
            exit()
        
else:
    print("Invalid subjects input!")
    exit()
name=input("Enter student name : ")
branch=input("Enter branch  :")
city=input("Enter city of student : ")
semester=int(input("Enetr semester of student"))


details={
    "Student name":name,
    "Branch":branch,
    "City":city,
    "semester":semester
}

total,average,highest,lowest,passed,failed=calc_marks(*marks)
grade=calc_grade(average)
percentage=calc_percentage(total,subjects)
status=student_status(average,failed)
report(username,total,average,percentage,highest,lowest,passed,failed,grade,status,marks,**details)











