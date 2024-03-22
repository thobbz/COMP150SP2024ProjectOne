from project_code.src.Statistic import *
import random

class Character:

    def __init__(self, name: str = None, character_type: str = None):
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
            stat.base_value += amount
        else:
            print(f"No such stat: {stat_name}")

    def decrease_stat(self, stat_name, amount):
        stat = getattr(self, stat_name, None)
        if stat is not None:
            stat.base_value -= amount
        else:
            print(f"No such stat: {stat_name}")


# Example of creating Iron Man character
iron_man = Character(name="Tony Stark", character_type="Iron Man")
print("Iron Man's stats:")
print("Name:", iron_man.name)
print("Character Type:", iron_man.character_type)
print("Strength:", iron_man.strength.base_value)
print("Dexterity:", iron_man.dexterity.base_value)
print("Constitution:", iron_man.constitution.base_value)
print("Vitality:", iron_man.vitality.base_value)
print("Endurance:", iron_man.endurance.base_value)
print("Intelligence:", iron_man.intelligence.base_value)
print("Wisdom:", iron_man.wisdom.base_value)
print("Knowledge:", iron_man.knowledge.base_value)
print("Willpower:", iron_man.willpower.base_value)
print("Spirit:", iron_man.spirit.base_value)

thor = Character(name="Thor", character_type="Thor")
print("Thor's stats:")
print("Name:", thor.name)
print("Character Type:", thor.character_type)
print("Strength:", thor.strength.base_value)
print("Dexterity:", thor.dexterity.base_value)
print("Constitution:", thor.constitution.base_value)
print("Vitality:", thor.vitality.base_value)
print("Endurance:", thor.endurance.base_value)
print("Intelligence:", thor.intelligence.base_value)
print("Wisdom:", thor.wisdom.base_value)
print("Knowledge:", thor.knowledge.base_value)
print("Willpower:", thor.willpower.base_value)
print("Spirit:", thor.spirit.base_value)

hulk = Character(name="Bruce Banner", character_type="Hulk")
print("Hulk's stats:")
print("Name:", hulk.name)
print("Character Type:", hulk.character_type)
print("Strength:", hulk.strength.base_value)
print("Dexterity:", hulk.dexterity.base_value) 
print("Constitution:", hulk.constitution.base_value)
print("Vitality:", hulk.vitality.base_value)
print("Endurance:", hulk.endurance.base_value)
print("Intelligence:", hulk.intelligence.base_value)
print("Wisdom:", hulk.wisdom.base_value)
print("Knowledge:", hulk.knowledge.base_value)  
print("Willpower:", hulk.willpower.base_value)  
print("Spirit:", hulk.spirit.base_value) 

black_widow = Character(name="Natasha Romanoff", character_type="Black Widow")
print("Black Widow's stats:")
print("Name:", black_widow.name)
print("Character Type:", black_widow.character_type)
print("Strength:", black_widow.strength.base_value)
print("Dexterity:", black_widow.dexterity.base_value)
print("Constitution:", black_widow.constitution.base_value)
print("Vitality:", black_widow.vitality.base_value)
print("Endurance:", black_widow.endurance.base_value)
print("Intelligence:", black_widow.intelligence.base_value)
print("Wisdom:", black_widow.wisdom.base_value)
print("Knowledge:", black_widow.knowledge.base_value)
print("Willpower:", black_widow.willpower.base_value)
print("Spirit:", black_widow.spirit.base_value)

hawkeye = Character(name="Clint Barton", character_type="Hawkeye")
print("Hawkeye's stats:")
print("Name:", hawkeye.name)
print("Character Type:", hawkeye.character_type)
print("Strength:", hawkeye.strength.base_value)
print("Dexterity:", hawkeye.dexterity.base_value)
print("Constitution:", hawkeye.constitution.base_value)
print("Vitality:", hawkeye.vitality.base_value)
print("Endurance:", hawkeye.endurance.base_value)
print("Intelligence:", hawkeye.intelligence.base_value)
print("Wisdom:", hawkeye.wisdom.base_value)
print("Knowledge:", hawkeye.knowledge.base_value)
print("Willpower:", hawkeye.willpower.base_value)
print("Spirit:", hawkeye.spirit.base_value)

