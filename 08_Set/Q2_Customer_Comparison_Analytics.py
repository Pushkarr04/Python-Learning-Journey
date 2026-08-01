username=input("Enter username : ")
number_a=int(input("How many customer in Campaign A? : "))
number_b=int(input("How many customer in Campaign B? : "))

customers_a=set()
customers_b=set()

a=1
while a<= number_a:
    customer_a=input(f"Enter customer A name {a} : ").lower()
    customers_a.add(customer_a)

    a+=1

b=1
while b<=number_b:
    customer_b=input(f"Enter customer B name {b} : ").lower()
    customers_b.add(customer_b)

    b+=1

while True:

    print("=" * 30)
    print("CUSTOMER ANALYTICS SYSTEM")
    print("=" * 30)    

    print("1. Show Campaign A")
    print("2. Show Campaign B")
    print("3. All Unique Customers")
    print("4. Common Customers")
    print("5. Only Campaign A Customers")
    print("6. Only Campaign B Customers")
    print("7. Customers in Exactly One Campaign")
    print("8. Check Subset")
    print("9. Check Superset")
    print("10. Check Disjoint")
    print("11. Exit")    

    choice=int(input("Enter your choice : "))

    if choice==11:
        print("Thank you!")
        break

    elif choice==1:
        for customer in customers_a:
            print(customer)

    elif choice==2:
        for customer in customers_b:
            print(customer)

    elif choice==3:
        print("All unique cutomers : ")
        unique=customers_a.union(customers_b)
        print(unique)

    elif choice==4:
        print("Common customers : ")
        common=customers_a.intersection(customers_b)
        print(common)

    elif choice==5:
        print("only campaign A : ")
        only_a=customers_a.difference(customers_b)
        print(only_a)

    elif choice==6:
        print("only campaign B : ")
        only_b=customers_b.difference(customers_a)
        print(only_b)

    elif choice==7:
        print("Customers in exactly one campaign : ")
        exactly_one=customers_a.symmetric_difference(customers_b)
        print(exactly_one)

    elif choice==8:
        print("check subset")
        print("B is subset of A : ",customers_b.issubset(customers_a))
        print("A is subset of B : ",customers_a.issubset(customers_b))

    elif choice==9:
        print("Check superset : ")
        print("A is superset of B : ",customers_a.issuperset(customers_b))
        print("B is superset of A : ",customers_b.issuperset(customers_a))

    elif choice==10:
        print("Check disjoint")
        print(customers_a.isdisjoint(customers_b))

    else:
        print("invalid input!")


