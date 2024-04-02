from typing import List
from enum import Enum
from project_code.src.statistic import Statistic, Strength, Dexterity, Spirit, Willpower, Knowledge, Wisdom, Intelligence, Endurance, Vitality, Constitution


class EventStatus(Enum):
    UNKNOWN = "UNKNOWN"
    FAIL = "FAIL"
    PASS = "PASS"
    PARTIAL_PASS = "PARTIAL_PASS"

class EventParser:
    def __init__(self):
        self.style = "console"

    def parse_event(self, event) -> str:
        # Display event information
        print(event.prompt_text)
        for i, choice in enumerate(event.choices, start=1):
            print(f"{i}. {choice}")
        choice_index = self.get_choice_input(event.choices)
        return event.choices[choice_index - 1]
    
    def get_choice_input(self, choices: List[str]) -> int:
        while True:
            try:
                choice_index = int(input("Enter your choice: "))
                if 1 <= choice_index <= len(choices):
                    return choice_index
                else:
                    print("Invalid choice. Please enter a number corresponding to the choice.")
            except ValueError:
                print("Invalid input. Please enter a number corresponding to the choice.")
    def select_party_member(self, party) -> str:
        print("Select a party member:")
        for i, member in enumerate(party, start=1):
            print(f"{i}. {member.name}")

        while True:
            try:
                choice = int(input("Enter the number of the party member: "))
                if 1 <= choice <= len(party):
                    return party[choice - 1].name
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def select_skill(self, chosen_one) -> str:
        print(f"Select a skill for {chosen_one}:")
        skills = ["Attack", "Defend", "Use Item"]
        for i, skill in enumerate(skills, start=1):
            print(f"{i}. {skill}")

        while True:
            try:
                choice = int(input("Enter the number of the skill: "))
                if 1 <= choice <= len(skills):
                    return skills[choice - 1]
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")


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

parser = EventParser()

event_data = {
    'prompt_text': "The fate of the universe hangs in the balance. What will you do?",
    'choices': ["Sacrifice yourself for the greater good", "Seek an alternate solution"],
    'pass_message': "You saved the universe! You passed.",
}

event = Event(parser, event_data)
user_choice = parser.parse_event(event)
print(event.pass_['message'] if user_choice == "Sacrifice yourself for the greater good" else event.fail['message'])
print("You chose:", user_choice)
