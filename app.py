def show_menu():
    print("\n=====// Contact Management App //=====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    contacts = []  # This is the list to store all contacts

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "5":
            print("Exiting the program")
            break
        else:
            print("I will implement this feature soon!")

if __name__ == "__main__":
    main()


def add_contact(contacts):
    print("\n---// Adding a New Contact //---")
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    # creating dictionary for one contact
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact is added successfully!")
