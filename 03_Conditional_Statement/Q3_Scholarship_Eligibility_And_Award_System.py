name=input("enter Student name : ")
roll_no=input("Enter Student roll no. : ")
cgpa=float(input("Enter student CGPA(0-10) : "))
annual_income=float(input("Enter family annual income : "))
attendance=float(input("Enter student attendence percentage : "))

print("="*30)
print("SCHOLARSHIP ELIGIBILITY REPORT")
print("="*30)

print(f"\nStudent name  : {name}")
print(f"Roll NO.      : {roll_no}")

if((cgpa<0 or cgpa>10) or (attendance <0 or attendance >100) or(annual_income<0)):
    print("Invalid input! ")
else:
    if(attendance<75 ):
        eligibility="student is not eligible"
        reason="attendence is below 75%"

    elif(cgpa<7.5 ):
         eligibility="student is not eligible"
         reason="CGPA Below Required Criteria"
    

    else:
        eligibility="Eligible"
        print(f"\nAttendence    : {attendance}")
        print(f"CGPA          : {cgpa}")
        print(f"\nAnnual income : {annual_income}")


    print(f"Eligibility : {eligibility}")
    if(eligibility=="student is not eligible"):
        print(f"Reason : {reason}")
        
    
    if(eligibility=="Eligible"):
        
        if(cgpa>=9 and annual_income<=250000):
            scholarship=80000
        elif(cgpa>=8.5 and annual_income<=350000):
            scholarship=60000
        elif(cgpa>=8 and annual_income<=500000):
            scholarship=40000
        elif(cgpa>=7.5 and annual_income<=800000):
            scholarship=20000
        else:
            scholarship=0
    
        print(f"\nSholarship amount : {scholarship}")





print("="*30)
