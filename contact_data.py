def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts.")
        return
    for idx, c in enumerate(contacts, 1):
        print(f"{idx}. {c['name']} - {c['phone']} - {c['email']}")
