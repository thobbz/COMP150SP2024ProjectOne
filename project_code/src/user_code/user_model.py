import json
import getpass
import sys
import os
from project_code.src.utils.parser import UserInputParser

# Add the project's root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from project_code.src.core.game import Game

class User:

    def __init__(self, input, username: str, password: str, legacy_points: int = 0):
        self.username = username
        self.password = password
        self.legacy_points = legacy_points
        self.input = input
        self.current_game = self._get_retrieve_saved_game_state_or_create_new_game()

    def _get_retrieve_saved_game_state_or_create_new_game(self) -> Game:
        new_game = Game()
        return new_game

    def save_game(self):
        #implement saving game state
        #save game state to a file
        game_state = self.current_game.get_state()

        with open(f"{self.username}_game_state.json", "w") as file:
            json.dump(game_state, file)
        pass




        
class UserFactory:

    @staticmethod
    def create_user(parser: UserInputParser) -> User:
        username = parser.parse("Enter a username: ")
        password = parser.parse("Enter a password: ", password=True)
        # Here you can add more logic as needed, e.g., validate input
        input = "some_input_value"
        return User(input, username, password)
    
    def add_user(self, username, user_data):
        # Add a user to the user manager with the given ID and data
        self.users[username] = user_data

    def get_user(self, username, password):
        # Retrieve a user's data based on their ID
        return self.users.get(username)  # Returns None if user_id is not found