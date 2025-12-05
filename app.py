# Contact Management App (Start)
# Author: Abdul Ahad
# This is the very basic structure of the program.

def show_menu():
    print("\n===== Contact Management App =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    contacts = []  # list to store all contacts

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Option not yet added. Coming soon!")

if __name__ == "__main__":
    main()
