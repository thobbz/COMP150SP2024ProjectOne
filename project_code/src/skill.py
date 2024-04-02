class Skill:
    def __init__(self, name: str, description: str, base_damage: int, attributes: list):
        self.name = name
        self.description = description
        self.base_damage = base_damage
        self.attributes = attributes

    def __str__(self):
        return f"{self.name}: {self.description}"

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_base_damage(self) -> int:
        return self.base_damage

    def get_attributes(self) -> list:
        return self.attributes

    def set_name(self, name: str):
        self.name = name

    def set_description(self, description: str):
        self.description = description

    def set_base_damage(self, base_damage: int):
        self.base_damage = base_damage

    def set_attributes(self, attributes: list):
        self.attributes = attributes