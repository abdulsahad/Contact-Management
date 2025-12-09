import json
from typing import List, Dict

def save_contacts(path: str, contacts: List[Dict]) -> None:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(contacts, f, indent=2)
    except Exception as e:
        print(f"Error saving contacts: {e}")

def load_contacts(path: str) -> List[Dict]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading contacts: {e}")
        return []
