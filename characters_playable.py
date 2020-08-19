import level, common_functions as cf
import random

### Character object handling

class char:
    """Creating class for all playable characters."""
    def __init__(self, name, level, level_threshold, in_party: bool, max_hp, current_hp, max_mp, current_mp, str_, defense, spd, mgatk, mgdef, luck, dex, exp=0, atb=0, actions=['Attack', 'Item']):
        self.name = name
        self.level = level
        self.level_threshold = level_threshold
        self.in_party = in_party
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.max_mp = max_mp
        self.current_mp = current_mp
        self.str_ = str_
        self.defense = defense
        self.spd = spd
        self.mgatk = mgatk
        self.mgdef = mgdef
        self.luck = luck
        self.dex = dex
        self.exp = exp
        self.atb = atb
        self.actions = actions

### Initializing characters

cloud = char(name='Cloud', level=7, level_threshold=[], in_party=True, max_hp=322, current_hp=700, max_mp=50, current_mp=50, str_=12, defense=10, spd=10, mgatk=10, mgdef=10, luck=11, dex=10)
tifa = char(name='Tifa', level=7, level_threshold=[], in_party=False, max_hp=325, current_hp=650, max_mp=60, current_mp=60, str_=13, defense=9, spd=12, mgatk=12, mgdef=12, luck=10, dex=14)
barret = char(name='Barret', level=7, level_threshold=[], in_party=False, max_hp=350, current_hp=900, max_mp=30, current_mp=30, str_=10, defense=12, spd=8, mgatk=9, mgdef=10, luck=14, dex=11)

### Party management

def add_to_party(char):

    if char not in current_party:
        print(char.name + ' joined the party.')
        char.in_party = True
        current_party.append(char)
        return current_party, char.in_party
    else:
        print(char.name + ' is already in the party.')
        return current_party

def remove_from_party(char):

    if char in current_party and not len(current_party) <= 1:
        print(char.name + ' left the party.')
        char.in_party = False
        current_party.remove(char)
        return current_party, char.in_party
    elif len(current_party) <= 1 and char in current_party:
        print('Cannot remove all party members.')
        return current_party
    else:
        print(char.name + ' isn\'t in your current party.')
        return current_party

characters = []
current_party = [cloud]

def add_char (name):
    #print('Added ' + name.name + ' to the list of characters.')
    return characters.append(name.name)

add_char(tifa)
add_char(cloud)
add_char(barret)

actions = ['Attack', 'Item']

### Stat increases

def rnd(num_1, num_2):
    random_number = random.randint(num_1, num_2)
    return random_number

## Cloud

cloud_hp_increase = {8: rnd(323, 334), 9: rnd(351, 372)}
cloud_mp_increase = {8: rnd(30, 40), 9: rnd(40, 50)}
cloud_str_increase = {8: rnd(3, 5), 9: rnd(4, 6)}
cloud_defense_increase = {8: rnd(3, 5), 9: rnd(4, 6)}
cloud_spd_increase = {8: rnd(3, 5), 9: rnd(4, 6)}
cloud_mgatk_increase = {8: rnd(3, 5), 9: rnd(4, 6)}
cloud_mgdef_increase = {8: rnd(3, 5), 9: rnd(4, 6)}
cloud_luck_increase = {8: rnd(3, 5), 9: rnd(4, 6)}
cloud_dex_increase = {8: rnd(3, 5), 9: rnd(4, 6)}

## Tifa

tifa_hp_increase = {8: rnd(332, 353), 9: rnd(354, 372)}
tifa_mp_increase = {8: rnd(30, 40), 9: rnd(40, 50)}
tifa_str_increase = {8: rnd(4, 6), 9: rnd(5, 7)}
tifa_defense_increase = {8: rnd(3, 5), 9: rnd(4, 6)}
tifa_spd_increase = {8: rnd(3, 5), 9: rnd(4, 6)}
tifa_mgatk_increase = {8: rnd(3, 5), 9: rnd(4, 6)}
tifa_mgdef_increase = {8: rnd(3, 5), 9: rnd(4, 6)}
tifa_luck_increase = {8: rnd(3, 5), 9: rnd(4, 6)}
tifa_dex_increase = {8: rnd(3, 5), 9: rnd(4, 6)}

## Barret

