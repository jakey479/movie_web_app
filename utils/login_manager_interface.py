from abc import ABC, abstractmethod

# this interface is designed to allow you to initialize your connection to data in whatever way is necessary which is why I have left out the init method
class LoginManagerInterface(ABC):

    def _is_valid_email(self, email_attempt: str) -> bool:
        pass

    def _return_user_password(self, email: str) -> str:
        pass

    def _is_valid_password(self, password: str, password_attempt: str) -> bool:
        pass    

    def is_valid_login(
            self, 
            email_attempt: str, 
            password_attempt: str
            ) -> bool:
        pass