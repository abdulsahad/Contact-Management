import json
from typing import List, Dict

def save_contacts(path: str, contacts: List[Dict]) -> None:
    """Save contacts list (list of dicts) to JSON file."""
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(contacts, f, indent=2)
    except Exception as e:
        print(f"Error saving contacts to {path}: {e}")

def load_contacts(path: str) -> List[Dict]:
    """Load contacts from JSON file. Return empty list if file missing or invalid."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading contacts from {path}: {e}")
        return []
