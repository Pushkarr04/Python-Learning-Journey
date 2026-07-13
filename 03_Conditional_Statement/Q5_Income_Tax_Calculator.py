name=input("Enter employee name : ")
id=input("Enter Employee ID : ")
salary=float(input("Enter annual salary : "))
experience=float(input("Enter experience of work (year : )"))
rating=int(input("Enter experience rating : "))
perfomance_bonus=0
experience_bonus=0
tax=0
tax_percentage=0

print("="*30)
print("EMPLOYEE TAX REPORT")
print("="*30)
print(f"\nEmployee name : {name}")
print(f"Employee id   : {id}\n")

if(salary<0 or experience<0 or rating <1 or rating>5):
    print("Invalid input!")
else:
    print(f"Annual salary     : {salary:.2f}")
    print(f"Experience        : {experience}")
    print(f"Perfomance rating : {rating}\n")
    if(rating==5):
        perfomance_bonus=salary*20/100
    elif(rating==4):
        perfomance_bonus=salary*15/100
    elif(rating==3):
        perfomance_bonus=salary*10/100
    elif(rating==2):
        perfomance_bonus=salary*5/100
    else:
        perfomance_bonus=salary*0/100
    print(f"Perfomance bonus : {perfomance_bonus:.2f}")

    if(experience>=10):
        experience_bonus=50000
    elif(experience>=5):
        experience_bonus=25000
    else:
        experience_bonus=0
    print(f"Experience bonus : {experience_bonus:.2f}\n")

    gross_salary=salary+perfomance_bonus+experience_bonus
    print(f"Gross salary : {gross_salary:.2f}\n")

    if(gross_salary<=500000):
        tax_percentage=0
        tax=gross_salary*tax_percentage/100
    elif(gross_salary <=1000000):
        tax_percentage=10
        tax=gross_salary*tax_percentage/100
    elif(gross_salary<=2000000):
        tax_percentage=20
        tax=gross_salary*tax_percentage/100
    else:
        tax_percentage=30
        tax=gross_salary*tax_percentage/100
    print(f"Tax percentage : {tax_percentage}")
    print(f"Tax amount : {tax:.2f}\n")
    net_salary=gross_salary-tax

    print(f"Net salary : {net_salary:.2f}\n")

print("="*30)

    
    
    