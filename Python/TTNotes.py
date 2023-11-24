import tkinter as tk

# Dictionary to store notes
notes = {'People': {}, 'Places': {}, 'Things that Happen': {}, 'Items': {}, 'History': {}, 'Knowledge': {}, 'Jokes': {}}

def display_last_logs():
    # You should modify this function to update a text widget in the GUI
    pass

def save_notes(session_num, game_title):
    # You should modify this function to save the notes to a file from the GUI
    pass

def handle_choice(choice):
    if choice == '8':
        session_num = session_num_entry.get()
        game_title = game_title_entry.get()
        save_notes(session_num, game_title)
        root.destroy()
    else:
        category = list(notes.keys())[int(choice) - 1]
        title = title_entry.get()
        description = description_entry.get("1.0", "end-1c")  # Get text from a Text widget
        if title in notes[category]:
            notes[category][title] += '\n' + description
        else:
            notes[category][title] = description
        display_last_logs()  # Update the display in the GUI

root = tk.Tk()
root.title("D&D Note-Logging App")

# Create and configure GUI elements
category_label = tk.Label(root, text="Choose a category:")
category_label.pack()

category_choices = ["People", "Places", "Things that Happen", "Items", "History", "Knowledge", "Jokes"]
category_var = tk.StringVar()
category_var.set(category_choices[0])
category_menu = tk.OptionMenu(root, category_var, *category_choices)
category_menu.pack()

title_label = tk.Label(root, text="Enter a title:")
title_label.pack()
title_entry = tk.Entry(root)
title_entry.pack()

description_label = tk.Label(root, text="Enter a description:")
description_label.pack()
description_entry = tk.Text(root, height=5, width=40)
description_entry.pack()

session_label = tk.Label(root, text="Enter session number:")
session_label.pack()
session_num_entry = tk.Entry(root)
session_num_entry.pack()

game_title_label = tk.Label(root, text="Enter the title of the game:")
game_title_label.pack()
game_title_entry = tk.Entry(root)
game_title_entry.pack()

exit_button = tk.Button(root, text="Exit", command=lambda: handle_choice('8'))
exit_button.pack()

save_button = tk.Button(root, text="Save", command=lambda: handle_choice(category_var.get()))
save_button.pack()

root.mainloop()

