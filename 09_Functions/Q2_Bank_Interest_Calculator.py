def calc_interest(principle,rate=7.5,year=1):
    interest=(principle*rate*year)/100
    return interest

def calc_amount(principle,interest):
    total_amount=principle+interest
    return total_amount

def line():
    print("="*30)

def heading():
    line()
    print("INTEREST CALCULATOR")
    line()

def report(username,name,principle,rate,year,interest,total_amount):
    heading()
    print(f"Username : {username}")
    print(f"Name : {name}")
    print(f"Principle amount : {principle}")

    

    print(f"Interest rate : {rate}")
    print(f"years : {year}")

    print(f"Interest : {interest}")
    print(f"Final Amount : {total_amount}")

    line()

username=input("Enter username : ") 
name=input("Enter customer name : ")
principle=float(input("Enter principle amount : "))
if principle<=0:
    print("invalid principle amount!")
    exit()
print("1. Use default interest rate ")
print("2. Enter Custom interest rate ")

choice=int(input("Choose option 1 or 2 : "))

if choice ==1:
    rate=7.5
    year=1
    interest=calc_interest(principle)
elif choice==2:
    rate=float(input("Enter custom interest rate : "))
    year=int(input("Enter custom year for interest : "))

    if rate>0 and year>0:
        interest=calc_interest(principle,rate,year)
    else:
        print("invalid input")
        exit()
else:
    print("Invalid choice!")
    exit()


total_amount=calc_amount(principle,interest)
report(username,name,principle,rate,year,interest,total_amount)

