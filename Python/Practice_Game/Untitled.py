import random

#Variables
characterName = []
enemyName = []

experience = []

strength = random.random()
speed = random.random()
defense = random.random()
magic = random.random()
charisma = random.random()
proficiency = magic + 1
luck = proficiency * random.random()


statValue = [strength, speed, defense, magic, charisma, luck]
statName = ["strength", "speed", "defense", "magic", "charisma", "luck"]

stats = [statName, " ", statValue]

for stat in stats:
    print("\n", stat)
