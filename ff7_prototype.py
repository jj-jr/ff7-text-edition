from typing import Type, List

print('')
print('Initializing all assets.')
print('')

### Object handling

class char:
    def __init__(self, name, level, in_party: bool, max_hp, current_hp, str, defense, spd, mgatk, mgdef, luck, dex, exp, atb):
        self.name = name
        self.level = level
        self.in_party = in_party
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.str = str
        self.defense = defense
        self.spd = spd
        self.mgatk = mgatk
        self.mgdef = mgdef
        self.luck = luck
        self.dex = dex
        self.exp = exp
        self.atb = atb


class enemy:
    def __init__(self, name, level, max_hp, current_hp, str, defense, spd, mgatk, mgdef, luck, dex, exp, atb, item, drop_rate):
        self.name = name
        self. level = level
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.str = str
        self.defense = defense
        self.spd = spd
        self.mgatk = mgatk
        self.mgdef = mgdef
        self.luck = luck
        self.dex = dex
        self.exp = exp
        self.atb = atb
        self.item = item
        self.drop_rate = drop_rate

class area:
    def __init__(self, name, is_active: bool, encounter_rate, items):
        self.name = name
        self.is_active = is_active
        self.encounter_rate = encounter_rate
        self.items = items

class item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def potion(self, target):

        hp_remainder = target.max_hp - target.current_hp

        # Adding the full 100 HP to a target who is missing 100 or more HP.
        if target.current_hp <= target.max_hp - 100 and target.current_hp != target.max_hp and target.current_hp != 0:
            target.current_hp += 100
            print(target.name + ' used a potion and restored 100 HP! They currently have ' + str(target.current_hp) + ' HP.')
            return target.current_hp
        # Adding the potion amount to characters missing less than 100 HP or less.
        elif target.current_hp > target.max_hp - 100 and target.current_hp != target.max_hp and target.current_hp != 0:
            target.current_hp += hp_remainder
            print(target.name + ' used a potion and restored ' + str(hp_remainder) + ' HP! They currently have ' + str(target.current_hp) + ' HP.')
            return target.current_hp
        # Character is already at Max HP
        elif target.current_hp == target.max_hp:
            target.current_hp = target.max_hp
            print(target.name + ' is already at max health. ' + target.name + ' has ' + str(target.max_hp) + ' HP.')
            return target.current_hp
        # Item can't be used on fallen party members
        elif target.current_hp == 0:
            print('Item cannot be used on a character with 0 HP.')
        else:
            print('Error.')



### Initializing characters

cloud = char(name='Cloud', level=7, in_party=True, max_hp=700, current_hp=700, str=12, defense=10, spd=10, mgatk=10, mgdef=10, luck=11, dex=10, exp=0, atb=1)
tifa = char(name='Tifa', level=7, in_party=False, max_hp=650, current_hp=650, str=10, defense=9, spd=12, mgatk=12, mgdef=12, luck=10, dex=14, exp=0, atb=1)
barrett = char(name='Barrett', level=7, in_party=False, max_hp=900, current_hp=900, str=10, defense=12, spd=8, mgatk=9, mgdef=10, luck=14, dex=11, exp=0, atb=1)

characters = []
current_party = {'Cloud': True}

def add_char (name):
    print('Added ' + name.name + ' to the list of characters.')
    return characters.append(name.name)


add_char(tifa)
add_char(cloud)
add_char(barrett)


def add_to_party(char):

    global current_party
    if current_party.get(char.name) == None:
        print(char.name + ' joined the party.')
        current_party[char.name] = True
        return current_party
    else:
        print(char.name + ' is already in the party.')
        current_party[char.name] = True
        return current_party

def remove_from_party(char):
    global current_party
    if current_party.get(char.name) != None and not len(current_party) <= 1:
        print(char.name + ' left the party.')
        current_party.pop(char.name)
        return current_party
    elif len(current_party) <= 1 and current_party.get(char.name != None):
        print('Cannot remove all party members.')
        return current_party
    elif current_party.get(char.name) == KeyError:
        print('Didn\'t recognize that input. Try again with a valid party member.')
    else:
        print(char.name + ' isn\'t in your current party.')
        return current_party

### Inventory / item handling

items = []
weapons = []
item_inventory = {}
key_items = []

