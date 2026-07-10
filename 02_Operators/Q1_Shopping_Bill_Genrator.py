product_name=input("Enter product name       : ")
price=float(input("enter price of 1 product  : "))
quantity=int(input("enter quantity purchased : "))
discount=float(input("enter discount(%)      :"))
total_price=price*quantity
discount_amount = total_price*discount/100
discounted_price = total_price - discount_amount
gst=discounted_price*18/100
final_bill=discounted_price+gst
print("="*30)
print("Shopping Bill Genrator")
print("="*30)
print(f"Product name : {product_name}")
print(f"price        : {price:.2f}")
print(f"quantity     : {quantity}\n")

print(f"Total price            : {total_price:.2f}")
print(f"Discount ({discount}%)       : {discount_amount:.2f}")
print(f"Price after discount   : {discounted_price:.2f}")
print(f"GST(18%)               : {gst:.2f}\n")
print(f"Final amount           : {final_bill:.2f}")
print("="*30)
