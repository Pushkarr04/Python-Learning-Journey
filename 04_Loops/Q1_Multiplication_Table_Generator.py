name=input("Enter username : ")
number=int(input("Enter number : "))
start_multiplier=int(input("Enter start multiplier : "))
end_multiplier=int(input("Enter end multiplier : "))

print("="*30)
print("MULTIPLICATION TABLE GENERATOR")
print("="*30)
print(f"Username : {name}")

if(number>0 and start_multiplier>0 and end_multiplier>0 and start_multiplier<=end_multiplier):
    print(f"Number : {number}")
    for i in range(start_multiplier,end_multiplier+1):
        print(number,"*",i,"=",number*i,end="\n")
    
else:
    print("Invalid input!")

print("="*30)

