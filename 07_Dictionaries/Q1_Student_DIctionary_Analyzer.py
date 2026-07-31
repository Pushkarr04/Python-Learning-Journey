username=input("Enter username : ")
name=input("enter student name : ")
age=int(input("Enter student age : "))
branch=input("Enter student branch: ")
cgpa=float(input("Enter student cgpa : "))
city =input("Enter student city : ")


print("="*30)
print("STUDENT DICTIONARY ANALYZER")
print("="*30)

print(f"username : {username}\n")


      

student={
    "name":name,
    "age": age,
    "branch":branch,
    "cgpa":cgpa,
    "city":city
    }
print(f"Original dictionary : {student}\n")

print("-"*10)
print("\nSTUDENT DETAILS\n")


print("name : ",student.get("name"))
print("branch : ",student.get("branch"))
print("cgpa : ",student.get("cgpa"))

print("-"*10)
print("\nUPDATED DICTIONARY\n")


student["cgpa"]=9.0
print(student)

student.update({"status":"pass"})
print(student)

student.pop("city")
print(student)

print("-"*10)
print("\nMETHODS\n")
print(student.keys())
print(student.values())
print(student.items())


print("-"*10)
print("\nMEMBERSHIP CHECK\n")
found="branch" in student

print("branch key exist : ",found)



print("phone : ",student.get("phone"))


print("-"*10)

for key,value in student.items():
    print(f"{key}:{value}")