barret_hp_increase = {8: rnd(354, 378), 9: rnd(379, 400)}
barret_mp_increase = {8: rnd(50, 70), 9: rnd(50, 70)}
barret_str_increase = {8: rnd(3, 5), 9: rnd(3, 5)}
barret_defense_increase = {8: rnd(3, 5), 9: rnd(4, 6)}
barret_spd_increase = {8: rnd(3, 5), 9: rnd(4, 6)}
barret_mgatk_increase = {8: rnd(3, 5), 9: rnd(4, 6)}
barret_mgdef_increase = {8: rnd(3, 5), 9: rnd(4, 6)}
barret_luck_increase = {8: rnd(3, 5), 9: rnd(4, 6)}
barret_dex_increase = {8: rnd(3, 5), 9: rnd(4, 6)}

### Stat mapping and level handling

stats_map = {(cloud.name, 'Max HP'): cloud_hp_increase, (cloud.name, 'Max MP'): cloud_mp_increase,
             (cloud.name, 'Strength'): cloud_str_increase, (cloud.name, 'Defense'): cloud_defense_increase,
             (cloud.name, 'Magic Attack'): cloud_mgatk_increase, (cloud.name, 'Magic Defense'): cloud_mgdef_increase,
             (cloud.name, 'Luck'): cloud_luck_increase, (cloud.name, 'Dexterity'): cloud_dex_increase,

             (tifa.name, 'Max HP'): tifa_hp_increase, (tifa.name, 'Max MP'): tifa_mp_increase,
             (tifa.name, 'Strength'): tifa_str_increase, (tifa.name, 'Defense'): tifa_defense_increase,
             (tifa.name, 'Magic Attack'): tifa_mgatk_increase, (tifa.name, 'Magic Defense'): tifa_mgdef_increase,
             (tifa.name, 'Luck'): tifa_luck_increase, (tifa.name, 'Dexterity'): tifa_dex_increase,

             (barret.name, 'Max HP'): barret_hp_increase, (barret.name, 'Max MP'): barret_mp_increase,
             (barret.name, 'Strength'): barret_str_increase, (barret.name, 'Defense'): barret_defense_increase,
             (barret.name, 'Magic Attack'): barret_mgatk_increase, (barret.name, 'Magic Defense'): barret_mgdef_increase,
             (barret.name, 'Luck'): barret_luck_increase, (barret.name, 'Dexterity'): barret_dex_increase}

def level_up(character):

    old_hp = character.max_hp
    old_mp = character.max_mp
    old_str_ = character.str_
    old_def = character.defense
    old_mgatk = character.mgatk
    old_mgdef = character.mgdef
    old_luck = character.luck
    old_dex = character.dex

    character.level += 1
    print('******')
    print(character.name + ' leveled up!')
    print(character.name + ' is now level ' + str(character.level) + '.')
    print('******')
    print('')

    character.max_hp = stats_map[character.name, 'Max HP'][character.level]
    character.max_mp = stats_map[character.name, 'Max MP'][character.level]
    character.str_ = stats_map[character.name, 'Strength'][character.level]
    character.defense = stats_map[character.name, 'Defense'][character.level]
    character.mgatk = stats_map[character.name, 'Magic Attack'][character.level]
    character.mgdef = stats_map[character.name, 'Magic Defense'][character.level]
    character.luck = stats_map[character.name, 'Luck'][character.level]
    character.dex = stats_map[character.name, 'Dexterity'][character.level]

    hp_increase = character.max_hp - old_hp
    mp_increase = character.max_mp - old_mp
    str_increase = character.str_ - old_str_
    def_increase = character.defense - old_def
    mgatk_increase = character.mgatk - old_mgatk
    mgdef_increase = character.mgdef - old_mgdef
    luck_increase = character.luck - old_luck
    dex_increase = character.dex - old_dex

    print(f'HP increased by {hp_increase}!')
    print(f'MP increased by {mp_increase}!')
    print(f'Strength increased by {str_increase}!')
    print(f'Defense increased by {def_increase}!')
    print(f'Magic Attack increased by {mgatk_increase}!')
    print(f'Magic Defense increased by {mgdef_increase}!')
    print(f'Luck increased by {luck_increase}!')
    print(f'Dexterity increased by {dex_increase}!')
    cf.space()

    return character.max_hp, character.max_mp, character.str_, character.defense, \
           character.mgatk, character.mgdef, character.luck, character.dex