import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from project_code.src.user_code.user_model import User
from project_code.src.user_code.user_model import UserFactory        
from project_code.src.utils.parser import UserInputParser



class InstanceCreator:
    def __init__(self, user_factory: UserFactory, parser: UserInputParser):
        self.user_factory = user_factory
        self.parser = parser

    def _new_user_or_login(self) -> User:
        response = self.parser.parse("Create a new username or login to an existing account?")
        if "login" in response:
            username = self.parser.parse("Enter your username: ")
            return self._load_user(username)
        else:
            return self.user_factory.create_user(self.parser)

    def get_user_info(self, response: str) -> User:
        if "yes" in response.lower():
            return self._new_user_or_login()
        else:
            return User(username="default", password="", input=self.parser)

    def _load_user(self, username: str) -> User:
        try:
            with open(f"{username}_game_state.json", "r") as file:
                game_state = json.load(file)
            return User(self.parser, username=username, password="", legacy_points=game_state["legacy_points"])
        except FileNotFoundError:
            print("User data not found. Creating a new user.")
            return User(self.parser, username=username, password="")
        pass