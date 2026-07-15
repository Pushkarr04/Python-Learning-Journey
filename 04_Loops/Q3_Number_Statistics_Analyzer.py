name=input("Enter username : ")
number=int(input("Number of values : "))
total_sum=0
maximum=0
minimum=0
even=0
odd=0
positive=0
negative=0
zeros=0

if(number>0):
    for i in range(1,number+1):
        value=int(input("Enter value : "))
        total_sum+=value
        if i==1:
            maximum=value
            minimum=value
        if(value>maximum):
            maximum=value
        if(value<minimum):
            minimum=value
        if value>0:
            positive+=1
        if value<0:
            negative+=1
        if value==0:
            zeros+=1
        if value%2==0:
            even+=1
        if value%2!=0:
            odd+=1
        
    average=total_sum/number
    print("="*30)
    print("NUMBER STATISTICS ANALYZER :  ")
    print("="*30)
    print(f"Username         : {name}\n")
    print(f"Numnbers entered : {number}\n")

    print(f"Total sum        : {total_sum}")
    print(f"Average          : {average}\n")

    print(f"Highest number   : {maximum}")
    print(f"Lowest number    : {minimum}\n")

    print(f"Positive numbers : {positive}")
    print(f"Negative numbers : {negative}")
    print(f"Zeros : {zeros}\n")

    print(f"Even numbers     : {even}")
    print(f"Odd numbers      : {odd}\n")

    print("="*30)

else:
    print("Invalid input!")









