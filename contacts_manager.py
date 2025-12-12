from typing import List, Dict, Optional

class ContactsManager:
    def __init__(self):
        self.contacts: List[Dict[str, str]] = []
        # index: maps lower-case name -> contact dict (first occurrence)
        self.index: Dict[str, Dict[str, str]] = {}

    def _index_name(self, name: str) -> str:
        return name.strip().lower()

    def add_contact(self, name: str, phone: str, email: str = "") -> None:
        contact = {"name": name.strip(), "phone": phone.strip(), "email": email.strip()}
        self.contacts.append(contact)
        key = self._index_name(contact["name"])
        # keeping first occurrence if duplicate names exist
        if key not in self.index:
            self.index[key] = contact

    def list_contacts(self) -> List[Dict[str, str]]:
        return list(self.contacts)

    def find_by_name(self, name: str) -> Optional[Dict[str, str]]:
        key = self._index_name(name)
        # O(1) lookup through index
        contact = self.index.get(key)
        if contact:
            return contact
        # fallback to linear scan (in case index not present)
        for c in self.contacts:
            if c.get("name", "").strip().lower() == key:
                return c
        return None

    def update_contact(self, name: str, phone: Optional[str] = None, email: Optional[str] = None) -> bool:
        c = self.find_by_name(name)
        if not c:
            return False
        if phone is not None:
            c["phone"] = phone.strip()
        if email is not None:
            c["email"] = email.strip()
        # update index if needed
        self.index[self._index_name(c["name"])] = c
        return True

    def delete_contact(self, name: str) -> bool:
        c = self.find_by_name(name)
        if c:
            try:
                self.contacts.remove(c)
            except ValueError:
                pass
            key = self._index_name(c.get("name", ""))
            # remove from index; but need to rebuild if duplicates exist
            if key in self.index and self.index[key] is c:
                # rebuild index entry for any other contact with same name
                self.index.pop(key, None)
                for other in self.contacts:
                    if other.get("name", "").strip().lower() == key:
                        self.index[key] = other
                        break
            return True
        return False

    def clear_all(self) -> None:
        self.contacts.clear()
        self.index.clear()
