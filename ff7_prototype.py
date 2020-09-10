import battle_system as b
import characters_playable as char
import enemies
import inventory

print('')
print('Starting the game.')
print('')

### Beginning of gameplay

char.tifa.in_party = True
char.barret.in_party = True

enemy = [enemies.shinra_mech, enemies.shinra_soldier, enemies.shinra_dog]
current_party = [char.cloud, char.tifa, char.barret]

b.battle(current_party, enemy)

print(inventory.item_inventory)