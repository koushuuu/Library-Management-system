"""
The Code contributed by Pavan Vignesh Tirupathi & Attaluri Koushik
EmpID : 1850426 & 1850557

"""

from Book import *
from Borrower import *
from library_owner_services import *
from User import *

def main():
  
  # Call the library_owner_services function to get the owner's choice
  choice = library_owner_services()
   
  # Check the user's choice for managing the library system
  if 1 == choice:
    csv_file = r'C:\Users\HP\Documents\Library Application\Data\Books_data_.csv'
    try:
        library = Library(csv_file)
        system = LibraryManagementSystem(library)
        system.run()
    # Handle the case where the specified file does not exist
    except FileNotFoundError:
        print("Error: The file '{}' does not exist.".format(csv_file))
        print("Please ensure the file is in the correct location and try again.")

  elif 2 == choice:
    csv_file_2 = r'C:\Users\HP\Documents\Library Application\Data\Users_data.csv'
    try:
        users = User_data(csv_file_2)
        system = UserManagementSystem(users)
        system.run()
    except FileNotFoundError:
        print("Error: The file '{}' does not exist.".format(csv_file))
        print("Please ensure the file is in the correct location and try again.")

  elif 3 == choice:
    csv_file = r'C:\Users\HP\Documents\Library Application\Data\borrowers.csv'  # Make sure this file exists in your working directory
    try:
        borrower_data = BorrowerData(csv_file)
        system = BorrowerManagementSystem(borrower_data)
        system.run()
    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' does not exist.")

# Entry point of the program
if __name__ == "__main__":
  main()