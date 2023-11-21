from .crud_user_data_interface import CrudUserDataInterface
from .file_manager_interface import FileManagerInterface
from werkzeug.security import generate_password_hash
from utils import helpers
from uuid import uuid4


class JsonCrudUserData(CrudUserDataInterface):
    def __init__(self, filemanager: FileManagerInterface):
        self.filemanager = filemanager
        self.users_database = self.filemanager.read_file()

    def initialize_file(self):
        self.filemanager.write_to_file(data={})

    def add_user(self, username: str, password: str):
        hashed_password = generate_password_hash(password=password)
        self.users_database[username] = {
            "password": hashed_password,
            "user_data": {
                "user_movies": {}
            }
        }
        self.filemanager.write_to_file(data=self.users_database)

    def add_movie(self, username: str, movie_data: dict) -> None:
        movie_id = str(uuid4()).replace('-', '')
        self.users_database[username]['user_data']["user_movies"][movie_id] = movie_data
        self.filemanager.write_to_file(data=self.users_database)

    def return_user_movies(self, username: str) -> dict:
        return self.users_database[username]['user_data']['user_movies']
    
    def return_users_database(self):
        return self.users_database
    
    def update_user_movie(
            self, 
            username: str,
            movie_id: str, 
            movie_dictionary: dict
            ) -> None:
        self.users_database[username]['user_data']['user_movies'][movie_id] = movie_dictionary
        self.filemanager.write_to_file(data=self.users_database)

    def delete_user_movie(self, username: str, movie_id: str):
        del self.users_database[username]['user_data']['user_movies'][movie_id]
        self.filemanager.write_to_file(data=self.users_database)
    
