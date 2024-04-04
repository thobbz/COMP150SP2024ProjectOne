import json
from typing import List

from project_code.src.core.character import Character
from .event import Event, EventStatus
from .location import Location
from ..eventparser import EventParser


class Game:

    def __init__(self):
        self.continue_playing = True
        self.characters: List[Character] = []
        self.locations: List[Location] = []
        self.events: List[Event] = []
        self.party: List[Character] = []
        self.current_location = None
        self.current_event = None
        self._initialize_game()

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
        event_parser = EventParser()
        character_list = [Character() for _ in range(10)]
        location_list = [Location(event_parser) for _ in range(2)]

        for character in character_list:
            self.add_character(character)

        for location in location_list:
            self.add_location(location)

    def load_locations(self, file_path):
        with open(file_path, 'r') as file:
            self.locations = json.load(file)

    def load_events(self, file_path):
        with open(file_path, 'r') as file:
            self.events = json.load(file)

    def start_game(self):
        return self._main_game_loop()

    def _main_game_loop(self):
        """The main game loop."""
        while self.continue_playing:
            if not self.locations:
                print("No locations available. Exiting game loop.")
                break

            self.current_location = self.locations[0]

            if not self.current_location.events:
                print(f"No events available in {self.current_location}. Skipping to the next location.")
                continue

            self.current_event = self.current_location.get_event(0)

            if self.current_event:
                self.current_event.execute(self.party)

                if self.current_event.status == EventStatus.FAIL:
                    print(self.current_event.fail["message"])
                    # award legacy points or handle failure
                    self.continue_playing = False
                    return "Save and quit"
                elif self.current_event.status == EventStatus.PASS:
                    print(self.current_event.pass_["message"])
                    # handle success
                elif self.current_event.status == EventStatus.PARTIAL_PASS:
                    print(self.current_event.partial_pass["message"])
                    # handle partial success
            else:
                print("No events available. Exiting game loop.")
                break
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
            "characters": [char for char in self.characters],
            "locations": [loc for loc in self.locations],
            "events": [event for event in self.events],
            "party": [char for char in self.party],
            "current_location": self.current_location if self.current_location else None,
            "current_event": self.current_event if self.current_event else None,
            "continue_playing": self.continue_playing
        }
        return state
