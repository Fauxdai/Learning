print("I have information for the following planetMod:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

Venus = 0.91
Mars = 0.38
Jupiter = 2.34
Saturn = 1.06
Uranus = 0.92
Neptune = 1.19

planetMod= [Venus, Mars, Jupiter, Saturn, Uranus, Neptune]
planetNames = ["Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

planetChoice = planetMod[planet-1]
planetName=planetNames[planet-1]

for weights, name in zip(planetMod, planetNames): print("you will be " + str(int(weights*weight)) + " on " +str(name))

print("") 
print("You are on: " + planetName) 
print("Your Weight is: "+str(int(planetChoice*weight))) 
print("")