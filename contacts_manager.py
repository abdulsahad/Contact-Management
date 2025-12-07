from typing import List, Dict, Optional

class ContactsManager:
    def __init__(self):
        self.contacts: List[Dict[str, str]] = []
        self.index: Dict[str, Dict[str, str]] = {}

    def _index_name(self, name: str) -> str:
        return name.strip().lower()

    def add_contact(self, name: str, phone: str, email: str = "") -> None:
        contact = {"name": name.strip(), "phone": phone.strip(), "email": email.strip()}
        self.contacts.append(contact)
        key = self._index_name(name)
        if key not in self.index:
            self.index[key] = contact

    def list_contacts(self) -> List[Dict[str, str]]:
        return list(self.contacts)

    def find_by_name(self, name: str) -> Optional[Dict[str, str]]:
        key = self._index_name(name)
        return self.index.get(key, None)

    def update_contact(self, name: str, phone: Optional[str] = None, email: Optional[str] = None) -> bool:
        c = self.find_by_name(name)
        if not c:
            return False
        if phone is not None:
            c["phone"] = phone.strip()
        if email is not None:
            c["email"] = email.strip()
        self.index[self._index_name(c["name"])] = c
        return True

    def delete_contact(self, name: str) -> bool:
        c = self.find_by_name(name)
        if c:
            self.contacts.remove(c)
            key = self._index_name(c["name"])
            if key in self.index:
                self.index.pop(key)
            return True
        return False

    def clear_all(self) -> None:
        self.contacts.clear()
        self.index.clear()