scarlet_witch = Character(name="Wanda Maximoff", character_type="Scarlet Witch")
print("Scarlet Witch's stats:")
print("Name:", scarlet_witch.name)
print("Character Type:", scarlet_witch.character_type)
print("Strength:", scarlet_witch.strength.base_value)
print("Dexterity:", scarlet_witch.dexterity.base_value)
print("Constitution:", scarlet_witch.constitution.base_value)
print("Vitality:", scarlet_witch.vitality.base_value)
print("Endurance:", scarlet_witch.endurance.base_value)
print("Intelligence:", scarlet_witch.intelligence.base_value)
print("Wisdom:", scarlet_witch.wisdom.base_value)
print("Knowledge:", scarlet_witch.knowledge.base_value)
print("Willpower:", scarlet_witch.willpower.base_value)
print("Spirit:", scarlet_witch.spirit.base_value)

captain_marvel = Character(name="Carol Danvers", character_type="Captain Marvel")
print("Captain Marvel's stats:")
print("Name:", captain_marvel.name)
print("Character Type:", captain_marvel.character_type)
print("Strength:", captain_marvel.strength.base_value)
print("Dexterity:", captain_marvel.dexterity.base_value)
print("Constitution:", captain_marvel.constitution.base_value)
print("Vitality:", captain_marvel.vitality.base_value)
print("Endurance:", captain_marvel.endurance.base_value)
print("Intelligence:", captain_marvel.intelligence.base_value)
print("Wisdom:", captain_marvel.wisdom.base_value)
print("Knowledge:", captain_marvel.knowledge.base_value)
print("Willpower:", captain_marvel.willpower.base_value)
print("Spirit:", captain_marvel.spirit.base_value)

black_panther = Character(name="T'Challa", character_type="Black Panther")
print("Black Panther's stats:")
print("Name:", black_panther.name)
print("Character Type:", black_panther.character_type)
print("Strength:", black_panther.strength.base_value)
print("Dexterity:", black_panther.dexterity.base_value)
print("Constitution:", black_panther.constitution.base_value)
print("Vitality:", black_panther.vitality.base_value)
print("Endurance:", black_panther.endurance.base_value)
print("Intelligence:", black_panther.intelligence.base_value)
print("Wisdom:", black_panther.wisdom.base_value)
print("Knowledge:", black_panther.knowledge.base_value)
print("Willpower:", black_panther.willpower.base_value)
print("Spirit:", black_panther.spirit.base_value)

doctor_strange = Character(name="Stephen Strange", character_type="Doctor Strange")
print("Doctor Strange's stats:")
print("Name:", doctor_strange.name)
print("Character Type:", doctor_strange.character_type)
print("Strength:", doctor_strange.strength.base_value)
print("Dexterity:", doctor_strange.dexterity.base_value)
print("Constitution:", doctor_strange.constitution.base_value)
print("Vitality:", doctor_strange.vitality.base_value)
print("Endurance:", doctor_strange.endurance.base_value)
print("Intelligence:", doctor_strange.intelligence.base_value)
print("Wisdom:", doctor_strange.wisdom.base_value)
print("Knowledge:", doctor_strange.knowledge.base_value)
print("Willpower:", doctor_strange.willpower.base_value)
print("Spirit:", doctor_strange.spirit.base_value)

spiderman = Character(name="Peter Parker", character_type="Spiderman")
print("Spiderman's stats:")
print("Name:", spiderman.name)
print("Character Type:", spiderman.character_type)
print("Strength:", spiderman.strength.base_value)
print("Dexterity:", spiderman.dexterity.base_value)
print("Constitution:", spiderman.constitution.base_value)
print("Vitality:", spiderman.vitality.base_value)
print("Endurance:", spiderman.endurance.base_value)
print("Intelligence:", spiderman.intelligence.base_value)
print("Wisdom:", spiderman.wisdom.base_value)
print("Knowledge:", spiderman.knowledge.base_value)
print("Willpower:", spiderman.willpower.base_value)
print("Spirit:", spiderman.spirit.base_value)

