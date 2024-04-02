from typing import List
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

parser = EventParser()