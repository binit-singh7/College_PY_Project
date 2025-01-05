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


class Library:
    def __init__(self):
        #Available book
        self.Book=["Book1","Book2","Book3","Book4"]
        self.borrowed_Book={}
#function for viewing book
    def view_books(self):
        if not self.Book:
            print("\nNo Books are available:")
        else:    
            for Book in self.Book:
                print(f"-{Book}")   

    #function for Borrowing books
    def Borrow_book(self,user_id):
        book=input("Enter the book you want to borrow: ").strip()
        if book in self.Book:
            self.Book.remove(book)
            self.borrowed_Book[book]=user_id
            print(f"\n{book} is borrowed successfully.")
        else:
            print(f"{book} is not available.")

    #function for returning books
    def return_book(self,user_id):
        book=input("Enter the book you want to return: ").strip()
        if book in self.borrowed_Book and self.borrowed_Book[book]==user_id:
            self.Book.append(book)
            del self.borrowed_Book[book]
            print(f"{book} is returned successfully.")
        elif book in self.borrowed_Book:
            print(f"\n{book} is not recgognized borrowed.") 
        else:
            print(f"\n You are not authorized to return {book}.")            
    
    #function for Dispaly menu
    def menu(self,user_id):
        while True:
            print("\nLibrary Management System")
            print("1. View books")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Exit")
            try:
                choice=int(input("Enter your choice :"))        
                if choice==1:
                    self.view_books()
                elif choice==2:
                    self.Borrow_book(user_id)
                elif choice==3:
                    self.return_book(user_id)
                elif choice==4:
                    print("Exiting Library\n")
                    return           
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a numeric choice.")        
class User:
    def __init__(self,user_id,valid_id):
        self.user_id=user_id
        self.valid_id=valid_id
        
    def verify_user(self):
        #Verify user ID before granting access.
        return self.user_id in self.valid_id
    
def main():
    valid_id = range(80010908, 80010955)
    while True:
        try:
            user_id = int(input("Enter your ID: "))
            user = User(user_id, valid_id)
            if user.verify_user():
                print("\nWelcome to the Library!")
                library = Library()
                library.menu(user_id)
                break
            else:
                print("\nInvalid ID. Access denied.")
        except ValueError:
            print("\nInvalid input. Please enter a numeric ID.")                 

# Call the main function       
if __name__ == "__main__":
    main()