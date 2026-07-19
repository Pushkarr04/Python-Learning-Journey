name=input("Enter username : ")
pattern=int(input("choose pattern : "))

# 1. Solid Square
# 2. Right Triangle
# 3. Inverted Triangle
# 4. Right Aligned Triangle
# 5. Number Triangle
# 6. Repeated Number Triangle
# 7. Floyd's Triangle
# 8. Hollow right Triangle
# 9. Butterfly Pattern

size=int(input("Enter size of pattern : "))
print("="*30)
print("   PATTERN GENERATOR")
print("="*30)
print(f"username : {name}\n")

if(pattern==1):
    print("1.Solid Square\n")
    for i in range(1,size+1):
        for j in range(1,size+1):
            print("* ",end="")
        print()

elif(pattern==2):
    print("2.Right triangle")
    for i in range(1,size+1):
        for j in range(1,i+1):
            print("* ",end="")
        print()

elif(pattern==3):
    print("3.Inverted triangle")
    for i in range(1,size+1):
        for j in range(size+1,i,-1):
            print("* ",end="")
        print()

elif(pattern==4):
    print("4.Right Aligned triangle")
    for i in range(1,size+1):
        for j in range(size,i,-1):
            print("  ",end="")
        for j in range (0,i):
              print("* ",end="")
        print()

elif(pattern==5):
    print("5.Number triangle")
    for i in range(1,size+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
elif(pattern==6):
    print("6.Repeated number triangle")
    for i in range(1,size+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()

elif(pattern==7):
    print("7.Floyds triangle")
    num=1
    for i in range(1,size+1):
        for j in range(1,i+1):
            print(num,end=" ")
            num+=1
        print()
elif(pattern==8):
    print("8.Hollow Right Triangle")
    for i in range(1,size+1):
        for j in range(1,i+1):
            if(i==j or i==size or j==1):
                print("*",end="")
            else:    
                print(" ",end="")
        print()
elif(pattern==9):
    print("9.Butterfly Pattern")
    for i in range(1,size+1):
        for j in range(1,i+1):
            print("*",end="")
        

        for j in range(1,2*(size-i)+1):
              print(" ",end="")
        

        for j in range(0,i):
              print("*",end="")

        print()
    for i in range(1,size+1):
        for j in range(size,i,-1):
            print("*",end="")
        
    
        for j in range(2*i,0,-1):
            print(" ",end="")
        
        
        for j in range(size-i+1,1,-1):
            print("*",end="")
        print()    
else:
    print("Invalid pattern number!")