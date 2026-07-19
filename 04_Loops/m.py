size=5
num =1
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
            

        
        