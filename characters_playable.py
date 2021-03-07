import common_functions as cf
import random

### Character object handling

class char:
    """Creating class for all playable characters."""
    def __init__(self, name, level, level_threshold, in_party: bool, ko: bool, max_hp, current_hp, max_mp, current_mp, str_, defense, spd, mgatk, mgdef, luck, dex, exp=0, atb=0, actions=['Attack', 'Item']):
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
        self.ko = ko

### Initializing characters

cloud = char(name='Cloud', level=7, level_threshold=[], in_party=True, ko=False, max_hp=322, current_hp=322, max_mp=50, current_mp=50, str_=12, defense=10, spd=10, mgatk=10, mgdef=10, luck=11, dex=7)
tifa = char(name='Tifa', level=7, level_threshold=[], in_party=False, ko=False, max_hp=325, current_hp=325, max_mp=50, current_mp=60, str_=13, defense=9, spd=12, mgatk=12, mgdef=12, luck=10, dex=14)
barret = char(name='Barret', level=7, level_threshold=[], in_party=False, ko=False, max_hp=350, current_hp=350, max_mp=30, current_mp=30, str_=10, defense=12, spd=8, mgatk=9, mgdef=10, luck=14, dex=11)

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
    return characters.append(name.name)

add_char(tifa)
add_char(cloud)
add_char(barret)

actions = ['Attack', 'Item']

### Stat diffs

def rnd(num_1, num_2):
    random_number = random.randint(num_1, num_2)
    return random_number

## Cloud

cloud.level_threshold = [10, 50, 150, 275, 500]

cloud_hp_diff = {8: rnd(323, 334), 9: rnd(351, 372), 10: rnd(373, 391), 11: rnd(392, 410), 12: rnd(439, 464), 13: rnd(476, 510)}
cloud_mp_diff = {8: rnd(57, 63), 9: rnd(66, 69), 10: rnd(71, 76), 11: rnd(77, 82), 12: rnd(89, 94), 13: rnd(95, 101)}
cloud_str_diff = {8: rnd(20, 24), 9: rnd(25, 26), 10: rnd(27, 28), 11: rnd(29, 30), 12: rnd(31, 32), 13: rnd(33, 34)}
cloud_defense_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}
cloud_spd_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}
cloud_mgatk_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}
cloud_mgdef_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}
cloud_luck_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}
cloud_dex_diff = {8: rnd(8, 12), 9: rnd(13, 14), 10: rnd(15, 16), 11: rnd(17, 18), 12: rnd(19, 20), 13: rnd(21, 22)}

## Barret

barret.level_threshold = [10, 50, 150, 275, 500]

barret_hp_diff = {8: rnd(354, 378), 9: rnd(379, 400), 10: rnd(401, 422), 11: rnd(423, 444), 12: rnd(484, 511), 13: rnd(551, 578)}
barret_mp_diff = {8: rnd(52, 55), 9: rnd(57, 61), 10: rnd(63, 67), 11: rnd(68, 72), 12: rnd(75, 80), 13: rnd(82, 87)}
barret_str_diff = {8: rnd(19, 22), 9: rnd(23, 25), 10: rnd(26, 27), 11: rnd(28, 29), 12: rnd(30, 31), 13: rnd(32, 33)}
barret_defense_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}
barret_spd_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}
barret_mgatk_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}
barret_mgdef_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}
barret_luck_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}
barret_dex_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}

## Tifa

tifa.level_threshold = [10, 50, 150, 275, 500]

tifa_hp_diff = {8: rnd(332, 353), 9: rnd(354, 372), 10: rnd(373, 391), 11: rnd(392, 410), 12: rnd(430, 455), 13: rnd(468, 496)}
tifa_mp_diff = {8: rnd(55, 58), 9: rnd(60, 64), 10: rnd(66, 70), 11: rnd(72, 76), 12: rnd(79, 84), 13: rnd(86, 91)}
tifa_str_diff = {8: rnd(16, 21), 9: rnd(22, 23), 10: rnd(24, 25), 11: rnd(26, 27), 12: rnd(28, 29), 13: rnd(30, 31)}
tifa_defense_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}
tifa_spd_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}
tifa_mgatk_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}
tifa_mgdef_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}
tifa_luck_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}
tifa_dex_diff = {8: rnd(16, 20), 9: rnd(21, 22), 10: rnd(23, 24), 11: rnd(25, 26), 12: rnd(27, 28), 13: rnd(29, 30)}

### Stat mapping and level handling

stats_map = {(cloud.name, 'Max HP'): cloud_hp_diff, (cloud.name, 'Max MP'): cloud_mp_diff,
             (cloud.name, 'Strength'): cloud_str_diff, (cloud.name, 'Defense'): cloud_defense_diff,
             (cloud.name, 'Magic Attack'): cloud_mgatk_diff, (cloud.name, 'Magic Defense'): cloud_mgdef_diff,
             (cloud.name, 'Luck'): cloud_luck_diff, (cloud.name, 'Dexterity'): cloud_dex_diff,

             (tifa.name, 'Max HP'): tifa_hp_diff, (tifa.name, 'Max MP'): tifa_mp_diff,
             (tifa.name, 'Strength'): tifa_str_diff, (tifa.name, 'Defense'): tifa_defense_diff,
             (tifa.name, 'Magic Attack'): tifa_mgatk_diff, (tifa.name, 'Magic Defense'): tifa_mgdef_diff,
             (tifa.name, 'Luck'): tifa_luck_diff, (tifa.name, 'Dexterity'): tifa_dex_diff,

             (barret.name, 'Max HP'): barret_hp_diff, (barret.name, 'Max MP'): barret_mp_diff,
             (barret.name, 'Strength'): barret_str_diff, (barret.name, 'Defense'): barret_defense_diff,
             (barret.name, 'Magic Attack'): barret_mgatk_diff, (barret.name, 'Magic Defense'): barret_mgdef_diff,
             (barret.name, 'Luck'): barret_luck_diff, (barret.name, 'Dexterity'): barret_dex_diff}

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

    hp_diff = character.max_hp - old_hp
    mp_diff = character.max_mp - old_mp
    str_diff = character.str_ - old_str_
    def_diff = character.defense - old_def
    mgatk_diff = character.mgatk - old_mgatk
    mgdef_diff = character.mgdef - old_mgdef
    luck_diff = character.luck - old_luck
    dex_diff = character.dex - old_dex

    print(f'HP increased by {hp_diff}!')
    print(f'MP increased by {mp_diff}!')
    print(f'Strength increased by {str_diff}!')
    print(f'Defense increased by {def_diff}!')
    print(f'Magic Attack increased by {mgatk_diff}!')
    print(f'Magic Defense increased by {mgdef_diff}!')
    print(f'Luck increased by {luck_diff}!')
    print(f'Dexterity increased by {dex_diff}!')
    cf.space()

    return character.max_hp, character.max_mp, character.str_, character.defense, \
           character.mgatk, character.mgdef, character.luck, character.dex