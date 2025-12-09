from contacts_manager import ContactsManager
from storage import load_contacts, save_contacts
from utils import valid_name, valid_phone, valid_email
from sample_data import generate_contacts

DATA_FILE = "contacts.json"

def show_menu():
    print("\n=====// Contact Management App //=====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")
    print("7. Sort contacts & compare algorithms")

def main():
    mgr = ContactsManager()
    # load existing contacts
    initial = load_contacts(DATA_FILE)
    for d in initial:
        mgr.add_contact(d.get("name", ""), d.get("phone", ""), d.get("email", ""))

    # also generate sample contacts for demonstration
    sample_contacts = generate_contacts(20)
    for c in sample_contacts:
        mgr.add_contact(c['name'], c['phone'], c['email'])

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            if not valid_name(name):
                print("Name cannot be empty.")
                continue
            phone = input("Phone: ").strip()
            if not valid_phone(phone):
                print("Phone looks invalid.")
                continue
            email = input("Email (optional): ").strip()
            if not valid_email(email):
                print("Email looks invalid.")
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
            name = input("Name to search: ").strip()
            found = mgr.find_by_name(name)
            if found:
                print(f"Found: {found['name']} - {found['phone']} - {found['email']}")
            else:
                print("Contact not found.")
        elif choice == "4":
            name = input("Name to delete: ").strip()
            ok = mgr.delete_contact(name)
            print("Deleted." if ok else "Contact not found.")
        elif choice == "5":
            name = input("Name to update: ").strip()
            phone = input("New phone (leave blank to keep): ").strip()
            email = input("New email (leave blank to keep): ").strip()
            phone_arg = phone if phone != "" else None
            email_arg = email if email != "" else None
            updated = mgr.update_contact(name, phone=phone_arg, email=email_arg)
            print("Updated." if updated else "Contact not found.")
        elif choice == "6":
            save_contacts(DATA_FILE, mgr.list_contacts())
            print("Goodbye. Contacts saved.")
            break
        elif choice == "7":
            contacts = mgr.list_contacts()
            if not contacts:
                print("No contacts to sort.")
            else:
                from sorts import bubble_sort, merge_sort, time_sort
                sample = contacts[:20]  # small sample
                t_b = time_sort(bubble_sort, sample)
                t_m = time_sort(merge_sort, sample)
                print(f"Bubble sort: {t_b:.6f}s, Merge sort: {t_m:.6f}s")
                sorted_sample = merge_sort(sample)[:10]
                print("First 10 contacts sorted by name (merge sort):")
                for c in sorted_sample:
                    print(f"{c['name']} - {c['phone']}")
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
