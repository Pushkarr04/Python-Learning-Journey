librarian_name=input("Enter librarian name : ")
total_book_issued=0
total_page_issued=0
largest_book=""
largest_book_pages=0
smallest_book=""
smallest_book_pages=0
big_book=0
small_book=0

fine_collected=0
total_book_return=0

book_search=0

valid_operation=0


while True:

    print("="*30)
    print("LIBRARY MANAGEMENT SYSTEM ")
    print("="*30)
    print("1.Issue boook")
    print("2.Return book ")
    print("3.Search book")
    print("4.Library statistics")
    print("5.Exit")

    choice=int(input("Enter choice : "))

    if(choice==5):
        print("THANK YOU FOR USING LIBRARY MANAGEMENT SYSTEM")
        break

    if(choice==1):
        book_name=input("Enter book name : ")
        pages=int(input("Enter number of pages : "))
        if(pages<=0 or book_name==""):
            print("Invalid book details!")
            continue

        else:
            print("Book issued succesfully!")
            total_book_issued+=1
            total_page_issued+=pages

            if valid_operation==0:
                smallest_book=book_name
                smallest_book_pages=pages
                largest_book=book_name
                largest_book_pages=pages
            if(pages>largest_book_pages):
                largest_book=book_name
                largest_book_pages=pages
            if(pages<smallest_book_pages):
                smallest_book=book_name
                smallest_book_pages=pages
            if(pages>500):
                big_book+=1
            if(pages<=500):
                small_book+=1

            valid_operation+=1

        
    elif(choice==2):
        book_name=input("enter book name: ")
        late_days=int(input("Enter late days : "))
        if(late_days<0):
            print("Invalid!")
            continue
        elif(late_days==0):
            fine=0
        elif(late_days<=5):
            fine=late_days*10
        elif(late_days<=10):
            fine=5*10+(late_days-5)*20
        else:
            fine=5*10+5*20+(late_days-10)*30

        total_book_return+=1
        fine_collected+=fine
        print(f"fine : {fine}")
    
    elif(choice==3):
        book_name=input("Enter book name : ")
        if(book_name==""):
            print("Invalid book name!")
        else:
            print("Book found!")
            book_search+=1

    elif(choice==4):
        print("="*30)
        print("LIBRARY REPORT")
        print("="*30)
        print(f"Librarian : {librarian_name}\n")

        print(f"Books issued : {total_book_issued}")
        print(f"Book returned : {total_book_return}")
        print(f"Book searched : {book_search}\n")
        
        print(f"Total page issued : {total_page_issued}\n")
        if total_book_issued>0:
            average_page=total_page_issued/total_book_issued
            print(f"Average pages per issued book  : {average_page:.2f}\n")

        print(f"largest book : {largest_book}")
        print(f"pages: {largest_book_pages}\n")

        print(f"smallest book : {smallest_book}")
        print(f"pages : {smallest_book_pages}\n")

        print(f"Book >500 pages  : {big_book}")
        print(f"Book <=500 pages : {small_book}\n")

        print(f"Total fine collected : {fine_collected}\n")

        print("="*30)

    else:
        print("invalid choice!")
        continue




        
            