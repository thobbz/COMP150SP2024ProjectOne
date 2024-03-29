import unittest
from unittest.mock import MagicMock
from project_code.src.instancecreator import InstanceCreator
from project_code.src.userfactory import UserFactory
from project_code.src.userinputparser import UserInputParser
from project_code.src.user import User

class TestInstanceCreator(unittest.TestCase):
    def setUp(self):
        self.mock_user_factory = MagicMock(spec=UserFactory)
        self.mock_parser = MagicMock(spec=UserInputParser)
        self.instance_creator = InstanceCreator(self.mock_user_factory, self.mock_parser)

    def test_get_user_info_yes_creates_new_user(self):
        # Prepare the mock objects
        self.mock_parser.parse.return_value = "new"  # Simulate the response for creating a new user
        mock_user = MagicMock(spec=User)
        self.mock_user_factory.create_user.return_value = mock_user

        # Execute the method under test
        user = self.instance_creator.get_user_info("yes")

        # Verify the results
        self.mock_parser.parse.assert_called_once_with("Create a new username or login to an existing account?")
        self.mock_user_factory.create_user.assert_called_once_with(self.mock_parser)
        self.assertEqual(user, mock_user, "The method should return a new user object")

    def test_get_user_info_no_returns_none(self):
        # Execute the method under test with a response that should not create a user
        user = self.instance_creator.get_user_info("no")

        # Verify the results
        self.assertIsNone(user, "The method should return None for a 'no' response")

    # You can add more tests to cover other scenarios, such as handling login

if __name__ == '__main__':
    unittest.main()

class TestEventMethods(unittest.TestCase):
    def setUp(self):
        self.parser = UserInputParser()
        self.event = Event(self.parser)

    def test_execute(self):
        # Mock party and skill selection
        party = ['Character1', 'Character2']
        with patch('builtins.input', side_effect=['1', '2']):  # Mocking party member and skill selection
            self.event.execute(party)

        # Check if event status is set to PASS after execution
        self.assertEqual(self.event.status, EventStatus.PASS)

    def test_set_status(self):
        # Test setting event status to PASS
        self.event.set_status(EventStatus.PASS)
        self.assertEqual(self.event.status, EventStatus.PASS)

    def test_resolve_choice_fail(self):
        # Mock character and skill attributes for testing
        party = ['Character1', 'Character2']
        character = Character(name="TestCharacter")
        chosen_skill = Skill(attributes=["attribute1", "attribute2"])  # Mock skill attributes

        # Resolve choice with non-overlapping attributes
        self.event.resolve_choice(party, character, chosen_skill)
        self.assertEqual(self.event.status, EventStatus.FAIL)

    def test_resolve_choice_partial_pass(self):
        # Mock character and skill attributes for testing
        party = ['Character1', 'Character2']
        character = Character(name="TestCharacter")
        chosen_skill = 

class TestLocationMethods(unittest.TestCase):
    def setUp(self):
        self.parser = UserInputParser()
        self.location = Location(self.parser)

    def test_create_custom_event_from_static_text_file(self):
        # Mock file path for testing
        file_path = "test_event.json"

        # Create a mock JSON file with event data
        event_data = {
            "primary_attribute": "Strength",
            "secondary_attribute": "Dexterity",
            "prompt_text": "Custom event prompt",
            "pass": {"message": "Custom pass message"},
            "fail": {"message": "Custom fail message"},
            "partial_pass": {"message": "Custom partial pass message"}
        }
        with open(file_path, "w") as file:
            json.dump(event_data, file)

        # Call the function to create a custom event
        custom_event = self.location.create_custom_event_from_static_text_file(file_path)

        # Check if the custom event is created with correct attributes
        self.assertEqual(custom_event.primary.description, "Strength is a measure of physical power.")
        self.assertEqual(custom_event.secondary.description, "Dexterity measures agility, coordination, and quickness.")
        self.assertEqual(custom_event.prompt_text, "Custom event prompt")
        self.assertEqual(custom_event.pass_["message"], "Custom pass message")
        self.assertEqual(custom_event.fail["message"], "Custom fail message")
        self.assertEqual(custom_event.partial_pass["message"], "Custom partial pass message")

    def test_get_event(self):
        # Test getting an event from the location
        event = self.location.get_event()
        self.assertIsNotNone(event)
        self.assertIsInstance(event, Event)

    def test_location_initialization(self):
        # Test location initialization with events
        location = Location(self.parser, number_of_events=3)
        self.assertEqual(len(location.events), 3)

class TestUserMethods(unittest.TestCase):
    def setUp(self):
        self.parser = UserInputParser()
        self.user_factory = UserFactory()
        self.instance_creator = InstanceCreator(self.user_factory, self.parser)

    def test_start_game_new_user(self):
        # Mock user input to simulate starting a new game with a new user
        with patch('builtins.input', side_effect=['yes', 'NewUser', 'Password']):  # Mocking new user input
            start_game()

        # Check if a new user is created and the game is started
        self.assertIsNotNone(game_instance)
        self.assertTrue(isinstance(game_instance, Game))
        self.assertTrue(game_instance.continue_playing)

    def test_start_game_existing_user(self):
        # Mock user input to simulate starting a new game with an existing user
        with patch('builtins.input', side_effect=['no', 'yes']):  # Mocking existing user input
            start_game()

        # Check if an existing user is loaded and the game is started
        self.assertIsNotNone(game_instance)
        self.assertTrue(isinstance(game_instance, Game))
        self.assertTrue(game_instance.continue_playing)

    def test_save_game(self):
        # Create a mock game state to save
        game_state = {"legacy_points": 100}

        # Create a mock user
        user = User(self.parser, "TestUser", "Password")

        # Call the save_game method
        user.save_game(game_state)

        # Check if the game state file is created
        file_path = "TestUser_game_state.json"
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, "r") as file:
            saved_game_state = json.load(file)
        self.assertEqual(saved_game_state["legacy_points"], 100)

