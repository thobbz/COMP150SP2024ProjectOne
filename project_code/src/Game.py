import random
from typing import List

from project_code.src.Character import Character
from project_code.src.Event import Event
from project_code.src.Location import Location


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








