import PirateClass


class Rogue(PirateClass.Pirate):
    def __init__(self, _variables):
        variables = list(_variables)
        PirateClass.Pirate.__init__(self, variables[0], variables[1], variables[2])
        self.bow_arrow = 20
        self.cloak = 10
        self.boots = 30

    def get_def(self):
        return self.defense + self.cloak

    def get_att(self):
        return self.attack + self.bow_arrow

    def get_dex(self):
        return self.dexterity + self.boots

    def print_stats(self):
        print(self.name + "(" + self.type + "):\n\tTotal Att: " + str(self.get_att()) +
              "\n\tTotal Def: " + str(self.get_def()) + "\n\tTotal Dex: " + str(
            self.get_dex()) + "\n\tID: " + str(self.id) + "\n")


class Mage(PirateClass.Pirate):
    def __init__(self, _variables):
        variables = list(_variables)
        PirateClass.Pirate.__init__(self, variables[0], variables[1], variables[2])
        self.magic_staff = 30
        self.robe = 20
        self.speed_spell = 10

    def get_def(self):
        return self.defense + self.robe

    def get_att(self):
        return self.attack + self.magic_staff

    def get_dex(self):
        return self.dexterity + self.speed_spell

    def print_stats(self):
        print(self.name + "(" + self.type + "):\n\tTotal Att: " + str(self.get_att()) +
              "\n\tTotal Def: " + str(self.get_def()) + "\n\tTotal Dex: " + str(
            self.get_dex()) + "\n\tID: " + str(self.id) + "\n")


class Warrior(PirateClass.Pirate):
    def __init__(self, _variables):
        variables = list(_variables)
        PirateClass.Pirate.__init__(self, variables[0], variables[1], variables[2])
        self.leatherArmour = 30
        self.blades = 20
        self.metalBoots = 10

    def get_def(self):
        return self.defense + self.leatherArmour

    def get_att(self):
        return self.attack + self.blades

    def get_dex(self):
        return self.dexterity + self.metalBoots

    def print_stats(self):
        print(self.name + "(" + self.type + "):\n\tHeath: " + str(self.health) + "\n\tTotal Att: " +
              str(self.get_att()) + "\n\tTotal Def: " + str(self.get_def()) + "\n\tTotal Dex: " + str(
            self.get_dex()) + "\n\tID: " + str(self.id) + "\n")