antman = Character(name="Scott Lang", character_type="Antman")
print("Antman's stats:")
print("Name:", antman.name)
print("Character Type:", antman.character_type)
print("Strength:", antman.strength.base_value)
print("Dexterity:", antman.dexterity.base_value)
print("Constitution:", antman.constitution.base_value)
print("Vitality:", antman.vitality.base_value)
print("Endurance:", antman.endurance.base_value)
print("Intelligence:", antman.intelligence.base_value)
print("Wisdom:", antman.wisdom.base_value)
print("Knowledge:", antman.knowledge.base_value)
print("Willpower:", antman.willpower.base_value)
print("Spirit:", antman.spirit.base_value)

wasp = Character(name="Hope van Dyne", character_type="Wasp")
print("Wasp's stats:")
print("Name:", wasp.name)
print("Character Type:", wasp.character_type)
print("Strength:", wasp.strength.base_value)
print("Dexterity:", wasp.dexterity.base_value)
print("Constitution:", wasp.constitution.base_value)
print("Vitality:", wasp.vitality.base_value)
print("Endurance:", wasp.endurance.base_value)
print("Intelligence:", wasp.intelligence.base_value)
print("Wisdom:", wasp.wisdom.base_value)
print("Knowledge:", wasp.knowledge.base_value)
print("Willpower:", wasp.willpower.base_value)
print("Spirit:", wasp.spirit.base_value)

falcon = Character(name="Sam Wilson", character_type="Falcon")
print("Falcon's stats:")
print("Name:", falcon.name)
print("Character Type:", falcon.character_type)
print("Strength:", falcon.strength.base_value)
print("Dexterity:", falcon.dexterity.base_value)
print("Constitution:", falcon.constitution.base_value)
print("Vitality:", falcon.vitality.base_value)
print("Endurance:", falcon.endurance.base_value)
print("Intelligence:", falcon.intelligence.base_value)
print("Wisdom:", falcon.wisdom.base_value)
print("Knowledge:", falcon.knowledge.base_value)
print("Willpower:", falcon.willpower.base_value)
print("Spirit:", falcon.spirit.base_value)

nwoye = Character(name="Nwoye", character_type="Nwoye")
print("Nwoye's stats:")
print("Name:", nwoye.name)
print("Character Type:", nwoye.character_type)
print("Strength:", nwoye.strength.base_value)
print("Dexterity:", nwoye.dexterity.base_value)
print("Constitution:", nwoye.constitution.base_value)
print("Vitality:", nwoye.vitality.base_value)
print("Endurance:", nwoye.endurance.base_value)
print("Intelligence:", nwoye.intelligence.base_value)
print("Wisdom:", nwoye.wisdom.base_value)
print("Knowledge:", nwoye.knowledge.base_value)
print("Willpower:", nwoye.willpower.base_value)
print("Spirit:", nwoye.spirit.base_value)

nebula = Character(name="Nebula", character_type="Nebula")
print("Nebula's stats:")
print("Name:", nebula.name)
print("Character Type:", nebula.character_type)
print("Strength:", nebula.strength.base_value)
print("Dexterity:", nebula.dexterity.base_value)
print("Constitution:", nebula.constitution.base_value)
print("Vitality:", nebula.vitality.base_value)
print("Endurance:", nebula.endurance.base_value)
print("Intelligence:", nebula.intelligence.base_value)
print("Wisdom:", nebula.wisdom.base_value)
print("Knowledge:", nebula.knowledge.base_value)
print("Willpower:", nebula.willpower.base_value)
print("Spirit:", nebula.spirit.base_value)

