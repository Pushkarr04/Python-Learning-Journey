amount=float(input("Enter loan amount : "))
time_year=float(input("enter duration of loan(in year) : "))
rate=float(input("Enter rate of interest(annual) : "))

simple_interest=(amount*time_year*rate)/100
total_amount=simple_interest+amount
monthly_emi=total_amount/(time_year*12)
total_months=time_year*12
remaining_amount=total_amount-monthly_emi

print("="*30)
print("LOAN EMI CALCULATOR")
print("="*30)

print(f"\nLoan amount      : {amount:.2f}")
print(f"Loan duration    : {time_year:.0f}year")
print(f"Rate of interest : {rate}%\n")


print(f"\nSimple interest  : {simple_interest:.2f}")
print(f"Total amount     : {total_amount:.2f}")
print(f"Total months     : {total_months}")
print(f"Monthly EMI      : {monthly_emi:.2f}")
print(f"Remaining amount : {remaining_amount:.2f}\n")

print("="*30)


