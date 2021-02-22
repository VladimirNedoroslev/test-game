import random

from v2.classes.enemy_spawner import EnemySpawner
from v2.configuration import enemies_list

enemy_spawner = EnemySpawner()

print("You find yourself in a poorly lit dungeon, there are three routes in front of you, "
      "you need to get out this stinking hole alive!")
# player_choice = input("Which way will you go? ")

random_enemies = enemy_spawner.spawn_random_enemies(enemies_list, 3)

print('You face ', )

