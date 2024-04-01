import json
from project_code.src.event import Event, EventParser #import Event class from Event.py


class Location:
    def __init__(self, parser: EventParser, number_of_events: int = 1):
        self.parser = parser
        self.events = [Event(parser, {}) for _ in range(number_of_events)]

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
            event.pass_text = event_data.get('pass', {})
            event.fail_text = event_data.get('fail', {})
            event.partial_pass_result = event_data.get('partial_pass', {})
            self.events.append(event)
    
    pass

