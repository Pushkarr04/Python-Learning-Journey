def line():
    print("="*30)
def heading(title="sales analytics"):
    line()
    print(title.upper())
    line()


    
def show_products(products,categories,quantities,prices):
    heading("product list")
    print(f"{'Products':15}{'categories':15}{'quantities':15}{'prices':15}")
    print("-"*50)
    for i in range(len(products)):
        print(f"{products[i]:15}{categories[i]:15}{quantities[i]:15}{prices[i]:15}")

def search_product(search,products,categories,quantities,prices):
    found=False

    for i in range(len(products)):
        if products[i].lower()==search:
            print("Product found")
            
            
            print(f"Product : {products[i]}")
            print(f"category : {categories[i]}")
            print(f"quantity : {quantities[i]:.2f}")
            print(f"prices : {prices[i]:.2f}")
            revanue=quantities[i]*prices[i]
            print(f"Revanue : {revanue:.2f}")
            found=True
            break

    if not found:
        print("product not found")

def update_product(update,new_category,new_quantity,new_price,products,categories,quantities,prices):
    found=False

    for i in range(len(products)):
        if products[i].lower()==update:
            categories[i]=new_category
            quantities[i]=new_quantity
            prices[i]=new_price

            print("Updated succesfully")
            found =True

            print(f"Product : {products[i]}")
            print(f"category : {categories[i]}")
            print(f"quantity : {quantities[i]:.2f}")
            print(f"prices : {prices[i]:.2f}")
            break
    if not found:
        print("product not found")

def delete_product(delete,products,categories,quantities,prices):
    found=False
    for i in range(len(products)):
        if products[i].lower()==delete:
            products.pop(i)
            categories.pop(i)
            quantities.pop(i)
            prices.pop(i)

            print("product removed succesfully")
            found=True
            break
    if not found:
        print("product not found ")   

def calc_revanue(quantities,prices):
    revanues=[]
    for i in range((len(quantities))):
        revanue=quantities[i]*prices[i]
        revanues.append(revanue)
    return revanues

def analytics(products,categories,quantities,prices,revanues,username):
    total_products=0
    total_quantity=0
    total_reavnue=0
    avg_revanue=0
    highest_revanue=0
    lowest_revanue=0
    highest_revanue_product="" 
    lowest_revanue_product=""
    
    above_avg_revanue=0
    below_avg_revanue=0
    electronics_count=0
    stationery_count=0
    other_category_count=0

    if len(products)!=0:
        most_expensive_product=products[prices.index(max(prices))]
        chepaest_product=products[prices.index(min(prices))]
        total_products=len(products)
        total_quantity=sum(quantities)
        total_reavnue=sum(revanues)
        
        highest_revanue=max(revanues)
        lowest_revanue=min(revanues)
        highest_revanue_product=products[revanues.index(highest_revanue)]
        lowest_revanue_product=products[revanues.index(lowest_revanue)]

        avg_revanue=total_reavnue/total_products
        for revanue in revanues:
            if revanue>avg_revanue:
                    above_avg_revanue+=1
            else:
                below_avg_revanue+=1

        for i in range(len(categories)):
            if(categories[i].lower()=="electronics"):
                electronics_count+=1
            elif(categories[i].lower()=="stationery"):
                stationery_count+=1
            else:
                other_category_count+=1

    else:
        print("product list is empty!")
        return


    heading("sales analytics report")
    print(f"username : {username}")
    print(f"Total products : {total_products}\n")
    print(f"Total quantity sold : {total_quantity}\n")

    print(f"Total revanue : {total_reavnue:.2f}")
    print(f"average revanue : {avg_revanue:.2f}\n")

    print("HIGHEST REVANUE PRODUCT")
    print(f"product : {highest_revanue_product}")
    print(f"revanue : {highest_revanue}\n")

    print("LOWEST REVANUE PRODUCT")
    print(f"product: {lowest_revanue_product}")
    print(f"revanue : {lowest_revanue}\n")

    print(f"Most expensive product : {most_expensive_product}")
    print(f"cheapest product  : {chepaest_product}\n")

    print(f"Products above average revanue : {above_avg_revanue}")
    print(f"Products below average revanue : {below_avg_revanue}\n")

    print(f"Electronics product  : {electronics_count}")
    print(f"Stationery products : {stationery_count}")
    print(f"other products  : {other_category_count}")




username=input("enter username : ")
number=int(input("Enter how many products :"))

products=[]
categories=[]
quantities=[]
prices=[]
revanues=[]


for i in range(number):

    print("-"*15)
    print(F"PRODUCT {i+1}")
    print("-"*15)
    product=input("enter name of product : ").lower()
    category=input("enter product category : ").lower()
    quantity=int(input("enter product quantity  :"))
    price=float(input("enter product price : "))

    if product.replace(" ","").isalpha() and quantity>=0 and price>0 and category!="":
        products.append(product)
        categories.append(category)
        quantities.append(quantity)
        prices.append(price)



while True:
    print("1. show product")
    print("2. search")
    print("3. update")
    print("4. delete product")
    print("5. sales analytics")
    print("6. exit")

    choice=int(input("Enter choice : "))

    if choice==6:
        print("thank you")
        break
    elif choice==1:
        show_products(products,categories,quantities,prices)
    elif choice==2:
        search=input("enter product to search :").lower()
        search_product(search,products,categories,quantities,prices)
    elif choice==3:
        update=input("Enter product to update : ").lower()
        new_category=input("enter new category :")
        new_quantity=int(input("Enetr new quantity :"))
        new_price=float(input("Enter new price  :"))
        if new_price>0 and new_quantity>=0 and new_category!="":
            update_product(update,new_category,new_quantity,new_price,products,categories,quantities,prices)
        else:
            print("invalid input")

    elif choice==4:
        delete=input("enetr product to delete ").lower()
        delete_product(delete,products,categories,quantities,prices)
    elif choice==5:
        revanues=calc_revanue(quantities,prices)
        analytics(products,categories,quantities,prices,revanues,username)
    else:
        print("invalid choice")

