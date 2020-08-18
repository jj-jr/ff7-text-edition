from typing import Type, List
import areas, \
    battle_system as b, \
    characters_playable as char, \
    enemies, inventory, \
    items, \
    level, \
    art, \
    common_functions as cf, \
    keyboard

import random

print('')
print('Starting the game.')
print('')

### Beginning of gameplay

enemies = [enemies.shinra_mech, enemies.shinra_soldier, enemies.shinra_dog]
current_party = [char.cloud, char.tifa, char.barret]

b.battle(current_party, enemies)
print('Total gil is: ' + str(inventory.gil))
print(inventory.item_inventory)
print(art.tifa_image)

print(f'Current Cloud HP: {char.cloud.max_hp}')
print('Cloud HP increase amount: ' + str((level.cloud_stat_up.hp.get(8))))
print(level.cloud_stat_up.hp.get(8))
char.cloud.max_hp += level.cloud_stat_up.hp.get(8)
print(char.cloud.max_hp)
print(level.cloud_stat_up.hp.get(9))
print(char.cloud.max_hp + level.cloud_stat_up.hp.get(9))
#print(level.cloud_stat_up.)

#if char.

print(char.cloud.level)
print(char.cloud.stats)