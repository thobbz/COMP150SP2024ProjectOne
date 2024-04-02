# avengers_game.py

import random
import json

# Character class
class Character:
    def __init__(self, name, strength, dexterity, constitution, vitality, endurance, intelligence, wisdom, knowledge, willpower, spirit):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.vitality = vitality
        self.endurance = endurance
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.knowledge = knowledge
        self.willpower = willpower
        self.spirit = spirit

# Party class
class Party:
    def __init__(self):
        self.members = []
    
    def add_member(self, character):
        self.members.append(character)
    
    def remove_member(self, character):
        self.members.remove(character)
    
    def is_eliminated(self):
        return len(self.members) == 0

# Event class
class Event:
    def __init__(self, description, choices):
        self.description = description
        self.choices = choices
    
    def resolve(self, choice, character):
        # Perform skill check based on character attributes
        skill = choice['skill']
        difficulty = choice['difficulty']
        
        if skill == 'strength':
            success = character.strength >= difficulty
        elif skill == 'dexterity':
            success = character.dexterity >= difficulty
        elif skill == 'intelligence':
            success = character.intelligence >= difficulty
        elif skill == 'wisdom':
            success = character.wisdom >= difficulty
        else:
            success = False
        
        if success:
            return 'success'
        else:
            return 'failure'

# Game class
class Game:
    def __init__(self):
        self.party = Party()
        self.locations = []
        self.events = []
        self.legacy_points = 0
        self.infinity_stones = 0
    
    def load_locations(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.locations = json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in '{file_path}': {e}")

    
    def load_events(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.events = json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in '{file_path}': {e}")
    
    def create_character(self):
        name = input("Enter character name: ")
        strength = int(input("Enter strength (1-10): "))
        dexterity = int(input("Enter dexterity (1-10): "))
        constitution = int(input("Enter constitution (1-10): "))
        vitality = int(input("Enter vitality (1-10): "))
        endurance = int(input("Enter endurance (1-10): "))
        intelligence = int(input("Enter intelligence (1-10): "))
        wisdom = int(input("Enter wisdom (1-10): "))
        knowledge = int(input("Enter knowledge (1-10): "))
        willpower = int(input("Enter willpower (1-10): "))
        spirit = int(input("Enter spirit (1-10): "))
        
        character = Character(name, strength, dexterity, constitution, vitality, endurance, intelligence, wisdom, knowledge, willpower, spirit)
        self.party.add_member(character)
    
    def start(self):
        # Game loop
        while not self.party.is_eliminated():
            # Choose a random location
            location = random.choice(self.locations)
            print(f"\nLocation: {location['name']}")
            
            # Choose a random event
            event = random.choice(self.events)
            print(event['description'])
            
            # Prompt user for character and choice
            character = self.select_character()
            choice = self.select_choice(event)
            
            # Resolve the event
            result = event.resolve(choice, character)
            print(f"Result: {result}")
            
            # Update game state based on the result
            if result == 'success':
                self.legacy_points += 1
                print("Legacy points increased!")
                if random.random() < 0.2:
                    self.infinity_stones += 1
                    print("Obtained an Infinity Stone!")
            else:
                self.party.remove_member(character)
                print(f"{character.name} has been removed from the party.")
            
            if self.infinity_stones == 6:
                print("Congratulations! You have collected all the Infinity Stones and defeated Thanos!")
                break
        
        print("Game Over!")
    
    def select_character(self):
        print("\nSelect a character:")
        for i, character in enumerate(self.party.members, 1):
            print(f"{i}. {character.name}")
        
        choice = int(input("Enter your choice: "))
        return self.party.members[choice - 1]
    
    def select_choice(self, event):
        print("\nSelect a choice:")
        for i, choice in enumerate(event['choices'], 1):
            print(f"{i}. {choice['description']}")
        
        choice = int(input("Enter your choice: "))
        return event['choices'][choice - 1]

# Tests
def test_character_creation():
    character = Character("Iron Man", 8, 7, 6, 9, 7, 10, 8, 9, 9, 8)
    assert character.name == "Iron Man"
    assert character.strength == 8
    assert character.dexterity == 7
    assert character.constitution == 6
    assert character.vitality == 9
    assert character.endurance == 7
    assert character.intelligence == 10
    assert character.wisdom == 8
    assert character.knowledge == 9
    assert character.willpower == 9
    assert character.spirit == 8

def test_party_management():
    party = Party()
    character1 = Character("Captain America", 9, 8, 8, 9, 9, 7, 8, 7, 10, 8)
    character2 = Character("Thor", 10, 7, 9, 10, 9, 6, 7, 6, 9, 10)
    
    party.add_member(character1)
    party.add_member(character2)
    assert len(party.members) == 2
    assert party.members[0].name == "Captain America"
    assert party.members[1].name == "Thor"
    
    party.remove_member(character1)
    assert len(party.members) == 1
    assert party.members[0].name == "Thor"

def test_event_resolution():
    character = Character("Black Widow", 7, 10, 6, 7, 8, 9, 8, 9, 8, 7)
    
    event = Event("Test Event", [
        {'description': 'Choice 1', 'skill': 'strength', 'difficulty': 8},
        {'description': 'Choice 2', 'skill': 'dexterity', 'difficulty': 9},
        {'description': 'Choice 3', 'skill': 'intelligence', 'difficulty': 7}
    ])
    
    assert event.resolve(event.choices[0], character) == 'failure'
    assert event.resolve(event.choices[1], character) == 'success'
    assert event.resolve(event.choices[2], character) == 'success'

# Main
def main():
    game = Game()
    game.load_locations('locations.json')
    game.load_events('events.json')

    print("Loaded locations:")
    print(game.locations)
    
    print("Loaded events:")
    print(game.events)
    
    # Character creation
    while True:
        game.create_character()
        choice = input("Add another character? (y/n): ")
        if choice.lower() != 'y':
            break
    
    game.start()

if __name__ == '__main__':
    main()