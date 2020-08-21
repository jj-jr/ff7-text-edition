import battle_system as b
import characters_playable as char
import enemies
import inventory

print('')
print('Starting the game.')
print('')

### Beginning of gameplay

enemy = [enemies.shinra_mech, enemies.shinra_soldier, enemies.shinra_dog]
current_party = [char.cloud, char.tifa, char.barret]

#b.battle(current_party, enemies)
#print('Total gil is: ' + str(inventory.gil))
#print(inventory.item_inventory)
#print(art.tifa_image)

b.battle(current_party, enemy)
print(enemy)
enemy = [enemies.shinra_mech, enemies.shinra_soldier, enemies.shinra_dog]
print(enemy)
b.battle(current_party, enemy)
enemy = [enemies.shinra_mech, enemies.shinra_soldier, enemies.shinra_dog]
b.battle(current_party, enemy)
print(inventory.item_inventory)