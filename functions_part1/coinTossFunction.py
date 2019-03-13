from random import random

def flip_coin():
    #generate random num 0-1
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"



def flip_coin():  ####### this will override the same function above
    if random() > 0.5:
        return "HEADS"
    else:
        return "TAILS"

print(flip_coin())


