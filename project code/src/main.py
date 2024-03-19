import sys

from UserInputParser import UserInputParser
from InstanceCreator import InstanceCreator
from Game import Game
from User import User


def start_game():
    parser = UserInputParser()
    response: str = parser.parse("Would you like to start a new game? (yes/no)")
    print(f"Response: {response}")
    instance_creator: InstanceCreator = InstanceCreator(parser)
    user: User = instance_creator.get_user_info(response)
    if user is not None:
        game_instance: Game = user.current_game
        if game_instance is not None:
            response = game_instance.start_game()
            if response == "Save and quit":
                user.save_game()
                print("Game saved. Goodbye!")
                sys.exit()
            elif response:
                print("Goodbye!")
                sys.exit()
    else:
        print("See you next time!")
        sys.exit()


if __name__ == '__main__':
    start_game()
