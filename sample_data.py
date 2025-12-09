from contacts_manager import ContactsManager

def generate_contacts(n: int):
    mgr = ContactsManager()
    for i in range(n):
        mgr.add_contact(f"User{i}", f"07{100000+i}", f"user{i}@example.com")
    return mgr.list_contacts()
