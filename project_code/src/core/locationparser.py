from core.event import EventStatus




class LocationParser:
    def __init__(self):
        self.style = "console"

    def parse_location(self, location):
        # Display location information
        print(f"Location: {location.name}")
        print(f"Description: {location.description}")
        
        # Display available events
        print("Available events:")
        for i, event in enumerate(location.events, start=1):
            print(f"{i}. {event.prompt_text}")

        # Get user input for event selection
        while True:
            try:
                choice = int(input("Enter the number of the event you want to explore: "))
                if 1 <= choice <= len(location.events):
                    return location.events[choice - 1]
                else:
                    print("Invalid choice. Please enter a valid event number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def display_event_result(self, event):
        # Display the result of the event based on its status
        if event.status == EventStatus.PASS:
            print(event.pass_["message"])
        elif event.status == EventStatus.FAIL:
            print(event.fail["message"])
        elif event.status == EventStatus.PARTIAL_PASS:
            print(event.partial_pass["message"])
        else:
            print("Unknown event status.")