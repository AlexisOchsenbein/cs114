#Make a program that asks a user their name and returns a randomly chosen "fortune" response from the
#"magic 8 ball". Make 9 different possible "fortunes".
    #setup
from random import randint

#Get users name

print(" Welcome to the magic 8-ball game, what is your name?")
name = input()

# setting up random
r = randint(1,9)

# print(r , name)
def fortune(r):

    if r == 1:
        fortune_random = ("Okay, " + str(name) + " Signs point to yes. ")

    if r == 2:
        fortune_random = ("Okay, " + str(name) + " Outlook good")

    if r == 3:
        fortune_random = ("Okay, " + str(name) + " Very doubtful")

    if r == 4:
        fortune_random = ("Okay, " + str(name) + " Without a doubt")

    if r == 5:
        fortune_random = ("Okay, " + str(name) + " Yes, definitely")

    if r == 6:
        fortune_random = ("Okay, " + str(name) + " It is decidedly so")

    if r == 7:
        fortune_random = ("Okay, " + str(name) + " Don’t count on it")

    if r == 8:
        fortune_random = ("Okay, " + str(name) + " My reply is no ")

    if r == 9:
        fortune_random = ("Okay, " + str(name) + " You may rely on it")
    return fortune_random

def main():
    fortune_random = fortune(r)
    return print(fortune_random)

main()
