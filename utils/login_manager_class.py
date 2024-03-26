from data_models import User
from db_configuration import Session
from login_manager_interface import LoginManagerInterface
from sqlalchemy import select, exists
from werkzeug.security import check_password_hash

class SqliteLoginManager(LoginManagerInterface):

    def _is_valid_user(self, email_attempt: str) -> bool:
        # returns True or False depending on whether there is a row where User.email matches email_attempt 
        is_valid_email_query = select(exists().where(User.email == email_attempt))
        # scalar() converts the returns the first column of the first row from the result of the query and returns None if the result is empty
        is_valid_email = Session.execute(is_valid_email_query).scalar()
        # Return True if a user with the given email exists, False otherwise
        return is_valid_email
    
    def _return_hashed_user_password(self, email: str) -> str:
        # return user object based on email
        hashed_password_query = select(User.password).where(User.email == email)
        return Session.execute(hashed_password_query).scalar()
    
    def _is_valid_password(self, hashed_user_password: str, password_attempt: str) -> bool:
        return check_password_hash(
            pwhash=hashed_user_password, 
            password=password_attempt
            )

    def is_valid_login(
            self, 
            email_attempt: str, 
            password_attempt: str
            ) -> bool:
        if self._is_valid_email(
            email_attempt=email_attempt
            ):
            hashed_user_password = self._return_hashed_user_password(email=email_attempt)
            return self._is_valid_password(
                password=_password, 
                password_attempt=password_attempt
                )
        return False

# class JsonLoginManager(LoginManagerInterface):

#     def __init__(self, data_manager: DataManagerInterface):
#         self.data_manager = data_manager

#     def _is_valid_email(self, email_attempt: str) -> bool:
#         user_database = self.file_manager.read_file()
#         if email_attempt in user_database:
#             return True
#         return False        

#     def _return_user_password(self, email: str) -> str:
#         user_database = self.file_manager.read_file()
#         return user_database[email]["password"]
    
#     def _is_valid_password(self, password: str, password_attempt: str) -> bool:
#         return check_password_hash(
#             pwhash=password, 
#             password=password_attempt
#             )

#     def is_valid_login(
#             self, 
#             email_attempt: str, 
#             password_attempt: str
#             ) -> bool:
#         if self._is_valid_username(
#             username_attempt=email_attempt
#             ):
#             valid_password = self._return_user_password(username=email_attempt)
#             return self._is_valid_password(
#                 password=valid_password, 
#                 password_attempt=password_attempt
#                 )
#         return False
    

