from werkzeug.security import check_password_hash

class LoginManager():
    def __init__(self, user_database: dict) -> None:
        self.user_database = user_database

    def _is_valid_username(self, username_attempt: str) -> bool:
        if username_attempt in self.user_database:
            return True
        return False        

    def _return_user_password(self, username: str) -> str:
        return self.user_database[username]["password"]
    
    def _is_valid_password(self, password: str, password_attempt: str) -> bool:
        return check_password_hash(
            pwhash=password, 
            password=password_attempt
            )

    def is_valid_login(
            self, 
            username_attempt: str, 
            password_attempt: str
            ) -> bool:
        if self._is_valid_username(
            username_attempt=username_attempt
            ):
            valid_password = self._return_user_password(username=username_attempt)
            return self._is_valid_password(
                password=valid_password, 
                password_attempt=password_attempt
                )
        return False
