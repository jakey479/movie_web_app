from .crud_user_movie_data_interface import CrudUserMovieDataInterface
from .file_manager_interface import FileManagerInterface
from uuid import uuid4
import json


class JsonCrudUserMovieData(CrudUserMovieDataInterface):
    def __init__(self, filemanager: FileManagerInterface):
        self.filemanager = filemanager
        self.user_movie_dict: dict

    # def add_user(self, username: str, user_password: str):
    #     new_user_id = str(uuid4()).replace('-', '')
    #     movie_database = self.return_movie_database()
    #     movie_database[new_username] = {
    #         "username": username,
    #         "password": user_password,
    #         "movies": {
    #         }
    #     }
        # self.filemanager.write_to_file(data=movie_database)

    def add_movie(self, user_id: str, movie_data: dict) -> None:
        movie_database = self.return_movie_database()
        movie_id = str(uuid4()).replace('-', '')
        movie_database[user_id]["movies"][movie_id] = movie_data
        self.filemanager.write_to_file(data=movie_database)

    def return_movie_database(self) -> dict:
        # loads the database dictionary into a python file using json.load()
        try:
            return self.filemanager.read_file()
        except json.JSONDecodeError:
            self.initialize_file()
            return self.filemanager.read_file() 

    def return_user_movies(self, user_id: str) -> dict:
        movie_database = self.return_movie_database
        return movie_database[user_id]["movies"]
    
    def update_user_movie(
            self, 
            user_id: str,
            movie_id: str, 
            movie_dictionary: dict
            ) -> None:
        movie_database = self.return_movie_database
        movie_database[user_id]["movies"][movie_id] = movie_dictionary
        self.filemanager.write_to_file(data=movie_database)

    def delete_movie_dictionary(self, user_id: str, movie_id: str):
        movie_database = self.return_movie_database
        del movie_database[user_id]["movies"][movie_id]
        self.filemanager.write_to_file(data=movie_database)
    
