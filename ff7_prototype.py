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

### Beginning of gameplay

enemies = [enemies.shinra_mech, enemies.shinra_soldier, enemies.shinra_dog]
current_party = [char.cloud, char.tifa, char.barrett]

b.battle(current_party, enemies)
print('Total gil is: ' + str(inventory.gil))
print(inventory.item_inventory)
print(art.tifa_image)
