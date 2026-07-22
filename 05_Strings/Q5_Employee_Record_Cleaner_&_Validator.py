username=input("enter username : ")
record=input("Enter Employee record : ")

total_character=0
space_count=0
digit_count=0
vowel_count=0
consonant_count=0
sp_character_count=0


fields=record.split(",")

name=fields[0].strip()
department=fields[1].strip()
age=int(fields[2].strip())
salary=float(fields[3].strip())
city=fields[4].strip()

name=name.title()
department=department.upper()
city=city.title()

name_validity="valid"
for i in name: 
    if not(i.isalpha() or i==" "):
        name_validity="invalid"
        break
    

if 18<=age <=60:
    age_validity="valid"
else:
    age_validity="invalid"

if salary>0:
    salary_validity="valid"
else:
    salary_validity="invalid"

if department !="":
    department_validity="valid"
else:
    department_validity="invalid"
if city !="":
    city_validity="valid"
else:
    city_validity="invalid"


name_length=len(name)
words=name.split()
word_length=len(words)

first_name=words[0]
last_name=words[-1]
initials=""
for word in words:
    initials+=word[0].upper()

department_length=len(department)
start_with_DATA=department.upper().startswith("DATA")
end_with_ICS=department.upper().endswith("ICS")
analytics="ANALYTICS" in department.upper()

monthly_salary=salary
annual_salary=monthly_salary*12
daily_salary=monthly_salary/30

if monthly_salary>=100000:
    category="high income"
elif monthly_salary>=50000:
    category="medium income"
else:
    category="low income"


longest=fields[0].strip()
shortest=fields[0].strip()

for field in fields:
    field=field.strip()
    if len(field)>len(longest):
         longest=field
    if len(field)<len(shortest):
         shortest=field

for field in fields:
    for ch in field:
        total_character+=1
        
        if ch.isalpha():
                
                if ch in "AEIOUaeiou":
                    vowel_count+=1
                else:
                    consonant_count+=1
        elif ch.isdigit():
                digit_count+=1
        elif(ch==" "):
            space_count+=1
        
        else:
                sp_character_count+=1

    






print("="*30)
print("EMPLOYEE RECORD ANALYZER")
print("="*30)

print(f"username : {username}")
print(f"original record : {record}")

print("-"*30)

print(f"\ncleaned record\n")

print(f"name : {name}")
print(f"department : {department}")
print(f"age : {age}")
print(f"SALARY : {salary:.2f}")
print(f"city  : {city}")

print("-"*30)

print("\nVALIDATION\n")
print(f"name : {name_validity}")
print(f"age : {age_validity}")
print(f"salary : {salary_validity}")
print(f"department : {department_validity}")
print(f"city : {city_validity}")


print("-"*30)

print("\nNAME ANALYSIS\n")

print(f"lenght : {name_length}")
print(f"words : {word_length}")
print(f"first name : {first_name}")
print(f"last name : {last_name}")
print(f"initialas : {initials}")

print("-"*30)

print("\nDEPARTMENT ANALYSIS\n")

print(f"lenght : {department_length}")
print(f"starts with DATA : {start_with_DATA}")
print(f"end with ICS : {end_with_ICS}")
print(f"contains analysis : {analytics}")


print("-"*30)
print(f"\nSalary Analysis\n")

print(f"monthaly salary  : {monthly_salary:.2f}")
print(f"annual salary : {annual_salary:.2f}")
print(f"daily salray  : {daily_salary:.2f}")

print(f"\ncategorty : {category}")


print("-"*30)

print("\nANALYTICS SUMMARY\n")

print(f"longest field  : {longest}")
print(f"shortest field : {shortest}")

print(f"characters  :{total_character}")
print(f"vowels : {vowel_count}")
print(f"consonant : {consonant_count}")
print(f"digit : {digit_count}")
print(f"spaces  : {space_count}")
print(f"special character : {sp_character_count}")

print("="*30)
    