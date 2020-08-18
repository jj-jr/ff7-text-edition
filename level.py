import characters_playable as char
import random

### Level handling

char.cloud.level_threshold = [10, 50, 150, 275, 500]
char.tifa.level_threshold = [10, 50, 150, 275, 500]
char.barret.level_threshold = [10, 50, 150, 275, 500]

### Attribute increase lists

class stat_up:
    def __init__(self, hp, mp, str_, defense, spd, mgatk, mgdef, luck, dex):
        self.hp = hp
        self.mp = mp
        self.str_ = str_
        self.defense = defense
        self.spd = spd
        self.mgatk = mgatk
        self.mgdef = mgdef
        self.luck = luck
        self.dex = dex

### Stat increases

## Cloud

cloud_hp_increase = {8: random.randint(30,40), 9: random.randint(40,50)}
cloud_mp_increase = {8: random.randint(30,40), 9: random.randint(40,50)}
cloud_str_increase = {8: random.randint(3,5), 9: random.randint(4,6)}
cloud_defense_increase = {8: random.randint(3,5), 9: random.randint(4,6)}
cloud_spd_increase = {8: random.randint(3,5), 9: random.randint(4,6)}
cloud_mgatk_increase = {8: random.randint(3,5), 9: random.randint(4,6)}
cloud_mgdef_increase = {8: random.randint(3,5), 9: random.randint(4,6)}
cloud_luck_increase = {8: random.randint(3,5), 9: random.randint(4,6)}
cloud_dex_increase = {8: random.randint(3,5), 9: random.randint(4,6)}

## Tifa

tifa_hp_increase = {8: random.randint(25,35), 9: random.randint(35,40)}
tifa_mp_increase = {8: random.randint(30,40), 9: random.randint(40,50)}
tifa_str_increase = {8: random.randint(4,6), 9: random.randint(5,7)}
tifa_defense_increase = {8: random.randint(3,5), 9: random.randint(4,6)}
tifa_spd_increase = {8: random.randint(3,5), 9: random.randint(4,6)}
tifa_mgatk_increase = {8: random.randint(3,5), 9: random.randint(4,6)}
tifa_mgdef_increase = {8: random.randint(3,5), 9: random.randint(4,6)}
tifa_luck_increase = {8: random.randint(3,5), 9: random.randint(4,6)}
tifa_dex_increase = {8: random.randint(3,5), 9: random.randint(4,6)}

## Barret

barret_hp_increase = {8: random.randint(50,70), 9: random.randint(50,70)}
barret_mp_increase = {8: random.randint(50,70), 9: random.randint(50,70)}
barret_str_increase = {8: random.randint(3,5), 9: random.randint(3,5)}
barret_defense_increase = {8: random.randint(3,5), 9: random.randint(4,6)}
barret_spd_increase = {8: random.randint(3,5), 9: random.randint(4,6)}
barret_mgatk_increase = {8: random.randint(3,5), 9: random.randint(4,6)}
barret_mgdef_increase = {8: random.randint(3,5), 9: random.randint(4,6)}
barret_luck_increase = {8: random.randint(3,5), 9: random.randint(4,6)}
barret_dex_increase = {8: random.randint(3,5), 9: random.randint(4,6)}

cloud_stat_up = stat_up(hp=cloud_hp_increase, mp=cloud_mp_increase, str_=cloud_str_increase, defense=cloud_defense_increase, spd=cloud_spd_increase, mgatk=cloud_mgatk_increase, mgdef=cloud_mgdef_increase, luck=cloud_luck_increase, dex=cloud_dex_increase)
tifa_stat_up = stat_up(hp=tifa_hp_increase, mp=tifa_mp_increase, str_=tifa_str_increase, defense=tifa_defense_increase, spd=tifa_spd_increase, mgatk=tifa_mgatk_increase, mgdef=tifa_mgdef_increase, luck=tifa_luck_increase, dex=tifa_dex_increase)
barret_stat_up = stat_up(hp=barret_hp_increase, mp=barret_mp_increase, str_=barret_str_increase, defense=barret_defense_increase, spd=barret_spd_increase, mgatk=barret_mgatk_increase, mgdef=barret_mgdef_increase, luck=barret_luck_increase, dex=barret_dex_increase)

stat_container = {char.cloud.name: cloud_stat_up, char.tifa.name: tifa_stat_up, char.barret.name: barret_stat_up}

def level_up(character):
    print('******')
    print(character.name + ' leveled up!')
    print(character.name + ' is now level ' + str(character.level) + '.')
    print('******')
    print('')
    character.level += 1
    #if character.name in stat_container:
    #    get


    #return character.level