

class Pirate:
    def __init__(self, _name, _type, _id):
        self.name = _name
        self.type = _type
        self.id = _id
        self.health = 100
        self.defense = 30
        self.attack = 50
        self.dexterity = 30

    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True
