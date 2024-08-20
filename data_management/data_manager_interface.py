from abc import ABC, abstractmethod
from typing import Any, Optional

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
    def return_user(self, user_id: int) -> Any:
        pass

    @abstractmethod
    def return_all_users(self) -> Optional[list[Any]]: 
        pass

    @abstractmethod
    def return_user_movie(self, user_id: int) -> Any:
        pass

    @abstractmethod
    def return_user_movies(self, email) -> Optional[list[Any]]: 
        pass

    @abstractmethod
    def return_all_review

    @abstractmethod
    def update_user_movie(
        self, 
        email: str,     
        movie_id: str, 
        movie_dictionary: dict
        ) -> None: 
        pass

    @abstractmethod
    def delete_user_movie(self, email: str, movie_id: str) -> None: 
        pass

