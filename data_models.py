from __future__ import annotations

from db_configuration import engine
import datetime
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase

# the pytohnic representation of the database schema will be stored in the metadata attribute within the base class. 
class Base(DeclarativeBase):
    pass

# creating an association table which manages the many to many relationship between the users and movies tables, using SQLalchemy core as the orm generally adds alayer of complexity and features that is unnecesary for this purpose. Column names contain foreign keys that are the primary keys of the tables managed by the association table. 
users_movies = Table(
    'users_movies',
    Base.metadata,
    Column('user_id', ForeignKey('users.user_id')),
    Column('movie_id', ForeignKey('movies.movie_id'))
)

class User(Base):
    __tablename__ = 'users'
    # referenced column
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)

    movies: Mapped[list[Movie]] = relationship(
        secondary=users_movies, back_populates='users'
    )

    reviews: Mapped[list[Review]] = relationship(
        back_populates='user'
    )

    def __repr__(self):
        return f'UserLogin(\'{self.user_id}\', \'{self.username}\', \'{self.email}\')'

class Movie(Base):
    __tablename__ = 'movies'
    movie_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    review_id: Mapped[int] = mapped_column(Integer, ForeignKey('reviews.review_id'), nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    director: Mapped[str] = mapped_column(String, nullable=False)
    cast: Mapped[str] = mapped_column(String, nullable=False)
    release_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    plot: Mapped[str] = mapped_column(String, nullable=False)

    users: Mapped[list[User]] = relationship(
        secondary=users_movies, back_populates='movies'
    )

    reviews: Mapped[list[Review]] = relationship(
        back_populates='movie'
    )

    def __repr__(self):
        return f'Movie(\'{self.title}\')'
    
class Review(Base):
    __tablename__ = 'reviews'
    # referenced column
    review_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    # foreign key columns
    movie_id: Mapped[int] = mapped_column(Integer, ForeignKey('movies.movie_id'), nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.user_id'), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String, nullable=False)

    user: Mapped[User] = relationship(
        back_populates='reviews'
    )

    movie: Mapped[Movie] = relationship(
        back_populates='reviews'
    )
    
    def __repr__(self):
        return f'Review(\'{self.movie_id}\', \'{self.user_id}\', \'{self.review}\', \'{self.rating}\')'
    
# create the tables from the schema in the Base class
Base.metadata.create_all(engine)