star_lord = Character(name="Peter Quill", character_type="Star-Lord")
print("Star-Lord's stats:")
print("Name:", star_lord.name)
print("Character Type:", star_lord.character_type)
print("Strength:", star_lord.strength.base_value)
print("Dexterity:", star_lord.dexterity.base_value)
print("Constitution:", star_lord.constitution.base_value)
print("Vitality:", star_lord.vitality.base_value)
print("Endurance:", star_lord.endurance.base_value)
print("Intelligence:", star_lord.intelligence.base_value)
print("Wisdom:", star_lord.wisdom.base_value)
print("Knowledge:", star_lord.knowledge.base_value)
print("Willpower:", star_lord.willpower.base_value)
print("Spirit:", star_lord.spirit.base_value)

groot = Character(name="Groot", character_type="Groot")
print("Groot's stats:")
print("Name:", groot.name)
print("Character Type:", groot.character_type)
print("Strength:", groot.strength.base_value)
print("Dexterity:", groot.dexterity.base_value)
print("Constitution:", groot.constitution.base_value)
print("Vitality:", groot.vitality.base_value)
print("Endurance:", groot.endurance.base_value)
print("Intelligence:", groot.intelligence.base_value)
print("Wisdom:", groot.wisdom.base_value)
print("Knowledge:", groot.knowledge.base_value)
print("Willpower:", groot.willpower.base_value)
print("Spirit:", groot.spirit.base_value)

rocket = Character(name="Rocket", character_type="Rocket")
print("Rocket's stats:")
print("Name:", rocket.name)
print("Character Type:", rocket.character_type)
print("Strength:", rocket.strength.base_value)
print("Dexterity:", rocket.dexterity.base_value)
print("Constitution:", rocket.constitution.base_value)
print("Vitality:", rocket.vitality.base_value)
print("Endurance:", rocket.endurance.base_value)
print("Intelligence:", rocket.intelligence.base_value)
print("Wisdom:", rocket.wisdom.base_value)
print("Knowledge:", rocket.knowledge.base_value)
print("Willpower:", rocket.willpower.base_value)
print("Spirit:", rocket.spirit.base_value)

thanos = Character(name="Thanos", character_type="Thanos")
print("Thanos's stats:")
print("Name:", thanos.name)
print("Character Type:", thanos.character_type)
print("Strength:", thanos.strength.base_value)
print("Dexterity:", thanos.dexterity.base_value)
print("Constitution:", thanos.constitution.base_value)
print("Vitality:", thanos.vitality.base_value)
print("Endurance:", thanos.endurance.base_value)
print("Intelligence:", thanos.intelligence.base_value)
print("Wisdom:", thanos.wisdom.base_value)
print("Knowledge:", thanos.knowledge.base_value)
print("Willpower:", thanos.willpower.base_value)
print("Spirit:", thanos.spirit.base_value)


def generate_random_character():
    character_type = random.choice["Iron Man", "Captain America", "Thor", "Hulk", "Black Widow", "Hawkeye", "Scarlet Witch", "Captain Marvel", "Black Panther", "Doctor Strange", "Spiderman", "Antman", "Wasp", "Falcon", "Nwoye", "Nebula", "Star-Lord", "Groot", "Rocket", "Thanos"]

    random_name = "Random Character"  # Generate random name
    random_type = "random.choice(character_types)"  # Generate random type

    random_character = Character(name=random_name, character_type=random_type)
    return random_character


random_character = generate_random_character()
print("Random Character's stats:")
print("Name:", random_character.name)
print("Character Type:", random_character.character_type)
print("Strength:", random_character.strength.base_value)
print("Dexterity:", random_character.dexterity.base_value)
print("Constitution:", random_character.constitution.base_value)
print("Vitality:", random_character.vitality.base_value)
print("Endurance:", random_character.endurance.base_value)
print("Intelligence:", random_character.intelligence.base_value)
print("Wisdom:", random_character.wisdom.base_value)
print("Knowledge:", random_character.knowledge.base_value)
print("Willpower:", random_character.willpower.base_value)
print("Spirit:", random_character.spirit.base_value)

      

#Create a function that will randomly generate a character with random attributes


#Create default characters in a character_list that will be randomly rolled when starting a new game.
#Maybe a legacy perk is being able to recruit a unique custom character with random attributes and either custom name or random name
#Maybe default characters are legacy

def create_character():
    character_list = []
    random_character = Character()
    character_list.append(Character())

