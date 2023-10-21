import os
import tkinter as tk
from tkinter import ttk

# Dictionary to store notes
notes = {'People': {}, 'Places': {}, 'Things that Happen': {}, 'Items': {}, 'History': {}, 'Knowledge': {}, 'Jokes': {}}



# Function to display the last 5 logs
def display_last_logs():
    for category, entries in notes.items():
        if entries:
            print(f"Category: {category}")
            for title, description in list(entries.items())[-5:]:
                print(f"Title: {title}")
                print(f"Description: {description}")
                print('-' * 30)

# Function to save notes to a text file
def save_notes(session_num):
    with open(f"session_{session_num}_notes.txt", 'w') as file:
        for category, entries in notes.items():
            for title, description in entries.items():
                file.write(f"Category: {category}\n")
                file.write(f"Title: {title}\n")
                file.write(f"Description: {description}\n")
                file.write('-' * 30 + '\n')

# Function to handle the "Save and Exit" button click event
def save_and_exit():
    session_num_entry = (input(str))
    session_num = session_num_entry.get()
    save_notes(session_num)
    root.destroy()

# Main menu loop
root = tk.Tk()
root.title("TTRPG Notatilator V.1")

# Create and configure GUI elements
label = tk.Label(root, text="Choose a category below, write a title, then write a description for entry!")
label.pack()

category_label = tk.Label(root, text="Choose a category:")
category_label.pack()

category_var = tk.StringVar(value='People')
category_dropdown = ttk.Combobox(root, textvariable=category_var, values=list(notes.keys()))
category_dropdown.pack()

title_label = tk.Label(root, text="Enter a title (48 characters):")
title_label.pack()

title_entry = tk.Entry(root, width=48)
title_entry.pack()

description_label = tk.Label(root, text="Enter a description (140 characters):")
description_label.pack()

description_entry = tk.Entry(root, width=140)
description_entry.pack()

save_exit_button = tk.Button(root, text="Save and Exit", command=save_and_exit)
save_exit_button.pack()

while True:
    root.update()
    choice = category_var.get()
    if choice == 'Exit':
        session_num = session_num_entry.get()
        save_notes(session_num)
        break


    if choice in notes:
        category = choice
        title = title_entry.get()

        if title in notes[category]:
            description = description_entry.get()
            notes[category][title] += '\n' + description
        else:
            description = description_entry.get()
            notes[category][title] = description

# End of the program