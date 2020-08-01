from typing import Type, List
import areas, \
    battle_system as b, \
    characters_playable as char, \
    enemies, inventory, \
    items, \
    level, \
    art
import random

print('')
print('Initializing all assets.')
print('')

print(level.cloud_exp_threshold)

### Beginning of gameplay

b.battle(char.cloud, enemies.shinra_mech)
b.battle(char.cloud, enemies.shinra_soldier)
b.battle(char.cloud, enemies.shinra_soldier)
b.battle(char.cloud, enemies.shinra_soldier)
b.battle(char.cloud, enemies.shinra_mech)
b.battle(char.cloud, enemies.shinra_mech)
'''char.cloud.current_hp = 422
items.use_hi_potion(char.barrett, char.cloud)
char.cloud.current_mp = 22
items.use_turbo_ether(char.cloud, char.cloud)
items.use_phoenix_down(char.barrett, char.cloud)
char.cloud.current_hp = 0
items.use_phoenix_down(char.barrett, char.cloud)
char.cloud.current_hp = 72
items.use_molotov_cocktail(enemies.shinra_soldier, char.cloud)
inventory.add_to_inventory(items.potion, 0)'''
print(char.cloud.exp)
print(level.cloud_exp_threshold)
print('Total gil is: ' + str(inventory.gil))
print(inventory.item_inventory)