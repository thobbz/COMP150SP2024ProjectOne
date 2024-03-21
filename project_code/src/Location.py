class Location:
    def __init__(self, number_of_events: int = 1):
        self.parser = parser
        self.events = [Event(self.parser) for _ in range(number_of_events)]
    def create_custom_event_from_static_text_file(self):
        """json files will be stored like this:
        {
        primary.attribute: value, prompt_text: "", pass: "", fail: "", partial_pass = ""
        }"""
        #load text file from path
        with open(file_path, "r") as file:
            data = json.load(file)
            
        #parse json file
        self.primary = data['primary attribute']
        self.secondary = data['secondary attribute']
        self.prompt_text = data
    pass