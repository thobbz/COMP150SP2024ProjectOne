from typing import List
from enum import Enum
from project_code.src.eventparser import EventParser    #import EventParser class from EventParser.py
from project_code.src.statistic import Statistic, Strength, Dexterity, Spirit, Willpower, Knowledge, Wisdom, Intelligence, Endurance, Vitality, Constitution


class EventStatus(Enum):
    UNKNOWN = "UNKNOWN"
    FAIL = "FAIL"
    PASS = "PASS"
    PARTIAL_PASS = "PARTIAL_PASS"


class Event:
    def __init__(self, parser, data: dict = {}):
        self.parser = parser
        self.choices = []
        self.fail = {
            "message": "You failed."
        }
        self.pass_ = {
            "message": "You Passed."
        }
        self.partial_pass = {
            "message": "You Partially Passed."
        }
        self.prompt_text = data.get('prompt_text', "Thanos appears, what will you do?")
        self.primary: Statistic = Strength(0)
        self.secondary: Statistic = Dexterity(0)
        self.prompt_text = ""
        self.pass_text = ""
        self.fail_text = ""
        self.partial_pass_result = ""

        if data:
            self.initialize_from_data(data) 

    def initialize_from_data(self, data: dict):
        self.choices = data.get('choices', [])


    def execute(self, party):
        chosen_one = self.parser.select_party_member(party)
        chosen_skill = self.parser.select_skill(chosen_one)
        self.resolve_choice(party, chosen_one, chosen_skill)    
        pass

    def set_status(self, status: EventStatus = EventStatus.UNKNOWN):
        self.status = status

    def resolve_choice(self, party, character, chosen_skill):
        # check if the skill attributes overlap with the event attributes
        # if they don't overlap, the character fails
        # if one overlap, the character partially passes
        # if they do overlap, the character passes
        # Get the attributes of the chosen skill
        skill_attributes = chosen_skill.attributes
        
        # Get the attributes of the event
        event_attributes = {
            "primary": self.primary,
            "secondary": self.secondary,
            # Add other attributes here
        }
        
        # Check if any skill attribute overlaps with event attributes
        overlap = False
        for attribute in skill_attributes:
            if attribute in event_attributes.values():
                overlap = True
                break
        
        # Resolve the outcome based on overlap
        if not overlap:
            self.set_status(EventStatus.FAIL)
        elif overlap and len(set(skill_attributes) & set(event_attributes.values())) == 1:
            self.set_status(EventStatus.PARTIAL_PASS)
        else:
            self.set_status(EventStatus.PASS)

event_data = {
    'prompt_text': "The fate of the universe hangs in the balance. What will you do?",
    'choices': ["Sacrifice yourself for the greater good", "Seek an alternate solution"],
    'pass_message': "You saved the universe! You passed.",
}
parser = EventParser()

event = Event(parser, event_data)
user_choice = parser.parse_event(event)
print(event.pass_['message'] if user_choice == "Sacrifice yourself for the greater good" else event.fail['message'])
print("You chose:", user_choice)
