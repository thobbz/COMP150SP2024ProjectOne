# main.py
import json
import sys
from typing import List
import random
from enum import Enum



class Location:

    def __init__(self, parser, number_of_events: int = 1):
        self.parser = parser
        self.events = [Event(self.parser) for _ in range(number_of_events)]

    def get_event(self):
        # Placeholder for retrieving an event from the location's event list
        if self.events:
            return random.choice(self.events)
        else:
            return None


    import json

    def create_custom_event_from_static_text_file(self, file_path):
        # load json file from path
        with open(file_path, "r") as file:
            data = json.load(file)

        return Event(self.parser, data)








class EventStatus(Enum):
    UNKNOWN = "unknown"
    PASS = "pass"
    FAIL = "fail"
    PARTIAL_PASS = "partial_pass"

class EventStatus(Enum):
    UNKNOWN = "unknown"
    PASS = "pass"
    FAIL = "fail"
    PARTIAL_PASS = "partial_pass"

class Event:

    def __init__(self, parser, data: dict = None):
        self.parser = parser

        # Initialize attributes from data or with default values
        if data:
            self.primary: Statistic = data.get('primary_attribute', Strength(random.randint(1, 10)))
            self.secondary: Statistic = data.get('secondary_attribute', Dexterity(random.randint(1, 10)))
            self.prompt_text = data.get('prompt_text', "Default prompt text")
            self.pass_ = data.get('pass', {"message": "You passed."})
            self.fail = data.get('fail', {"message": "You failed."})
            self.partial_pass = data.get('partial_pass', {"message": "You partially passed."})
        else:
            self.primary: Statistic = Strength(random.randint(1, 10))
            self.secondary: Statistic = Dexterity(random.randint(1, 10))
            self.prompt_text = "Default prompt text"
            self.pass_ = {"message": "You passed."}
            self.fail = {"message": "You failed."}
            self.partial_pass = {"message": "You partially passed."}

        self.status = EventStatus.UNKNOWN
        self.fail = {
                "message": "You failed."
            }
        self.pass_ = {
                "message": "You passed."
            }
        self.partial_pass = {
                "message": "You partially passed."
            }
        self.prompt_text = "Thanos appears! Prepare to attack."

        def execute(self, party):
            chosen_one = self.parser.select_party_member(party)
            chosen_skill = self.parser.select_skill(chosen_one)

            self.set_status(EventStatus.PASS)
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
        """Generate a starting value for the statistic based on random number and user properties."""
        """This is just a placeholder for now. Perhaps some statistics will be based on user properties, and others 
        will be random."""
        return legacy_points / 100 + random.randint(1, 3)


class Strength(Statistic):

    def __init__(self, value):
        super().__init__(value)
        self.description = "Strength is a measure of physical power."

