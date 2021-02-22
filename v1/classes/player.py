from armor import Armor
from weapon import Weapon


class Player:
    def __init__(self, hp=100):
        self.hp = hp
        self.weapon = Weapon(10)
        self.armor = Armor(1)

    def is_alive(self):
        return self.hp > 0
