username=input("Enter username : ")
number=int(input("how mnay skills? : "))
skills=set()
i=1
while i<=number:
    skill=input("Enetr skill : ").lower()
    skills.add(skill)
    i+=1

print(skills)

new_skill=input("Enter skill :").lower()
if new_skill in skills:
    print("skill already exist")
else:
    skills.add(new_skill)
    print("Skill added succesfully")

remove=input("Enter skill to remove ").lower()
if remove in skills:
   skills.discard(remove)
   print("Skill removed succesfully")
else:
    print("Skill not exist")

print("Skills analytics")

print(f"total unique skills : {len(skills)}")
print(f"Alphabetically sorted : {sorted(skills)}")


if len(skills)==0:
    print("no skills available")
else:
    longest=max(skills,key=len)
    shortest=min(skills,key=len)
    

print(f"Longest skill : {longest}")
print(f"Shortest skill : {shortest}")

start_p=0
contain_AI=0
total_len=0
for skill in skills:
    if skill.lower().startswith("p"):
        start_p+=1
        print(f"Skills start with p : ",skill)

    if "ai" in skill.lower() :
        contain_AI+=1
        print("Skills containing AI : ",skill)


    total_len+=len(skill)

print(f"TOtal skill start with p : {start_p}")
print(f"total skill contain ai : {contain_AI}")
average =total_len/len(skills)

print(f"Average : {average}")