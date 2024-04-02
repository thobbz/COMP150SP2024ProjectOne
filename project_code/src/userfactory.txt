# UserFactory.py
from project_code.src.user_code.user_model import User       
from project_code.src.utils.parser import UserInputParser


class UserFactory:

    @staticmethod
    def create_user(parser: UserInputParser) -> User:
        username = parser.parse("Enter a username: ")
        password = parser.parse("Enter a password: ", password=True)
        # Here you can add more logic as needed, e.g., validate input
        input = "some_input_value"
        return User(input, username, password)
    
    def __init__(self):
        self.users = {}
    
    def get_user(self, username: str) -> User | None:
        return self.users.get(username)
