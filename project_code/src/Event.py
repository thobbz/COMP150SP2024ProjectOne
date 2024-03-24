from typing import List 
from project_code.src.Statistic import Statistic, Strength, Dexterity


class EventStatus:
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
        # Placeholder logic for selecting party member
        pass

    def select_skill(self, chosen_one) -> str:
        # Placeholder logic for selecting skill
        pass


class Event:
    def __init__(self, parser, data: dict = None):
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

        if data:
            self.initialize_from_data(data) 

    def initialize_from_data(self, data: dict):
        self.choices = data.get('choices', [])


    def execute(self, party):
        chosen_one = self.parser.select_party_member(party)
        chosen_skill = self.parser.select_skill(chosen_one)
        self.resolve_status(party, chosen_one, chosen_skill)    
        pass

    def set_status(self, status: EventStatus = EventStatus.UNKNOWN):
        self.status = status

    def resolve_status(self, party, character, chosen_skill): 
        # Placeholder logic for resolving event status
        pass

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