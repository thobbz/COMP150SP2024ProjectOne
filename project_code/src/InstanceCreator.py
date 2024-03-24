# InstanceCreator.py
from project_code.src.User import User
from project_code.src.UserFactory import UserFactory
from project_code.src.UserInputParser import UserInputParser


class InstanceCreator:

    def __init__(self, user_factory: UserFactory, parser: UserInputParser):
        self.user_factory = user_factory
        self.parser = parser

    def _new_user_or_login(self) -> User:
        response = self.parser.parse("Create a new username or login to an existing account?")
        if "login" in response:
            return self._load_user()
        else:
            return self.user_factory.create_user(self.parser)

    def get_user_info(self, response: str) -> User | None:
        if "yes" in response:
            return self._new_user_or_login()
        else:
            return None

    def _load_user(self) -> User:
        username = self.parser.parse("Enter your username:")
      
        if username in self.user_factory.users:
            return self.user_factory.users[username]
        else:
            print("User not found. Please try again or create a new account.")
            return None
    
        pass
