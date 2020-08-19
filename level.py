import characters_playable as char
import random

def rnd(num_1, num_2):
    random_number = random.randint(num_1, num_2)
    return random_number

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

cloud_hp_increase = {8: random.randint(30,40), 9: random.randint(45,55)}
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

#def value_increase(level):


def level_up(character):
    print('******')
    print(character.name + ' leveled up!')
    print(character.name + ' is now level ' + str(character.level) + '.')
    print('******')
    print('')
    character.level += 1


    #return character.level

'''def cloud_level_up():
    print('******')
    print(char.cloud.name + ' leveled up!')
    print(char.cloud.name + ' is now level ' + str(char.cloud.level) + '.')
    print('******')
    print('')
    char.cloud.level += 1
    level = char.cloud.level
    char.cloud.max_hp = cloud_stat_up.hp[level]
    char.cloud.max_mp = cloud_stat_up.mp[level]
    char.cloud.str_ = cloud_stat_up.str_[level]
    char.cloud.defense = cloud_stat_up.defense[level]
    char.cloud.spd = cloud_stat_up.spd[level]
    char.cloud.mgatk = cloud_stat_up.mgatk[level]
    char.cloud.mgdef = cloud_stat_up.mgdef[level]
    char.cloud.luck = cloud_stat_up.luck[level]
    char.cloud.dex = cloud_stat_up.dex[level]'''''