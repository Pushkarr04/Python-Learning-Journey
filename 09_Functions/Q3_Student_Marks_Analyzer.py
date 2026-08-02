def calc_result(*marks):
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

def line():
    print("="*30)
def heading ():
    line()
    print("MARKS ANALYZER")
    line()

def display_report(username,name,total,average,highest,lowest,passed,failed):
    heading()
    print(f"USername : {username}")
    print(f"Student name : {name}")
    print(f"total : {total}")
    print(f"average : {average}")
    print(f"highest : {highest}")
    print(f"lowest : {lowest}")
    print(f"Passes Subjects  :{passed}")
    print(f"Failed Subjects : {failed}")

    line()

username =input("Enter username : ")
name =input("Enter Student name : ")
subjects=int(input("Enter number of subjects : "))

if subjects<=0:
    print("Invalid input!")
    exit()

marks=[]
for i in range(subjects):
    mark=int(input(f"Enter mark of subject{i+1} : "))
    if 0<=mark<=100:
        marks.append(mark)
    else:
        print("Invalid marks!")
        exit()


total,average,highest,lowest,passed,failed=calc_result(*marks)

display_report(username,name,total,average,highest,lowest,passed,failed)