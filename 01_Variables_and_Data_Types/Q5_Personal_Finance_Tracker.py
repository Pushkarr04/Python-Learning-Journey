name=input("Enter name : ")
monthly_salary=float(input("Enter monthly salary : "))
house_rent=float(input("Enter house rent : "))
food_expenses=float(input("Enter food expenses : "))
transport_expenses=float(input("Enter transport expenses : "))
entertainment_expenses=float(input("Enter entertainment expenses : "))
other_expenses=float(input("Enter other expenses : "))

total_expenses=house_rent + food_expenses + transport_expenses + entertainment_expenses + other_expenses
savings=monthly_salary-total_expenses
savings_percent=savings/monthly_salary*100

print("="*30)
print("PERSONAL FINANCE TRACKER")
print("="*30)

print(f"name : {name} ")
print(f"monthly salary        : {monthly_salary}")
print(f"house rent             : {house_rent}")
print(f"food expenses          : {food_expenses}")
print(f"transport expenses     : {transport_expenses}")
print(f"entertainment expenses : {entertainment_expenses}")
print(f"other_expenses         : {other_expenses}")

print(f"total expenses  : {total_expenses:.2f}")
print(f"savings         : {savings:.2f}")
print(f"savings percent : {savings_percent:.2f}")

print("="*30)
