import random

stats = ['Strength', 'Dexterity', 'Constitution', 'Wisdom', 'Intelligence', 'Charisma']
stat_values = {}

def roll_stat():
    return random.randint(1, 20)

def display_stats():
    print("\n----- Current Stats -----")
    for stat in stats:
        if stat in stat_values:
            print(f"{stat}: {stat_values[stat]}")
        else:
            print(f"{stat}: Not rolled yet")
    print("-------------------------\n")

def main():
    print("Welcome to the D&D Stat Roller!")
    while True:
        display_stats()
        choice = input("Press R to roll a stat, E to exit: ").lower()

        if choice == 'r':
            stat = random.choice(stats)
            stat_value = roll_stat()
            stat_values[stat] = stat_value
            print(f"\n{stat} rolled: {stat_value}\n")
        elif choice == 'e':
            print("\nExiting the D&D Stat Roller. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == '__main__':
    main()

