from contacts_manager import ContactsManager
from storage import load_contacts, save_contacts
from utils import valid_name, valid_phone, valid_email


def show_menu():
    print("\n=====// Contact Management App //=====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")

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



def search_contact(contacts):
    print("\n---// Search Contact //---")
    name = input("Enter name to search: ").strip()
    if not name:
        print("Please enter a name.")
        return

    # Here is a linear search through contacts (O(n))
    for contact in contacts:
        if contact.get("name", "").strip().lower() == name.lower():
            print("Contact found:")
            print(f"Name: {contact.get('name')}")
            print(f"Phone: {contact.get('phone')}")
            print(f"Email: {contact.get('email')}")
            return

    print("Contact not found.")



def delete_contact(contacts):
    print("\n---// Delete Contact //---")
    name = input("Name to delete: ").strip()
    if not name:
        print("Please enter a name.")
        return

    # linear search through the list to find and remove
    for contact in contacts:
        if contact.get("name", "").strip().lower() == name.lower():
            confirm = input(f"Delete '{contact.get('name')}'? (y/n): ").strip().lower()
            if confirm == 'y':
                contacts.remove(contact)
                print("Deleted.")
            else:
                print("Delete cancelled.")
            return

    print("Contact not found.")





DATA_FILE = "contacts.json"

def main():
    mgr = ContactsManager()
    # load existing contacts
    initial = load_contacts(DATA_FILE)
    for d in initial:
        # expect dict with keys name/phone/email
        mgr.add_contact(d.get("name", ""), d.get("phone", ""), d.get("email", ""))

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
           print("\n--- Add Contact ---")
           name = input("Name: ").strip()
           if not valid_name(name):
               print("Name cannot be empty.")
               continue
           phone = input("Phone: ").strip()
           if not valid_phone(phone):
                print("Phone looks invalid. Save cancelled.")
                continue
           email = input("Email (optional): ").strip()
           if not valid_email(email):
                print("Email looks invalid. Save cancelled.")
                continue
           mgr.add_contact(name, phone, email)
           print("Contact added.")
        elif choice == "2":
            contacts = mgr.list_contacts()
            if not contacts:
                print("No contacts found.")
            else:
                print("\n--- All Contacts ---")
                for i, c in enumerate(contacts, start=1):
                    print(f"{i}. {c.get('name')} - {c.get('phone')} - {c.get('email')}")
        elif choice == "3":
            name = input("Name to search: ")
            found = mgr.find_by_name(name)
            if found:
                print("Found:", found)
            else:
                print("Contact not found.")
        elif choice == "4":
            name = input("Name to delete: ")
            ok = mgr.delete_contact(name)
            print("Deleted." if ok else "Contact not found.")
        elif choice == "5":
            name = input("Name to update: ")
            phone = input("New phone (leave blank to keep): ")
            email = input("New email (leave blank to keep): ")
            phone_arg = phone if phone.strip() != "" else None
            email_arg = email if email.strip() != "" else None
            updated = mgr.update_contact(name, phone=phone_arg, email=email_arg)
            print("Updated." if updated else "Contact not found.")
        elif choice == "6":
            # Save on exit
            save_contacts(DATA_FILE, mgr.list_contacts())
            print("Goodbye. Contacts saved.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()