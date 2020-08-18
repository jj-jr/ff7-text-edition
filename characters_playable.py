import level
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

    def rnd(num_1, num_2):
        random_number = random.randint(num_1, num_2)
        return random_number

    @property
    def strength(self):
        return self.str_

    def defense(self):
        return self.defense

    level_7 = {strength: rnd(4, 5)}
    level_8 = {defense: rnd(5, 6)}

    stats_map = {7: level_7}, {8: level_8}#, 8: level_8, 9: level_9, 10: level_10, 11: level_11}

    @property
    def stats(self):
        return self.stats_map[self.level]



### Initializing characters

cloud = char(name='Cloud', level=7, level_threshold=[], in_party=True, max_hp=700, current_hp=700, max_mp=50, current_mp=50, str_=12, defense=10, spd=10, mgatk=10, mgdef=10, luck=11, dex=10)
tifa = char(name='Tifa', level=7, level_threshold=[], in_party=False, max_hp=650, current_hp=650, max_mp=60, current_mp=60, str_=13, defense=9, spd=12, mgatk=12, mgdef=12, luck=10, dex=14)
barret = char(name='Barret', level=7, level_threshold=[], in_party=False, max_hp=900, current_hp=900, max_mp=30, current_mp=30, str_=10, defense=12, spd=8, mgatk=9, mgdef=10, luck=14, dex=11)

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