def add_contact(contacts):
    print("\n---// Adding a New Contact ---")
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!")


def view_contacts(contacts):
    print("\n---// All Contacts //---")
    if len(contacts) == 0:
        print("No contacts found.")
        return

    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")
