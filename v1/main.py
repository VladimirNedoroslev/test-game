from classes.enemy import Enemy
from    classes.player import Player

TURNS_TO_WIN = 3
AVAILABLE_DIRECTIONS = ['l', 'r', 'f']
AFTER_TURN_PHRASE = {
    'l': 'You went to the left',
    'r': 'You went to the right',
    'f': 'You went forward'
}
print('Welcome to the game')

player = Player(hp=100)
turns_taken = 0

while turns_taken < TURNS_TO_WIN and player.is_alive():
    enemies = {'l': Enemy.create_random_enemy(),
               'r': Enemy.create_random_enemy(),
               'f': Enemy.create_random_enemy(), }
    print(enemies)
    chosen_direction = input('Where will you go? ').lower()
    if chosen_direction not in AVAILABLE_DIRECTIONS:
        print('Available options are: "l" - turn left, "r" - turn right, "f" - go forward')
        continue


    print(AFTER_TURN_PHRASE[chosen_direction])

    target_enemy = enemies[chosen_direction]
    print(f'And now you face {target_enemy.name}')
    target_enemy.show_info()

    while player.is_alive() or target_enemy.is_alive():
        player_damage = player.weapon.damage

        if player.armor.defense >= target_enemy.damage:
            print('Vash vrag pizdec lox ne mojet probit broniyu, on podox!')
            target_enemy.kill()
            break

        target_enemy.hp -= player_damage
        print(f"You attack! You've dealt {player_damage} to {target_enemy.name}")
        if target_enemy.is_alive():
            print(f'He has {target_enemy.hp} HP left')
        else:
            print('He died in agony!')
            break

        player.hp = player.hp - target_enemy.damage + player.armor.defense
        print(f"{target_enemy.name} attacks you! He's dealt {target_enemy.damage} to you")
        if player.is_alive():
            print(f'Now you have {player.hp} HP')
        else:
            print('LOX EBANIY, SDOX!')
            break

    turns_taken += 1


print('KRASAVA!')