"""
The Code contributed by Esha Arankalle & Keerthi Kandukuri
EmpID : 1850683 & 1850374
"""

import csv
from datetime import datetime, timedelta

class Book:
    def __init__(self, bid, title, author, category, status, stock_count):
        self.bid = bid
        self.title = title
        self.author = author
        self.category = category
        self.status = status
        self.stock_count = stock_count

    def __str__(self):
        return f"{self.title} by {self.author} (ID: {self.bid}, Status: {self.status}, Stock: {self.stock_count})"


class Library:
    def __init__(self, books_csv):
        self.books = []
        self.load_books_from_csv(books_csv)

    def load_books_from_csv(self, csv_file):
        """Load the books from a CSV file."""
        try:
            with open(csv_file, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    book = Book(
                        bid=row['bid'],
                        title=row['title'],
                        author=row['author'],
                        category=row['category'],
                        status=row['status'],
                        stock_count=int(row['Stock Count'])
                    )
                    self.books.append(book)
            print("Books loaded successfully from CSV!")
        except FileNotFoundError:
            print(f"Error: The file {csv_file} was not found.")
        except Exception as e:
            print(f"An error occurred while loading the books: {e}")

    def search_book(self, search_term):
        """Search for a book by title or author."""
        results = []
        search_term = search_term.lower()
        for book in self.books:
            if search_term in book.title.lower() or search_term in book.author.lower():
                results.append(book)

        if results:
            print(f"\nSearch Results for '{search_term}':")
            for result in results:
                print(f"  ID: {result.bid}, Title: '{result.title}', Author: {result.author}, "
                      f"Category: {result.category}, Status: {result.status}, Stock Count: {result.stock_count}")
        else:
            print(f"\nNo results found for '{search_term}'.")

    def display_books(self):
        """Display all books in a tabular format."""
        print("\n===== Books Available =====")
        print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'Category':<15} {'Status':<15} {'Stock Count':<10}")
        print("=" * 100)
        for book in self.books:
            print(f"{book.bid:<5} {book.title:<30} {book.author:<20} {book.category:<15} {book.status:<15} {book.stock_count:<10}")
            print("-" * 100)  # Line between rows
        print("=" * 100)  # Final line at the end of the table

    def borrow_book(self, book_title, user_service, user_uid):
        """Borrow a book if available."""
        if user_uid is None or user_uid not in user_service.users['uid'].values:
            print("Error: User UID not found.")
            return

        for book in self.books:
            if book.title.lower() == book_title.lower():
                if book.status.lower() == 'available' and book.stock_count > 0:
                    book.stock_count -= 1  # Decrement stock count
                    user_service.update_user(user_uid, book.title)  # Update user info
                    self.add_borrower_record(user_service, user_uid, book.title)
                    print(f"\nConfirmation: You have successfully borrowed '{book.title}'.")
                    due_date = datetime.now() + timedelta(days=14)
                    print(f"Due date to return the book: {due_date.strftime('%Y-%m-%d')}")
                    return
                else:
                    print(f"\nSorry, '{book.title}' is currently not available.")
                    return
        print(f"\nThe book '{book_title}' is not available in the library.")

    def add_borrower_record(self, user_service, user_uid, book_title):
        """Add a record of the borrowed book to the borrowers CSV file."""
        user_data = user_service.users[user_service.users['uid'] == user_uid]
        
        if not user_data.empty:  # Check if user exists
            name = user_data['name'].values[0]
            city = user_data['city'].values[0]
        else:
            print("Error: User UID not found.")
            return

        borrow_date = datetime.now().strftime('%Y-%m-%d')
        return_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')

        # Prepare new record
        new_record = {
            'uid': user_uid,
            'name': name,
            'city': city,
            'books_borrowed': book_title,
            'borrow_dates': borrow_date,
            'return_dates': return_date
        }

        # Append to borrowers CSV
        try:
            with open('borrowers.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=new_record.keys())
                writer.writerow(new_record)
            print("Borrower record updated successfully!")
        except Exception as e:
            print(f"An error occurred while updating borrower record: {e}")
