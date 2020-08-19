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

'''print(f'Current Cloud HP: {char.cloud.max_hp}')
print('Cloud HP increase amount: ' + str((level.cloud_stat_up.hp.get(8))))
print(level.cloud_stat_up.hp.get(8))
char.cloud.max_hp += level.cloud_stat_up.hp.get(8)
print(char.cloud.max_hp)
print(level.cloud_stat_up.hp.get(9))
print(char.cloud.max_hp + level.cloud_stat_up.hp.get(9))'''
#print(level.cloud_stat_up.)

#if char.

#print(char.cloud.level)
#print(char.cloud.stats)

#level.cloud_level_up()

'''char.cloud.level = 8
print(char.cloud.level)
#char.cloud.max_hp = char.cloud_hp_increase[char.cloud.level]
char.cloud.max_hp = char.stats_map[char.cloud.name, 'max_hp'][char.cloud.level]
print('Prior max HP: ' + str(char.cloud.max_hp))
char.cloud.level = 9
#char.cloud.max_hp = char.cloud_hp_increase[char.cloud.level]
char.cloud.max_hp = char.stats_map[char.cloud.name, 'max_hp'][char.cloud.level]
print(char.cloud.level)
print('Post increase level HP: ' + str(char.cloud.max_hp))'''

'''char.barret.level = 8
print(char.barret.level)
#char.cloud.max_hp = char.cloud_hp_increase[char.cloud.level]
char.barret.max_hp = char.stats_map[char.barret.name, 'max_hp'][char.barret.level]
print('Prior max HP: ' + str(char.barret.max_hp))
char.barret.level = 9
#char.cloud.max_hp = char.cloud_hp_increase[char.cloud.level]
char.barret.max_hp = char.stats_map[char.barret.name, 'max_hp'][char.barret.level]
print(char.barret.level)
print('Post increase level HP: ' + str(char.barret.max_hp))'''
