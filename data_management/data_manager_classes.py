from .data_manager_interface import DataManagerInterface
from data_models import User, Movie, Review
from db_configuration import Session
from sqlalchemy import select, update, and_

class SqliteDataManager(DataManagerInterface):

    def add_user(self, name: str, username: str, email: str, hashed_password: str):
        new_user = User(
            name=name,
            username=username,
            email=email,
            hashed_password=hashed_password
        )
        Session.add(new_user)
        Session.commit()
        Session.remove()
        

    def add_movie(self, user_email: str, movie_data: dict) -> None:
        new_movie = Movie(
            user_id=self.return_user_id(email=user_email),
            title=movie_data['title'],
            director=movie_data['director'],
            cast=movie_data['cast'],
            release_date=movie_data['release_date'],
            plot=movie_data['plot']
        )
        self.session.add(new_movie)
        self.session.commit()

    def return_user_movies(self, email: str) -> list:
        # creating a query statement
        query_statement = select(User.movies).where(User.email == email)
        # executing the query statement and returning the results in a 'Result' object
        user_movies = self.session.execute(query_statement)
        # 
        return user_movies.scalars().all()
    
    def return_user(self, email) -> User:
        query_statement = select(User).where(User.email == email)
        user = self.session.execute(query_statement)
        return user.scalar()

    def return_movie_to_update(self, user: User, movie_id: int) -> Movie:
        movie_to_upate = user.movie_dicts[movie_id]
        return movie_to_upate


    
