# User.py
import json
from project_code.src.Game import Game

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
