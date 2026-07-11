Customer_name=input("Enter customer name : ")
unit_consumed=int(input("Enter unit consumed :"))

print("="*30)
print("ELECTRICITY BILL")
print("="*30)

print(f"Customer name : {Customer_name}")
print(f"Unit Consumed : {unit_consumed}\n")

if(unit_consumed<=100):
    electricity_bill=unit_consumed*5
    print(f"Electricity bill : {electricity_bill:.2f}")

elif(unit_consumed<=200):
    electricity_bill=100*5+(unit_consumed-100)*7
    print(f"Electricity bill : {electricity_bill:.2f}")
else:
    electricity_bill=100*5+100*7+(unit_consumed-200)*10
    print(f"Electricity bill : {electricity_bill:.2f}")
tax=electricity_bill*5/100

final_bill=electricity_bill+tax
print(f"tax(5%)             : {tax:.2f}")
print(f"Final bill          : {final_bill:.2f}")