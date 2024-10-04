"""
The Code contributed by Esha Arankalle & Keerthi Kandukuri
EmpID : 1850683 & 1850374
"""

import csv
from Book_Library import *
from User import *


# Main program
def main():
    print("Welcome to the Library Management System!")
    user_service = User(r'C:\Users\HP\Documents\Library Application\Data\Users_data.csv')
    library = Library(r'C:\Users\HP\Documents\Library Application\Data\Books_data_.csv')  # Specify your desired CSV file path

    print("Users and books loaded.")
    
    user_uid = None  # Initialize user_uid here

    # Registration option
    register = input("Do you want to register as a new user? (yes/no): ")
    if register.lower() == 'yes':
        user_uid = user_service.add_new_user()  # Capture the returned UID
    else:
        user_uid_input = input("Enter your UID number: ")
        # Check if UID exists
        if not user_uid_input.isdigit() or int(user_uid_input) not in user_service.users['uid'].values:
            print("UID not found. Please register as a new user.")
            return
        user_uid = int(user_uid_input)  # Convert to int after validating

    while True:
        print("\n===== Library Menu =====")
        print("1. Display Books Table")
        print("2. Search a Book by Title or Author")
        print("3. Borrow a Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library.display_books()

        elif choice == '2':
            search_term = input("Enter the title or author to search: ")
            # Implement search_book method in Library if needed
            library.search_book(search_term)

        elif choice == '3':
            book_title = input("Enter the title of the book you want to borrow: ")
            library.borrow_book(book_title, user_service, user_uid)

        elif choice == '4':
            print("Exiting the library system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
