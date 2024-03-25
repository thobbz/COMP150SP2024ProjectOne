# main.py
import random
import json
from enum import Enum
from typing import List
from project_code.test.UserInputParser import UserInputParser
from project_code.test.InstanceCreator import InstanceCreator
from project_code.test.UserFactory import UserFactory



class Statistic:
    def __init__(self, legacy_points: int):
        self.value = self._generate_starting_value(legacy_points)
        self.description = None
        self.min_value = 0
        self.max_value = 100

    def __str__(self):
        return f"{self.value}"

    def increase(self, amount):
        self.value += amount
        if self.value > self.max_value:
            self.value = self.max_value

    def decrease(self, amount):
        self.value -= amount
        if self.value < self.min_value:
            self.value = self.min_value

    def _generate_starting_value(self, legacy_points: int):
        """Generate a starting value for the statistic."""
        """This is just a placeholder for now."""
        return legacy_points / 100 + random.randint(1, 3)


class Strength(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "Strength is a measure of physical power."
        self.max_value = 20

class Dexterity(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "Dexterity measures agility, coordination, and quickness."
        self.max_value = 20

class Constitution(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "Constitution represents the body's resilience and natural armor."
        self.max_value = 20

class Vitality(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "Vitality reflects overall health and energy levels."
        self.max_value = 20

class Endurance(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "Endurance determines how quickly the body recovers from fatigue and injuries."
        self.max_value = 20

class Intelligence(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "Intelligence measures mental acuity, problem-solving abilities, and knowledge."
        self.max_value = 20

class Wisdom(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "Wisdom reflects a character's insight, intuition, and decision-making skills."
        self.max_value = 20

class Knowledge(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "Knowledge represents the breadth and depth of a character's understanding."
        self.max_value = 20

class Willpower(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "Willpower measures mental strength, resistance to control, and self-discipline."
        self.max_value = 20

class Spirit(Statistic):
    def __init__(self, legacy_points: int):
        super().__init__(legacy_points)
        self.description = "Spirit represents the ability to perform otherworldly acts and learn new skills."
        self.max_value = 20

class Capacity(Statistic):
    def __init__(self, legacy_points: int, capacity_type: str):
        super().__init__(legacy_points)
        self.capacity_type = capacity_type
        self.description = f"Capacity for {capacity_type} abilities."
        self.max_value = 20

class Location:
    def __init__(self, parser,number_of_events: int = 1):
        self.parser = parser
        self.events = [Event(self.parser) for _ in range(number_of_events)]

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
            event.pass_text = event_data.get('pass', '')
            event.fail_text = event_data.get('fail', '')
            event.partial_pass_result = event_data.get('partial_pass', '')
            self.events.append(event)
    
    pass

class Character:

    def __init__(self, name: str = None, character_type: str = None):

        self.name = self._generate_name() if name is None else name
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
        if character_type:
            self.apply_character_type(character_type)

    def apply_character_type(self, character_type: str):

        if character_type == "Iron Man":
            self.increase_stat("intelligence", 2)
            self.increase_stat("dexterity", 1)
        elif character_type == "Captain America":
            self.increase_stat("strength", 2)
            self.increase_stat("constitution", 1)
            self.increase_stat("wisdom", 1)
        elif character_type == "Thor":
            self.increase_stat("strength", 3)
            self.increase_stat("vitality", 2)
            self.increase_stat("constitution", 1)
            self.decrease_stat("intelligence", 1)
            self.decrease_stat("wisdom", 1)
        elif character_type == "Hulk":
            self.increase_stat("strength", 5)
            self.increase_stat("vitality", 3)
            self.increase_stat("constitution", 3)
            self.decrease_stat("intelligence", 2)
            self.decrease_stat("dexterity", 2)
        elif character_type == "Black Widow":
            self.increase_stat("dexterity", 3)
            self.increase_stat("intelligence", 2)
            self.increase_stat("willpower", 1)
        elif character_type == "Hawkeye":
            self.increase_stat("dexterity", 4)
            self.increase_stat("wisdom", 2)
        elif character_type == "Scarlet Witch":
            self.increase_stat("intelligence", 3)
            self.increase_stat("willpower", 3)
            self.increase_stat("spirit", 2)
        elif character_type == "Captain America":
            self.increase_stat("strength", 2)
            self.increase_stat("constitution", 2)
            self.increase_stat("wisdom", 1)
        elif character_type == "captain marvel":
            self.increase_stat("strength", 4)
            self.increase_stat("intelligence", 1)
            self.increase_stat("willpower", 2)
            self.increase_stat("wisdom", 1)
        elif character_type == "Black Panther":
            self.increase_stat("strength", 2)
            self.increase_stat("constitution", 2)
            self.increase_stat("wisdom", 1)
        elif character_type == "Doctor Strange":
            self.increase_stat("intelligence", 3)
            self.decrease_stat("strength", 2)
            self.decrease_stat("vitality", 2)
            self.increase_stat("wisdom", 3)
        elif character_type == "Spiderman":
            self.increase_stat("dexterity", 2)
            self.increase_stat("strength", 2)
            self.increase_stat("intelligence", 1)
        elif character_type == "Antman":
            self.increase_stat("dexterity", 2)
            self.increase_stat("intelligence", 2)
        elif character_type == "Wasp":
            self.increase_stat("dexterity", 3)
            self.increase_stat("intelligence", 3)
        elif character_type == "Falcon":
            self.increase_stat("dexterity", 3)
            self.increase_stat("wisdom", 2)
        elif character_type == "Nwoye":
            self.increase_stat("strength", 2)
            self.increase_stat("constitution", 1)
            self.increase_stat("willpower", 1)
        elif character_type == "Nebula":
            self.increase_stat("dexterity", 2)
            self.increase_stat("intelligence", 3)
        elif character_type == "Star-Lord":
            self.increase_stat("dexterity", 3)
            self.increase_stat("intelligence", 2)
        elif character_type == "Groot":
            self.increase_stat("strength", 3)
            self.increase_stat("constitution", 3)
            self.decrease_stat("intelligence", 2)
        elif character_type == "Rocket":
            self.increase_stat("dexterity", 4)
            self.increase_stat("intelligence", 3)
        elif character_type == "Winter Soldier":
            self.increase_stat("strength", 3)
            self.increase_stat("dexterity", 2)
            self.increase_stat("constitution", 2)
            self.increase_stat("endurance", 3)
            self.increase_stat("willpower", 2)
            self.increase_stat("knowledge", 1)
        elif character_type == "thanos":
            self.increase_stat("strength", 5)
            self.increase_stat("vitality", 5)
            self.increase_stat("constitution", 5)
            self.increase_stat("intelligence", 5)
            self.increase_stat("wisdom", 5)
            self.increase_stat("knowledge", 5)
            self.increase_stat("willpower", 5)
            self.increase_stat("spirit", 5)
        
        # Add more characters based on the Avengers team

    def _generate_name(self):
        return "Bob"  # Default name if not provided

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


# Example of creating Iron Man character
iron_man = Character(name="Tony Stark", character_type="Iron Man")
print("Iron Man's stats:")
print("Name:", iron_man.name)
print("Character Type:", iron_man.apply_character_type)
print("Strength:", iron_man.strength.value)
print("Dexterity:", iron_man.dexterity.value)
print("Constitution:", iron_man.constitution.value)
print("Vitality:", iron_man.vitality.value)
print("Endurance:", iron_man.endurance.value)
print("Intelligence:", iron_man.intelligence.value)
print("Wisdom:", iron_man.wisdom.value)
print("Knowledge:", iron_man.knowledge.value)
print("Willpower:", iron_man.willpower.value)
print("Spirit:", iron_man.spirit.value)

thor = Character(name="Thor", character_type="Thor")
print("Thor's stats:")
print("Name:", thor.name)
print("Character Type:", thor.apply_character_type)
print("Strength:", thor.strength.value)
print("Dexterity:", thor.dexterity.value)
print("Constitution:", thor.constitution.value)
print("Vitality:", thor.vitality.value)
print("Endurance:", thor.endurance.value)
print("Intelligence:", thor.intelligence.value)
print("Wisdom:", thor.wisdom.value)
print("Knowledge:", thor.knowledge.value)
print("Willpower:", thor.willpower.value)
print("Spirit:", thor.spirit.value)

hulk = Character(name="Bruce Banner", character_type="Hulk")
print("Hulk's stats:")
print("Name:", hulk.name)
print("Character Type:", hulk.apply_character_type)
print("Strength:", hulk.strength.value)
print("Dexterity:", hulk.dexterity.value) 
print("Constitution:", hulk.constitution.value)
print("Vitality:", hulk.vitality.value)
print("Endurance:", hulk.endurance.value)
print("Intelligence:", hulk.intelligence.value)
print("Wisdom:", hulk.wisdom.value)
print("Knowledge:", hulk.knowledge.value)  
print("Willpower:", hulk.willpower.value)  
print("Spirit:", hulk.spirit.value) 

black_widow = Character(name="Natasha Romanoff", character_type="Black Widow")
print("Black Widow's stats:")
print("Name:", black_widow.name)
print("Character Type:", black_widow.apply_character_type)
print("Strength:", black_widow.strength.value)
print("Dexterity:", black_widow.dexterity.value)
print("Constitution:", black_widow.constitution.value)
print("Vitality:", black_widow.vitality.value)
print("Endurance:", black_widow.endurance.value)
print("Intelligence:", black_widow.intelligence.value)
print("Wisdom:", black_widow.wisdom.value)
print("Knowledge:", black_widow.knowledge.value)
print("Willpower:", black_widow.willpower.value)
print("Spirit:", black_widow.spirit.value)

hawkeye = Character(name="Clint Barton", character_type="Hawkeye")
print("Hawkeye's stats:")
print("Name:", hawkeye.name)
print("Character Type:", hawkeye.apply_character_type)
print("Strength:", hawkeye.strength.value)
print("Dexterity:", hawkeye.dexterity.value)
print("Constitution:", hawkeye.constitution.value)
print("Vitality:", hawkeye.vitality.value)
print("Endurance:", hawkeye.endurance.value)
print("Intelligence:", hawkeye.intelligence.value)
print("Wisdom:", hawkeye.wisdom.value)
print("Knowledge:", hawkeye.knowledge.value)
print("Willpower:", hawkeye.willpower.value)
print("Spirit:", hawkeye.spirit.value)

scarlet_witch = Character(name="Wanda Maximoff", character_type="Scarlet Witch")
print("Scarlet Witch's stats:")
print("Name:", scarlet_witch.name)
print("Character Type:", scarlet_witch.apply_character_type)
print("Strength:", scarlet_witch.strength.value)
print("Dexterity:", scarlet_witch.dexterity.value)
print("Constitution:", scarlet_witch.constitution.value)
print("Vitality:", scarlet_witch.vitality.value)
print("Endurance:", scarlet_witch.endurance.value)
print("Intelligence:", scarlet_witch.intelligence.value)
print("Wisdom:", scarlet_witch.wisdom.value)
print("Knowledge:", scarlet_witch.knowledge.value)
print("Willpower:", scarlet_witch.willpower.value)
print("Spirit:", scarlet_witch.spirit.value)


captain_marvel = Character(name="Carol Danvers", character_type="Captain Marvel")
print("Captain Marvel's stats:")
print("Name:", captain_marvel.name)
print("Character Type:", captain_marvel.apply_character_type)
print("Strength:", captain_marvel.strength.value)
print("Dexterity:", captain_marvel.dexterity.value)
print("Constitution:", captain_marvel.constitution.value)
print("Vitality:", captain_marvel.vitality.value)
print("Endurance:", captain_marvel.endurance.value)
print("Intelligence:", captain_marvel.intelligence.value)
print("Wisdom:", captain_marvel.wisdom.value)
print("Knowledge:", captain_marvel.knowledge.value)
print("Willpower:", captain_marvel.willpower.value)
print("Spirit:", captain_marvel.spirit.value)


black_panther = Character(name="T'Challa", character_type="Black Panther")
print("Black Panther's stats:")
print("Name:", black_panther.name)
print("Character Type:", black_panther.apply_character_type)
print("Strength:", black_panther.strength.value)
print("Dexterity:", black_panther.dexterity.value)
print("Constitution:", black_panther.constitution.value)
print("Vitality:", black_panther.vitality.value)
print("Endurance:", black_panther.endurance.value)
print("Intelligence:", black_panther.intelligence.value)
print("Wisdom:", black_panther.wisdom.value)
print("Knowledge:", black_panther.knowledge.value)
print("Willpower:", black_panther.willpower.value)
print("Spirit:", black_panther.spirit.value)


doctor_strange = Character(name="Stephen Strange", character_type="Doctor Strange")
print("Doctor Strange's stats:")
print("Name:", doctor_strange.name)
print("Character Type:", doctor_strange.apply_character_type)
print("Strength:", doctor_strange.strength.value)
print("Dexterity:", doctor_strange.dexterity.value)
print("Constitution:", doctor_strange.constitution.value)
print("Vitality:", doctor_strange.vitality.value)
print("Endurance:", doctor_strange.endurance.value)
print("Intelligence:", doctor_strange.intelligence.value)
print("Wisdom:", doctor_strange.wisdom.value)
print("Knowledge:", doctor_strange.knowledge.value)
print("Willpower:", doctor_strange.willpower.value)
print("Spirit:", doctor_strange.spirit.value)


spiderman = Character(name="Peter Parker", character_type="Spiderman")
print("Spiderman's stats:")
print("Name:", spiderman.name)
print("Character Type:", spiderman.apply_character_type)
print("Strength:", spiderman.strength.value)
print("Dexterity:", spiderman.dexterity.value)
print("Constitution:", spiderman.constitution.value)
print("Vitality:", spiderman.vitality.value)
print("Endurance:", spiderman.endurance.value)
print("Intelligence:", spiderman.intelligence.value)
print("Wisdom:", spiderman.wisdom.value)
print("Knowledge:", spiderman.knowledge.value)
print("Willpower:", spiderman.willpower.value)
print("Spirit:", spiderman.spirit.value)


antman = Character(name="Scott Lang", character_type="Antman")
print("Antman's stats:")
print("Name:", antman.name)
print("Character Type:", antman.apply_character_type)
print("Strength:", antman.strength.value)
print("Dexterity:", antman.dexterity.value)
print("Constitution:", antman.constitution.value)
print("Vitality:", antman.vitality.value)
print("Endurance:", antman.endurance.value)
print("Intelligence:", antman.intelligence.value)
print("Wisdom:", antman.wisdom.value)
print("Knowledge:", antman.knowledge.value)
print("Willpower:", antman.willpower.value)
print("Spirit:", antman.spirit.value)


wasp = Character(name="Hope van Dyne", character_type="Wasp")
print("Wasp's stats:")
print("Name:", wasp.name)
print("Character Type:", wasp.apply_character_type)
print("Strength:", wasp.strength.value)
print("Dexterity:", wasp.dexterity.value)
print("Constitution:", wasp.constitution.value)
print("Vitality:", wasp.vitality.value)
print("Endurance:", wasp.endurance.value)
print("Intelligence:", wasp.intelligence.value)
print("Wisdom:", wasp.wisdom.value)
print("Knowledge:", wasp.knowledge.value)
print("Willpower:", wasp.willpower.value)
print("Spirit:", wasp.spirit.value)

falcon = Character(name="Sam Wilson", character_type="Falcon")
print("Falcon's stats:")
print("Name:", falcon.name)
print("Character Type:", falcon.apply_character_type)
print("Strength:", falcon.strength.value)
print("Dexterity:", falcon.dexterity.value)
print("Constitution:", falcon.constitution.value)
print("Vitality:", falcon.vitality.value)
print("Endurance:", falcon.endurance.value)
print("Intelligence:", falcon.intelligence.value)
print("Wisdom:", falcon.wisdom.value)
print("Knowledge:", falcon.knowledge.value)
print("Willpower:", falcon.willpower.value)
print("Spirit:", falcon.spirit.value)

nwoye = Character(name="Nwoye", character_type="Nwoye")
print("Nwoye's stats:")
print("Name:", nwoye.name)
print("Character Type:", nwoye.apply_character_type)
print("Strength:", nwoye.strength.value)
print("Dexterity:", nwoye.dexterity.value)
print("Constitution:", nwoye.constitution.value)
print("Vitality:", nwoye.vitality.value)
print("Endurance:", nwoye.endurance.value)
print("Intelligence:", nwoye.intelligence.value)
print("Wisdom:", nwoye.wisdom.value)
print("Knowledge:", nwoye.knowledge.value)
print("Willpower:", nwoye.willpower.value)
print("Spirit:", nwoye.spirit.value)

nebula = Character(name="Nebula", character_type="Nebula")
print("Nebula's stats:")
print("Name:", nebula.name)
print("Character Type:", nebula.apply_character_type)
print("Strength:", nebula.strength.value)
print("Dexterity:", nebula.dexterity.value)
print("Constitution:", nebula.constitution.value)
print("Vitality:", nebula.vitality.value)
print("Endurance:", nebula.endurance.value)
print("Intelligence:", nebula.intelligence.value)
print("Wisdom:", nebula.wisdom.value)
print("Knowledge:", nebula.knowledge.value)
print("Willpower:", nebula.willpower.value)
print("Spirit:", nebula.spirit.value)

star_lord = Character(name="Peter Quill", character_type="Star-Lord")
print("Star-Lord's stats:")
print("Name:", star_lord.name)
print("Character Type:", star_lord.apply_character_type)
print("Strength:", star_lord.strength.value)
print("Dexterity:", star_lord.dexterity.value)
print("Constitution:", star_lord.constitution.value)
print("Vitality:", star_lord.vitality.value)
print("Endurance:", star_lord.endurance.value)
print("Intelligence:", star_lord.intelligence.value)
print("Wisdom:", star_lord.wisdom.value)
print("Knowledge:", star_lord.knowledge.value)
print("Willpower:", star_lord.willpower.value)
print("Spirit:", star_lord.spirit.value)

groot = Character(name="Groot", character_type="Groot")
print("Groot's stats:")
print("Name:", groot.name)
print("Character Type:", groot.apply_character_type)
print("Strength:", groot.strength.value)
print("Dexterity:", groot.dexterity.value)
print("Constitution:", groot.constitution.value)
print("Vitality:", groot.vitality.value)
print("Endurance:", groot.endurance.value)
print("Intelligence:", groot.intelligence.value)
print("Wisdom:", groot.wisdom.value)
print("Knowledge:", groot.knowledge.value)
print("Willpower:", groot.willpower.value)
print("Spirit:", groot.spirit.value)

rocket = Character(name="Rocket", character_type="Rocket")
print("Rocket's stats:")
print("Name:", rocket.name)
print("Character Type:", rocket.apply_character_type)
print("Strength:", rocket.strength.value)
print("Dexterity:", rocket.dexterity.value)
print("Constitution:", rocket.constitution.value)
print("Vitality:", rocket.vitality.value)
print("Endurance:", rocket.endurance.value)
print("Intelligence:", rocket.intelligence.value)
print("Wisdom:", rocket.wisdom.value)
print("Knowledge:", rocket.knowledge.value)
print("Willpower:", rocket.willpower.value)
print("Spirit:", rocket.spirit.value)

winter_soldier = Character(name="Bucky Barnes", character_type="Winter Soldier")
print("Winter Soldier's stats:")
print("Name:", winter_soldier.name)
print("Character Type:", winter_soldier.apply_character_type)
print("Strength:", winter_soldier.strength.value)
print("Dexterity:", winter_soldier.dexterity.value)
print("Constitution:", winter_soldier.constitution.value)
print("Vitality:", winter_soldier.vitality.value)
print("Endurance:", winter_soldier.endurance.value)
print("Intelligence:", winter_soldier.intelligence.value)
print("Wisdom:", winter_soldier.wisdom.value)
print("Knowledge:", winter_soldier.knowledge.value)
print("Willpower:", winter_soldier.willpower.value)
print("Spirit:", winter_soldier.spirit.value)


thanos = Character(name="Thanos", character_type="Thanos")
print("Thanos's stats:")
print("Name:", thanos.name)
print("Character Type:", thanos.apply_character_type)
print("Strength:", thanos.strength.value)
print("Dexterity:", thanos.dexterity.value)
print("Constitution:", thanos.constitution.value)
print("Vitality:", thanos.vitality.value)
print("Endurance:", thanos.endurance.value)
print("Intelligence:", thanos.intelligence.value)
print("Wisdom:", thanos.wisdom.value)
print("Knowledge:", thanos.knowledge.value)
print("Willpower:", thanos.willpower.value)
print("Spirit:", thanos.spirit.value)


character_types = ["Iron Man", "Captain America", "Thor", "Hulk", "Black Widow", "Hawkeye", "Scarlet Witch", "Captain Marvel", "Black Panther", "Doctor Strange", "Spiderman", "Antman", "Wasp", "Falcon", "Nwoye", "Nebula", "Star-Lord", "Groot", "Rocket", "Thanos"]

def generate_random_character():
    random_name = "Random Character"  # Generate random name
    random_type = "random.choice(character_types)"  # Generate random type

    random_character = Character(name=random_name, character_type=random_type)
    return random_character


random_character = generate_random_character()
print("Random Character's stats:")
print("Name:", random_character.name)
print("Character Type:", random_character.apply_character_type)
print("Strength:", random_character.strength.value)
print("Dexterity:", random_character.dexterity.value)
print("Constitution:", random_character.constitution.value)
print("Vitality:", random_character.vitality.value)
print("Endurance:", random_character.endurance.value)
print("Intelligence:", random_character.intelligence.value)
print("Wisdom:", random_character.wisdom.value)
print("Knowledge:", random_character.knowledge.value)
print("Willpower:", random_character.willpower.value)
print("Spirit:", random_character.spirit.value)



class EventStatus(Enum):
    UNKNOWN = "unknown"
    PASS = "pass"
    FAIL = "fail"
    PARTIAL_PASS = "partial_pass"


class Event:
    def __init__(self, parser, data: dict = None):
        self.parser = parser
        if data:
            self.primary = data['primary_attribute']
            self.secondary = data['secondary_attribute']
            self.prompt_text = data['prompt_text']
            self.pass_ = data['pass']
            self.fail = data['fail']
            self.partial_pass = data['partial_pass']
        else:
            self.primary = None
            self.secondary = None
            self.prompt_text = "A default prompt text."
            self.pass_ = {"message": "You passed."}
            self.fail = {"message": "You failed."}
            self.partial_pass = {"message": "You partially passed."}

        self.status = EventStatus.UNKNOWN
        self.primary = Strength()
        self.secondary = Dexterity()

    def execute(self, party):
        chosen_one = self.parser.select_party_member(party)
        chosen_skill = self.parser.select_skill(chosen_one)

        self.set_status(EventStatus.PASS)

    def set_status(self, status: EventStatus = EventStatus.UNKNOWN):
        self.status = status

    def resolve_choice(self, party, character, chosen_skill):
        pass





class Game:

    def __init__(self):
        self.characters: List[Character] = []
        self.locations: List[Location] = []
        self.events: List[Event] = []
        self.party: List[Character] = []
        self.current_location = None
        self.current_event = None
        self._initialize_game()
        self.continue_playing = True

    def add_character(self, character: Character):
        """Add a character to the game."""
        self.characters.append(character)

    def add_location(self, location: Location):
        """Add a location to the game."""
        self.locations.append(location)

    def add_event(self, event: Event):
        """Add an event to the game."""
        self.events.append(event)

    def _initialize_game(self):
        """Initialize the game with characters, locations, and events based on the user's properties."""
        avengers_characters = ["Iron Man", "Captain America", "Thor", "Hulk", "Black Widow", "Hawkeye", "Scarlet Witch","Captain Marvel", "Black Panther", "Doctor Strange", "Spiderman", "Antman", "Wasp", "Falcon", "Winter Soldier", "Star-Lord", "Rocket", "Groot", "Nebula"]
        for character_name in avengers_characters:
            character = Character(character_name)
            self.add_character(character)

        # add locations
        avengers_locations = ["New York City", "San Francisco", "Wakanda", "Asgard", "Vormir", "New Jersey","Earth"]
        for location_name in avengers_locations:
            self.add_location(Location(location_name))

        # add events
        avengers_events = ["Avengers vs. Thanos","Battle of New York","Asgard","Morag","Vormir","Final Battle"]
        for event_name in avengers_events:
            self.add_event(Event(event_name))

        self.current_location = random.choice(self.locations)
        pass

    def start_game(self):
        return self._main_game_loop()

    def _main_game_loop(self):
        """The main game loop."""
        while self.continue_playing:
            # print game state
            print("Current location:", self.current_location)
            print("Current event:", self.current_event.name if self.current_event else "None")

            if all(character.is_dead for character in self.party):
                # award legacy points and end instance of game
                self.continue_playing = False
                return "Game Over"

            pass
            # ask for user input
            # parse user input
            # update game state
            # check if party is all dead
            # if party is dead, award legacy points and end instance of game
            # if party is not dead, continue game
        if not self.continue_playing:
            return True
        elif self.continue_playing == "Save and quit":
            return "Save and quit"
        else:
            return False

    def update_game_state(self, user_input):
        pass




class User:

    def __init__(self, input, username: str, password: str, legacy_points: int = 0):
        self.username = username
        self.password = password
        self.legacy_points = legacy_points
        self.input = input
        self.current_game = self._get_retrieve_saved_game_state_or_create_new_game()

    def _get_retrieve_saved_game_state_or_create_new_game(self) -> Game:
        new_game = Game()
        return new_game

    def save_game(self):
        #implement saving game state
        #save game state to a file
        game_state = self.current_game.get_state()

        with open(f"{self.username}_game_state.json", "w") as file:
            json.dump(game_state, file)
        pass


class UserInputParser:

    def __init__(self):
        self.style = "console"

    def parse(self, prompt) -> str:
        response: str = input(prompt)
        return response



class UserFactory:

    @staticmethod
    def create_user(parser: UserInputParser) -> User:
        username = parser.parse("Enter a username: ")
        password = parser.parse("Enter a password: ")
        # Here you can add more logic as needed, e.g., validate input
        return User(username, password)



class InstanceCreator:

    def __init__(self, user_factory: UserFactory, parser: UserInputParser):
        self.user_factory = user_factory
        self.parser = parser

    def _new_user_or_login(self) -> User:
        response = self.parser.parse("Create a new username or login to an existing account?")
        if "login" in response:
            return self._load_user()
        else:
            return self.user_factory.create_user(self.parser)

    def get_user_info(self, response: str) -> User | None:
        if "yes" in response:
            return self._new_user_or_login()
        else:
            return None

    def _load_user(self) -> User:
        username = self.parser.parse("Enter your username:")
      
        if username in self.user_factory.users:
            return self.user_factory.users[username]
        else:
            print("User not found. Please try again or create a new account.")
            return None
    
        pass


def start_game():
    parser = UserInputParser()
    user_factory = UserFactory()
    instance_creator = InstanceCreator(user_factory, parser)

    response = parser.parse("Would you like to start a new game? (yes/no)")
    print(f"Response: {response}")
    user = instance_creator.get_user_info(response)
    if user is not None:
        game_instance = user.current_game
        if game_instance is not None:
            response = game_instance.start_game()
            if response == "Save and quit":
                user.save_game()
                print("Game saved. Goodbye!")
                sys.exit()
            elif response:
                print("Goodbye!")
                sys.exit()
    else:
        print("See you next time!")
        sys.exit()

if __name__ == '__main__':
    start_game()




