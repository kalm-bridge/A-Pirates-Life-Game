import PirateShipClass
import Game


def main():
    print("Welcome to the Pirate's Life For Me\n")
    print('First things first, You must form your band of'
          ' merry pirate\'s!\n')

    team1 = PirateShipClass.PirateShip(input("What is Your Team's Name!: "))

    print("Remember there can only be three members on each team.\n")
    x = 0
    while x < 3:
        print('There are three main classes '
              '\n(1)Rogue\n(2)Warrior\n(3)Mage\nRead your scrolls for their '
              'further breakdown.\nwhat kind of pirate would you like to make?\n')
        player_type = input("Choose one of the three options: ")
        player_type = player_type.lower()
        if player_type == 'mage' or player_type == "warrior" or player_type == "rogue" \
                or player_type == "1" or player_type == "2" or player_type == "3":
            team1.add_pirates(input("What is your name?\n"), player_type)
            x = x + 1
        else:
            print("Incorrect input, please try again.\n")

    team1.print_team()

    print("An enemy ship has entered the " + team1.name + "'s waters!\nWho are they?\n")
    team2 = PirateShipClass.PirateShip(input("What is The enemy Team's Name!: "))

    print("Remember there can only be three member on each team.\n")
    y = 0
    while y < 3:
        print('There are three main classes '
              '\n(1)Rogue\n(2)Warrior\n(3)Mage\nRead your scrolls for their '
              'further breakdown.\nwhat kind of pirate would you like to make?\n')
        player_type = input("Choose one of the three options: ")
        player_type = player_type.lower()
        if player_type == 'mage' or player_type == "warrior" or player_type == "rogue" \
                or player_type == "1" or player_type == "2" or player_type == "3":
            team2.add_pirates(input("What is your name?\n"), player_type)
            y = y + 1
        else:
            print("Incorrect input, please try again.\n")

    team2.print_team()
    starter = ""
    while starter.lower() != "start":
        starter = input("Type Start to begin the battle!\n\tOr press 'Ctrl + C' to exit\n")

    _round = 0
    attackers = team2
    defenders = team1
    while (not Game.game_over(team1, team2)) and _round < 5:
        player_damage = [0, 0, 0]
        if _round == 0:
            attackers = team2
            defenders = team1
        if _round == 1:
            attackers = team1
            defenders = team2
        if _round == 2:
            attackers = team2
            defenders = team1
        if _round == 3:
            attackers = team1
            defenders = team2
        if _round == 4:
            attackers = team2
            defenders = team1
        print("Round: " + str(_round) + "! Start!\n")
        print(attackers.name + " will now launch there assault on " + defenders.name +
              "'s ship!\n")
        player_damage = Game.team_att(attackers, defenders, player_damage)
        print(defenders.name + " can now counter " + attackers.name +
              " on there assault on their ship!\n")
        player_damage = Game.team_counter(defenders, player_damage)

        player_damage = Game.apply_damage(defenders, player_damage)

        _round += 1

    if team1.team_hp_check() and (not team2.team_hp_check()):
        print("Congratulations " + team1.name + " won the game!!\n")
    elif team2.team_hp_check() and (not team1.team_hp_check()):
        print("Congratulations " + team2.name + " won the game!!\n")
    else:
        print("AW! it was a draw...somehow\n")

    input("Press Enter to exit.\n")


main()

