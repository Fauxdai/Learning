import csv
import os
from statistics import mode

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def read(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
    else:
        data = [['Name', 'Rolls', 'Total', 'Average', 'Mode']]
    return data

# Other functions...

def display_results_table(data):
    print("}---------- RESULTS ----------{")
    print(" || {:<15} || {:<25} || {:<10} || {:<15} || {:<10} ||".format("Name", "Rolls", "Total", "Average", "Mode"))
    for row in data:
        print(" || {:<15} || {:<25} || {:<10} || {:<15} || {:<10} ||".format(*row))
    print("}-------------------------------{")

def main():
    global file_path
    clear_screen()
    username = get_username()
    rolls = get_dice_rolls()
    total, average, mode_value = calculate_statistics(rolls)

    entry = [username, rolls, total, average, mode_value]
    file_path = "Roll_Log.csv"

    data = read(file_path)

    display_results(username, rolls, total, average, mode_value)

    input("Press Enter to Continue")
    clear_screen()

    print("Saving Data\n\n")
    data.append(entry)
    save_to_csv(file_path, data)

    display_results_table(data)

    input("Press Enter to exit")

if __name__ == "__main__":
    main()
