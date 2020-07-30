from typing import Type, List

print('')
print('Initializing all assets.')
print('')

### Object handling

class char:
    def __init__(self, name, level, in_party: bool, max_hp, current_hp, str, defense, spd, mgatk, mgdef, luck, dex, exp=0, atb=0):
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
    def __init__(self, name, description, quantity=0):
        self.name = name
        self.description = description
        self.quantity = quantity

    def potion(self, target):

        hp_remainder = target.max_hp - target.current_hp

        # Adding the full 100 HP to a target who is missing 100 or more HP.
        if target.current_hp <= target.max_hp - 100 and target.current_hp != target.max_hp and target.current_hp != 0:
            target.current_hp += 100
            self.quantity - 1
            print(target.name + ' used a potion and restored 100 HP! They currently have ' + str(target.current_hp) + ' HP.')
            return target.current_hp, self.quantity
        # Adding the potion amount to characters missing less than 100 HP or less.
        elif target.current_hp > target.max_hp - 100 and target.current_hp != target.max_hp and target.current_hp != 0:
            target.current_hp += hp_remainder
            self.quantity - 1
            print(target.name + ' used a potion and restored ' + str(hp_remainder) + ' HP! They currently have ' + str(target.current_hp) + ' HP.')
            return target.current_hp, self.quantity
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

cloud = char(name='Cloud', level=7, in_party=True, max_hp=700, current_hp=700, str=12, defense=10, spd=10, mgatk=10, mgdef=10, luck=11, dex=10)
tifa = char(name='Tifa', level=7, in_party=False, max_hp=650, current_hp=650, str=10, defense=9, spd=12, mgatk=12, mgdef=12, luck=10, dex=14)
barrett = char(name='Barrett', level=7, in_party=False, max_hp=900, current_hp=900, str=10, defense=12, spd=8, mgatk=9, mgdef=10, luck=14, dex=11)

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
        item.quantity += quantity
        print('Added ' + str(quantity) + ' ' + item + 's to your inventory.')
        return item_inventory, item.quantity
    elif item in item_inventory and quantity > 0:
        item_inventory[item] += quantity
        item.quantity += quantity
        print('Added ' + str(quantity) + ' ' + item + ' to your inventory.')
        return item_inventory, item.quantity
    elif item in item_inventory and quantity < 0:
        item_inventory[item] += quantity
        item.quantity += quantity, item.quantity
        print('Removed ' + str(abs(quantity)) + ' ' + item + 's from your inventory.')
        return item_inventory, item.quantity
    else:
        print('Error')

### Creating item objects

potion = item('Potion', 'Restore 100 HP', 0)
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

    enemy.current_hp = enemy.max_hp
    party_counter = 0
    enemy_counter = 0
    enemy_defeat = False
    party_defeat = False
    party_attack = party.str * 3
    enemy_attack = enemy.str * 3

    def party_atb(char, atb):

        rate_party = char.spd * 1.2
        atb += rate_party
        return round(atb)

    def enemy_atb(enemy, atb):

        rate_enemy = enemy.spd * 1.2
        atb += rate_enemy
        return round(atb)

    while enemy_defeat == False and party_defeat == False:
        while party_counter < 100 or enemy_counter < 100:
            party_counter = party_atb(party, party_counter)
            enemy_counter = enemy_atb(enemy, enemy_counter)
            if party_counter >= 100:
                enemy.current_hp -= party_attack
                if enemy.current_hp <= 0:
                    print(party.name + ' dealt ' + str(party_attack) + ' damage. ' + enemy.name + ' has been defeated.')
                    print('Battle over.')
                    enemy_defeat = True
                    break
                else:
                    print(party.name + ' dealt ' + str(party_attack) + ' damage. ' + enemy.name + ' has ' + str(enemy.current_hp) + ' HP remaining.')
                    party_counter = 0
                    break
            elif enemy_counter >= 100:
                party.current_hp -= enemy_attack
                if party.current_hp <= 0:
                    party_defeat = True
                    print(enemy.name + ' dealt ' + str(enemy_attack) + ' damage. ' + party.name + ' has been defeated.')
                    print('Game over.')
                    break
                else:
                    print(enemy.name + ' dealt ' + str(enemy_attack) + ' damage. ' + party.name + ' has ' + str(party.current_hp) + ' HP remaining.')
                    enemy_counter = 0
                    break
    else:
        pass

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

tifa.current_hp = 200

battle(cloud, shinra_soldier)

print('Potion quantity is ' + str(potion.quantity))
print('Cloud ATB is ' + str(cloud.atb))

remove_from_party(barrett)

