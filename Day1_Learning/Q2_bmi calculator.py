name=input("name: ")
height=float(input("height : "))
weight=int(input("weight : "))

bmi=(weight/(height*height))
print("hello",name)
print(f"your BMI is: {bmi:.2f}")

if BMI<18.5:
    print("category : underweight")
elif BMI<25:
    print("category : normal weight")    
elif BMI<30:
    print("category : overweight")  
else:
    print("category : obese")      