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