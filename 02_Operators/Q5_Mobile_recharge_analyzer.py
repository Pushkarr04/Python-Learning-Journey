recharge_amount=float(input("Enter recharge amount   : "))
total_data=float(input("Enter total data(GB     : "))
data_used=float(input("Enter data used (GB)    : "))

remaining_data=total_data-data_used
cost_per_gb=recharge_amount/total_data
data_fully_consumed=total_data==data_used
used_50_data=data_used>total_data/2
less_than_1_GB=remaining_data<1
percent_used=data_used/total_data*100

print("="*30)
print("MOBILE RECHARGE ANALYZER")
print("="*30)

print(f"\nRecharge amount     : {recharge_amount:.2f}")
print(f"Total data          : {total_data}GB")
print(f"Data used           : {data_used}GB\n")

print(f"Remaining data      : {remaining_data}GB")
print(f"Cost per GB         : {cost_per_gb:.2f}\n")

print(f"Data fully consumed : {data_fully_consumed}")
print(f"More than 50% used  : {used_50_data}")
print(f"Reamianing < 1 GB   : {less_than_1_GB}\n")
print(f"Data used(%)        : {percent_used:.2f}%")

print("="*30)



