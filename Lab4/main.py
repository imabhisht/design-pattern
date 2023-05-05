from bookshop import BookShop
from book import Book
import random
import os

def main():
    bookshop_list = []
    selected_bookshop = None
    temp_bookshop = None
    temp_book = None

    while True:
        os.system('clear')
        if selected_bookshop:
            print(f"Welcome to Book Store Menu | Selected Book Store: {selected_bookshop.name}")
        else:
            print("Welcome to Book Store Menu")

        print("1) Create Book Store")
        print("2) Select Book Store")
        print("3) Add Book to Book Store")
        print("4) Delete Book from Book Store")
        print("5) Copy Books between Book Store")
        print("6) List Books in Book Store")
        print("7) Edit Book in Book Store")
        print("8) Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            os.system('clear')
            print("Book Store Creation Menu\n")
            name = input("Enter Book Store Name: ")
            bookshop_list.append(BookShop(name)) 
            input("Press any key to continue...")
        
        elif choice == 2:
            os.system('clear')
            if bookshop_list == []:
                print("No Book Store Available")
                input("Press any key to continue...")
                continue

            print("Book Store Selection Menu\n")
            print("Select Book Store:")
            for i in range(len(bookshop_list)):
                print(f"{i+1}) {bookshop_list[i].name}")
            choice = int(input("\nEnter your choice: "))

            selected_bookshop = bookshop_list[choice-1]

        elif choice == 3:
            os.system('clear')
            print("Book Store Addition Menu\n")
            if selected_bookshop == None:
                print("No Book Store Selected")
                input("Press any key to continue...")
            else:
                while True:
                    os.system('clear')
                    print("Book Store Addition Menu\n")
                    title = input("Enter Book Title: ")
                    id = random.randint(1, 1000)
                    book = Book()
                    book.setTitle(title)
                    book.setId(id)
                    selected_bookshop.addBook(book)
                    print("Book Added...")
                    choice = input("Do you want to add more books? (y/n): ")
                    if choice == 'n':
                        input("Press any key to continue...")
                        break
            
        elif choice == 4:
            os.system('clear')
            print("Book Store Deletion Menu\n")
            if selected_bookshop == None:
                print("No Book Store Selected")
                input("Press any key to continue...")
            else:
                while True:
                    os.system('clear')
                    selected_bookshop.printBooks()
                    id = int(input("Enter Book Id: "))
                    selected_bookshop.removeBookById(id)
                    print("Book Removed...")
                    choice = input("Do you want to remove more books? (y/n): ")
                    if choice == 'n':
                        break

        elif choice == 5:
            os.system('clear')
            print("Book Store Copy Menu\n")
            if selected_bookshop == None:
                print("No Book Store Selected")
            else:
                while True:
                    os.system('clear')
                    print("Select Book Store")
                    for i in range(len(bookshop_list)):
                        print(f"{i+1}) {bookshop_list[i].name}")
                    choice = int(input("Enter your choice: "))

                    temp_bookshop = bookshop_list[choice-1]

                    if temp_bookshop != selected_bookshop:
                        break
                    else:
                        print("Same Book Store Selected")
                
                temp_bookshop.addBooks(selected_bookshop.getBooks())
                # selected_bookshop.addBooks(temp_bookshop.getBooks())
                # temp_bookshop.getBooks().clear()
                print("Books Copied...")
                input("Press any key to continue...")

        elif choice == 6:
            os.system('clear')
            print("Book Store Listing Menu\n")
            if selected_bookshop == None:
                print("No Book Store Selected")
            else:
                os.system('clear')
                selected_bookshop.printBooks()
                input("\nPress any key to continue...")

        elif choice == 7:
            os.system('clear')
            print("Book Store Editing Menu\n")
            
            if selected_bookshop == None:
                print("No Book Store Selected")
            else:
                while True:
                    os.system('clear')
                    print("Select Book: ")
                    selected_bookshop.printBooks()
                    id = int(input("\nEnter Id: "))
                    temp_book = selected_bookshop.getBookById(id)

                    if temp_book != None:
                        break
                    else:
                        print("Invalid Id")
                        input("\nPress any key to continue...")
                
                title = input("Enter new Title: ")
                temp_book.setTitle(title)

                selected_bookshop.removeBookById(temp_book.getId())

                print("Books Edited...")
                input("Press any key to continue...")


        elif choice == 8:
            print("Thank You")
            input("Press any key to continue...")
            break
                





if __name__ == "__main__":
    main()
