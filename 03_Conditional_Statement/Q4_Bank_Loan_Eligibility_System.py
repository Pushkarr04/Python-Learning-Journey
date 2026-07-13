name=input("Enter applicant name : ")
age =int(input("Enter applicant age : "))
salary=float(input("Enter applicant monthaly salary : "))
cibil=int(input("Enter applicant CIBIL score :")) 
existing_loan=float(input("Enter existing loan amount : "))

print("="*30)
print("BANK LOAN ELIGIBILTY REPORT")
print("="*30)
print(f"Applicant name      : {name}")

if(age<18 or salary<0 or cibil<300 or cibil>900 or existing_loan<0):
    print("Invalid input!")
else:
    if(age<21):
        loan_status="rejected"
        reason="minimum age should be greater than 21 year"
    elif(salary<25000):
        loan_status="rejected"
        reason="monthly salary should be more than 25000"
    elif(cibil<700):
        loan_status="rejected"
        reason="low cibil score"
    elif(existing_loan>500000):
        loan_status="rejected"
        reason="existing loan amount too high"
    else:
        loan_status="approved"
        reason="you passed all the eligibilty criteria"
    
    if(loan_status=="approved"):
        print(f"Age                 : {age}")
        print(f"Monthaly salary     : {salary}")
        print(f"CIBIL score         : {cibil}")
        print(f"Existing loan       : {existing_loan}")
        print(f"Loan status         : {loan_status}")
        
    else:
        print(f"Loan status         : {loan_status}")
        print(f"Reason              : {reason}")
    

    if(loan_status=="approved"):
        if(salary >=25000 and salary<=49999):
            maximum_loan=500000
        elif(salary>=50000 and salary <=74999):
            maximum_loan=1000000
        elif(salary>=75000 and salary<=99999):
            maximum_loan=1500000
        else:
            maximum_loan=2000000
        print(f"MAximum loan Amount : {maximum_loan}")


print("="*30)