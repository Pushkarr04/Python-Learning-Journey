name=input("Enter username : ")
total_expenses=0
valid_expenses=0
highest_expense=0
lowest_expense=0
highest_category=""
lowest_category=""
expensive_count=0
small_count=0





while True:
    expense=input("Enter expense category : ")
    if(expense.upper()=="STOP"):
        break
    amount=float(input("Enter expense amount : "))

    if(amount<=0):
        print("Invalid Expense amount!")
        continue
    
    if valid_expenses==0:
        highest_expense=amount
        highest_category=expense
        lowest_expense=amount
        lowest_category=expense
    if(amount>highest_expense):
        highest_expense=amount
        highest_category=expense
    if(amount<lowest_expense):
        lowest_expense=amount
        lowest_category=expense    
    if(amount>5000):
        expensive_count+=1
    if(amount<500):
        small_count+=1
    
    valid_expenses+=1
    total_expenses+=amount

    

if(valid_expenses==0):
    print("No valid expenses record !")
else:
    average=total_expenses/valid_expenses

    print("="*30)
    print("EXPENSE TRACKER REPORT ")
    print("="*30)
    
    print(f" username : {name}")
    print(f"valid expenses : {valid_expenses}\n")
    print(f"total expense  : {total_expenses:.2f}")
    print(f"average : {average}\n")
    
    print(f"highest expense : \n{highest_category}-{highest_expense:.2f}\n")
    print(f"lowest expense  : \n {lowest_category}-{lowest_expense:.2f}\n")
    
    print(f"Expense>5000 : {expensive_count}")
    print(f"Expense<500  : {small_count}\n")
    
    print("="*30)
    
    
        

