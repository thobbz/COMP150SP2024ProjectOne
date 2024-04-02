import json

import random
from project_code.src.core.event import Event#import Event class from Event.py
from project_code.src.eventparser import EventParser#import EventParser class from EventParser.py
from project_code.src.common.statistic import Statistic, Strength, Dexterity, Spirit, Willpower, Knowledge, Wisdom, Intelligence, Endurance, Vitality, Constitution
from project_code.src.core.event import Event #import Event class from Event.py
from project_code.src.eventparser import EventParser #import EventParser class from EventParser.py



class Location:
    def __init__(self, parser: EventParser, number_of_events: int = 1):
        self.parser = parser

        self.events = [Event(parser, {}) for _ in range(number_of_events)]

        self.events = [Event(EventParser) for _ in range(number_of_events)]


    def create_custom_event_from_static_text_file(self, file_path: str):
        """json files will be stored like this:
        {
        primary.attribute: value, prompt_text: "", pass: "", fail: "", partial_pass = ""
        }"""
        #load text file from path
        with open(file_path, "r") as file:
            data = json.load(file)
        
        event = Event(self.parser)
        event.primary = Statistic(data.get('primary_attribute', ''))
        event.secondary = Statistic(data.get('secondary_attribute', ''))
        event.prompt_text = data.get('prompt_text', '')
        event.pass_ = data.get('pass', {})
        event.fail = data.get('fail', {})
        event.partial_pass = data.get('partial_pass', {})
            
        return event


    def get_event(self, event_id):
        # Search for an event by its ID and return it
        for event in self.events:
            if event.get('id') == event_id:
                return event
        return self.events.pop(0)  # Return None if the event is not found

