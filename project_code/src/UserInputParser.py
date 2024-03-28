import getpass

class UserInputParser:

    def __init__(self):
        self.style = "console"
    
    def parse(self, prompt: str, password: bool = False) -> str:
        if password:
            return getpass.getpass(prompt)
        else:
            return input(prompt)
