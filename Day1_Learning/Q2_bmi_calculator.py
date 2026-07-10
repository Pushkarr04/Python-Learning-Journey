name=input("name: ")
height=float(input("height : "))
weight=int(input("weight : "))

bmi=(weight/(height*height))
print("hello",name)
print(f"your BMI is: {bmi:.2f}")

if bmi<18.5:
    print("category : underweight")
elif bmi<25:
    print("category : normal weight")    
elif bmi<30:
    print("category : overweight")  
else:
    print("category : obese")      