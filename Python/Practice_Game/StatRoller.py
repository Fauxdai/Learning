import random

#-----corestats

strength = ()
dexterity = ()
constitution = () 
wisdom = ()
intelligence = () 
charisma = ()

#-----Script
print("")
print("Welcome to StatRoller!")
print("Here is your stats: ")

print("")
print("")


# This function takes the name array and the random number generator and concatenates them. 
def stats():
    statname = ["Strength: ", "Dexterity: ", "Constitution: ", "Wisdom: ", "Intelligence: ", "Charisma: "]
    corestats = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    for statname in statname:
        corestats = random.randint(1,20)
        print(str(statname) + str(corestats))
        
# ------- This formats the function for (hopefully) better readability. 
print("##########")
print("")
stats()
print("")
print("##########")
# ------- End of Function


# - This section asks if you would like to re-roll. If so, it will run the function again. If not, it will exit. If given bad input, the program will ask again. 
print("")
print("")
roll = str.lower(input("Roll Again? Y/N/Exit: "))
print("")

while roll.lower() not in ("Yes"):
    print("")
    if roll == "no":
        exit()
    elif roll == "n":
        exit()
    elif roll == "exit":
        exit()
    elif roll == "Exit":
        exit()
    elif roll == "yes":
        print("##########")
        print("")
        stats()
        print("")
        print("##########")
        print("")
        roll = str.lower(input("Roll Again? Y/N/Exit: "))
        print ("")
        continue
    elif roll == "y":
        print("##########")
        print("")
        stats()
        print("")
        print("##########")
        print("")
        roll = str.lower(input("Roll Again? Y/N/Exit: "))
        print("")
        continue
    else:
        print("Invalid Response. Try again")
        print("")
        roll = str.lower(input("Roll Again? Y/N/Exit: "))