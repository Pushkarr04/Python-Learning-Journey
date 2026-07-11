account_balance=float(input("Enter Account Balance   : "))
withdrawal_amount=float(input("Enter Withdrawl Amount  : "))

print("="*30)
print("     ATM WITHDRAWAL")
print("="*30)
remaining_balance=account_balance-withdrawal_amount
print(f"\nAccount balance   : {account_balance:.2f}")
print(f"Withdrawal Amount : {withdrawal_amount:.2f}\n")

if(withdrawal_amount<=0):
    print("Invalid Withdrawal Amount")
elif (withdrawal_amount>account_balance):
    print("Transaction failed!\nInsufficient balance.")
else:
    print(f"Transaction Successful!\n")
    print(f"Remaining Balance : {remaining_balance:.2f}")

print("="*30)