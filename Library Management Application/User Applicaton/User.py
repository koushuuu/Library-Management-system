"""
The Code contributed by Esha Arankalle & Keerthi Kandukuri
EmpID : 1850683 & 1850374
"""

import csv
from datetime import datetime, timedelta
import pandas as pd

class User:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.load_users()

    def load_users(self):
        """Load the users from a CSV file."""
        try:
            self.users = pd.read_csv(self.csv_file)
            print("Users loaded successfully from CSV!")

            if self.users.empty:
                self.current_uid = 0
            else:
                if 'uid' in self.users.columns:
                    self.current_uid = self.users['uid'].max()
                else:
                    print("Warning: 'uid' column not found. Setting current_uid to 0.")
                    self.current_uid = 0
        except FileNotFoundError:
            print(f"Error: The file {self.csv_file} was not found. Creating a new one.")
            self.current_uid = 0
            self.users = pd.DataFrame(columns=['uid', 'name', 'email', 'mobile', 'city', 'total_books_borrowed', 'current_issued_book'])
        except Exception as e:
            print(f"An error occurred while loading the users: {e}")
            self.current_uid = 0

    def add_new_user(self):
        """Add a new user to the system."""
        name = input("Enter Your Name: ")
        email = input("Enter email id: ")
        mobile = input("Enter mobile number: ")
        city = input("Enter City: ")

        self.current_uid += 1
        
        new_data = {
            'uid': self.current_uid,
            'name': name,
            'email': email,
            'mobile': mobile,
            'city': city,
            'total_books_borrowed': 0,
            'current_issued_book': ''
        }
        
        self.users = pd.concat([self.users, pd.DataFrame([new_data])], ignore_index=True)
        
        try:
            self.users.to_csv(self.csv_file, index=False)
            print(f"Registered successfully! Your UID number is: {self.current_uid}")
            return self.current_uid  # Return the new UID
        except PermissionError:
            print("Error: Permission denied. Please close the file or check your permissions.")

    def update_user(self, user_uid, book_title):
        """Update user info after borrowing a book."""
        user_index = self.users[self.users['uid'] == user_uid].index[0]
        self.users.at[user_index, 'total_books_borrowed'] += 1
        self.users.at[user_index, 'current_issued_book'] = book_title

        # Save the updated user data back to CSV
        try:
            self.users.to_csv(self.csv_file, index=False)
            print("User data updated successfully.")
        except Exception as e:
            print(f"An error occurred while updating user data: {e}")