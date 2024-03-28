# UserFactory.py
from project_code.src.userinputparser import UserInputParser
from project_code.src.user import User


class UserFactory:

    @staticmethod
    def create_user(parser: UserInputParser) -> User:
        username = parser.parse("Enter a username: ")
        password = parser.parse("Enter a password: ", password=True)
        # Here you can add more logic as needed, e.g., validate input
        input = "some_input_value"
        return User(input, username, password)
