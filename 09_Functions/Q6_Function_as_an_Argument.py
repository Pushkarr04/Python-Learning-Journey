def line():
    print("="*30)
def heading(title="marks analytics"):
    line()
    print(title.upper())
    line()
    
def calculate_total(marks):
    total=sum(marks)
    return total

def calculate_avg(marks):
    average=calculate_total(marks)/len(marks)
    return average

def find_highest(marks):
    highest=max(marks)
    return highest

def find_lowest(marks):
    lowest=min(marks)
    return lowest

def process_marks(marks,operations):
    return operations(marks)
    

def report(username,marks,total,average,highest,lowest):
    heading(title="marks analytics report")
    print(f"Username : {username}\n")
    print(f"marks : {marks}\n")

    print(f"total : {total:.2f}")
    print(f"average : {average:.2f}")
    print(f"highest  : {highest:.2f}")
    print(f"lowest : {lowest:.2f}")


username=input("Enter username : ")
subjects=int(input("Enetr number of subjects : "))

marks=[]
for i in range (subjects):
    mark=int(input(f"Enter mark of subject {i+1} : "))
    if 0<=mark<=100:
        marks.append(mark)
    else:
        print("invalid input!")
        exit()

total=process_marks(marks,calculate_total)
average=process_marks(marks,calculate_avg)
highest=process_marks(marks,find_highest)
lowest=process_marks(marks,find_lowest)


report(username,marks,total,average,highest,lowest)



