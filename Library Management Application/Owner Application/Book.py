"""
The Code contributed by Pavan Vignesh Tirupathi & Attaluri Koushik
EmpID : 1850426 & 1850557

"""
import csv
import pandas as pd
from tabulate import tabulate  # Importing tabulate

# Class which represents the book
class Book:
    def __init__(self, bid, title, author, category, status, stock_count): #initializer (or constructor) method
        self.bid = bid           #creating an instance variable
        self.title = title
        self.author = author
        self.category = category
        self.status = status
        self.stock_count = stock_count

    def __str__(self):
        # Method which returns a string representation of the object
        return f"{self.title} by {self.author} (Category: {self.category}, Status: {self.status}, Stock: {self.stock_count})"  

# Class which represents the library
class Library:
    
    # Initialization method that sets the attributes of the Library instance
    def __init__(self, file_path):
        self.file_path = file_path # Assigns the provided file path to the instance variable 'file_path'
        self.books = []
        self.load_books()
    
    # Method to load books from a CSV file
    def load_books(self):
        global df
        df = pd.read_csv(self.file_path) # Reads the CSV file into a DataFrame using pandas
        for _, row in df.iterrows():
            book = Book(row['bid'], row['title'], row['author'], row['category'], row['status'], row['Stock Count'])
            self.books.append(book)
    
    # Method to display books by genre
    def display_books_by_genre(self, genre):
        print(f"Books under genre '{genre}':")
        # Filter the DataFrame for rows where the 'category' matches the specified genre
        df_genre = df[df['category'] == genre]
        if df_genre.empty:
            print("No books found under the genre.")
        else:
            # Print the filtered DataFrame in a tabulated format using the 'tabulate' library
            print(tabulate(df_genre, headers='keys', tablefmt='pretty'))
    
    # Method to display books by searching for a name (or part of a name)
    def display_books_by_name(self, name):
        # Filter the DataFrame for rows where the 'title' contains the search term
        df_name = df[df['title'].str.contains(name, case=False)]
        if df_name.empty:
            print("No books found with that name.")
        else:
            print(tabulate(df_name, headers='keys', tablefmt='pretty'))
    
    # Method to display all books in the library
    def display_all_books(self):
        print("All books in the library:")
        print(tabulate(df, headers='keys', tablefmt='pretty'))
    
    # Method to add a new book to the library database
    def add_new_book(self):
        #Prompting Owner for Various Book Data
        bid = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        category = input("Enter Book Category: ")
        status = input("Enter Book Status (available/unavailable): ")
        stock_count = input("Enter Stock Count: ")
        
        # Create a dictionary to hold the new book's data, using the user inputs
        new_data = {'bid': bid, 'title': title, 'author': author, 'category': category, 'status': status, 'Stock Count': stock_count}
        df = pd.read_csv(self.file_path)
        # Concatenate the new book's data (wrapped in a DataFrame) with the existing data
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        # Save the updated DataFrame back to the CSV file
        df.to_csv(self.file_path, index=False)
        self.load_books()

        print(f"Book '{title}' added successfully!")

class LibraryManagementSystem:

    def __init__(self, library):
        self.library = library
    
    # Main method to run the system
    def run(self):
        # An infinite loop to keep the system running until the user exits
        while True:
            print("\nLibrary Management System")
            print("1. View books by genre")
            print("2. View books by name")
            print("3. View all books")
            print("4. Add a new book")
            print("5. Exit")
            choice = input("Enter your choice (1/2/3/4/5): ")

            if '1' == choice:
                unique_names = df['category'].unique()
                print("Available genres:", unique_names)
                genre = input("Enter the genre you want to view: ")
                self.library.display_books_by_genre(genre)

            elif '2' == choice:
                name = input("Enter the name you want to search for: ")
                self.library.display_books_by_name(name)
            elif '3' == choice:
                self.library.display_all_books()
            elif '4' == choice:
                self.library.add_new_book()
            elif '5' == choice:
                print("Exiting the Library Management System.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")