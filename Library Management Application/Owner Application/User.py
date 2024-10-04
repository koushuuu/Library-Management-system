"""
The Code contributed by Pavan Vignesh Tirupathi & Attaluri Koushik
EmpID : 1850426 & 1850557

"""

import pandas as pd
import csv

# Class which represents the user
class User:
    # Constructor method to initialize a User object
    def __init__(self, uid, name, email, mobile, city, total_books_borrowed, current_issued_book):
        self.uid = uid
        self.name = name
        self.email = email
        self.mobile = mobile
        self.city = city
        self.total_books_borrowed = total_books_borrowed
        self.current_issued_book = current_issued_book
    
    # Method to return a string representation of the user
    def __str__(self):
        issued_book_str = f"Currently issued: {self.current_issued_book}" if self.current_issued_book else "No book currently issued"
        return (f"User: {self.name} (ID: {self.uid})\nEmail: {self.email}, Mobile: {self.mobile}, City: {self.city}\n"
                f"Total Books Borrowed: {self.total_books_borrowed}, {issued_book_str}")

# Class through which the library owner can view and manage user data
class User_data:

    # Constructor method to initialize a User_data object
    def __init__(self, file_path_1):
        self.file_path_1 = file_path_1
        self.users = []
        self.load_users()

    # Method to load users from a CSV file into the system
    def load_users(self):
        global df_users
        # Read the user data from the CSV file into a pandas DataFrame
        df_users = pd.read_csv(self.file_path_1)
        for _, row in df_users.iterrows():
            # Create a User object from each row in the DataFrame
            user = User(row['uid'], row['name'], row['email'], row['mobile'], row['city'], row['total_books_borrowed'], row['current_issued_book'])
            self.users.append(user)

    # Method to search for a user by name
    def search_user_data(self, name):
        # Filter the DataFrame for rows where the name contains the search string
        df_user = df_users[df_users['name'].str.contains(name)]
        # Check if any user data matches the search
        if df_user.empty:
            print("No users found with the given name.")
        else:
            print(df_user)
    
    # Method to display all user data
    def display_user_data(self):
        print("All users data:")
        print(df_users)

    # Method to delete a user by their user ID (uid)
    def delete_user_data(self, uid):
        # Try block to handle exceptions like invalid input
        # Check if the user with the given uid exists
        try: 
            if uid in df_users['uid'].values:
                # Drop the user from the DataFrame
                df_update = df_users[df_users['uid'] != uid]
                # Save the updated DataFrame to the CSV
                df_update.to_csv(self.file_path_1, index=False)
                print(f"User with ID {uid} has been deleted.")
                self.load_users()
            else:
                print(f"No user found with ID {uid}.")
        except ValueError:
            print(f"Please Enter a Number")

class UserManagementSystem:

    # Constructor method that initializes the system 
    def __init__(self, users):
        self.users = users
    
    # Method to run the system's main loop, providing the menu and handling user interactions
    def run(self):
        while True:
            print("\nUser Management System")
            print("1. Display all the users data")
            print("2. Search user data by name")
            print("3. delete any user data")
            print("4. Exit")
            choice = input("Enter your choice (1/2/3/4): ")

            if '1' == choice:
                self.users.display_user_data()

            elif '2' == choice:
                name = input("Enter the name you want to search for: ")
                self.users.search_user_data(name)

            elif '3' == choice:
                uid = input("Enter the ID of the user you want to delete: ")
                uid = int(uid)
                self.users.delete_user_data(uid)
            elif '4' == choice:
                print("Exiting the User Management System.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4 or 5")