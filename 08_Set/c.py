skills={"python","java","excel","powerbi","sql","python","pandas","excel","AIML"}
print(type(skills))
print(skills)
print(len(skills))
x=set((sorted(skills)))
print(x,type(x))



longest=max(skills,key=len)
shortest=min(skills,key=len)

print("longest and shortest ",longest,shortest)



start_p=0
contain_AI=0
total_len=0
for skill in skills:
    if skill.startswith("p"):
        print(f"Skills start with p : ",skill)

    if "AI" in skill :
        print("Skills containing AI : ",skill)


    total_len+=len(skill)

average =total_len/len(skills)