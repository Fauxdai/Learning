import random
import os

# Character Class Choices
classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin',
           'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

# Character Race Choices
races = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn', 'Gnome', 'Half-Elf',
         'Half-Orc', 'Tiefling']

# Ability Scores Constants
ABILITY_SCORES = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']

def roll_ability_score():
    """Rolls a random ability score between 3 and 18"""
    return random.randint(3, 18)

def roll_ability_scores():
    """Rolls ability scores for all six abilities"""
    ability_scores = {}
    for ability in ABILITY_SCORES:
        ability_scores[ability] = roll_ability_score()
    return ability_scores

def select_class():
    """Prompts the user to select a character class"""
    clear_screen()
    print("Select a Character Class:")
    for index, char_class in enumerate(classes, start=1):
        print(f"{index}. {char_class}")
    while True:
        choice = int(input("Enter the number corresponding to your choice: "))
        if choice > 0 and choice <= len(classes):
            return classes[choice - 1]
        print("Invalid choice. Please try again.")

def select_race():
    """Prompts the user to select a character race"""
    clear_screen()
    print("Select a Character Race:")
    for index, race in enumerate(races, start=1):
        print(f"{index}. {race}")
    while True:
        choice = int(input("Enter the number corresponding to your choice: "))
        if choice > 0 and choice <= len(races):
            return races[choice - 1]
        print("Invalid choice. Please try again.")

def generate_character():
    """Generates a new D&D character"""
    clear_screen()
    character = {}
    character['Class'] = select_class()
    character['Race'] = select_race()
    character['Ability Scores'] = roll_ability_scores()
    return character

def display_character(character):
    """Displays the character's details"""
    clear_screen()
    print("\n----- Character Details -----")
    print(f"Class: {character['Class']}")
    print(f"Race: {character['Race']}")
    print("\nAbility Scores:")
    for ability, score in character['Ability Scores'].items():
        print(f"{ability}: {score}")
    print("-----------------------------\n")

def clear_screen():
    """Clears the terminal/console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("Welcome to the D&D Character Creator!")
    while True:
        character = generate_character()
        display_character(character)
        choice = input("Press 'R' to create another character or 'E' to exit: ").lower()
        if choice == 'e':
            clear_screen()
            print("\nExiting the D&D Character Creator. Goodbye!")
            break

if __name__ == '__main__':
    main()
