<<<<<<< HEAD
import sys
import os
import sys
import os

# Add the project's root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from project_code.src.user_code.user_model import User
from project_code.src.utils.parser import UserInputParser
from project_code.src.core.instancecreator import InstanceCreator
from project_code.src.user_code.user_model import UserFactory
from project_code.src.core.game import Game

=======

import sys
import os

# main.py
from project_code.src.user_code.user_model import User
from project_code.src.user_code.user_model import UserFactory   
from project_code.src.core.instancecreator import InstanceCreator     
from project_code.src.utils.parser import UserInputParser
from project_code.src.core.game import Game
import sys  
>>>>>>> bde05581abe9edea3c5f7cca74d871afb86f1624



def start_game():
    parser = UserInputParser()
    user_factory = UserFactory()
    instance_creator = InstanceCreator(user_factory, parser)
    game_instance = Game()

    response = parser.parse("Would you like to start a new game? (yes/no)")
    print(f"Response: {response}")
    user = instance_creator.get_user_info(response)
    if user is not None:
        game_instance = user.current_game
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

