name=input("Enter Customer name : ")
number=int(input("Enter number of transaction : "))
total_deposit=0
total_withdrawal=0
deposit_count=0
withdrawal_count=0
max_transaction=0
max_transaction_type=""
small_transaction_type=""
small_transaction=0
valid=True
valid_transaction=0

if(number>0):
    for i in range (1,number+1):
        transaction_type=input("Enter transaction type (D for deposit) and (W for withdrawal) : ")
        amount=float(input("Enter amount of transaction : "))

        if(amount<=0):
            print("Invalid transaction amount! ")
            continue
        if (transaction_type!="W" and transaction_type!="D"):
            print("invalid transaction type!")
            continue

        
        if valid_transaction==0:
            max_transaction=amount
            max_transaction_type=transaction_type
            small_transaction=amount
            small_transaction_type=transaction_type
        if(amount>max_transaction):
            max_transaction=amount
            max_transaction_type=transaction_type
        if(amount<small_transaction):
            small_transaction=amount
            small_transaction_type=transaction_type
        if(transaction_type=="D"):
            total_deposit+=amount
            deposit_count+=1
        elif(transaction_type=="W"):
            total_withdrawal+=amount
            withdrawal_count+=1
        valid_transaction+=1
    net_balance_change=(total_deposit-total_withdrawal)
    total_transaction=total_withdrawal+total_deposit
    if valid_transaction>0:
        average=total_transaction/valid_transaction
        print("="*30)
        print("ATM TRANSACTION REPORT ")
        print("="*30)
        print(f"Customer name         : {name}\n")
        print(f"valid transaction     : {valid_transaction}\n")
    
        print(f"Deposits              : {deposit_count}")
        print(f"withdrawal            : {withdrawal_count}\n")
    
        print(f"Total deposit         : {total_deposit:.2f}")
        print(f"Total withdrawal      : {total_withdrawal}\n")
    
        print(f"net balanace change   : {net_balance_change}\n")
    
        
        if(max_transaction_type=="D"):
            print(f"largest transaction   : Deposit {max_transaction}")
        else:
            print(f"largest transaction   : Withdrawal {max_transaction}")
        
        if(small_transaction_type=="W"):
            print(f"Small transaction     : Withdrawal {small_transaction}")
        else:
            print(f"Small transaction     : Deposit {small_transaction}")
        
        print(f"Average transaction   : {average}\n")

        print("="*30)
else:
    print("Invalid input!")
     






