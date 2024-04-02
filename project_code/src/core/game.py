import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from typing import List

from project_code.src.core.character import Character
from project_code.src.core.event import Event
from project_code.src.core.location import Location


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
        pass

    def start_game(self):
        return self._main_game_loop()

    def _main_game_loop(self):
        """The main game loop."""
        while self.continue_playing:
            pass
            # ask for user input
            # parse user input
            # update game state
            # check if party is all dead
            # if part is dead, award legacy points and end instance of game
            # if party is not dead, continue game
        if self.continue_playing is False:
            return True
        elif self.continue_playing == "Save and quit":
            return "Save and quit"
        else:
            return False
        

    def get_state(self) -> dict:
        """
        Returns the current state of the game as a dictionary.
        """
        state = {
            "characters": [char.__dict__ for char in self.characters],
            "locations": [loc.__dict__ for loc in self.locations],
            "events": [event.__dict__ for event in self.events],
            "party": [char.__dict__ for char in self.party],
            "current_location": self.current_location.__dict__ if self.current_location else None,
            "current_event": self.current_event.__dict__ if self.current_event else None,
            "continue_playing": self.continue_playing
        }
        return state



