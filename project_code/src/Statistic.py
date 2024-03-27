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

# Example usage:
# strength_stat = Strength(10)
# print(strength_stat.value)  # Output: 10
# print(strength_stat.description)  # Output: Strength is a measure of physical power.
