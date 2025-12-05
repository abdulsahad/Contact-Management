import re

def valid_name(name: str) -> bool:
    return bool(name and name.strip())

def valid_phone(phone: str) -> bool:
    # allow digits, spaces, +, -, parentheses. Keep it simple.
    if not phone: 
        return False
    cleaned = phone.strip()
    return bool(re.fullmatch(r'[\d\+\-\s\(\)]{5,20}', cleaned))

def valid_email(email: str) -> bool:
    if not email:
        return True  # optional field accepted as empty
    # email check
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))
