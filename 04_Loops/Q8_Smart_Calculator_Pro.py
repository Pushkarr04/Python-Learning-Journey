name=input("enter your name : ")

total_operations=0
addition_count=0
subtraction_count=0
multiplication_count=0
division_count=0
power_count=0
modulus_count=0
floor_division_count=0
total_result=0
largest_result=0
smallest_result=0
result=0
valid=True
valid_operation=0
average=0


while True:
    valid=True
    
    print("="*30)
    print("SMART CALCULATOR")
    print("="*30)

    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.divison")
    print("5.Power")
    print("6.Modulus")
    print("7.Floor divison")
    print("8.exit")    

    choice=int(input("Enter your choice : "))
    if(choice==8):
        break


    num1=float(input("Enter first number : "))
    num2=float(input("Enter second number : "))

    if(choice==1):
        result=num1+num2
        print(f"= {result}")
        addition_count+=1
        
    elif(choice==2):
        result=num1-num2
        print(f"= {result}")
        subtraction_count+=1
        
    elif(choice==3):       
        result=num1*num2
        print(f"= {result}")
        multiplication_count+=1
        
    elif(choice==4):
        if(num2!=0):
            result=num1/num2
            print(f"= {result}")
            division_count+=1
        else:
            valid=False
            print("invalid divison!")
        
    elif(choice==5):
        result=num1**num2
        print(f"= {result}")
        power_count+=1
        
    elif(choice==6):
        if(num2!=0):
            result=num1%num2
            print(f"= {result}")
            modulus_count+=1
        else:
            print("Invalid modulus")
            valid=False
        
    elif(choice==7):
        if(num2!=0):
            result=num1//num2
            print(f"= {result}")
            floor_division_count+=1
        else:
            print("invalid floor divison!")
            valid=False
    else:
        print("Invalid choices!")
        continue

        
    if valid_operation==0:
        largest_result=result
        smallest_result=result
    if(result>largest_result):
        largest_result=result
    if(result<smallest_result):
        smallest_result=result
    if valid:
        total_operations+=1
        valid_operation+=1
        total_result+=result
        average=total_result/valid_operation

print("="*30)
print("CALCULATOR SUMMARY")
print("="*30)
print(f"username : {name}")

print(f"addition  : {addition_count}")
print(f"substraction : {subtraction_count}")
print(f"multiplication : {multiplication_count}")
print(f"divison : {division_count}")
print(f"power : {power_count}")
print(f"modulous : {modulus_count}")
print(f"floor divison : {floor_division_count}")
print(f"largest result : {largest_result}")
print(f"smallest result : {smallest_result}")

print(f"sum of result : {total_result}")
print(f"average : {average}")

print("THANK YOU FOR USING SMART CALCULATOR")

print("="*30)


    


