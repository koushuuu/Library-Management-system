"""
The Code contributed by Pavan Vignesh Tirupathi & Attaluri Koushik
EmpID : 1850426 & 1850557

"""
import pandas as pd
from datetime import datetime, timedelta

# Class representing a Borrower
class Borrower:
    # Constructor to initialize a Borrower object with their details
    def __init__(self, uid, name, city, books_borrowed, borrow_dates, return_dates):
        self.uid = uid
        self.name = name
        self.city = city
        self.books_borrowed = books_borrowed.split(', ')
        self.borrow_dates = borrow_dates.split(', ')
        self.return_dates = return_dates.split(', ')

    # String representation of the borrower object
    def __str__(self):
        borrow_info = [f"{book} (Borrowed: {borrow}, Due: {due})"
                       for book, borrow, due in zip(self.books_borrowed, self.borrow_dates, self.return_dates)]
        # Return a formatted string with borrower details and the list of books borrowed with dates
        return (f"Borrower: {self.name} (ID: {self.uid})\nCity: {self.city}\nBooks Borrowed:\n"
                + "\n".join(borrow_info))

# Class to manage Borrower data
class BorrowerData:
    # Constructor to initialize with a file path (CSV file) containing borrower data
    def __init__(self, file_path):
        self.file_path = file_path
        self.df_borrowers = None
        self.load_borrowers()

    # Method to load borrower data from the CSV file
    def load_borrowers(self):
        self.df_borrowers = pd.read_csv(self.file_path)
        print(f"Loaded {len(self.df_borrowers)} borrowers.")

    # Method to search for borrowers by name
    def search_borrower(self, name):
        # Find borrowers where the 'name' column contains the search term
        found_borrowers = self.df_borrowers[self.df_borrowers['name'].str.contains(name)]
        if found_borrowers.empty:
            print("No borrowers found with the given name.")
        else:
            print(found_borrowers)

    # Method to display all borrowers in the DataFrame
    def display_borrowers(self):
        print(self.df_borrowers)

    # Method to delete borrower data based on user ID
    def delete_user_data(self, uid):
        # Check if the given uid exists in the 'uid' column of the DataFrame
        if uid in self.df_borrowers['uid'].values:
            # Drop the user from the DataFrame
            df_update = self.df_borrowers[self.df_borrowers['uid'] != uid]
            # Save the updated DataFrame to the CSV
            df_update.to_csv(self.file_path)
            print(f"User with ID {uid} has been deleted.")
            # Reload the updated borrower data to refresh the in-memory DataFrame
            self.load_borrowers()
        else:
            print(f"No user found with ID {uid}.")
    
    def check_near_due_dates(self, days_before_due=7):
        # Convert the 'return_dates' column to datetime format for proper date manipulation
        self.df_borrowers['return_dates'] = pd.to_datetime(self.df_borrowers['return_dates'], dayfirst=True)

        # Filter borrowers who have return dates within the specified range (default is 7 days before due)
        near_due_borrowers = self.df_borrowers[self.df_borrowers['return_dates'] - datetime.now() <= pd.Timedelta(days=days_before_due)]

        # Check if there are any borrowers with near due dates
        if not near_due_borrowers.empty:
            print("Borrowers with near due dates:")
            for index, row in near_due_borrowers.iterrows():
                print(f"{row['name']} (ID: {row['uid']}) - Due: {row['return_dates'].strftime('%d-%m-%Y')}")
        else:
            print("No borrowers with near due dates.")
    

# Class to manage the system interface
class BorrowerManagementSystem:
    def __init__(self, borrower_data):
        self.borrower_data = borrower_data

    def run(self):
        while True:
            print("\nBorrower Management System")
            print("1. Display all borrowers")
            print("2. Search borrower by name")
            print("3. Check due dates of Borrowers")
            print("4. Delete any user data")
            print("5. Exit")
            choice = input("Enter your choice (1/2/3/4/5): ")

            if '1' == choice:
                self.borrower_data.display_borrowers()
            elif '2' == choice:
                name = input("Enter the name to search: ")
                self.borrower_data.search_borrower(name)
            elif '3' == choice:
                self.borrower_data.check_near_due_dates()  # Call the check_near_due_dates method here
            elif '4' == choice:
                uid = input("Enter the ID of the user you want to delete: ")
                uid = int(uid)
                self.borrower_data.delete_user_data(uid)
            elif '5' == choice:
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")