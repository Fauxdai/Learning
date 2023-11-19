import os

# Dictionary to store notes
notes = {'People': {}, 'Places': {}, 'Things that Happen': {}, 'Items': {}, 'History': {}, 'Knowledge': {},'Meta':{}, 'Jokes': {}}

# Function to display the last 5 logs
def display_last_logs():
    for category, entries in notes.items():
        if entries:
            print(f"\nCategory: {category}")
            print('#' * 60 + '\n')
            for title, description in list(entries.items())[-50:]:
                print(f"Title: {title}")
                print(f"Description: {description}\n")
                print('-' * 30)

# Function to save notes to a text file
def save_notes(session_num):
    with open(f"session_{session_num}_notes.txt", 'w') as file:
        for category, entries in notes.items():
            file.write(f"\nCategory: {category}\n")
            file.write('#' * 60 + '\n')
            for title, description in entries.items():
                file.write(f"Title: {title}\n")
                file.write(f"Description: {description}\n")
                file.write('-' * 30 + '\n')
                
                
# Main menu loop
while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    print("------------------ WELCOME TO THE TTRPG Notatilator V.1! ------------------")
    print("Choose a category below, Write a title, Then write a description for entry!")
    print("To append an entry, simply duplicate your title")
    print("---------------------------------------------------------------------------")
    display_last_logs()
    print("\nChoose a category:")
    print("1. People")
    print("2. Places")
    print("3. Things that Happen")
    print("4. Items")
    print("5. History")
    print("6. Knowledge")
    print("7. Meta")
    print("8. Jokes")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '9':
        session_num = input("Name of File: ")
        save_notes(session_num)
        break

    if choice in {'1', '2', '3', '4', '5', '6', '7', '8'}:
        category = list(notes.keys())[int(choice) - 1]
        title = input("Enter a title: ")

        if title.casefold().title() in notes[category]:
            description = input("Enter a description (append to the existing entry): ")
            notes[category][title.casefold().title()] += '\n' + '\n' + "- " + description
        else:
            description = input("Enter a description: ")
            notes[category][title.casefold().title()] = '\n'+ "- " + description

# End of the program









