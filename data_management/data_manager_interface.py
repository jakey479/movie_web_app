from abc import ABC, abstractmethod

class DataManagerInterface(ABC):

    @abstractmethod
    def add_user(
        self, 
        name: str, 
        username: str, 
        email: str, 
        password: str
        ) -> None: 
        pass

    @abstractmethod
    def add_movie(
        self, 
        email: str, 
        movie_data: dict
        ) -> None: 
        pass

    @abstractmethod
    def return_all_users(self) -> dict: 
        pass

    @abstractmethod
    def return_user_movies(self, email) -> dict: 
        pass

    @abstractmethod
    def update_user_movie(
        self, 
        email: str, 
        movie_id: str, 
        movie_dictionary: dict
        ) -> None: 
        pass

    @abstractmethod
    def delete_user_movie(self, email: str, movie_id: str): 
        pass

