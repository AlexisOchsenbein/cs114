#Make a program that asks a user their name and returns a randomly chosen "fortune" response from the
#"magic 8 ball". Make 9 different possible "fortunes".
    #setup
from random import randint

#Get users name

print(" Welcome to the magic 8-ball game, what is your name?")
name = input()

# setting up random
r = randint(1,8)

# print(r , name)
def fortune(r):
    fortune_list = [
    " You may rely on it",
    " My reply is no ",
    " Don’t count on it",
    " It is decidedly so",
    " Yes, definitely",
    " Without a doubt",
    " Very doubtful",
    " Outlook good",
    " Signs point to yes. ",
    ]
    return fortune_list[r]
def main():
    fortune_list = fortune(r)
    return print(fortune_list)

main()
