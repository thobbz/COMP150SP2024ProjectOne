# main.py
import random
import json
from enum import Enum
from typing import List
from Project_One_Code import *
import sys


        



class EventStatus(Enum):
    UNKNOWN = "unknown"
    PASS = "pass"
    FAIL = "fail"
    PARTIAL_PASS = "partial_pass"


class Event:
    def __init__(self, parser, data: dict = None):
        self.parser = parser
        if data:
            self.primary = data['primary_attribute']
            self.secondary = data['secondary_attribute']
            self.prompt_text = data['prompt_text']
            self.pass_ = data['pass']
            self.fail = data['fail']
            self.partial_pass = data['partial_pass']
        else:
            self.primary = None
            self.secondary = None
            self.prompt_text = "A default prompt text."
            self.pass_ = {"message": "You passed."}
            self.fail = {"message": "You failed."}
            self.partial_pass = {"message": "You partially passed."}

        self.status = EventStatus.UNKNOWN
        self.primary = Strength()
        self.secondary = Dexterity()

    def execute(self, party):
        chosen_one = self.parser.select_party_member(party)
        chosen_skill = self.parser.select_skill(chosen_one)

        self.set_status(EventStatus.PASS)

    def set_status(self, status: EventStatus = EventStatus.UNKNOWN):
        self.status = status

    def resolve_choice(self, party, character, chosen_skill):
        pass


class Game:

    def __init__(self):
        self.characters: List[Character] = []
        self.locations: List[Location] = []
        self.events: List[Event] = []
        self.party: List[Character] = []
        self.current_location = None
        self.current_event = None
        self._initialize_game()
        self.continue_playing = True

    def add_character(self, character: Character):
        """Add a character to the game."""
        self.characters.append(character)

    def add_location(self, location: Location):
        """Add a location to the game."""
        self.locations.append(location)

    def add_event(self, event: Event):
        """Add an event to the game."""
        self.events.append(event)

    def _initialize_game(self):
        """Initialize the game with characters, locations, and events based on the user's properties."""
        avengers_characters = ["Iron Man", "Captain America", "Thor", "Hulk", "Black Widow", "Hawkeye", "Scarlet Witch","Captain Marvel", "Black Panther", "Doctor Strange", "Spiderman", "Antman", "Wasp", "Falcon", "Winter Soldier", "Star-Lord", "Rocket", "Groot", "Nebula"]
        for character_name in avengers_characters:
            character = Character(character_name)
            self.add_character(character)

        # add locations
        avengers_locations = ["New York City", "San Francisco", "Wakanda", "Asgard", "Vormir", "New Jersey","Earth"]
        for location_name in avengers_locations:
            self.add_location(Location(location_name))

        # add events
        avengers_events = ["Avengers vs. Thanos","Battle of New York","Asgard","Morag","Vormir","Final Battle"]
        for event_name in avengers_events:
            self.add_event(Event(event_name))

        self.current_location = random.choice(self.locations)
        pass

    def start_game(self):
        return self._main_game_loop()

    def _main_game_loop(self):
        """The main game loop."""
        while self.continue_playing:
            # print game state
            print("Current location:", self.current_location)
            print("Current event:", self.current_event.name if self.current_event else "None")

            if all(character.is_dead for character in self.party):
                # award legacy points and end instance of game
                self.continue_playing = False
                return "Game Over"

            pass
            # ask for user input
            # parse user input
            # update game state
            # check if party is all dead
            # if party is dead, award legacy points and end instance of game
            # if party is not dead, continue game
        if not self.continue_playing:
            return True
        elif self.continue_playing == "Save and quit":
            return "Save and quit"
        else:
            return False

    def update_game_state(self, user_input):
        pass

class User:

    def __init__(self, input , username: str, password: str, legacy_points: int = 0):
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

    






class EventStatus(Enum):
    UNKNOWN = "unknown"
    PASS = "pass"
    FAIL = "fail"
    PARTIAL_PASS = "partial_pass"


