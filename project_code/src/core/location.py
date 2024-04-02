import json
<<<<<<< HEAD
import random
from project_code.src.core.event import Event#import Event class from Event.py
from project_code.src.eventparser import EventParser#import EventParser class from EventParser.py
=======
from project_code.src.core.event import Event #import Event class from Event.py
from project_code.src.eventparser import EventParser #import EventParser class from EventParser.py
>>>>>>> bde05581abe9edea3c5f7cca74d871afb86f1624


class Location:
    def __init__(self, parser: EventParser, number_of_events: int = 1):
        self.parser = parser
<<<<<<< HEAD
        self.events = [Event(parser, {}) for _ in range(number_of_events)]
=======
        self.events = [Event(EventParser) for _ in range(number_of_events)]
>>>>>>> bde05581abe9edea3c5f7cca74d871afb86f1624

    def create_custom_event_from_static_text_file(self, file_path: str):
        """json files will be stored like this:
        {
        primary.attribute: value, prompt_text: "", pass: "", fail: "", partial_pass = ""
        }"""
        #load text file from path
        with open(file_path, "r") as file:
            data = json.load(file)
        
        for event_data in data.values():
            event = Event(self.parser)
            event.primary = event_data.get('primary attribute', '')
            event.prompt_text = event_data.get('prompt_text', '')
<<<<<<< HEAD
            event.pass_text = event_data.get('pass', {})
            event.fail_text = event_data.get('fail', {})
            event.partial_pass_result = event_data.get('partial_pass', {})
=======
            event.pass_ = event_data.get('pass', '')
            event.fail = event_data.get('fail', '')
            event.partial_pass = event_data.get('partial_pass', '')
>>>>>>> bde05581abe9edea3c5f7cca74d871afb86f1624
            self.events.append(event)

    def get_event(self) -> Event:
        return self.events.pop(0)
    
<<<<<<< HEAD
    pass
=======
    def get_event(self, event_id):
        # Search for an event by its ID and return it
        for event in self.events:
            if event.get('id') == event_id:
                return event
        return None  # Return None if the event is not found
>>>>>>> bde05581abe9edea3c5f7cca74d871afb86f1624
