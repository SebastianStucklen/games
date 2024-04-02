import random

# Common (60.00% Base Drop Rate)
# Uncommon (26.00% Base Drop Rate)
# Rare (10.00% Base Drop Rate)
# Very Rare (3.00% Base Drop Rate)
# Legendary (1.00% Base Drop Rate)

#chance upgrade = 12
def fishgen(chance = 0):
    roll = random.random()
    roll *= 100
    if roll < 1+chance/3:
        return "Legendary"
    elif roll < 3+chance/3:
        return "Very Rare"
    elif roll < 10+chance/3:
        return "Rare"
    elif roll < 26-chance/2:
        return "Uncommon"
    elif roll < 60-chance/2:
        return "Common"