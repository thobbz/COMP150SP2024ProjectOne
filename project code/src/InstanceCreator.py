import UserInputParser

from User import User
from Game import Game


class InstanceCreator:

    def __init__(self, parser: UserInputParser):
        self.game = None
        self.parser = parser
        self.user = None

    def _new_user_or_login(self) -> User:
        response = self.parser.parse("Create a new username or login to an existing account?")
        if "login" in response:
            return self._load_user()
        else:
            return self._create_new_user()

    def get_user_info(self, response: str) -> User | None:
        if "yes" in response:
            self.user = self._new_user_or_login()
            if self.user.current_game is not None:
                self.user.current_game = self.create_new_game()
                return self.user
            else:
                return None
        else:
            return None

    def _load_user(self) -> User:
        """Load an existing user from the database or csv file."""
        pass

    def _create_new_user(self) -> User:
        """Create a new user and save it to the database or csv file."""
        return User(self.parser, self.parser.parse("Enter a username: "))

    def create_new_game(self) -> Game:
        """Create a new game instance."""
        self.game: Game = Game()
        return self.game