class Dexterity(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Dexterity measures agility, coordination, and quickness."

class Constitution(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Constitution represents the body's resilience and natural armor."

class Vitality(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Vitality reflects overall health and energy levels."

class Endurance(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Endurance determines how quickly the body recovers from fatigue and injuries."

class Intelligence(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Intelligence measures mental acuity, problem-solving abilities, and knowledge."

class Wisdom(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Wisdom reflects a character's insight, intuition, and decision-making skills."

class Knowledge(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Knowledge represents the breadth and depth of a character's understanding."

class Willpower(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Willpower measures mental strength, resistance to control, and self-discipline."

class Spirit(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Spirit represents the ability to perform otherworldly acts and learn new skills."

class Capacity(Statistic):
    def __init__(self, value, capacity_type):
        super().__init__(value)
        self.capacity_type = capacity_type
        self.description = f"Capacity for {capacity_type} abilities."

# Example usage:
# strength_stat = Strength(10)
# print(strength_stat.value)  # Output: 10
# print(strength_stat.description)  # Output: Strength is a measure of physical power.
            

class Character:

    def __init__(self, name: str = None):
        """
        Core Stats: Everyone has these ad some text
        - Strength: How much you can lift. How strong you are. How hard you punch, etc.
        - Dexterity: How quick your limbs can perform intricate tasks. How adept you are at avoiding blows you anticipate. Impacts speed.
        - Constitution: The bodies natural armor. Characters may have unique positive or negative constitutions that provide additional capabilities
        - vitality: A measure of how lively you feel. How many Hit Points you have. An indirect measure of age.
        - Endurance: How fast you recover from injuries. How quickly you recover from fatigue.
        - Intelligence: How smart you are. How quickly you can connect the dots to solve problems. How fast you can think.
        - Wisdom: How effectively you can make choices under pressure. Generally low in younger people.
        - Knowledge: How much you know? This is a raw score for all knowledge. Characters may have specific areas of expertise with a bonus or deficit in some areas.
        - Willpower: How quickly or effectively the character can overcome natural urges. How susceptible they are to mind control.
        - Spirit: Catchall for ability to perform otherworldly acts. High spirit is rare. Different skills have different resource pools they might use like mana, stamina, etc. These are unaffected by spirit. Instead spirit is a measure of how hard it is to learn new otherworldly skills and/or master general skills.
         """
        self.name = self._generate_name() if name is None else name
        self.strength = Strength(value=random.randint(1, 10))
        self.dexterity = Dexterity(value=random.randint(1, 10))
        self.constitution = Constitution(value=random.randint(1, 10))
        self.vitality = Vitality(value=random.randint(1, 10))
        self.endurance = Endurance(value=random.randint(1, 10))
        self.intelligence = Intelligence(value=random.randint(1, 10))
        self.wisdom = Wisdom(value=random.randint(1, 10))
        self.knowledge = Knowledge(value=random.randint(1, 10))
        self.willpower = Willpower(value=random.randint(1, 10))
        self.spirit = Spirit(value=random.randint(1, 10))

        
        # etc
        # self.intelligence: Intelligence = Intelligence(self)

    def _generate_name(gender=None, initials=None, length=None):
        #return "Spider-Man"
        import random
        import string

        # Sample data for names
        male_first_names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Charles', 'Thomas']
        female_first_names = ['Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen']
        last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Martinez', 'Lopez']

    # Function to generate a random name
    
        if gender == 'male':
            first_name = random.choice(male_first_names)
        elif gender == 'female':
            first_name = random.choice(female_first_names)
        else:
            first_name = random.choice(male_first_names + female_first_names)
        
        last_name = random.choice(last_names)

        if initials:
            initials = initials.upper()
            first_name = first_name[0] + '.' if 'F' in initials else first_name[0]
            last_name = last_name[0] + '.' if 'L' in initials else last_name[0]
        
        full_name = f"{first_name} {last_name}"

        if length and len(full_name) > length:
            full_name = full_name[:length]
        
        return full_name

        # Function to generate multiple random names
    def generate_random_names(num_names, gender=None, initials=None, length=None):
        random_names = []
        for _ in range(num_names):
            random_names.append(Character._generate_name(gender, initials, length))
        return random_names

        # Example usage
        # num_names_to_generate = 5
        # random_names = generate_random_names(num_names_to_generate, gender='male', initials='FL', length=10)
        # for name in random_names:
        #     print(name)

    
spider_man = Character(name="Spider-Man")
print(spider_man.name)
print(spider_man.strength.value)
print(spider_man.dexterity.value)
print(spider_man.constitution.value)
print(spider_man.vitality.value)
print(spider_man.endurance.value)
print(spider_man.intelligence.value)
print(spider_man.wisdom.value)
print(spider_man.knowledge.value)
print(spider_man.willpower.value)
print(spider_man.spirit.value)


Thor = Character(name="Thor")
print(Thor.name)
print(Thor.strength.value)
print(Thor.dexterity.value)
print(Thor.constitution.value)
print(Thor.vitality.value)
print(Thor.endurance.value)    
print(Thor.intelligence.value)
print(Thor.wisdom.value)
print(Thor.knowledge.value)
print(Thor.willpower.value)
print(Thor.spirit.value)


class Game:

    def __init__(self, parser):
        self.parser = parser
        self.characters: List[Character] = []
        self.locations: List[Location] = []
        self.events: List[Event] = []
        self.party: List[Character] = []
        self.current_location = None
        self.current_event = None
        self.continue_playing = True

        self._initialize_game()

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
        character_list = [Character() for _ in range(10)]
        location_list = [Location(self.parser) for _ in range(2)]

        for character in character_list:
            self.add_character(character)

        for location in location_list:
            self.add_location(location)

    def start_game(self):
        return self._main_game_loop()

    def _main_game_loop(self):
        """The main game loop."""
        while self.continue_playing:
            self.current_location = self.locations[0]
            self.current_event = self.current_location.events[0]

            self.current_event.execute()

            if self.party is None:
                # award legacy points
                self.continue_playing = False
                return "Save and quit"
            else:
                continue
        if self.continue_playing is False:
            return True
        elif self.continue_playing == "Save and quit":
            return "Save and quit"
        else:
            return False


class User:

    def __init__(self, parser, username: str, password: str, legacy_points: int = 0):
        self.username = username
        self.password = password
        self.legacy_points = legacy_points
        self.current_game = self._get_retrieve_saved_game_state_or_create_new_game()
        self.parser = parser

    def _get_retrieve_saved_game_state_or_create_new_game(self) -> Game:
        new_game = Game(self.parser)
        return new_game

    def save_game(self):
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
        return User(parser, username=username, password=password)


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

    def get_user_info(self, response: str) -> User:
        if "yes" in response:
            return self._new_user_or_login()
        else:
            return None

    def _load_user(self, username: str) -> User:
        try:
            with open(f"{username}_game_state.json", "r") as file:
                game_state = json.load(file)
            return User(self.parser, username=username, password="", legacy_points=game_state["legacy_points"])
        except FileNotFoundError:
            print("User data not found. Creating a new user.")
            return None
        

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
        """Generate a starting value for the statistic based on random number and user properties."""
        """This is just a placeholder for now. Perhaps some statistics will be based on user properties, and others 
        will be random."""
        value = legacy_points / 100 + random.randint(1, 3)
        return value


class Strength(Statistic):
    def __init__(self, value: int):
        super().__init__(value)
        self.description = "Strength is a measure of physical power."

class Dexterity(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Dexterity measures agility, coordination, and quickness."

class Constitution(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Constitution represents the body's resilience and natural armor."

class Vitality(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Vitality reflects overall health and energy levels."

class Endurance(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Endurance determines how quickly the body recovers from fatigue and injuries."

class Intelligence(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Intelligence measures mental acuity, problem-solving abilities, and knowledge."

class Wisdom(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Wisdom reflects a character's insight, intuition, and decision-making skills."

class Knowledge(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Knowledge represents the breadth and depth of a character's understanding."

class Willpower(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Willpower measures mental strength, resistance to control, and self-discipline."

class Spirit(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Spirit represents the ability to perform otherworldly acts and learn new skills."

class Capacity(Statistic):
    def __init__(self, value, capacity_type):
        super().__init__(value)
        self.capacity_type = capacity_type
        self.description = f"Capacity for {capacity_type} abilities."

# Example usage:
# strength_stat = Strength(10)
# print(strength_stat.value)  # Output: 10
# print(strength_stat.description)  # Output: Strength is a measure of physical power.


class User:

    def __init__(self, parser, username: str, password: str, legacy_points: int = 0):
        self.username = username
        self.password = password
        self.legacy_points = legacy_points
        self.parser = parser
        self.current_game = self._get_retrieve_saved_game_state_or_create_new_game()

    def _get_retrieve_saved_game_state_or_create_new_game(self) -> Game:
        new_game = Game(self.parser)
        return new_game

    def save_game(self, game_state: dict):
        with open(f"{self.username}_game_state.json", "w") as file:
            json.dump(game_state, file)
            print("Game saved successfully.")


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