from .file_manager_interface import FileManagerInterface
from uuid import uuid4


class MovieDatabaseCrud():
    def __init__(self, filepath: str, filemanager: FileManagerInterface):
        self.filepath = filepath
        self.filemanager = filemanager

    def initialize_file(self):
        self.filemanager.write_to_file(filepath=self.filepath, data={})

    def add_new_user(self, movie_database: dict, username: str):
        new_user_id = str(uuid4()).replace('-', '')
        movie_database[new_user_id] = {
            "user_name": username,
            "user_movies": {
            }
        }
        self.filemanager.write_to_file(filepath=self.filepath, data=movie_database)

    def add_movie_dictionary(self, user_id: str, movie_database: dict, movie_dictionary: dict) -> None:
        movie_id = str(uuid4()).replace('-', '')
        movie_database[user_id]["user_movies"][movie_id] = movie_dictionary
        self.filemanager.write_to_file(filepath=self.filepath, data=movie_database)

    def return_movie_database(self):
        return self.filemanager.read_file(filepath=self.filepath)
    
    def return_users(self, movie_database: dict):
        return [[user_id, user_data["user_name"]] for user_id, user_data in movie_database.items()]

    def return_user_data(self, movie_database: dict, user_id: str) -> dict:
        return movie_database[user_id]

    def return_user_movies(self, movie_database: dict, user_id: str) -> dict:
        return movie_database[user_id]["user_movies"]
    
    def update_user_movie(
            self, 
            user_id: str, 
            movie_database: dict,
            movie_id: str, 
            movie_key: str,
            movie_value: str
            ) -> None:
        # requires a movie key to be passed in order to update that key's value
        movie_database[user_id]["user_movies"][movie_id][movie_key] = movie_value
        self.filemanager.write_to_file(filepath=self.filepath, data=movie_database)

    def delete_movie_dictionary(self, user_id: str, movie_database: dict,movie_id: str):
        del movie_database[user_id]["user_movies"][movie_id]
        self.filemanager.write_to_file(filepath=self.filepath, data=movie_database)
    
