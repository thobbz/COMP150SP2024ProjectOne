import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from project_code.src.common.statistic import Strength, Dexterity, Constitution, Vitality, Endurance, Intelligence, \
    Wisdom, Knowledge, Willpower, Spirit


def _generate_name():
    return "Bob"  # Default name if not provided


def generate_random_character():
    random_name = "Random Character"  # Generate random name
    random_type = "random.choice(character_types)"  # Generate random type

    random_character = Character(name=random_name, character_type=random_type)
    return random_character


class Character:
    character_stats = {
        "Iron Man": {"intelligence": 2, "dexterity": 1},
        "Captain America": {"strength": 2, "constitution": 2, "wisdom": 1},
        "Thor": {"strength": 3, "vitality": 2, "constitution": 1, "intelligence": -1, "wisdom": -1},
        "Hulk": {"strength": 5, "vitality": 3, "constitution": 3, "intelligence": -2, "dexterity": -2},
        "Black Widow": {"dexterity": 3, "intelligence": 2, "willpower": 1},
        "Hawkeye": {"dexterity": 4, "wisdom": 2},
        "Scarlet Witch": {"intelligence": 3, "willpower": 3, "spirit": 2},
        "captain marvel": {"strength": 4, "intelligence": 1, "willpower": 2, "wisdom": 1},
        "Black Panther": {"strength": 2, "constitution": 2, "wisdom": 1},
        "Doctor Strange": {"intelligence": 3, "strength": -2, "vitality": -2, "wisdom": 3},
        "Spiderman": {"dexterity": 2, "strength": 2, "intelligence": 1},
        "Antman": {"dexterity": 2, "intelligence": 2},
        "Wasp": {"dexterity": 3, "intelligence": 3},
        "Falcon": {"dexterity": 3, "wisdom": 2},
        "Nwoye": {"strength": 2, "constitution": 1, "willpower": 1},
        "Nebula": {"dexterity": 2, "intelligence": 3},
        "Star-Lord": {"dexterity": 3, "intelligence": 2},
        "Groot": {"strength": 3, "constitution": 3, "intelligence": -2},
        "Rocket": {"dexterity": 4, "intelligence": 3},
        "Winter Soldier": {"strength": 3, "dexterity": 2, "constitution": 2, "endurance": 3, "willpower": 2,
                           "knowledge": 1},
        "thanos": {"strength": 5, "vitality": 5, "constitution": 5, "intelligence": 5, "wisdom": 5, "knowledge": 5,
                   "willpower": 5, "spirit": 5}
    }

    def __init__(self, name: str = "", character_type: str = ""):

        self.character_type = character_type
        self.name = _generate_name() if name is None else name
        legacy_points = 100
        self.strength: Strength = Strength(legacy_points)
        self.dexterity: Dexterity = Dexterity(legacy_points)
        self.constitution: Constitution = Constitution(legacy_points)
        self.vitality: Vitality = Vitality(legacy_points)
        self.endurance: Endurance = Endurance(legacy_points)
        self.intelligence: Intelligence = Intelligence(legacy_points)
        self.wisdom: Wisdom = Wisdom(legacy_points)
        self.knowledge: Knowledge = Knowledge(legacy_points)
        self.willpower: Willpower = Willpower(legacy_points)
        self.spirit: Spirit = Spirit(legacy_points)
        # etc
        # self.intelligence: Intelligence = Intelligence(self)
        if self.character_type:
            self.apply_character_type()

    def apply_character_type(self):
        if self.character_type in Character.character_stats:
            for stat, value in Character.character_stats[self.character_type].items():
                if value >= 0:
                    self.increase_stat(stat, value)
                else:
                    self.decrease_stat(stat, abs(value))

    def increase_stat(self, stat_name, amount):
        stat = getattr(self, stat_name, None)
        if stat is not None:
            stat.increase(amount)
        else:
            print(f"No such stat: {stat_name}")

    def decrease_stat(self, stat_name, amount):
        stat = getattr(self, stat_name, None)
        if stat is not None:
            stat.decrease(amount)
        else:
            print(f"No such stat: {stat_name}")


def create_characters() -> List[Character]:
    character_dictionary = {
        "Tony Stark": "Iron Man",
        "Thor": "Thor",
        "Bruce Banner": "Hulk",
        "Natasha Romanoff": "Black Widow",
        "Clint Barton": "Hawkeye",
        "Wanda Maximoff": "Scarlet Witch",
        "Carol Danvers": "Captain Marvel",
        "T'Challa": "Black Panther",
        "Stephen Strange": "Doctor Strange",
        "Peter Parker": "Spiderman",
        "Hope van Dyne": "Wasp",
        "Sam Wilson": "Falcon",
        "Nwoye": "Nwoye",
        "Nebula": "Nebula",
        "Peter Quill": "Star-Lord",
        "Groot": "Groot",
        "Rocket": "Rocket",
        "Bucky Barnes": "Winter Soldier",
        "Thanos": "Thanos",
        "Scott Lang": "Antman",
        "Random": "Random"
    }

    characters = []
    for character_name, character_type in character_dictionary.items():
        if character_type == "Random":
            character = generate_random_character()
            characters.append(character)
        else:
            character = Character(name=character_name, character_type=character_type)
        characters.append(character)
        character.apply_character_type()
        print(f"{character_name}:")
        print(f"Strength: {character.strength.value}")
        print(f"Dexterity: {character.dexterity.value}")
        print(f"Constitution: {character.constitution.value}")
        print(f"Vitality: {character.vitality.value}")
        print(f"Endurance: {character.endurance.value}")
        print(f"Intelligence: {character.intelligence.value}")
        print(f"Wisdom: {character.wisdom.value}")
        print(f"Knowledge: {character.knowledge.value}")
        print(f"Willpower: {character.willpower.value}")
        print(f"Spirit: {character.spirit.value}")
    return characters
