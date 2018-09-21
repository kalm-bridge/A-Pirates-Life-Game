import PirateClass
import Players


class PirateShip:
    def __init__(self, _name):
        self.name = _name
        print(self.name + " has joined the fray a new band of pirates!\n")
        self.player_count = 0
        self.players = []

    def add_pirates(self, _name, _type):
        if _type == "mage" or _type == "3":
            _type = "mage"
            self.players.append(Players.Mage([_name, _type, self.player_count]))
        elif _type == "rogue" or _type == "1":
            _type = "rogue"
            self.players.append(Players.Rogue([_name, _type, self.player_count]))
        elif _type == "warrior" or _type == "2":
            _type = "warrior"
            self.players.append(Players.Warrior([_name, _type, self.player_count]))
        self.player_count = self.player_count + 1
        print(_type + " pirate: " + _name + " has joined " + self.name +
              "'s band of merry pirates.\n")

    def get_pirate(self, _name):
        for player in self.players:
            if player.name == _name:
                return player
        return None

    def print_team(self):
        print("There are " + str(len(self.players)) + " pirates on the" +
              self.name + " ship\n")
        for player in self.players:
            player.print_stats()

    def team_hp_check(self):
        death_count = 0
        ship_sunk = False
        print(self.name + ":\n")
        for player in self.players:
            if player.health <= 0:
                death_count = death_count + 1
                print(player.name + " has 0 HP.(out of the game)\n")
            else:
                print(player.name + " has " + str(player.health) + " HP.")
        if death_count == len(self.players):
            ship_sunk = True
        return ship_sunk
