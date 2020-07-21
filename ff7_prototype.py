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
    def __init__(self, name, level, max_hp, current_hp, str, defense, spd, mgatk, mgdef, luck, dex, exp, atb):
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

class area:
    def __init__(self, name, is_active: bool, encounter_rate, items):
        self.name = name
        self.is_active = is_active
        self.encounter_rate = encounter_rate
        self.items = items

class item:
    def __init__(self, name, description, effect, quantity):
        self.name = name
        self.description = description
        self.effect = effect
        self.quantity = quantity

    def potion(self, target):

        hp_remainder = target.max_hp - target.current_hp

        if target.current_hp <= target.max_hp - 100 and target.current_hp != target.max_hp:
            target.current_hp += 100
            print(target.name + ' restored 100 HP! They currently have ' + str(target.current_hp) + ' HP.')
            return target.current_hp
        elif target.current_hp > target.max_hp - 100 and target.current_hp != target.max_hp:#and target.max_hp - target.current_hp < 0:
            target.current_hp += hp_remainder
            print(target.name + ' restored ' + str(hp_remainder) + ' HP! They currently have ' + str(target.current_hp) + ' HP.')
            return target.current_hp
        elif target.current_hp == target.max_hp:
            target.current_hp = target.max_hp
            print(target.name + ' is already at max health. ' + target.name + ' has ' + str(target.max_hp) + ' HP.')
            return target.current_hp
        elif target.current_hp == 0:
            print('Item cannot be used on a character with 0 HP.')
        else:
            print('Error.')



### Initializing characters

cloud = char(name='Cloud', level=7, in_party=True, max_hp=700, current_hp=700, str=12, defense=10, spd=10, mgatk=10, mgdef=10, luck=11, dex=10, exp=0, atb=0)
tifa = char(name='Tifa', level=7, in_party=False, max_hp=650, current_hp=650, str=10, defense=9, spd=12, mgatk=12, mgdef=12, luck=10, dex=14, exp=0, atb=0)
barrett = char(name='Barrett', level=7, in_party=False, max_hp=900, current_hp=900, str=10, defense=12, spd=8, mgatk=9, mgdef=10, luck=14, dex=11, exp=0, atb=0)

def add_char (name):
    print('Added ' + name.name + ' to the list of characters.')
    return characters.append(name.name)

characters = []

add_char(tifa)
add_char(cloud)
add_char(barrett)

### Inventory / item handling

inventory = []
weapons = []
item_inventory = []
key_items = []


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

'''def battle (character: object, enemy: object):

    print('A battle has started with ' + enemy + '!')

    char.atb = 0
    enemy.atb = 0

    def atb_step():
        atb_char = character.spd * 1.2
        atb_enemy = enemy.spd * 1.2
        return atb_char, atb_enemy

    while enemy.hp >= 0:
        if character.atb or enemy.atb >= 100:'''



### Initializing enemies

shinra_soldier = enemy(name='Shinra Soldier', level=6, max_hp=300, current_hp=300, str=4, defense=4, spd=9, mgatk=3, mgdef=5, luck=1, dex=5, exp=10, atb=0)
shinra_mech = enemy(name='Shinra Mech', level=7, max_hp=400, current_hp=400, str=5, defense=6, spd=7, mgatk=3, mgdef=5, luck=2, dex=6, exp=18, atb=0)

def add_enemy(name):
    print('Added ' + name.name + ' to the list of enemies.')
    return enemies.append(name.name)

enemies = []

add_enemy(shinra_soldier)

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

tifa.current_hp = 650

level_up(cloud)
item.potion((), tifa)
