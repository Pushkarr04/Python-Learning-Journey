mark1=int(input("Enter marks of student 1 : "))
mark2=int(input("Enter marks of student 2 : "))

print("="*30)
print("STUDENT MARKS COMPARISON")
print("="*30)
print(f"\nStudent 1 marks : {mark1}")
print(f"Student 2 marks : {mark2}\n")
print("Student 1 > student 2 : ",mark1>mark2)
print("Studernt 1 < student 2 : ",mark1<mark2)
print("Marks equal            : ",mark1==mark2)
print("Marks different        : ",mark1!=mark2)

print("\nStudent 1 passed       : ",mark1>=35)
print("Student 2 passed       : ",mark2>=35)

if mark1>mark2:
    print("\nDifference       : ",mark1-mark2,"\n")
else:
    print("\nDifference       : ",mark2-mark1,"\n")

print("="*30)








