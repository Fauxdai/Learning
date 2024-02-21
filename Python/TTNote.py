import os
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

# Dictionary to store notes
notes = {'People': {}, 'Places': {}, 'Things that Happen': {}, 'Items': {}, 'History': {}, 'Knowledge': {}, 'Jokes': {}, 'Meta':{}}

# Function to display the last 5 logs
def display_last_logs():
    for category, entries in notes.items():
        if entries:
            print(Fore.LIGHTMAGENTA_EX + f"---------- Category: {category} ----------")
            for title, description in list(entries.items())[-5:]:
                print(Fore.LIGHTGREEN_EX + f"-Title: {title.capitalize()}")
                print(Fore.LIGHTMAGENTA_EX + f"--Description: \n\n - {description}\n")
                print(Fore.LIGHTMAGENTA_EX + '---' * 30)

# Function to save notes to a text file
def save_notes(session_num):
    with open(f"session_{session_num}_notes.txt", 'w') as file:
        for category, entries in notes.items():
            for title, description in entries.items():
                file.write(f"---------- Category: {category} ---------\n")
                file.write(f"-Title: {title.capitalize()}\n")
                file.write(f"--Description:\n\n {description}\n")
                file.write('---' * 30 + '\n')

def displayBanner():
    banner = f"""
|------------------ WELCOME TO THE TTRPG Notatilator V.1! ------------------|
|Choose a category below, Write a title, Then write a description for entry!|
|To append an entry, simply duplicate your title")                          |
|---------------------------------------------------------------------------|
    """
    print(Fore.CYAN + banner)

def displayChoices():
    choice = f"""
Choose a category:
1. People
2. Places
3. Things that Happen
4. Items
5. History
6. Knowledge
7. Jokes
8. Meta/OOC
9. Exit
    """
    print(Fore.GREEN + choice)

# Main menu loop
while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    displayBanner()
    display_last_logs()
    displayChoices()

    choice = input("Enter your choice: ")

    if choice == '9':
        session_num = input("Enter session name: ")
        save_notes(session_num)
        break

    if choice in {'1', '2', '3', '4', '5', '6', '7', '8'}:
        category = list(notes.keys())[int(choice) - 1]
        title = input("  Enter a title: ")

        if title.casefold() in notes[category]:
            description = input("    Enter a description (append to the existing entry): ")
            notes[category][title.casefold()] += '\n' + '\n' + "- " + description
        else:
            description = input("    Enter a description: ")
            notes[category][title.casefold()] = description

# End of the program









