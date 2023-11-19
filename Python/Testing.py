import csv
import os
from statistics import mode

def read(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
    else:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        data = [['Name', 'Rolls', 'Sum', 'Average', 'Mode', 'Score']]
    return data

def get_valid_dice_roll():
    while True:
        try:
            roll = int(input("Enter a dice roll (1-6): "))
            if 1 <= roll <= 6:
                return roll
            else:
                print("Invalid input. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_dice_rolls():
    print("Enter 10 dice rolls:")
    rolls = [get_valid_dice_roll() for _ in range(10)]
    return rolls

def calculate_statistics(rolls):
    total = sum(rolls)
    average = total / float(len(rolls))

    try:
        mode_value = mode(rolls)
    except statistics.StatisticsError:
        mode_value = "No unique mode"

    return total, average, mode_value

def calculate_score(total, mode_value):
    score_value = total * mode_value
    return score_value

def display_results(username, rolls, total, average, mode_value, score_value):
    os.system('cls' if os.name == "nt" else "clear")
    print("=================================================")
    print(f"Your name is: {username}")
    print("Your rolls are:", rolls)
    print("Your sorted rolls are:", sorted(rolls))
    print("Your roll total is:", total)
    print("Your average is:", average)
    print("Your mode is:", mode_value)
    print("Your score is: ", score_value)
    print("=================================================")

def save_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)

def show_results(file_path, data):
    with open(file_path, 'r') as result:
        reader = csv.reader(result)
        data = list(reader)
        for row in data:
            print(" || {:<30} ".format(str(row[0])), " || {:<30} ".format(str(row[1])),
                  " || {:<15} ".format(str(row[2])), " || {:<15} ".format(str(row[3])),
                  " || {:<15} ".format(str(row[4])), " || {:<15} ".format(str(row[5])))

def main():
    file_path = os.path.expanduser("~/Documents/Roll_Log.csv")
    username = get_username()
    rolls = get_dice_rolls()
    total, average, mode_value = calculate_statistics(rolls)
    score_value = calculate_score(total, mode_value)
    entry = [username, rolls, total, average, mode_value, score_value]
    data = read(file_path)

    sort_results(file_path, data)
    save_to_csv(file_path, data)
    display_results(username, rolls, total, average, mode_value, score_value)
    data.append(entry)
    save_to_csv(file_path, data)
    show_results(file_path, data)

    input("Press enter to continue")

if __name__ == "__main__":
    main()
