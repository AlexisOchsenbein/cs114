
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
    print("Okay, " + str(name) + " Outlook good")

if r == 3:
    print("Okay, " + str(name) + " Very doubtful")

if r == 4:
    print("Okay, " + str(name) + " Without a doubt")

if r == 5:
    print("Okay, " + str(name) + " Yes, definitely")

if r == 6:
    print("Okay, " + str(name) + " It is decidedly so")

if r == 7:
    print("Okay, " + str(name) + " Don’t count on it")

if r == 8:
    print("Okay, " + str(name) + " My reply is no ")

if r == 9:
    print("Okay, " + str(name) + " You may rely on it")
