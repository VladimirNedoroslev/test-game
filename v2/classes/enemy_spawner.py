import random
from typing import List

from v2.classes.enemy import Enemy


class EnemySpawner:

    def spawn_random_enemies(self, enemies: List[Enemy], number_of_enemies_to_spawn: int) -> List[Enemy]:
        for i in range(len(enemies) - number_of_enemies_to_spawn):
            random_index = random.randint(0, len(enemies) - 1)
            enemies.pop(random_index)

        return enemies

