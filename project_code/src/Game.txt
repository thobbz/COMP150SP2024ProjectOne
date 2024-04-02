from typing import List
from project_code.src.user_code.user_model import User
from project_code.src.core.character import Character
from project_code.src.core.event import Event, EventStatus
from project_code.src.core.location import Location


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
        pass

    def start_game(self):
        game = Game()
        game._main_game_loop()
        return game

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
            self.continue_playing = False
        elif self.continue_playing == "Save and quit":
            self.continue_playing = False
        else:
            self.continue_playing = True
        

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