class Event:
    def __init__(self,legacy_points, parser, data: dict = None):
        self.parser = parser
        if data:
            self.primary = data['primary_attribute']
            self.secondary = data['secondary_attribute']
            self.prompt_text = data['prompt_text']
            self.pass_ = data['pass']
            self.fail = data['fail']
            self.partial_pass = data['partial_pass']
        else:
            self.primary = None
            self.secondary = None
            self.prompt_text = "A default prompt text."
            self.pass_ = {"message": "You passed."}
            self.fail = {"message": "You failed."}
            self.partial_pass = {"message": "You partially passed."}

        self.status = EventStatus.UNKNOWN
        self.primary = Strength(legacy_points)
        self.secondary = Dexterity()

    def execute(self, party):
        chosen_one = self.parser.select_party_member(party)
        chosen_skill = self.parser.select_skill(chosen_one)

        self.set_status(EventStatus.PASS)

    def set_status(self, status: EventStatus = EventStatus.UNKNOWN):
        self.status = status

    def resolve_choice(self, party, character, chosen_skill):
        pass





class Game:

    def __init__(self):
        self.characters: List[Character] = []
        self.locations: List[Location] = []
        self.events: List[Event] = []
        self.party: List[Character] = []
        self.current_location = None
        self.current_event = None
        self._initialize_game()
        self.continue_playing = True

    def add_character(self, character: Character):
        """Add a character to the game."""
        self.characters.append(character)

    def add_location(self, location: Location):
        """Add a location to the game."""
        self.locations.append(location)

    def add_event(self, event: Event):
        """Add an event to the game."""
        self.events.append(event)

    def _initialize_game(self):
        """Initialize the game with characters, locations, and events based on the user's properties."""
        avengers_characters = ["Iron Man", "Captain America", "Thor", "Hulk", "Black Widow", "Hawkeye", "Scarlet Witch","Captain Marvel", "Black Panther", "Doctor Strange", "Spiderman", "Antman", "Wasp", "Falcon", "Winter Soldier", "Star-Lord", "Rocket", "Groot", "Nebula"]
        for character_name in avengers_characters:
            character = Character(character_name)
            self.add_character(character)

        # add locations
        avengers_locations = ["New York City", "San Francisco", "Wakanda", "Asgard", "Vormir", "New Jersey","Earth"]
        for location_name in avengers_locations:
            self.add_location(Location(location_name))

        # add events
        avengers_events = ["Avengers vs. Thanos","Battle of New York","Asgard","Morag","Vormir","Final Battle"]
        for event_name in avengers_events:
            self.add_event(Event(event_name))

        self.current_location = random.choice(self.locations)
        pass

    def start_game(self):
        return self._main_game_loop()

    def _main_game_loop(self):
        """The main game loop."""
        while self.continue_playing:
            # print game state
            print("Current location:", self.current_location)
            print("Current event:", self.current_event.name if self.current_event else "None")

            if all(character.is_dead for character in self.party):
                # award legacy points and end instance of game
                self.continue_playing = False
                return "Game Over"

            pass
            # ask for user input
            # parse user input
            # update game state
            # check if party is all dead
            # if party is dead, award legacy points and end instance of game
            # if party is not dead, continue game
        if not self.continue_playing:
            return True
        elif self.continue_playing == "Save and quit":
            return "Save and quit"
        else:
            return False

    def update_game_state(self, user_input):
        pass






class UserInputParser:

    def __init__(self):
        self.style = "console"

    def parse(self, prompt) -> str:
        response: str = input(prompt)
        return response



class UserFactory:

    @staticmethod
    def create_user(parser: UserInputParser) -> User:
        username = parser.parse("Enter a username: ")
        password = parser.parse("Enter a password: ")
        legacy_points = 0
        # Here you can add more logic as needed, e.g., validate input
        return User(username, password, legacy_points)



class InstanceCreator:

    def __init__(self, user_factory: UserFactory, parser: UserInputParser):
        self.user_factory = user_factory
        self.parser = parser

    def _new_user_or_login(self) -> User:
        response = self.parser.parse("Create a new username or login to an existing account?")
        if "login" in response:
            return self._load_user()
        else:
            return self.user_factory.create_user(self.parser)

    def get_user_info(self, response: str) -> User | None:
        if "yes" in response:
            return self._new_user_or_login()
        else:
            return None

    def _load_user(self) -> User:
        username = self.parser.parse("Enter your username:")
      
        if username in self.user_factory.users:
            return self.user_factory.users[username]
        else:
            print("User not found. Please try again or create a new account.")
            return None
    
        pass


    def start_game():
        parser = UserInputParser()
        user_factory = UserFactory()
        instance_creator = InstanceCreator(user_factory, parser)

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
