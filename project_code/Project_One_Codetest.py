import json
import sys
from typing import List
import random
from enum import Enum

# Define the Location class
class Location:
    def __init__(self, parser, number_of_events: int = 1):
        self.parser = parser
        self.events = [Event(self.parser) for _ in range(number_of_events)]

    def create_custom_event_from_static_text_file(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
        return Event(self.parser, data)

# Define the EventStatus enum
class EventStatus(Enum):
    UNKNOWN = "unknown"
    PASS = "pass"
    FAIL = "fail"
    PARTIAL_PASS = "partial_pass"

# Define the Event class
class Event:
    def __init__(self, parser, data: dict = None):
        self.parser = parser
        if data:
            self.primary = data.get('primary_attribute', '')
            self.secondary = data.get('secondary_attribute', '')
            self.prompt_text = data.get('prompt_text', '')
            self.pass_message = data.get('pass', {}).get('message', 'You passed.')
            self.fail_message = data.get('fail', {}).get('message', 'You failed.')
            self.partial_pass_message = data.get('partial_pass', {}).get('message', 'You partially passed.')
        else:
            self.primary = ''
            self.secondary = ''
            self.prompt_text = 'A dragon appears, what will you do?'
            self.pass_message = 'You passed.'
            self.fail_message = 'You failed.'
            self.partial_pass_message = 'You partially passed.'
        self.status = EventStatus.UNKNOWN

    def execute(self):
        chosen_one = self.parser.select_party_member(self.party)
        chosen_skill = self.parser.select_skill(chosen_one)

        self.resolve_choice(self.party, chosen_one, chosen_skill)

    def set_status(self, status: EventStatus = EventStatus.UNKNOWN):
        self.status = status

    def resolve_choice(self, party, character, chosen_skill):
        skill_attributes = chosen_skill.attributes
        event_attributes = {"primary": self.primary, "secondary": self.secondary}
        
        overlap = any(attribute in skill_attributes for attribute in event_attributes.values())
        
        if not overlap:
            self.set_status(EventStatus.FAIL)
        elif overlap and len(set(skill_attributes) & set(event_attributes.values())) == 1:
            self.set_status(EventStatus.PARTIAL_PASS)
        else:
            self.set_status(EventStatus.PASS)

# Define the Statistic class and its subclasses
class Statistic:
    def __init__(self, value: int):
        self.value = value
        self.description = None
        self.min_value = 0
        self.max_value = 100

class Strength(Statistic):
    def __init__(self, value: int):
        super().__init__(value)
        self.description = "Strength is a measure of physical power."

class Dexterity(Statistic):
    def __init__(self, value: int):
        super().__init__(value)
        self.description = "Dexterity measures agility, coordination, and quickness."

class Constitution(Statistic):
    def __init__(self, value: int):
        super().__init__(value)
        self.description = "Constitution represents the body's resilience and natural armor."

# Define the Character class
class Character:
    def __init__(self, name: str = None):
        self.name = self._generate_name() if name is None else name
        self.strength = Strength(value=random.randint(1, 10))
        self.dexterity = Dexterity(value=random.randint(1, 10))
        self.constitution = Constitution(value=random.randint(1, 10))

    def _generate_name(self):
        # Your name generation logic here
        return "Spider-Man"

# Define the Game class
class Game:
    def __init__(self, parser):
        self.parser = parser
        self.characters: List[Character] = []
        self.locations: List[Location] = []
        self.events: List[Event] = []
        self.party: List[Character] = []
        self.current_location = None
        self.current_event = None
        self.continue_playing = True
        self._initialize_game()

    def add_character(self, character: Character):
        self.characters.append(character)

    def add_location(self, location: Location):
        self.locations.append(location)

    def add_event(self, event: Event):
        self.events.append(event)

    def _initialize_game(self):
        character_list = [Character() for _ in range(10)]
        location_list = [Location(self.parser) for _ in range(2)]

        for character in character_list:
            self.add_character(character)

        for location in location_list:
            self.add_location(location)

    def start_game(self):
        return self._main_game_loop()

    def _main_game_loop(self):
        while self.continue_playing:
            self.current_location = self.locations[0]
            self.current_event = self.current_location.events[0]  # Assuming there's at least one event

            self.current_event.execute()

            if self.party is None:
                self.continue_playing = False
                return "Save and quit"
            else:
                continue

        if self.continue_playing is False:
            return True
        elif self.continue_playing == "Save and quit":
            return "Save and quit"
        else:
            return False

# Define the UserInputParser class
class UserInputParser:
    def __init__(self):
        self.style = "console"

    def parse(self, prompt) -> str:
        return input(prompt)

# Define the User class
class User:
    def __init__(self, parser, username: str, password: str, legacy_points: int = 0):
        self.username = username
        self.password = password
        self.legacy_points = legacy_points
        self.parser = parser
        self.current_game = self._get_retrieve_saved_game_state_or_create_new_game()

    def _get_retrieve_saved_game_state_or_create_new_game(self) -> Game:
        new_game = Game(self.parser)
        return new_game

    def save_game(self):
        pass

# Define the main function to start the game
def start_game():
    parser = UserInputParser()
    user = User(parser, username="TestUser", password="12345")
    game_instance = user.current_game
    response = game_instance.start_game()
    if response == "Save and quit":
        user.save_game()
        print("Game saved. Goodbye!")
    elif response:
        print("Goodbye!")
    else:
        print("See you next time!")

if __name__ == '__main__':
    start_game()
