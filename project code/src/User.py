from UserInputParser import UserInputParser
from Game import Game


class User:

    def __init__(self, parser: UserInputParser, username: str, legacy_points: int = 0):
        self.parser: UserInputParser = parser
        self.username: str = username
        self.legacy_points: int = legacy_points
        self.password: str = self._get_password()
        self.current_game: Game = self._get_retrieve_saved_game_state_or_create_new_game()

    def _get_retrieve_saved_game_state_or_create_new_game(self) -> Game:
        """Load the user's current game from the database or csv file or create a new game."""
        new_game = Game()
        return new_game  # Placeholder for now

    def _get_password(self):
        """Ask user for a password """
        return self.parser.parse("Enter a password: ")

    def save_game(self):
        """Save the user's current game to the database or csv file."""
        pass
