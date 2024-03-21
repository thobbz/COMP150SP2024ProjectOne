from project_code.src.Statistic import *
import random

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
        # self.name = self._generate_name() if name is None else name
        # self.strength: Strength = Strength(self, base_value=5)
        # self.dexterity: Dexterity = Dexterity(self, base_value=9)
        # self.constitution: Constitution = Constitution(self, base_value=7)
        # self.vitality: Vitality = Vitality(self, base_value=10)
        # self.endurance: Endurance = Endurance(self, base_value=8)
        # self.intelligence: Intelligence = Intelligence(self, base_value=9)
        # self.wisdom: Wisdom = Wisdom(self, base_value=7)
        # self.knowledge: Knowledge = Knowledge(self, base_value=8)
        # self.willpower: Willpower = Willpower(self, base_value=8)
        # self.spirit: Spirit = Spirit(self, base_value=7)
        self.name = self._generate_name() if name is None else name
        self.strength: Strength = Strength(self, base_value=random.randint(1, 10))
        self.dexterity: Dexterity = Dexterity(self, base_value=random.randint(1, 10))
        self.constitution: Constitution = Constitution(self, base_value=random.randint(1, 10))
        self.vitality: Vitality = Vitality(self, base_value=random.randint(1, 10))
        self.endurance: Endurance = Endurance(self, base_value=random.randint(1, 10))
        self.intelligence: Intelligence = Intelligence(self, base_value=random.randint(1, 10))
        self.wisdom: Wisdom = Wisdom(self, base_value=random.randint(1, 10))
        self.knowledge: Knowledge = Knowledge(self, base_value=random.randint(1, 10))
        self.willpower: Willpower = Willpower(self, base_value=random.randint(1, 10))
        self.spirit: Spirit = Spirit(self, base_value=random.randint(1, 10))
        # etc
        # self.intelligence: Intelligence = Intelligence(self)

    def _generate_name(self):
        #return "Spider-Man"
        names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry"] #A list of random name choices that can be changed
        return random.choice(names)
    
spider_man = Character(name="Spider-Man")
print(spider_man.name)
print(spider_man.strength.base_value)
print(spider_man.dexterity.base_value)
print(spider_man.constitution.base_value)
print(spider_man.vitality.base_value)
print(spider_man.endurance.base_value)
print(spider_man.intelligence.base_value)
print(spider_man.wisdom.base_value)
print(spider_man.knowledge.base_value)
print(spider_man.willpower.base_value)
print(spider_man.spirit.base_value)

#Create default characters in a character_list that will be randomly rolled when starting a new game.
#Maybe a legacy perk is being able to recruit a unique custom character with random attributes and either custom name or random name
#Maybe default characters are legacy

def create_character():
    character_list = []
    random_character = Character()
    character_list.append(Character())

