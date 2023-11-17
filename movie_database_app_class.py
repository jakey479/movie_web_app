from data_management.file_manager_interface import FileManagerInterface
from utils import helpers

class MovieDatabaseApp():

    def __init__( 
        self, 
        filemanager: FileManagerInterface
        ) -> None:
        self.filemanager = filemanager
        self.database = self.filemanager.read_file()
        self.user_movies_data: dict = None

    def _is_valid_username(self, username_attempt: str) -> bool:
        if username_attempt in self.database:
            return True
        return False        

    def _return_user_password(self, username) -> str:
        return self.database[username]["password"]
    
    def _is_valid_password(self, password: str, password_attempt: str) -> bool:
        return helpers.is_valid_password(
            hashed_password=password, 
            password_attempt=password_attempt
            )
    
    def is_valid_login(self, username_attempt: str, password_attempt: str) -> bool:
        if self._is_valid_username(username_attempt=username_attempt):
            valid_password = self._return_user_password(username=username_attempt)
            if self._is_valid_password(password=valid_password, password_attempt=password_attempt):
                return True
        return False

    def set_user_movies_data(self, username: str):
        self.user_movies_data = self.database[username]["user_data"]["user_movies"]

    