def add_to_inventory(item, quantity):
    if item not in item_inventory:
        item_inventory[item] = quantity
        print('Added ' + str(quantity) + ' ' + item + 's to your inventory.')
        return item_inventory
    elif item in item_inventory and quantity > 0:
        item_inventory[item] += quantity
        print('Added ' + str(quantity) + ' ' + item + ' to your inventory.')
        return item_inventory
    elif item in item_inventory and quantity < 0:
        item_inventory[item] += quantity
        print('Removed ' + str(abs(quantity)) + ' ' + item + 's from your inventory.')
        return item_inventory
    else:
        print('Error')

### Creating item objects

potion = item('Potion', 'Restore 100 HP')
phoenix_down = item('Phoenix Down', 'Revives a downed party member and restores 100 HP')
ether = item('Ether', 'Restores 40 MP')


### Level handling

def level_up(character):
    print('')
    print('******')
    print(character.name + ' leveled up!')
    print(character.name + ' is now level ' + str(character.level) + '.')
    print('******')
    print('')
    character.level += 1
    return character.level

### Battle system handling

def battle (party, enemy):

    party.current_hp = party.max_hp
    enemy.current_hp = enemy.max_hp
    party_counter = 0
    enemy_counter = 0
    enemy_defeat = False
    party_defeat = False
    party_attack = party.str * 3
    enemy_attack = enemy.str * 3

    def party_atb(char, party_counter):

        #global party_counter
        rate_party = char.spd * 1.2
        party_counter += rate_party
        return party_counter

    def enemy_atb(enemy, enemy_counter):

        #global enemy_counter
        rate_enemy = enemy.spd * 1.2
        enemy_counter += rate_enemy
        return enemy_counter

    #party = current_party
    #enemy = current_enemy

    while enemy_defeat == False and party_defeat == False:
        print('loop')
        while party_counter < 100 or enemy_counter < 100:
            print('1')
            print(party_atb(party, party_counter))
            enemy_atb(enemy, enemy_counter)
            if party_counter >= 100:
                enemy.current_hp -= party_attack
                if enemy.current_hp <= 0:
                    print('Party attack dealt ' + str(party_attack) + ' damage. The enemy has been defeated.')
                    print('Battle over.')
                    enemy_defeat = True
                    break
                else:
                    print('Party attack dealt ' + str(party_attack) + ' damage. The enemy has ' + str(enemy.current_hp) + ' HP remaining.')
                    party_counter = 0
                    break
            elif enemy_counter >= 100:
                party.current_hp -= enemy_attack
                if party.current_hp <= 0:
                    print('Party attack dealt ' + str(enemy_attack) + ' damage. The party has been defeated.')
                    print('Game over.')
                    party_defeat = True
                    break
                else:
                    print('Enemy attack dealt ' + str(enemy_attack) + ' damage. The party has ' + str(party.current_hp) + ' HP remaining.')
                    enemy_counter = 0
                    break
    else:
        pass

'''   def party_atb(char):
        party_counter = 0
        step = 0
        step_total = 0
        rate_party = char.spd * 1.2
        while party_counter <= 100:
            print(round(party_counter))
            step += 1
            print(char.name + ' step ' + str(step))
            party_counter += rate_party
            print(step)
        step_total = step
        print('Step total: ' + str(step_total))
        return step_total
        #return round(party_counter)

    def enemy_atb(enemy):
        enemy_counter = 0
        step = 0
        rate_enemy = enemy.spd * 1.2
        while enemy_counter <= 100:
            print(round(enemy_counter))
            step += 1
            print(enemy.name + ' step ' + str(step))
            enemy_counter += rate_enemy
        return step
        #return round(enemy_counter) step '''

'''   while battle_active == True:
        enemy.current_hp = enemy.max_hp
        party.current_hp = party.max_hp
        party_counter = 0
        enemy_counter = 0
        party_attack = party.str * 3
        enemy_attack = enemy.str * 3
        print(enemy.current_hp, party.current_hp)
        if enemy.current_hp <= 0:
            ('You won the battle!')
            return battle_active == False
            break
        elif party.current_hp <= 0:
            ('Your party has been defeated')
            return battle_active == False
            break
        else:
            if party_counter >= 100:
                print('1')
                enemy.current_hp -= party_attack
                print(party.name + ' attacked for ' + str(party_attack))
                party_counter = 0
                return enemy.current_hp, party_counter
            elif enemy_counter >= 100:
                print('2')
                party.current_hp -= enemy_attack
                print('Enemy attacked for ' + str(enemy_attack))
                enemy_counter = 0
                return party.current_hp, enemy_counter
            elif party_counter < 100:
                print('3')
                party_atb(party)
                print(party_counter)
                print(party.current_hp)
                return party_counter
            elif enemy_counter < 100:
                print('4')
                enemy_atb(enemy)
                print(enemy_counter)
                print(enemy.current_hp)
                return enemy_counter
            else:
                print('Error.')'''





