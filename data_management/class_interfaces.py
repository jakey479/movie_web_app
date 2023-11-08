from abc import ABC, abstractmethod
from utils import helpers

class FileManagerInterface(ABC):

    @abstractmethod
    def read_file(self, filename):
        pass

    @abstractmethod
    def write_to_file(self, filename, data):
        pass

class UserDataManager(ABC):
    def __init__(self, user_id: str, username: str, password: str) -> None:
        self.user_id = user_id
        self.username = username
        self.password = password

    @abstractmethod
    def is_valid_password(self, password_attempt):
        pass
