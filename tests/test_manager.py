import unittest
import os
from contacts_manager import ContactsManager
from storage import save_contacts, load_contacts

class TestContactsManager(unittest.TestCase):
    def setUp(self):
        self.mgr = ContactsManager()

    def test_add_and_find(self):
        self.mgr.add_contact("Alice", "0711111111", "alice@example.com")
        found = self.mgr.find_by_name("Alice")
        self.assertIsNotNone(found)
        self.assertEqual(found["phone"], "0711111111")

    def test_update_and_delete(self):
        self.mgr.add_contact("Bob", "0722222222")
        self.assertTrue(self.mgr.update_contact("Bob", phone="0799999999"))
        self.assertEqual(self.mgr.find_by_name("Bob")["phone"], "0799999999")
        self.assertTrue(self.mgr.delete_contact("Bob"))
        self.assertIsNone(self.mgr.find_by_name("Bob"))

    def test_persistence_roundtrip(self):
        tmp = "test_contacts_tmp.json"
        data = [{"name":"X","phone":"0700000000","email":"x@e.com"}]
        save_contacts(tmp, data)
        loaded = load_contacts(tmp)
        self.assertEqual(len(loaded), 1)
        os.remove(tmp)

    def test_bulk(self):
        for i in range(500):
            self.mgr.add_contact(f"User{i}", f"07{100000+i}", f"user{i}@example.com")
        self.assertIsNotNone(self.mgr.find_by_name("User10"))
        self.assertIsNotNone(self.mgr.find_by_name("User499"))

if __name__ == "__main__":
    unittest.main()
