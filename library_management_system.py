# 4. Basic Library Management System
# Objective: Create a system to manage book borrowing.
# Steps:
# 1. Use a list to store available books (e.g., ["Book1", "Book2"]).
# 2. Display a menu:
# o View books.
# o Borrow a book (remove from the list if available).
# o Return a book (add to the list if not already in it).
# o Exit.
# 3. Keep the program running in a loop until the user exits.
# 4. Use functions for each operation to organize the code.

#Available book
Book=["Book1","Book2","Book3","Book4"]

#function for viewing book
def view_books(Book):
    print("\nAvailable books are:")
    for i in Book:
        print(i)    

#function for Borrowing books
def Borrow_book():
    book=input("Enter the book you want to borrow: ")
    if book in Book:
        Book.remove(book)
        print(f"{book} is borrowed successfully.")
    else:
        print(f"{book} is not available.")

#function for returning books
def return_book():
    book=input("Enter the book you want to return: ")
    if book not in Book:
        Book.append(book)
        print(f"{book} is returned successfully.")
    else:
        print(f"{book} was not borrowed.") 
        
#function for Dispaly menu
def menu():
    while True:
        print("\nLibrary Management System")
        print("1. View books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")
        choice=int(input("Enter your choice :"))        

    
        if choice==1:
            view_books(Book)
        elif choice==2:
            Borrow_book()
        elif choice==3:
            return_book()
        else:
            print("Exiting Library\n")
            break            

def ID_Verification():
    ID=[]
    for i in range(80010908 , 80010955):
        ID.append(i)
    while True:
        try:
            user_id=int(input("Enter your ID: "))
            if user_id in ID:
                print("Welcome to Library\n")
                menu()
                break
            else:
                print("Invalid ID. Please try again.")
        except ValueError:
            print("Rewrite Your ID :\n") 
ID_Verification()                   