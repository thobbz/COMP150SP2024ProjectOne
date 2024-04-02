import sys
import os
project_code_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_code_dir)





from project_code.src.utils.parser import UserInputParser
from project_code.src.core.instancecreator import InstanceCreator
from project_code.src.user_code.user_model import UserFactory
from project_code.src.core.game import Game




def start_game():
    parser = UserInputParser()
    user_factory = UserFactory()
    instance_creator = InstanceCreator(user_factory, parser)
    game_instance = Game()
    game_instance.load_locations('locations.json')
    game_instance.load_events('events.json')


    response = parser.parse("Would you like to start a new game? (yes/no)")
    introduction = (f"The Mad Titan's wake of destruction has left the universe in ruins.\n"
                f"Thanos, drunk on power after finally collecting all six Infinity Stones,\n"
                f"has used their combined might to reshape reality itself to his twisted vision.\n"
                f"Planets have been turned to dust, civilizations erased in an instant.\n\n"
                f"Those who remain are a scattered few - the last survivors of Thanos' genocidal rebalancing.\n"
                f"The few heroes left, those who dared to oppose his insane crusade, have regrouped and gone into hiding.\n"
                f"All seems lost against such unspeakable power. The Infinity Stones, once the universe's most dangerous weapons when split apart,\n"
                f"are now united as one under Thanos' iron grip.\n\n"
                f"But a rally cry has sounded from the ashes. A band of unlikely fighters has pledged to undertake an inconceivable mission -\n"
                f"to infiltrate Thanos' impregnable fortress, overpower his elite forces, and wrestle the Infinity Stones from his grasp.\n"
                f"Outnumbered and outmatched, this ragtag squad of the universe's last defenders has pinned their hopes on one desperate objective:\n"
                f"To reverse the snap that decimated all life and stop the Mad Titan's reign before he remakes the cosmos in his nightmarish image.\n\n"
                f"The risks are immeasurable, the costs invaluable. But without betting it all, there is no chance of victory...\n"
                f"and no future across the entire universe. The time to rally has come at last!")
    
    print(introduction)
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

