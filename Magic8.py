
# Magic 8 ball user will get one of 9 random fortunes.
# setup
from random import randint

#gets users name
print(" Welcome to the magic 8-ball game, what is your name?")
name = input()

# setting up random
r = randint(1,9)

# print(r , name)

if r == 1:
    print("Okay, " + str(name) + " Signs point to yes. ")

if r == 2:
    print( + str(name) + " Outlook good")

if r == 3:
    print( + str(name) + " Very doubtful")

if r == 4:
    print( + str(name) + " Without a doubt")

if r == 5:
    print( + str(name) + " Yes, definitely")

if r == 6:
    print( + str(name) + " It is decidedly so")

if r == 7:
    print( + str(name) + " Don’t count on it")

if r == 8:
    print( + str(name) + " My reply is no ")

if r == 9:
    print( + str(name) + " You may rely on it")
