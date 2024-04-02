import json
from project_code.src.core.event import Event #import Event class from Event.py
from project_code.src.eventparser import EventParser #import EventParser class from EventParser.py


class Location:
    def __init__(self, parser, number_of_events: int = 1):
        self.parser = parser
        self.events = [Event(EventParser) for _ in range(number_of_events)]

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
            event.pass_ = event_data.get('pass', '')
            event.fail = event_data.get('fail', '')
            event.partial_pass = event_data.get('partial_pass', '')
            self.events.append(event)
    
    def get_event(self, event_id):
        # Search for an event by its ID and return it
        for event in self.events:
            if event.get('id') == event_id:
                return event
        return None  # Return None if the event is not found