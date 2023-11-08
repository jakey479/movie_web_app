from .class_interfaces import FileManagerInterface
from uuid import uuid4
import json


class MovieDatabaseCrud():
    def __init__(self, filepath: str, filemanager: FileManagerInterface):
        self.filepath = filepath
        self.filemanager = filemanager
        self.movie_database = self._return_movie_database()

    def initialize_file(self):
        self.filemanager.write_to_file(filepath=self.filepath, data={})

    def add_new_user(self, username: str, user_password: str):
        new_user_id = str(uuid4()).replace('-', '')
        movie_database = self.movie_database
        movie_database[new_user_id] = {
            "username": username,
            "password": user_password,
            "movies": {
            }
        }
        self.filemanager.write_to_file(filepath=self.filepath, data=movie_database)

    def add_movie_dictionary(self, user_id: str, movie_dictionary: dict) -> None:
        movie_database = self.movie_database
        movie_id = str(uuid4()).replace('-', '')
        movie_database[user_id]["movies"][movie_id] = movie_dictionary
        self.filemanager.write_to_file(filepath=self.filepath, data=movie_database)

    def _return_movie_database(self) -> dict:
        try:
            return self.filemanager.read_file(filepath=self.filepath)
        except json.JSONDecodeError:
            self.initialize_file()
            return self.filemanager.read_file(filepath=self.filepath) 
    
    def return_users(self) -> list[list[str, str]]:
        movie_database = self.movie_database
        return [[user_id, user_data["username"]] for user_id, user_data in movie_database.items()]

    def return_user_data(self,  user_id: str) -> dict:
        movie_database = self.movie_database
        return movie_database[user_id]
    
    def return_username(self,  user_id: str) -> dict:
        movie_database = self.movie_database
        return movie_database[user_id]['username']
    
    def return_user_password(self,  user_id: str) -> dict:
        movie_database = self.movie_database
        return movie_database[user_id]['password']

    def return_user_movies(self, user_id: str) -> dict:
        movie_database = self.movie_database
        return movie_database[user_id]["movies"]
    
    def update_user_movie(
            self, 
            user_id: str,
            movie_id: str, 
            movie_dictionary: dict
            ) -> None:
        movie_database = self.movie_database
        movie_database[user_id]["movies"][movie_id] = movie_dictionary
        self.filemanager.write_to_file(filepath=self.filepath, data=movie_database)

    def delete_movie_dictionary(self, user_id: str, movie_id: str):
        movie_database = self.movie_database
        del movie_database[user_id]["movies"][movie_id]
        self.filemanager.write_to_file(filepath=self.filepath, data=movie_database)
    
