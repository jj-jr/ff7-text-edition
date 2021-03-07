from typing import Type, List
import items

class enemy:
    def __init__(self, name, level, max_hp, current_hp, max_mp, current_mp, str_, defense, spd, mgatk, mgdef, luck, dex, exp, gil, atb, item, drop_rate):
        self.name = name
        self. level = level
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
        self.gil = gil
        self.atb = atb
        self.item = item
        self.drop_rate = drop_rate

### Initializing enemies

shinra_soldier = enemy(name='Shinra Soldier', level=6, max_hp=50, current_hp=50, max_mp=50, current_mp=50, str_=4, defense=4, spd=9, mgatk=3, mgdef=5, luck=1, dex=5, exp=10, gil=100, atb=1, item=items.potion, drop_rate=0.6)
shinra_mech = enemy(name='Shinra Mech', level=7, max_hp=200, current_hp=125, max_mp=50, current_mp=50, str_=6, defense=6, spd=7, mgatk=3, mgdef=5, luck=2, dex=6, exp=18, gil=25, atb=1, item=items.phoenix_down, drop_rate=0.2)
shinra_dog = enemy(name='Shinra Dog', level=5, max_hp=40, current_hp=40, max_mp=50, current_mp=50, str_=4, defense=4, spd=9, mgatk=3, mgdef=5, luck=1, dex=5, exp=10, gil=100, atb=1, item=items.potion, drop_rate=0.6)

current_enemies = []

#def add_enemy(name):
    #print('Added ' + name.name + ' to the list of enemies.')
    #return enemies[name] = name.name