### Initializing enemies

shinra_soldier = enemy(name='Shinra Soldier', level=6, max_hp=300, current_hp=300, str=4, defense=4, spd=9, mgatk=3, mgdef=5, luck=1, dex=5, exp=10, atb=1, item=ether, drop_rate=0.3)
shinra_mech = enemy(name='Shinra Mech', level=7, max_hp=400, current_hp=400, str=5, defense=6, spd=7, mgatk=3, mgdef=5, luck=2, dex=6, exp=18, atb=1, item=phoenix_down, drop_rate=0.2)

#def add_enemy(name):
    #print('Added ' + name.name + ' to the list of enemies.')
    #return enemies[name] = name.name

enemies = {shinra_mech}
current_enemy = [shinra_mech]

#add_enemy(shinra_soldier)

### Initializing items for areas

midgar_items = ['Potion', 'Ether', 'Hi-Potion']
shinra_reactor_items = ['Phoenix Down', 'Potion', 'Molotov Cocktail']

### Initializing areas

shinra_reactor = area(name='Shinra Reactor', is_active=True, encounter_rate=30, items=shinra_reactor_items)
midgar_slums = area(name='Midgar Slums', is_active=False, encounter_rate=50, items=midgar_items)

def add_area(name):
    print('Added ' + name.name + ' to the list of areas.')
    return areas.append(name.name)

areas = []

add_area(shinra_reactor)
add_area(midgar_slums)

### Beginning of gameplay

tifa.current_hp = 0

level_up(cloud)
add_to_inventory(potion.name, 7)
print(item_inventory)
add_to_inventory(potion.name, -2)
print(item_inventory)
add_to_inventory(phoenix_down.name, 2)
print(item_inventory)
add_to_inventory(potion.name, -3)
print(item_inventory)
item.potion((), cloud)
cloud.current_hp = 640
print('Cloud took 60 damage!')
item.potion((), cloud)
print('Cloud took 700 damage from a critical hit! He is at 0 HP.')
cloud.current_hp = 700
item.potion((), cloud)

print('')
add_to_party(cloud)
add_to_party(cloud)
add_to_party(tifa)
remove_from_party(tifa)
remove_from_party(tifa)
print(current_party)
print('')

#print(battle(cloud, shinra_mech))

'''def party_atb(char):
    party_counter = 0
    step = 0
    rate_party = char.spd * 1.2
    while party_counter <= 100:
        #print(round(party_counter))
        step += 1
        #print(char.name + ' step ' + str(step))
        party_counter += rate_party
        #print(step)
    print('Step total: ' + str(step))
    return step
    # return round(party_counter)'''

'''party_counter = 0
enemy_counter = 0

def party_atb(char):

    global party_counter
    rate_party = char.spd * 1.2
    party_counter += rate_party
    return party_counter

def enemy_atb(enemy):

    global enemy_counter
    rate_enemy = enemy.spd * 1.2
    enemy_counter += rate_enemy
    return enemy_counter

enemy_hp = 100
party_hp = 200
turn_count = 0
party_defeat = False
enemy_defeat = False

while enemy_defeat == False and party_defeat == False:
    while party_counter < 100 or enemy_counter < 100:
        party_atb(cloud)
        enemy_atb(shinra_mech)
        if party_counter >= 100:
            attack = 40
            enemy_hp -= attack
            if enemy_hp <= 0:
                print('Party attack dealt ' + str(attack) + ' damage. The enemy has been defeated.')
                print('Battle over.')
                enemy_defeat = True
                break
            else:
                print('Party attack dealt ' + str(attack) + ' damage. The enemy has ' + str(enemy_hp) + ' HP remaining.')
            party_counter = 0
            break
        elif enemy_counter >= 100:
            enemy_attack = 80
            party_hp -= enemy_attack
            if party_hp <= 0:
                print('Party attack dealt ' + str(enemy_attack) + ' damage. The party has been defeated.')
                print('Game over.')
                party_defeat = True
                break
            else:
                print('Enemy attack dealt ' + str(enemy_attack) + ' damage. The party has ' + str(party_hp) + ' HP remaining.')
            enemy_counter = 0
            break
else:
    pass'''


#print(party_atb(cloud))
#print(enemy_atb(shinra_mech))
print(battle(cloud, shinra_mech))

