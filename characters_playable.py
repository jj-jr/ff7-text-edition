### Character object handling

class char:
    def __init__(self, name, level, in_party: bool, max_hp, current_hp, max_mp, current_mp, str, defense, spd, mgatk, mgdef, luck, dex, exp=0, atb=0):
        self.name = name
        self.level = level
        self.in_party = in_party
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.max_mp = max_mp
        self.current_mp = current_mp
        self.str = str
        self.defense = defense
        self.spd = spd
        self.mgatk = mgatk
        self.mgdef = mgdef
        self.luck = luck
        self.dex = dex
        self.exp = exp
        self.atb = atb

### Initializing characters

cloud = char(name='Cloud', level=7, in_party=True, max_hp=700, current_hp=700, max_mp=50, current_mp=50, str=12, defense=10, spd=10, mgatk=10, mgdef=10, luck=11, dex=10)
tifa = char(name='Tifa', level=7, in_party=False, max_hp=650, current_hp=650, max_mp=60, current_mp=60, str=10, defense=9, spd=12, mgatk=12, mgdef=12, luck=10, dex=14)
barrett = char(name='Barrett', level=7, in_party=False, max_hp=900, current_hp=900, max_mp=30, current_mp=30, str=10, defense=12, spd=8, mgatk=9, mgdef=10, luck=14, dex=11)

### Party management

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

characters = []
current_party = {'Cloud': True}

def add_char (name):
    print('Added ' + name.name + ' to the list of characters.')
    return characters.append(name.name)

add_char(tifa)
add_char(cloud)
add_char(barrett)