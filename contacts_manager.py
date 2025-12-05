from typing import List, Optional, Dict

class ContactsManager:
    def __init__(self):
        # primary storage: list of dicts (each dict = contact)
        self.contacts: List[Dict[str, str]] = []

    def add_contact(self, name: str, phone: str, email: str = "") -> None:
        """Add a new contact. (O(1) append)"""
        contact = {
            "name": name.strip(),
            "phone": phone.strip(),
            "email": email.strip()
        }
        self.contacts.append(contact)

    def list_contacts(self) -> List[Dict[str, str]]:
        """Return a shallow copy of contacts for display (safe)."""
        return list(self.contacts)

    def find_by_name(self, name: str) -> Optional[Dict[str, str]]:
        """Linear search by name (case-insensitive). Returns first match or None. O(n)."""
        target = name.strip().lower()
        for c in self.contacts:
            if c.get("name", "").strip().lower() == target:
                return c
        return None

    def update_contact(self, name: str, phone: Optional[str] = None, email: Optional[str] = None) -> bool:
        """
        Update first contact matching name.
        Returns True if updated, False if not found.
        """
        c = self.find_by_name(name)
        if not c:
            return False
        if phone is not None and phone != "":
            c["phone"] = phone.strip()
        if email is not None:
            c["email"] = email.strip()
        return True

    def delete_contact(self, name: str) -> bool:
        """Delete first contact matching name. Returns True if removed."""
        c = self.find_by_name(name)
        if c:
            self.contacts.remove(c)
            return True
        return False

    def clear_all(self) -> None:
        """Remove all contacts."""
        self.contacts.clear()
