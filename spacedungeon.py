import random
import sys

"""text based game where user makes decisions which affect a series of
encounters with 'enemies'"""

player = {
'HP': 100,
'attack': 100,
'defense': 100,
'name': 'Lame space man'
}

enemy1 = {
'HP': 100,
'attack': 100,
'defense': 100,
'name': 'Zombie AI human'
}

enemy2 = {
'HP': 50,
'attack': 50,
'defense': 50,
'name': 'Zombie crewman'
}

enemy3 = {
'HP': 30,
'attack': 15,
'defense': 5,
'name': 'Fluffy bunny'
}

enemy6 = {
'HP': 1,
'attack': 1,
'defense': 0,
'name': 'Half of a fluffy bunny'
}

enemy4 = {
'HP': 40,
'attack': 10,
'defense': 50,
'name': 'Talking Space cow'
}

enemy5 = {
'HP': 70,
'attack': 60,
'defense': 55,
'name': 'John Snow'
}


def game_over(player):
    print("GAME OVER -- ", player['name'], "You and everyone on *ship name* are dead, dessicated carbon. Decades\
     from now a scientific survey vessel will stumble across your ship and investigators\
     will log the incident.")
    return sys.exit()


def get_item(player):
    item_list = ["MRE", "First Aid Kit", "Meth-derived stim-pack", " bag of lost hopes and dreams"]

    print("You find a ", item_list[random.randint(0, 3)], "your health increased by ",
    (abs(player['HP'] - 100)), "HP")
    # player['HP'] += (abs(player['HP'] - 100))
    player['HP'] = 100
    return player


def attack(opponent):
    rand_damage = random.randint(8, 32)
    opponent['HP'] -= rand_damage
    print(rand_damage, " damage!")
    return opponent


def fight(oppo1, oppo2):
    while (oppo1['HP'] > 0) and (oppo2['HP'] > 0):
        print(oppo1['name'], " attacks ", oppo2['name'])
        attack(oppo2)
        if oppo2['HP'] <= 0:
            print(oppo1['name'], " is winner")
        else:
            print(oppo2['name'], " attacks ", oppo1['name'])
            attack(oppo1)
        if oppo1['HP'] <= 0:
            print(oppo2['name'], " is winner")
            game_over(oppo1)
    print('player1 oppo1 HP: ', oppo1['HP'])
    print('enemy1  oppo2 HP: ', oppo2['HP'])


def encounter(player, opponent):
    if player['HP'] > 45:
        fight(player, opponent)
        # if player['HP'] <= 0:
        #     return game_over(player)
        input('Press any key to continue')
    elif opponent['name'] == 'Zombie AI human':
        fight(player, opponent)
        # return player
    else:
        get_item(player)
        input('Press any key to continue')



"""there are encounters, each encounter offers an option to
open a door, the door will either have an enemy or an item"""


def main():
    # fight(player, enemy1)

    # get_item(player)
    print('encounter 1...\n\n')

    encounter(player, enemy3)

    print('encounter 2...\n\n')

    encounter(player, enemy6)

    print('encounter 3...\n\n')

    encounter(player, enemy4)

    print('encounter 4...\n\n')

    encounter(player, enemy5)

    print('encounter 5...\n\n')

    encounter(player, enemy2)

    print('encounter 6...\n\n')

    encounter(player, enemy1)



    print("YOU HAVE ESCAPED -- WINNER", player['name'], " HP: ", player['HP'])


if __name__ == "__main__":
    # print("Executing as main program")
    # print("Value of __name__ is: ", __name__)
    main()