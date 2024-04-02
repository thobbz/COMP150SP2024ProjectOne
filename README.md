# Avengers Legacy Game

Welcome to the Avengers Legacy Game! This is a text-based adventure game where you play as a member of the Avengers team and make choices to save the universe from the threat of Thanos.

## Game Setup

1. Make sure you have Python installed on your system.
2. Clone or download the game files from the repository.
3. Install any required dependencies by running `pip install -r requirements.txt` in the project directory.

## How to Play

1. Run the game by executing the `main.py` file using Python.
2. The game will prompt you to either create a new user or log in to an existing account. Follow the instructions to enter a username and password.
3. If you are starting a new game, you will be asked to select a character from the available Avengers team members.
4. You are also prompted to create a random character with random attributes which can be selected from the party.
5. The game will present you with different locations and events. Read the descriptions carefully and choose your actions from the available options.
6. Each choice you make will have an impact on the outcome of the game. Your character's attributes (strength, dexterity, intelligence, etc.) will determine the success or failure of certain actions.
7. As you progress through the game, you will earn legacy points based on your performance. These points can be used to enhance your character's abilities in future playthroughs.
8. The goal of the game is to make the right choices and successfully defeat Thanos to save the universe.
9. If you choose to quit the game at any point, your progress will be automatically saved, and you can resume from where you left off the next time you play.

## Game Files

- `main.py`: The main entry point of the game. Run this file to start playing.
- `game.py`: Contains the core game logic and manages the flow of the game.
- `character.py`: Defines the character classes and their attributes.
- `event.py`: Handles the events and choices presented to the player during the game.
- `location.py`: Represents the different locations in the game world.
- `statistic.py`: Defines the various character statistics and their properties.
- `parser.py`: Handles user input parsing and validation.
- `user_model.py`: Manages user accounts and game state persistence.
- `instancecreator.py`: Creates instances of game objects based on user input.
- `locations.json`: Contains data for the different locations in the game.
- `events.json`: Contains data for the events and choices in the game.

## Customization

You can customize the game by modifying the `locations.json` and `events.json` files. Add new locations, events, and choices to create your own unique game experience. Make sure to follow the existing data structure and format.

## Feedback and Support

If you encounter any issues or have suggestions for improving the game, please feel free to open an issue on the GitHub repository or contact the game developers.

Enjoy playing the Avengers Legacy Game and have fun saving the universe!