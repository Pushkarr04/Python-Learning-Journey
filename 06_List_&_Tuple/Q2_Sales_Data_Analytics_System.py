username=input("enter username : ")
number=int(input("How many products? : "))

products=[]
categories=[]
quantities=[]
prices=[]


for i in range(number):
    product=input("Enter product name : ")
    category=input("Enter product categorie : ")
    quantity=int(input("Enter product quantity : "))
    price=float(input("Enter product price : "))
    if product.replace(" ","").isalpha() and category.replace(" ","").isalpha() and quantity >0 and price >0 :
        products.append(product)
        categories.append(category)
        quantities.append(quantity)
        prices.append(price)
    else:
        print("Invalid input!")

while True:
    print("="*30)
    print("SALES DATA ANALYTICS SYSTEM")
    print("="*30)

    print("1.Show all products")
    print("2.Search product")
    print("3.Update product")
    print("4.Delete product")
    print("5.Sales Analytics")
    print("6.Exit")

    choice=int(input("Enter your choice : "))
    if(choice==6):
        print("Thank you for using sales data analytics")
        break
    elif(choice==1):
        for i in range(len(products)):
            print(f"{products[i]:15} {categories[i]:15} {quantities[i]:15} {prices[i]:10.2f}")
    elif(choice==2):
        search=input("Enter product to search : ")
        search=search.lower()
        found=False
        for i in range(len(products)):
            if products[i].lower()==search:
                print(f"Product : {products[i]}")
                print(f"category : {categories[i]}")
                print(f"quantity : {quantities[i]}")
                print(f"price : {prices[i]}")
                revenue=quantities[i]*prices[i]
                print(f"Revenue : {revenue}")
                found=True
                break
        if not found:
            print("Product not found")
    elif(choice==3):
        search=input("Enter product to update : ")
        search=search.lower()
        found=False
        
        for i in range(len(products)):
            if products[i].lower()==search:
                found_at=i
                new_category=input("Enter new category to update : ")
                new_quantity=int(input("Enter new quantity to update : "))
                new_price=float(input("Enter price to update : "))

                categories[found_at]=new_category

                if new_quantity >0 and new_price >0:
                    quantities[found_at]=new_quantity
                    prices[found_at]=new_price
                    print("product updated succesfully")
                    found=True
                    break
        if not found:
            print("product not found")   
    elif(choice==4):
        remove=input("Enter product to remove")
        remove=remove.lower()
        found=False
        for i in range(len(products)):
            if products[i].lower()==remove:
                found_at=i
                products.pop(found_at)
                categories.pop(found_at)
                quantities.pop(found_at)
                prices.pop(found_at)

                print("product removed succesfully")
                found=True
                break
        if not found:
            print("product not found.")
    elif(choice==5):
        total_revenue=0
        revenues=[]
        print("="*10)
        print("SALES ANALYTICS REPORT")
        print("="*10)
        print(f"username : {username}\n")
        print(f"Total products : {len(products)}\n")
        total_quantity=sum(quantities)
        print(f"Total quantity sold : {total_quantity}\n")
        
        if len(products)==0:
            print("products list is empty")
        else:
            for i in range(len(quantities)):
                revenue=quantities[i]*prices[i]
                revenues.append(revenue)
                total_revenue+=revenue
            print(f"Total revanue : {total_revenue}")
            average_revenue=total_revenue/len(products)
            highest_revenue=max(revenues)
            lowest_revenue=min(revenues)
            highest_revenue_product=products[revenues.index(highest_revenue)]
            lowest_revenue_product=products[revenues.index(lowest_revenue)]
            print(f"Average revanue per product : {average_revenue}\n")
            
            print(f"Highest revanue product : {highest_revenue_product}")
            print(f"Revanue : {highest_revenue}\n")
    
            print(f"Lowest revanue product : {lowest_revenue_product}")
            print(f"Revanue : {lowest_revenue}\n")

            above_average=0
            below_average=0
            for revanue in revenues:
                if revanue>average_revenue:
                    above_average+=1
                else:
                    below_average+=1
            print(f"Products above average revanue : {above_average}")
            print(f"Products below average revanue : {below_average}\n")
    
            most_expensive=products[prices.index(max(prices))]
            cheapest=products[prices.index(min(prices))]
            print(f"Most expensive product : {most_expensive}")
            print(f"cheapest product  : {cheapest}")
    
            electronics_products=0
            stationery_products=0
            other_categories=0
    
            for i in range(len(categories)):
                if(categories[i].lower()=="electronics"):
                    electronics_products+=1
                elif(categories[i].lower()=="stationery"):
                    stationery_products+=1
                else:
                    other_categories+=1
    
            print(f"Electronics product  : {electronics_products}")
            print(f"Stationery products : {stationery_products}")
            print(f"other products  : {other_categories}")


    else:
        print("Invalid choice!")













