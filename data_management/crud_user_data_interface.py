from abc import ABC, abstractmethod

class CrudUserDataInterface(ABC):

    def __init__(self, user_movies_dict: dict) -> None:
        self.user_movies = user_movies_dict
        

    @abstractmethod
    def initialize_file(self) -> None: 
        pass

    @abstractmethod
    def add_user(self) -> None: 
        pass

    @abstractmethod
    def add_movie(self) -> None: 
        pass

    @abstractmethod
    def return_user_movies(self) -> dict: 
        pass

    @abstractmethod
    def update_user_movie(self) -> None: 
        pass

    @abstractmethod
    def delete_user_movie(self): 
        pass

