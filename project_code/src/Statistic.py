import random


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
