from werkzeug.security import generate_password_hash, check_password_hash

def return_hashed_password(password: str):
    return generate_password_hash(password=password)

def is_valid_password(hashed_password: str, password_attempt):
    if check_password_hash(pwhash=hashed_password, password=password_attempt):
        return True
    return False