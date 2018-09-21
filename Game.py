
def game_over(team_a, team_b):
    if team_a.team_hp_check():
        return True
    print("\n")
    if team_b.team_hp_check():
        return True
    else:
        return False


def att_bonus(attacker, defender):
    bonus = 0
    if attacker.type == "mage" and defender.type == "warrior":
        bonus = attacker.get_att() * (20/100)
        return bonus
    if attacker.type == "rogue" and defender.type == "mage":
        bonus = attacker.get_att() * (20/100)
        return bonus
    elif attacker.type == "rogue" and defender.type == "rogue":
        bonus = attacker.get_att() * (10/100)
        return bonus
    if attacker.type == "warrior" and defender.type == "rogue":
        bonus = attacker.get_att() * (20/100)
        return bonus
    elif attacker.type == "warrior" and defender.type == "mage":
        bonus = attacker.get_att() * (10/100)
        return bonus
    return bonus


def attack(attacker, defender, player_damage):
    bonus = att_bonus(attacker, defender)
    player_damage[defender.id] += (attacker.get_att() + bonus) - defender.get_def()
    if player_damage[defender.id] <= 0:
        player_damage[defender.id] = 0
    print(attacker.name + " did " + str(attacker.get_att() + bonus) + " damage to "
          + defender.name + " but they deflected " + str(defender.get_def()) + " of it.\n")
    return player_damage


def team_att(attackers, defenders, player_damage):
    p1 = None
    while p1 is None:
        player1 = input("Who will go first? ")
        p1 = attackers.get_pirate(player1)
        if p1 is None:
            print("That pirate is not on " + attackers.name + "'s ship.\n")
            continue
        if not p1.is_alive():
            print("This pirate is no longer able to play.\n")
            break
        defender = input("Who would you like to attack: ")
        d1 = defenders.get_pirate(defender)
        if d1 is None:
            print("That pirate is not on " + defenders.name + "'s ship.\n")
            p1 = None
            continue
        player_damage = attack(p1, d1, player_damage)

    p2 = None
    while p2 is None:
        player2 = input("Who will go second?")
        p2 = attackers.get_pirate(player2)
        if p2 is None:
            print("That pirate is not on " + attackers.name + "'s ship.\n")
            continue
        elif p2.name == p1.name:
            print("pirate already made a move!\n")
            p2 = None
            continue
        if not p2.is_alive():
            print("This pirate is no longer able to play.\n")
            break
        defender2 = input("Who would you like to attack: ")
        d2 = defenders.get_pirate(defender2)
        if d2 is None:
            print("That pirate is not on " + defenders.name + "'s ship.\n")
            p2 = None
            continue
        player_damage = attack(p2, d2, player_damage)

    p3 = None
    while p3 is None:
        player3 = input("Who will go third?")
        p3 = attackers.get_pirate(player3)
        if p3 is None:
            print("That pirate is not on " + attackers.name + "'s ship.\n")
            continue
        elif p3.name == p1.name or p3.name == p2.name:
            print("pirate already made a move!\n")
            p3 = None
            continue
        if not p3.is_alive():
            print("This pirate is no longer able to play.\n")
            break
        defender3 = input("Who would you like to attack: ")
        d3 = defenders.get_pirate(defender3)
        if d3 is None:
            print("That pirate is not on " + defenders.name + "'s ship.\n")
            p3 = None
            continue
        player_damage = attack(p3, d3, player_damage)
    return player_damage


def counter(defender, counted, player_damage):
    c_bonus = counted.get_att() * (counted.get_dex()/100)
    player_damage[defender.id] = player_damage[defender.id] - c_bonus
    if player_damage[defender.id] <= 0:
        player_damage[defender.id] = 0
    print(counted.name + " deflected " + str(c_bonus) + " damage off "
          + defender.name + "\n")
    return player_damage


def team_counter(defenders, player_damage):
    count = 0
    while count < 3:
        if player_damage[count] == 0:
            print(defenders.players[count].name + " can save a teammate ")
            save = input("Who would they like to save: ")
            d3 = defenders.get_pirate(save)
            if d3 is None:
                print("That pirate is not on " + defenders.name + "'s ship.\n")
                continue
            elif d3.name == defenders.players[count].name:
                print("You can't save yourself!?\n")
                continue
            elif not d3.is_alive():
                print("This pirate is no longer able to play.\n")
                count = count + 1
                continue
            else:
                player_damage = counter(d3, defenders.players[count], player_damage)
                count = count + 1
        else:
            print(defenders.players[count].name + " can not save a teammate while defending")
            count = count + 1
    return player_damage


def apply_damage(team, player_damage):
    print(team.name + ": \n")
    for player in team.players:
        player.health = player.health - player_damage[player.id]
        print(player.name + " took " + str(player_damage[player.id]) + " to their HP\n")
    return player_damage