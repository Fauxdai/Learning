import random

#-----corestats

strength = ()
dexterity = ()
constitution = () 
wisdom = ()
intelligence = () 
charisma = ()


corestats = [strength, dexterity, constitution, wisdom, intelligence, charisma]
#-----Script
print("")
print("Welcome to StatRoller!")
print("Here is your stats: ")
print("")
print("")


# This function takes the name array and the random number generator and concatenates them. 
def stats():
    statname = ["Strength", "Dexterity", "Constitution", "Wisdom", "Intelligence", "Charisma"]
    for statname in statname:
        corestats = random.randint(8,20)
        def mod():
            match corestats:
                case 20: print("Your "+str(statname)+" modifier is 5")
                case 19: print("Your "+str(statname)+" modifier is 5")
                case 18: print("Your "+str(statname)+" modifier is 4")
                case 17: print("Your "+str(statname)+" modifier is 4")
                case 16: print("Your "+str(statname)+" modifier is 3")
                case 15: print("Your "+str(statname)+" modifier is 3")
                case 14: print("Your "+str(statname)+" modifier is 2")
                case 13: print("Your "+str(statname)+" modifier is 2")
                case 12: print("Your "+str(statname)+" modifier is 1")
                case 11: print("Your "+str(statname)+" modifier is 1")
                case 10: print("Your "+str(statname)+" modifier is 0")
                case 9: print("Your "+str(statname)+" modifier is -1")
                case 8: print("Your "+str(statname)+" modifier is -1")
                case 7: print("Your "+str(statname)+" modifier is -2")
                case 6: print("Your "+str(statname)+" modifier is -2")
                case 5: print("Your "+str(statname)+" modifier is -3")
                case 4: print("Your "+str(statname)+" modifier is -3")
                case 3: print("Your "+str(statname)+" modifier is -4")
                case 2: print("Your "+str(statname)+" modifier is -4")
                case 1: print("Your "+str(statname)+" modifier is -5")
        print(str(statname)+": " + str(corestats))
        mod()
        print("")



        
# ------- This formats the function for (hopefully) better readability. 
print("-----STATS-----")
print("")
stats()
print("_______________")
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
        print("-----STATS-----")
        print("")
        stats()
        print("")
        print("_______________")
        print("")
        roll = str.lower(input("Roll Again? Y/N/Exit: "))
        print ("")
        continue
    elif roll == "y":
        print("-----STATS-----")
        print("")
        stats()
        print("")
        print("_______________")
        print("")
        roll = str.lower(input("Roll Again? Y/N/Exit: "))
        print("")
        continue
    else:
        print("Invalid Response. Try again")
        print("")
        roll = str.lower(input("Roll Again? Y/N/Exit: "))