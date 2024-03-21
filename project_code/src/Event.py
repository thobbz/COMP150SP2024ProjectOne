class Event:
    def __init__(self, parser):
        self.fail = {
            "message": "You failed."
        }
        self.pass_ = {
            "message": "You Passed."
        }
        self.partial_pass = {
            "message": "You Partially Passed."
        }
        self.prompt_text = "Thanos appears, what will you do?"
        self.primary: Statistic = Strength()
        self.secondary: Statistic = Dexterity()
    def execute(self, party):
        chosen_one = self.parser.select_party_member(party)
        chosen_skill = self.parser.select_skill(chosen_one)
        self.set_status()
        pass

        self.set_status(EventStatus.PASS)
        pass
    def set_status(self, status: EventStatus = EventStatus.UNKNOWN):
        self.status = status

    def resolve_status(self, party, character, chosen_skill): 
        #check if the skill attributes overlap with the event attributes
        # if they don't overlap, the character fails
        # if one overlaps, the character partially passes
        # if they both overlap, the character passes
