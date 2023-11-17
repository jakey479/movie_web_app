from abc import ABC, abstractmethod

class CrudUserMovieDataInterface(ABC):

    def __init__(self, user_movies_dict: dict) -> None:
        self.user_movies = user_movies_dict
        

    @abstractmethod
    def initialize_file() -> None: 
        pass

    @abstractmethod
    def add_user(self) -> None: 
        pass

    @abstractmethod
    def add_movie(self) -> None: 
        pass

    # @abstractmethod
    # def add_movie_review():
    #     pass

    # @abstractmethod
    # def add_movie_rating():
    #     pass    

    @abstractmethod
    def return_user_movies(self) -> dict: 
        pass

    @abstractmethod
    def return_username(self):
        pass

    @abstractmethod
    def return_password(self):
        pass

    @abstractmethod
    def return_user_movie(self): 
        pass

    @abstractmethod
    def update_user_movie(self) -> None: 
        pass

    @abstractmethod
    def delete_user_movie(self): 
        pass

