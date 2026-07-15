store_name=input("Enter store name : ")
number=int(input("Number of product sold : "))

total_sales=0
highest_sale=0
lowest_sale=0
highest_Sale_product=""
lowest_sale_product=""
expensive_product_count=0
cheap_product_count=0
valid=True

if(number>0):
    for i in range(1,number+1):
        product_name=input("Enter product name : ")
        quantity=int(input("Quantity sold : "))
        price=float(input("Enter price of 1 product: "))
        if (quantity>=0 and price>=0):
            product_sale=quantity*price
            total_sales+=product_sale
            if i==1:
                highest_sale=product_sale
                lowest_sale=product_sale
                highest_Sale_product=product_name
                lowest_sale_product=product_name
            if(product_sale>highest_sale):
                highest_sale=product_sale
                highest_Sale_product=product_name
            if(product_sale<lowest_sale):
                lowest_sale=product_sale
                lowest_sale_product=product_name
            if(product_sale>50000):
                expensive_product_count+=1
            if(product_sale<10000):
                cheap_product_count+=1
        else:
            print("Invalid product details!")
            valid=False
            break
    
    if valid: 
        average_sale=total_sales/number
        print("="*30)
        print("SALES REPORT ")
        print("="*30)
        print(f"Store name : {store_name}")
        print(f"Products processed :{number} ")
        print(f"Total sales : {total_sales}")
        print(f"Average sale : {average_sale}\n")
    
        print(f"Highest selling product : {highest_Sale_product}")
        print(f"Highest sale : {highest_sale}\n")
    
        print(f"Lowest sale product : {lowest_sale_product}")
        print(f"Lowest sale : {lowest_sale}\n")
    
        print(f"products > 50000 : {expensive_product_count}")
        print(f"product < 10000 : {cheap_product_count}\n")
    
        print("="*30)

else:
    print("Invalid input!")






