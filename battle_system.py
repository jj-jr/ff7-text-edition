import level, inventory
import random

### Battle system handling

def battle (party, enemy):

    enemy.current_hp = enemy.max_hp
    party_counter = 0
    enemy_counter = 0
    enemy_defeat = False
    party_defeat = False
    base_attack = party.str * 3
    enemy_attack = enemy.str * 3

    def party_atb(char, atb):

        rate_party = char.spd * 1.2
        atb += rate_party
        return round(atb)

    def enemy_atb(enemy, atb):

        rate_enemy = enemy.spd * 1.2
        atb += rate_enemy
        return round(atb)

    print('Your party encountered a ' + enemy.name + '!')
    print('')

    while enemy_defeat == False and party_defeat == False:
        attack_randomizer = round(random.randint(round(int((-1 * ((0.3 * party.str))))), round(int(((0.3 * party.str))))))
        while party_counter < 100 or enemy_counter < 100:
            party_counter = party_atb(party, party_counter)
            enemy_counter = enemy_atb(enemy, enemy_counter)
            if party_counter >= 100:
                party_attack = base_attack
                party_attack += attack_randomizer
                enemy.current_hp -= party_attack
                if enemy.current_hp <= 0:
                    print(party.name + ' attacked and dealt ' + str(party_attack) + ' damage. ' + enemy.name + ' has been defeated!')
                    print('Battle over.')
                    party.exp += enemy.exp
                    enemy_defeat = True
                    break
                else:
                    print(party.name + ' attacked and dealt ' + str(party_attack) + ' damage. ' + enemy.name + ' has ' + str(enemy.current_hp) + ' HP remaining.')
                    party_counter = 0
                    break
            elif enemy_counter >= 100:
                party.current_hp -= enemy_attack
                if party.current_hp <= 0:
                    party_defeat = True
                    print(enemy.name + ' attacked and dealt ' + str(enemy_attack) + ' damage. ' + party.name + ' has been defeated!')
                    print('Game over.')
                    break
                else:
                    print(enemy.name + ' attacked and dealt ' + str(enemy_attack) + ' damage. ' + party.name + ' has ' + str(party.current_hp) + ' HP remaining.')
                    enemy_counter = 0
                    break
    else:
        pass

    if enemy_defeat == True:
        print('')
        print('The party gained ' + str(enemy.exp) + ' EXP and ' + str(enemy.gil) + ' gil!')
        inventory.gil += enemy.gil
        if random.random() <= enemy.drop_rate:
            print('The enemy dropped a ' + enemy.item.name + ' and it has been added to your inventory!')
            return inventory.add_to_inventory(enemy.item, 1)
        else:
            pass
    print('')
    if party.exp >= level.cloud_exp_threshold[0]:
        level.level_up(party)
        return level.cloud_exp_threshold.pop(0)
    else:
        pass
