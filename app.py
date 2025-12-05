def show_menu():
    print("\n=====// Contact Management App //=====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    contacts = []  # list to store contacts

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("This option will be added soon.")



if __name__ == "__main__":
    main()


def add_contact(contacts):
    print("\n---// Adding a New Contact ---")
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


def view_contacts(contacts):
    print("\n---// All Contacts //---")
    if len(contacts) == 0:
        print("No contacts found.")
        return

    for idx, contact in enumerate(contacts, start=1):
        name = contact.get("name", "")
        phone = contact.get("phone", "")
        email = contact.get("email", "")
        print(f"{idx}. {name} - {phone} - {email}")
