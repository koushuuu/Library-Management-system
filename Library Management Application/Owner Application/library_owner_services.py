"""
The Code contributed by Pavan Vignesh Tirupathi & Attaluri Koushik
EmpID : 1850426 & 1850557

"""

#Function to prompt owner what kind of services he need 

def library_owner_services():
    print("Welcome to the Library Owner Application!")
    print("Please select the service you need:")
    print("1. To know about book stock and the types of books available.")
    print("2. To display user data.")
    print("3. To know about current borrowers' data.")
    print("4. To exit.")

    try:
        choice = int(input("Enter the number of the service you'd like to access (1/2/3/4): "))

        if 1 == choice:
            print("You chose to know about book stock and types of books.")
            # Call the function for book stock here
        elif 2 == choice:
            print("You chose to display user data.")
            # Call the function for user data here
        elif 3 == choice:
            print("You chose to know about borrowers' data.")
            # Call the function for borrowers' data here
        elif 4 == choice:
            print("Exiting the Library Owner Application.")
            return 0
        else:
            print("Invalid choice! Please enter 1, 2, 3 or 4.")

        return choice

    except ValueError:
        print("Invalid input! Please enter a number.")