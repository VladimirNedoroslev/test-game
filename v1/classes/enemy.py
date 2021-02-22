# Goblin, hp=10, damage=2, loot=None
# Ogre, hp=70, damage=10, loot=None
# Pidor, hp=130, damage=20, loot=None
import random


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.loot = None

    def is_alive(self):
        return self.hp > 0

    def kill(self):
        self.hp = 0

    def show_info(self):
        print(f'Name - {self.name}')
        print(f'Hp - {self.hp}')
        print(f'Damage - {self.damage}')

    @staticmethod
    def create_random_enemy():

        random_index = random.randint(0, 2)
        if random_index == 0:
            return Enemy.create_goblin()
        if random_index == 1:
            return Enemy.create_ogre()
        if random_index == 2 :
            return Enemy.create_pidor()

    @staticmethod
    def create_goblin():
        return Enemy('Goblin', 10, 2)

    @staticmethod
    def create_ogre():
        return Enemy('Ogre', 70, 10)

    @staticmethod
    def create_pidor():
        return Enemy('Pidor!', 130, 20)

    def __repr__(self):
        return self.name
