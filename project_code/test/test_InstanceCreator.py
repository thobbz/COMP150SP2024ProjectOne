import unittest
from unittest.mock import MagicMock, patch
from project_code.src.user_code.user_model import User
from project_code.src.user_code.user_model import UserFactory        
from project_code.src.utils.parser import UserInputParser
from project_code.src.core.instancecreator import InstanceCreator
from project_code.src.user_code.user_model import User
from project_code.src.core.event import Event, EventStatus
from project_code.src.eventparser import EventParser
from project_code.src.core.location import Location
from project_code.src.core.character import Character
from project_code.src.common.statistic import Statistic
from project_code.src.skill import Skill
from project_code.src.core.game import Game
from project_code.src.main import start_game
import json
import os

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
        chosen_skill = Skill(name="TestSkill", description="Test skill description", base_damage=10, attributes=["attribute1", "attribute2"])

        # Set up the event with non-overlapping attributes
        self.event.primary = Statistic(30)
        self.event.secondary = Statistic(40)

        # Resolve choice with non-overlapping attributes
        self.event.resolve_choice(party, character, chosen_skill)
        self.assertEqual(self.event.status, EventStatus.FAIL)

    def test_resolve_choice_partial_pass(self):
        # Mock character and skill attributes for testing
        party = ['Character1', 'Character2']
        character = Character(name="TestCharacter")
        chosen_skill = Skill(name="TestSkill", description="Test skill description", base_damage=10, attributes=["attribute1", "attribute2"])

        # Set up the event with partially overlapping attributes
        self.event.primary = Statistic(10)
        self.event.secondary = Statistic(30)

        # Resolve choice with partially overlapping attributes
        self.event.resolve_choice(party, character, chosen_skill)
        self.assertEqual(self.event.status, EventStatus.PARTIAL_PASS)

    def test_resolve_choice_pass(self):
        # Mock character and skill attributes for testing
        party = ['Character1', 'Character2']
        character = Character(name="TestCharacter")
        chosen_skill = Skill(name="TestSkill", description="Test skill description", base_damage=10, attributes=["attribute1", "attribute2"])

        # Set up the event with fully overlapping attributes
        self.event.primary = Statistic(10)
        self.event.secondary = Statistic(20)

        # Resolve choice with fully overlapping attributes
        self.event.resolve_choice(party, character, chosen_skill)
        self.assertEqual(self.event.status, EventStatus.PASS)


class TestLocationMethods(unittest.TestCase):
    def setUp(self):
        self.parser = EventParser()
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
        event = self.location.get_event(0)
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
    with patch('builtins.input', side_effect=['yes', 'NewUser', 'Password']):
        game_instance = start_game()

    # Check if a new user is created and the game is started
    self.assertIsNotNone(game_instance)
    self.assertTrue(isinstance(game_instance, Game))
    self.assertTrue(game_instance.continue_playing)

def test_start_game_existing_user(self):
    # Mock user input to simulate starting a new game with an existing user
    with patch('builtins.input', side_effect=['no', 'yes']):
        game_instance = start_game()

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
        user.save_game()

        # Check if the game state file is created
        file_path = "TestUser_game_state.json"
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, "r") as file:
            saved_game_state = json.load(file)
        self.assertEqual(saved_game_state["legacy_points"], 100)
if __name__ == '__main__':
    unittest.main()
