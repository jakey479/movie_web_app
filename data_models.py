from __future__ import annotations
import datetime
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase

# the pythonic representation of the database schema will be stored in the metadata attribute within the base class. 
class Base(DeclarativeBase):
    pass

# the following tables do not hold foreign keys
class UserInfo(Base): 
    __tablename__ = 'users_info'
    user_info_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    contact_number: Mapped[int] = mapped_column(Integer, nullable=False)
    street_number: Mapped[int] = mapped_column(Integer, nullable=False)
    street_name: Mapped[str] = mapped_column(String, nullable=False)
    profession: Mapped[str] = mapped_column(String, nullable=False) 

    user_profiles: Mapped[list[UserProfile]] = relationship('UserProfile', back_populates='user_info')

class UserLogin(Base):
    __tablename__ = 'user_logins'
    user_login_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)

    user_profiles: Mapped[list[UserProfile]] = relationship('UserProfile', back_populates='user_login')

    def __repr__(self):
        return f'UserLogin(\'{self.user_login_id}\', \'{self.email}\')'

class Movie(Base):
    __tablename__ = 'movies'
    movie_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    director: Mapped[str] = mapped_column(String, nullable=False)
    cast: Mapped[str] = mapped_column(String, nullable=False)
    release_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    plot: Mapped[str] = mapped_column(String, nullable=False)
    rotten_tomatoes_rating: Mapped[int] = mapped_column(Integer, nullable=False)

    reviews: Mapped[list[Review]] = relationship('Review', back_populates='movie')


    def __repr__(self):
        return f'Movie(\'{self.title}\')'

# the following tables hold foreign keys
class Review(Base):
    __tablename__ = 'reviews'
    review_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_profile_id: Mapped[int] = mapped_column(Integer, ForeignKey('user_profiles.user_profile_id'), nullable=False)
    movie_id: Mapped[int] = mapped_column(Integer, ForeignKey('movies.movie_id'), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String, nullable=False)

    user_profile: Mapped[UserProfile] = relationship(back_populates='reviews')
    movie: Mapped[Movie] = relationship(back_populates='reviews')
    
    def __repr__(self):
        return f'Review(\'{self.movie_id}\', \'{self.user_profile_id}\', \'{self.review}\', \'{self.rating}\')'

class UserProfile(Base):
    __tablename__ = 'user_profiles'
    user_profile_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_profile_name: Mapped[str] = mapped_column(String, nullable=False)
    user_login_id: Mapped[int] = mapped_column(Integer, ForeignKey('user_logins.user_login_id'), nullable=False)
    user_info_id: Mapped[int] = mapped_column(Integer, ForeignKey('users_info.user_info_id'), nullable=False)

    reviews: Mapped[list[Review]] = mapped_column()
    user_login: Mapped[UserLogin] = relationship(back_populates='user_profiles')
    user_info: Mapped[UserInfo] = relationship(back_populates='user_profiles')
    

    def __repr__(self):
        return f'UserProfile(\'{self.user_profile_id}\')'

# creating association table which manages the many to many relationship between the users and movies tables, using SQLalchemy core, as the orm generally adds alayer of complexity and features that is unnecesary for this purpose.
users_movies = Table(
    'user_profiles_movies',
    Base.metadata,
    Column('user_id', ForeignKey('users.user_id')),
    Column('movie_id', ForeignKey('movies.movie_id'))
)


    

    
print(Base.metadata)