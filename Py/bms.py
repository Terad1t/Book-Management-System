book = []

def show_menu():
    print("\nBook Management System")
    print("1 - Insert book")
    print("2 - Remove book")
    print("3 - List books")
    print("4 - Exit")

def insert_book():
    name = input("Enter the book name: ")
    book.append(name)
    print(f"Book '{name}' has been inserted successfully.")

def remove_book():
    name = input("Enter the book name: ")
    if name in book:
        book.remove(name)
        print(f"Book '{name}' has been removed.")
    else:
        print("This book was not found.")

def list_book():
    if not book:
        print("No books found.")
    else:
        print("\nList of books:")
        for i, b in enumerate(book, start=1):
            print(f"{i}. {b}")

while True:
    show_menu()
    option = input("Choose an option: ")

    if option == "1":
        insert_book()
    elif option == "2":
        remove_book()
    elif option == "3":
        list_book()
    elif option == "4":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")
