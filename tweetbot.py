#twitterbot spammmer
#Setup
import random


#transform

def get_scream():
    numA = random.randint(1,15)
    numH = random.randint(1,15)
    textA = "a" * numA
    textH = "h" * numH
    return textA + textH

scream = get_scream()
print(scream)
