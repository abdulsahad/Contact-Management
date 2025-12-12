import re

def valid_name(name: str) -> bool:
    return bool(name and name.strip())

def valid_phone(phone: str) -> bool:
    return bool(re.fullmatch(r'[\d\+\-\s\(\)]{5,20}', phone.strip()))

def valid_email(email: str) -> bool:
    if not email:
        return True
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))




