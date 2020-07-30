from typing import Type, List

print('')
print('Initializing all assets.')
print('')

### Object handling

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


class enemy:
    def __init__(self, name, level, max_hp, current_hp, max_mp, current_mp, str, defense, spd, mgatk, mgdef, luck, dex, exp, atb, item, drop_rate):
        self.name = name
        self. level = level
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

    def potion(self, actor, target):

        hp_remainder = target.max_hp - target.current_hp

        # Adding the full 100 HP to a target who is missing 100 or more HP.
        if target.current_hp <= target.max_hp - 100 and target.current_hp != target.max_hp and target.current_hp != 0:
            target.current_hp += 100
            if actor.name != target.name:
                print(actor.name + ' used a Potion on ' + target.name + ' and restored 100 HP! ' + target.name + ' currently has ' + str(target.current_hp) + ' HP.')
                return target.current_hp
            else:
                print(target.name + ' used a Potion and restored 100 HP! They currently have ' + str(target.current_hp) + ' HP.')
                return target.current_hp
        # Adding the potion amount to characters missing less than 100 HP or less.
        elif target.current_hp > target.max_hp - 100 and target.current_hp != target.max_hp and target.current_hp != 0:
            target.current_hp += hp_remainder
            if actor.name != target.name:
                print(actor.name + ' used a Potion on ' + target.name + ' and restored ' + str(hp_remainder) + ' HP! ' + target.name + ' currently has ' + str(target.current_hp) + ' HP.')
                return target.current_hp
            else:
                print(target.name + ' used a Potion and restored ' + str(hp_remainder) + ' HP! They currently have ' + str(target.current_hp) + ' HP.')
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

    def hi_potion(self, actor, target):

        hp_remainder = target.max_hp - target.current_hp

        # Adding the full 500 HP to a target who is missing 500 or more HP.
        if target.current_hp <= target.max_hp - 500 and target.current_hp != target.max_hp and target.current_hp != 0:
            target.current_hp += 500
            if actor.name != target.name:
                print(actor.name + ' used a Hi-Potion on ' + target.name + ' and restored 500 HP! ' + target.name + ' currently has ' + str(target.current_hp) + ' HP.')
                return target.current_hp
            else:
                print(target.name + ' used a Hi-Potion and restored 500 HP! They currently have ' + str(target.current_hp) + ' HP.')
                return target.current_hp
        # Adding the hi-potion amount to characters missing less than 500 HP or less.
        elif target.current_hp > target.max_hp - 500 and target.current_hp != target.max_hp and target.current_hp != 0:
            target.current_hp += hp_remainder
            if actor.name != target.name:
                print(actor.name + ' used a Hi-Potion on ' + target.name + ' and restored ' + str(hp_remainder) + ' HP! ' + target.name + ' currently has ' + str(target.current_hp) + ' HP.')
                return target.current_hp
            else:
                print(target.name + ' used a Hi-Potion and restored ' + str(hp_remainder) + ' HP! They currently have ' + str(target.current_hp) + ' HP.')
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

    def ether(self, actor, target):

        mp_remainder = target.max_mp - target.current_mp

        # Adding the full 100 HP to a target who is missing 100 or more HP.
        if target.current_mp <= target.max_mp - 40 and target.current_mp != target.max_mp and target.current_hp != 0:
            target.current_mp += 40
            if actor.name != target.name:
                print(actor.name + ' used an Ether on ' + target.name + ' and restored 40 MP! ' + target.name + ' currently has ' + str(target.current_mp) + ' MP.')
                return target.current_mp
            else:
                print(target.name + ' used an Ether and restored 40 MP! They currently have ' + str(target.current_mp) + ' MP.')
                return target.current_mp
        # Adding the potion amount to characters missing less than 100 HP or less.
        elif target.current_mp > target.max_mp - 100 and target.current_mp != target.max_mp and target.current_hp != 0:
            target.current_mp += mp_remainder
            if actor.name != target.name:
                print(actor.name + ' used an Ether on ' + target.name + ' and restored ' + str(mp_remainder) + ' MP! ' + target.name + ' currently has ' + str(target.current_mp) + ' MP.')
                return target.current_mp
            else:
                print(target.name + ' used an Ether and restored ' + str(mp_remainder) + ' MP! They currently have ' + str(target.current_mp) + ' MP.')
                return target.current_mp
        # Character is already at Max MP
        elif target.current_mp == target.max_mp:
            target.current_mp = target.max_mp
            print(target.name + ' is already at max MP. ' + target.name + ' has ' + str(target.max_mp) + ' MP.')
            return target.current_mp
        # Item can't be used on fallen party members
        elif target.current_hp == 0:
            print('Item cannot be used on a character with 0 HP.')
        else:
            print('Error.')

    def turbo_ether(self, actor, target):

        if target.current_mp < target.max_mp and target.current_hp != 0:
            target.current_mp = target.max_mp
            if actor.name != target.name:
                print(actor.name + ' used a Turbo Ether on ' + target.name + ' and fully restored their MP! ' + target.name + ' currently has ' + str(target.current_mp) + ' MP.')
                return target.current_mp
            else:
                print(target.name + ' used a Turbo Ether and fully restored their MP! ' + target.name + ' currently has ' + str(target.current_mp) + ' MP.')
                return target.current_mp
        # Character is already at Max MP
        elif target.current_mp == target.max_mp:
            target.current_mp = target.max_mp
            print(target.name + ' is already at max MP. ' + target.name + ' has ' + str(target.max_mp) + ' MP.')
            return target.current_mp
        # Item can't be used on fallen party members
        elif target.current_hp == 0:
            print('Item cannot be used on a character with 0 HP.')
        else:
            print('Error.')

    def phoenix_down(self, actor, target):

        if target.current_hp == 0:
            target.current_hp = 100
            print(actor.name + ' used a Phoenix Down on ' + target.name + '! ' + target.name + ' has been revived and currently has ' + str(target.current_hp) + ' HP.')
            return target.current_hp
        else:
            print('Phoenix Down cannot be used on a target that is alive.')

    def molotov_cocktail(self, actor, target):

        hp_remainder = target.current_hp - 100

        # Reducing the full 100 HP of a target who has more than 100 HP.
        if target.current_hp > 100 and target.current_hp != 0:
            target.current_hp -= 100
            print(actor.name + ' used a Molotov Cocktail on ' + target.name + ' and dealt 100 damage! ' + target.name + ' currently has ' + str(target.current_hp) + ' HP.')
            return target.current_hp
        # Dealing 100 damage to a target with less than 100 HP, knocking them down.
        elif target.current_hp <= 100 and target.current_hp != 0:
            target.current_hp = 0
            print(actor.name + ' used a Molotov Cocktail on ' + target.name + ' and dealt ' + str(abs(hp_remainder)) + ' damage! ' + target.name + ' has fallen.')
            return target.current_hp
        # Item can't be used on fallen party members
        else:# target.current_hp == 0:
            print('Item cannot be used on a character with 0 HP.')
        #else:
        #    print('Error.')




### Initializing characters

cloud = char(name='Cloud', level=7, in_party=True, max_hp=700, current_hp=700, max_mp=50, current_mp=50, str=12, defense=10, spd=10, mgatk=10, mgdef=10, luck=11, dex=10)
tifa = char(name='Tifa', level=7, in_party=False, max_hp=650, current_hp=650, max_mp=60, current_mp=60, str=10, defense=9, spd=12, mgatk=12, mgdef=12, luck=10, dex=14)
barrett = char(name='Barrett', level=7, in_party=False, max_hp=900, current_hp=900, max_mp=30, current_mp=30, str=10, defense=12, spd=8, mgatk=9, mgdef=10, luck=14, dex=11)

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
        #item.quantity += quantity
        print('Added ' + str(quantity) + ' ' + item + 's to your inventory.')
        return item_inventory
    elif item in item_inventory and quantity > 0:
        item_inventory[item] += quantity
        #item.quantity += quantity
        print('Added ' + str(quantity) + ' ' + item + ' to your inventory.')
        return item_inventory
    elif item in item_inventory and quantity < 0:
        item_inventory[item] += quantity
        #item.quantity += quantity
        print('Removed ' + str(abs(quantity)) + ' ' + item + 's from your inventory.')
        return item_inventory
    else:
        print('Error')

### Creating item objects

potion = item('Potion', 'Restore 100 HP.')
phoenix_down = item('Phoenix Down', 'Revives a downed party member and restores 100 HP.')
ether = item('Ether', 'Restores 40 MP.')
hipotion = item('Hi-Potion', 'Restores 500 HP.')
molotov_cocktail = item('Molotov Cocktail', 'Deal 100 damage to an enemy.')

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

shinra_soldier = enemy(name='Shinra Soldier', level=6, max_hp=300, current_hp=300, max_mp=50, current_mp=50, str=4, defense=4, spd=9, mgatk=3, mgdef=5, luck=1, dex=5, exp=10, atb=1, item=ether, drop_rate=0.3)
shinra_mech = enemy(name='Shinra Mech', level=7, max_hp=400, current_hp=400, max_mp=50, current_mp=50, str=5, defense=6, spd=7, mgatk=3, mgdef=5, luck=2, dex=6, exp=18, atb=1, item=phoenix_down, drop_rate=0.2)

#def add_enemy(name):
    #print('Added ' + name.name + ' to the list of enemies.')
    #return enemies[name] = name.name

enemies = {shinra_mech}
current_enemy = [shinra_mech]

### Initializing items for areas

midgar_items = [potion.name, ether.name, hipotion.name]
shinra_reactor_items = [phoenix_down.name, potion.name, molotov_cocktail.name]

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

battle(cloud, shinra_mech)
print('')
cloud.current_hp = 422
item.hi_potion((), barrett, cloud)
cloud.current_mp = 22
item.turbo_ether((), cloud, cloud)
item.phoenix_down((), barrett, cloud)
cloud.current_hp = 0
item.phoenix_down((), barrett, cloud)
cloud.current_hp = 72
item.molotov_cocktail((), shinra_soldier, cloud)

def tifa_ascii ():
    print('2222222z222zzzzzssssssssssszzzzzzzzzzzzzsszzsszzzsssssssszzzzzzsszzszssssssszsszszzzzzzssssssz22z2zszzzzz2zssssssssssssszzzzzzzzzzzzzzzzzzzz2zzzzzzzzz')
    print('222222zz2z2zz22zzzssssssxsszzzzzzzzzzzzszszzzsssssszssssszzzzzsssszzzsssssszzzszssr. .rxsz2GG2zssssssssssssssssszzzzzzzzszzzzzz22zzzzzzzzzz')

    print('22222222222zz2zzzzzzssssssszzszzzzzzzzzszszzsszssssszszzzzzzsssszzzzzsssszzzsx, .s2ZBBBBBBBBBBBGr,.. ,ssssssssssssszzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')

    print('22z222z2222z2zsssz2zssssssssssszzssssszssssssssssssssssssszzzsssszzzzssszzx. .zBBBBBBBBBBBBBBBBBBBBBBBBWx .xszzzsszzzzzzzzzzzzzzzzzz222222zzzzzzzzzzzz')

    print('zzzz22zz2222zzsszz2zzzssssszssz2zssssszzzssssssssssszzsssszzzssssszzz2zs,. sBBBBBWWWWWWWWWWWBBWWBBBBBBBBBBs rsssssssssszzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')

    print('zzzzzzz22222z2zzzzzzsssssssszzzzzzzzssszzzzzzzssssssssszzzzszsssss2Gzsx,rGBBBBZzGBWWWBBBBZZZZWWBBBBBBBBBBBBBB. rssssssssssssssszzzzzzzzzzzzzzzzzzzzzzz')

    print('zzzzzzzz222zz2zzssz2zzzssssss22zzzzsszzzsssszzzsssssssszzzzzssszzzsxx..x2x2Bx,GBWZWBBBBBBWBBBBBBBBBBBBBBBBWWBBG ,ssssssssssssszzszzzzszzzzzz2zzzzzzzzz')

    print('zzzzzzzz2222z2zzzzz2z2zssxxszzzzzzzsszzsszzsszzssssssssszzszzzzzxr .. ,W2 2WBWBBBBBBWBBBBBWBBBBBBBZWWWBBWWWBBG.,sssssssszzszzzzzsszzzzzzzzzzzzzzzzzz')

    print('zzzzzzzzz22222zzssz2222zzxxxszzszzzsszzzssssszzzzsssssszzzzzzs,. sr. ,GW xZBWBBBWBBBWWBBBWWBBBZBBBBBBBBBBBBBBBz.,ssssssszzzzzssssszzzzzzzzzzzzzzzzzz')

    print('zzzzzzzszz2222zzzszz2z222ssssssszz22zzzzzszzzzzzzssssssszzzx. .xZWGszBBx xBBWBBWBBBBWZBBBBBWBB sBBZWBWGBBBBBB2.rssssszzzzzzssssszzzzz2zzzzzzzzzzzz')

    print('zzzzzsszsz222z222zzz22222z2zszsszzz2zsz2zzzzzzzz22zzzszzzx. rZBBWBBBBB zWZZWWzGZ2GxsBB2BBrZB 2BWZBWxWBZBBBs.s2zzzzzzzzszsssszzzzzzz22zzzzzzzzz')

    print('zzzzzzssss2GG2222zzz22222z2zszszzsz2zszzzszzzzzzzzzzzz2s..sBBBBBBBBB. xGr2rr2. z.s BB.zW 2B 2WWBBB ZszzBs2,szzzzszzzzsxszzzzzzzzz22zzzzszzzz')

    print('zzzzzzszzsszGG222zzz2G22Gsz2zzsszzzz222zzszzzzzzzz22zs. sBBBBBBBBBB 2Bz s ss z.zx B2, z r2 BWZBBz x ..Zxrzzzzz2zzzssszzzzzzzzz22zzzzzz222')

    print('szzzzzzzzzsszGG2222z2GGGZGz222zzz2zzz2G2zzzz22zzz2G2. 2BBBBWBBWWBB ,WB. .s zBWGZGBWB.rrx B. ,WZZBBrr, x B ssszzzzszzzz2z22zz2zzGzzz2222222')

    print('zzsszzzzzsszszz222G2GG222Z22222222zzzGG2zzzz22222z, zBBBWWBWWWBBB zBBG.2WBGBBxB,BBB .B2 ,zB .. .ZBWZBGBxWW, B,rszzzzzzzzzz2z2zzzzzz22222222222')

    print('ssssszzzzzzzss2222G2GGG2z222zG222zz22GGG2zz222G2x rBBBBWWBWWWBWWrWBBBsBBBZBB.B ZBB. zB ,Br WBWBZsBBBB BB xz22zzzzzzz22zz2zzzzzzzzz2222z2')

    print('ssszzzszszzszzz22222GGG22GG2z2z222z222GG2zzGZGz,.2BBBWWWBWWWWBB2ZBBBWWBBBrBG2Z BBz Bx . B ,s2GG2sr BBWBxBWWBzWB,,zzzzzzz22z2zz222zzzzzzzz222222')

    print('ssszzzzzzszzzzzGGzz22GGG2GG22222G222222GGG2ZGr.rWBWZZWBWWBBBWW22BBWWZBBBrsB Z BB . B ..BzZGx. rxsxxr BBB2BBWBZGBB z22zzz22222z22zzz222z222222222')

    print('sssssssssssszzz2G22zz2222GG2GG22GG22GGGG2ZWG..2BBZWBBBBWWBWWWBxBBWWWBBBBrBBsBGsBz ,.2 .,, xss, 2BBBBBBBZZBB r22z222zz2z222222222z222222222')

    print('sssssssssssszzz2Gzz2z22222GGGG2GGGGG22GGGZs ,BBWWBBBBBWBWBZWBZGBWWBWB2B2 2 Bs ... .... GBBBBBBBBZ WB ZBBBGGWB2 z2z222222222222222222222G2222')

    print('sssssssssssszszzG2zzzzz22222GG2222GGGGGZGr.rBBZWBBBBBWBBWzBBBzBWWWWBBxWs BBBBBxs......... BBrs szGx BBB B .. BBBZWWBB z2222222222zz2222222222222222')

    print('xssssssssszsss2zG22zzzz222z2GGGG2GG222Gsr xBWBBBWBBWBBBGGBBWZZBWBBBWBZ,GBz.xss2B .,...... s sBBBBBBsBGB22 sBx, GBBBBBBB s222z2z2222zGGGG22222222G2222')

    print('xxxxsssssssssszsGG2z2zz22zzz22222GGGZzx. sBZBBBGBWWBBBsZBWWWWBBBWWWZZBsx2 zBBB,B ....,... B WW2.B Bsxs BBBWBBBB,r2222222222G2222222222222GG22')

    print('xxxxxxsssssssssss222zzzzzzzzz2222GGGs, WBZGWsxBWWBBGzWBWWWWWBWBWBZWWWB, B.B2B, ......... sBBWWBBGs, BGxx BBBBWBBBB,r222222222222z2222zz222GG2222')

    print('xxxxxxxssssssszsssz2zzzzz2zz2222GZ2, ,zBWBs2 xBBBBBsGBBWWWWZWBWWWBWZBWWWr ,2BGBB r. .. Z2. sBBBBBWBBBB x22222222zz2222zzzz2222222222')

    print('rxxxxxxssssssssssssszzzzz2z2z2z2Gs BBBGz . sBBBBWxWBWWWWWWGWBWWWBWZWWBBB ,... r,s .,rrxx,. ,.r. r BBBBBBZZBBBB s222222222zzzz2z2222222222222')

    print('rrrxxxxxsssssssssssssszzzz2zz222r sBBBr sBBBBZzBBWWWWWZBsZBBBBBZZBWBBB2 .rr,,.xsB ..,r,,.,.,s. x. B2WBBWBBBBxBBBBB zG222222222zzzzz2zzz222222222')

    print('rrrxxxxxxssssssssssssssz22222Gz. BBBZ .,WrWZBBZxGBWWWBWWWWB,BBBBWBzZBWBBBBr ... sx .x. r, xBrBBBGBBB2,BWBB2 2222222222222zzz2zzzz22222222')

    print(',,rrxxxxxsssssssssssssszzz22Gs ,BBBsrZBBBB2G,,.WBWZWBWWWWWB BBBBWBrsBWBBBBB ..,.. ..... ., ,B BBBZz2Bsx2ZGBZ,r222222222222222z22z222222222z')

    print(',,,rxxxxxssssssssssssssz2222r zBBrxGBBBBBs2xs,BBZZWBWZWWWWB BBBWBBx.BBBBBBBB .....xs. ....,,,. B xBZZz 2B Gx,WxZ zG222222222222222222222222222z')

    print('xrrrrxxxxssssssssssssszz22z..ZBB rBBBBBB2sZ2,BBZZWBWWBBWWWB.BBBWBBW BWBWWWBBBBr .. ,...... r. B BWZZGss zZx,,.2,222zz22z22222222222222222222zz')

    print('ssxsxxxxxssssssssssssszzGz.rBBB rBBBWWWBWBGxBWZWBBZWBBWWBGzrZBBWBBBrBBWWWWWBBBBBBr ..... .xx ,BBBWB2BGxGWGz. xrs2zzzz22z222222222222z222222zzz')

    print('zsxxxxxrxxxxsssssssssz2Gz sBBB sBBBWBBBBBzsBWZWBBZZWWWBBrWBG,BWZBBWGzBWWWBBWZWBBBBBBr .22r BBWZBZ2BsBZBB2xxrxzzzzzzzzzzzz222222zzz222222zzzz')

    print('G22sxssxxxxxxsssssszzzGs GBB2 sBBWWWBBBBGzBZWWBBWBWBWB2sBBWB zBZBBZBzBBBBBBBBBBzr.rzBBBzxxs22s. BZzzWWBBBZBBZBG.rz2szzzzzzzzzzzz2zzz222222z2222z2')

    print('22zsssxxsxxxssssssszzzs ZBBs rBBBBBBBBBW2WZWBBBZWWBBWsZBWZWB 2GBBZZZWBBWZzr..r2WBBBBBB.rxrr,. BWWGzzBBWGBWBBz.szzssszzzzzzzzzzzzzzzz2zz222zzzz2')

    print('z2zssssxxxxxxxssssszzs zBBs ,BBBWBBBBBWWWZBBBWZWWBBGzBBWZZZB,, sGBBWBZsrrxzGWBBBBBBBBBB ,rr,. ,BBWG2ssBZBBBBW,rzssssszzszzzzzzzzzzzz22z222zzzzzz')

    print('zzsssssssxxxxxxxssszx sBBr. ZB2BBBBBWBWWWBWBZZWBBBzGBBZZZZZBzz .rBBGWB2ZBBBBBBBBBBBWZZ2 .. . BB2Zzz2sBBBBBs.sssssssssssszszzz2zzzzzz222zz2zzzz')

    print('zzzz2zssssxxxxxxxssx.xBB,,rxWrBBBBBZWBWBBsBGWZBBWGBBBWZWWBWBB.B,.GWBZBBBBBBBGx r, ,BGWrGG,BBBBx ssssssssssssszzzzzzzzzzzzzzzzz2zzzz')

    print('xxssszsszzszsssxxsx.sBBr,xrz,WBBWWZBBWBB,WZZWBBGGBBBWWWG22ZWB.BWZ zBBWBBs ... ,, GBWZG,Z2rZBW, xssssssssssssszzzzsszzzzz2zzzzz2zzz2')

    print('xxxsssssssszzssssx,rsBx.xrx.2BBBBGWBBBZ.,GZGBB2ZBBBWWB2sWGGZWW BBx,2B.BB, . xr... ..BBWZGr2ZszBBr .rxsssssssssszzzzzzzzzzzz2zz222zz')

    print('sxxxxxszzsxszszzs,s BW x.sx,BBWBZWBBBZZ zBWBB22Z2WWWZ2ss2WWGWBxWBBs,B rBGz ,x.. rBBZZZ22ZzzsBr,rBBBs ,.,xsssssszzszzzzzzzzz2z22zzz2')

    print('ssxxxxxsz22sssss.z WB r,r2xrBBZWZWWBBB,xBBBBs.rz2BBB2GBBBBBBBB2sBBZZBz zBrs,r. ,xrr,.,.. xBBZZZGzZGrZzzxsx,,GWss,GWsrrsszsssssszzzzzszzzzzzzzzz')

    print('2zsxxxxxszzzszsrrrrB .x sB,GBxB2WWBBBr,BBBBr ,zrsBB22WBBBx.. sBBBZBB BB x.sxrr,, .,rr,, ZBWZZZGz2WssGZGZGzr,. . xWB,sxssssssssszszzzzzzzzzzzz')

    print('2z2zssxxsz2zGGx.s,Bs r xBB WrWZBWBBBGrBBBBr xr 2BB2zBB2. . BBBZBBZ BB x ..,rssssssxrr. GBZZZZZGzZG.GBsBBBBGszz. ,rsssssssssszzz22zzzzzzz')

    print('z222222zs222GG,szBB xr BBxrsxB2WWWBBsBBBBr BZ.BBB.ZWr BBZZBBs rBz G,,r.. .. WBZGG2zGZsZs WB..rzGzsWBBW2x,.rZBz sssssssszzzzzzzzzzz2zz')

    print('zGGG22zzzzz2Gs.zBB rx GBZzs BxBWBWBWWBWBs BBzBBBBZ. .. sBBZWBB GBr Gz2xx. .,s2zx BBWBWZ2rZZz.zs2Br,rrr,. ,ZWx,2BBBGBr.xsssssszzzzzzzzzzz2z2')

    print('zGGGGG22222Gz GBB.rzr BBrBB BGBWBBBWrzBs BBBBBBBz . WBBGBBB ,BB W WBW2BWBBBZZW..ZsBBBs xr sBBZ2222Z2.rzzsszzzzzzzzz22z222')

    print('sszGGG2zzzGGr,BB2 22 sBZ2B22zBZWBBB z2G,BBBBWBB, ...xss. BBWzBB2 G2 B . ZB2WsBZZZWBWZZ.2sWWBBBW .BBZ2GGGGG2sZs.xzzzzzzzzzzzz22222')

    print('sszGGGG22z22 WBB sGz BBxBB,WsBZWBB ZrBBBWWBB. . .. BBBsBB, 2r B .. ZWGzB2WGZZWWBBBZGBBBBWWBBBz2BBGZZG2GZGZ2sx2r,s2zzzzzzzzzzzzz2')

    print('sxszzGG222Gx.BBs.2Gx,BW2BBrzBWWBB.2BZ2WBBWWBBr . . ..... .BBG.2G ,Z Gx . zWZsZWxBZWZGZZWBBGs s2BZBBBBszGxs2GGGGZZZzsz2.szzzzzzzzzz2zzz')

    print('ssxxrx22GGG ZBB sz2 ZBGBBBxrBZBBs2BBBZBBWWBBW .. . ........ r BB2,,, BG W . sZWZ2zZBZGZGxZGGBGxz rZW2zr.rsBBGGWZGGGGZZZW2xGW.szzszszzzzsszz')

    print('ssssxxxrzG2 BB,,G2z BBGBBB.zBWBWxBBBxBBWZBWBr ... .......... xBZzB2 B 2 .WZZ2zBZ BBZ2xZZWBBWr.BBB, rBBB .WBBZWGzGZWWZzzzB.szzssszzzzzzzz')

    print('ssssssszGGs BB z22s BBWBB2 BBWB2BBBsWBBWWBWBr ...... ..... ... xZxBB BZ r ZWZZBWWs,BWBWs,WBGBBBBzB, .BBB sBWWWGr .xZB ssssszzzzzzzzz')

    print('sszzssszG2x Bx.zzzs BWBBB, BWBWWBBWZBBWWBBWBz .............,xsx,..,. . 2sGB xB BWWBGGZZZZGZBBWB2 .rGBBx 2BBx rBBBx.sBBZZZWZ22Z22 ssssszzzzz22zz')

    print('zzzzzz2z2z.sB rsszr,B2B2sssBZBZBBBGBWWBBBB2ZB ............ x2s x BBB B 2BZW2GZ2GGGZGz2BBW,, sWB2 WBBB rBBs WBsGBWWWWZ22Wrrzsszzzzzz2zz2z')

    print('sszzzzzs22.GB sssz,xB2Zz BZBZBBBB2BWWWWBBZxZBz ............... .xG sBB B BWBG2G2szz22zzZZZB.,WBGGBG ,x.ZBZ, .B2ZBW2WrBr,sssszzzzzzzzzz')

    print('ssszzzzzzz Bz,zsxs.sB.sGrBWWWBBWWZBZBBBBZzGBBBW ...... ..,.rs BB z BWWZGGG2xxZ2sGWZZBBBGzGZGBBG . BBW BxWGzsG2zB2.ssssszzszzzzzz')

    print('szsssssszz B.xzsss.sB WZZBWWBWBBZBWWBBBZGzWWWBBBr ...rxssxxssxs,sx . BZ r . BWWZZG22GZzsGZGZZWsZZZZZG2GBBBBBBZzx.,BzGWBWGBszW2 sssssszszzzzzz')

    print('xszzsssszs B.szzzs.zB BWBBBZBWWBWWWWBBGWzZBBWWWBBB2..,....,xsssr,rrsszx. B ....... BGGZZZWW2rsZWWWWZWZZZG2WG2Gz2ZZGZZWBBBWZZBZ 2GZBBW rssssssszzzzzz')

    print('xxszsssszs B.szz2z.ZB BBBWWZWWWBWWBWBGZG2BBBZZWWWBBB rxxssr,.. ,,,,,.,xzr s ......, 2ZzZZWzGBWWGGG2WGGGBGZsGZz2ZGz2WWZZZZGZBGxZsGZx2zBB.,xsssszzzzzzz')

    print('ssssssssss.W.szszz ZB BBBWWZWWWZWWBWBZZGWBWGZZWWWWBB ..,.,,,,,,.,,rr...rG2, ...,,, sW2ZWZ2,2WZWWWGz2,ZBGWWxZW2r2Zzx2WWWWZZZWBBBBWZz G2Z.xr,.,x xxzz')

    print('ssxxssssss,Z,xssss BB BBBWBWBWWWWBBBZZ2GWBZGWWWWZWWB,.,,,,,...,rr,.,,xxxr .sGsxxr,,,.rBZZWWBZ2WZzGZWBZ.GBWGBBZZBWrr22,.xWBWWWZZZZWBBBWZ2,G rxszzZ xrxz')

    print('ssxxrxssssrsxrssss BW2BBBWWWBWWWWBBZWzZWBWGZBZZWWWWBz ,,,,rrrrrr,,,,.. .. .,rxszzzs BB2WWZZZsBZs2GZBBsZBZGBBBZWBGrxWZs..sGWZZZZZZZBBBWZZGG2GZBB..xsz')

    print('sssxrrssssx,Zrsxsx BWBBBBZZWBWZWWBBWZW2WBGZGBZWBBBBBW .,...rrr,. ... BZZ2ZZWZzzBzxrz2ZWGWBG2WBBBWWBz rZBB2szZWWZBBrWZzGGGZWBBGzzsrx22')

    print('ssssxxxxxss,zrxsxx BBWBBBWZWBWZWWBBBZWsBZZWZZWWZZ2zWB.szz22zzzzzssx, .rxxxx. WBBBzGGGZGGGBWzszzWBZBBGz2WBBBBWWs.rGWBGZGzrsW2GW2GZWWs .2,.sz')

    print('ssssssrrxssxrr,rr, BBBBWBWGBBWZBBBG2ZGzBsBBBZZ2WBZBBBx ...... ....rxz2GGGzsr, 2Br 2Gs2GGWZZGWBZZ2xZZWWBWsxZWWBBBBBBWZZ BZzrzZBGBZWZx.zZWGZWB, xx')

    print('sssssssx,xssx,r,,, BBBBWWBzWBBBBGsGZB2ZG2B.ZZBZzWs,WBZ..,,,,,,,,.... .,xz22s,,BZBBBGZrrGGZWZxZWBBZs2ZWZBWWBBBZGzsss2GB sWBW,xWBGBWZWZG2GZWWBB xx')

    print('sxxxxxxxsx,xsxxrr, WBZBBBBzBBB2rzGWZBx2GBB xWWZBBxsBBW2 ,,,,,,,,,,....... zBBzBzs ZZr,GGZZZzGZZBWrWW2GrWBs GWWWZGWZW2 BzsZZsZ WG2ZWBBBBZsrsrsz')

    print('ssssxxxxxrrxszssss 2B2BBBBBWzxxsZG2BzxBBBBBBWGzZBrZBWZB..,,r,,,............. 2B 2Zx.BsGWz.GGZZGWZZZZWBBBWB2zZZsGWZZWBBWWB.BBBGzsZBBBBBBs .rssz22')

    print('sssssssxxxrrsxxsss,rB2WBWzsz2szzssZB,BBBBBBBBWWWBx2W2ZGZ ,rr,,r,,............ rB, Gr 2BxzZZWWGWWZZWW GBWWBWBBBBZZGGGGGB2 GWBz ZBBsxsrs,xzzzzzszz')

    print('sssssssssx,.xsxxxsx BBZsrGBBZGssZBBzGBWZGx2G2ZBBx.2BWZ2zz rrrrr,,,........... BZ . BBxBBBZGGZZBW2ZZWBBGxzBBBsBZ sBWZZzZGGW sG2sZZx BW xsrssssssss')

    print('ssssssssxsx,,xszzzs.s rBBBW2szBBB2BZB2sG,,ZzBBz ,x, xBBBB ,rrrrr,,........... xB GBrsBZGWZWGzGBB2WBZZBBsBW ,ZZ222szzzG2GBBBBBZBz2,.BB xxssssssss')

    print('xxxxssssxssssxxssssx, sBWGzGZBBWZsBBzsZz.szzx.,xsssx BZBZs.rrrrrr,........... BZ 2B ..xWsGZBWGssBWGBGZZBsGx,x. WBBBBBBBBBBBZ2zxB,2x.Gs ,rsssssxsss')

    print('xxxxxsxsssssssxsssxsrxxWzWBBBZZs2zB2GBB2sGsr ,xsssx, BWWBZ ,rrrrr,,..,....... rBB xZBBWW,r.2G2GGWGGsrWWZ,WZBBGrszxrWW GBBBBBBBWZWBBBB WG W,sssssssss')

    print('ssxxxxxxssssssrrs2sr, WBBBBBBZZZZWBWBBBZBB,.rrrsxrr, BBBBGs.rrrr,r,,,,..... xss,zB2GZWBBBGGGZBBBG222BBrZzWr.,xs.2Zs GBBBBBBBBBBBWZWBB2r B,ssssssssz')

    print('sssssssxxxxsssxxxssxr zBZW,G2BGBBBBBWWBBB..sx,,xrxr. BBBBxB.,rxx,,rr,,,.. .GBz.srxBWZZzszsGBWWWWBWzWssrBGW ssssrxBxr WZz2zWZZZZ22GZZs2B.s,xzsxxxsssz')

    print('ssszsssxx,.,xxxxxxsssx BB2xrxWWBBBBBBWBBx.szzzsxxsr BBBBr 2 ,xs.,, ,GBBWGWr.s,,...,r2WWZWBZWWBWBrBBxzB sssss,Z,x GrB2sxr,rxsz2BZxZB.xssxsssszzz')

    print('ssssxxxsssx,rxxsssssssr ZBBWZBBZBBBBZZBZ rxxrrxsxss 2BBBBBrZWz2rsr ,sZBBZGGZGBBWGszssGZBWWBB2sWBBWWB GZWB2 rxxssxss.GBZ,BZZZZWBWGGGWB2.,rssssszzzzzz')

    print('rxxxxxr.,xsxr,rxsssssssx BBBBBBZBWBBsBB..r,r,,rxssr BBBBBBWsZZB.BBBBBBBWG22GGZZGz2Gz2ZBBWWWW2,xBWrGWBB.Wx22B. rsssssr.Wszz2rZBBBBBZGZGZB..ssszzzzzsszz')

    print('rrxxxssszzsszsx,,,rxssss 2GWBBBZBsWBWBB rxr,rrxsss WBBWWBBBBsGxsZ2zs2GGGGZZG2222z22BBWZZWZG2zsG ZBWB ZBB2rG B,.xss, BB,BBBBBBWWZGGZWWBBr,szzzzzzszzzz')

    print('xrrxssxxxssssssx,....,x..BGzWBBWZs2Gss ,ssssssssx. BBBWWZBBB2Z.B2W2x,.,rzz2GGWBBBBWZZZZZZZZZZGsZBWZZB BBW2BWxWWG .x.BBz BBBBWBWZZZG2s,2 szzzzzzzz222z')

    print('sx,xsssssssssssszx.... WGWWszWBBBBBBr rxsssssxrr 2BWWWWWWWBBZ.BzGZ2sWZZZGG22sxsGBBBWWWWWWWWZWWWZZZGWZxGZZB WGGGBz Bz.s BBBBBWWZZZGG2sZ.z2zzzz2zzzszz')

    print('sssssssssxxxxxssssz2sr WBGGZWZss2z2ZG sr .... BBBBBWWWWBBGrB22zzsGWGWGGGGGG2zsxzBBWWWWWZZWWZGGZZWWBz zB BGG22Z2 , rx BBBBBBBWZGG22zG,xsssssssszzzz')

    print('ssssssssssxrr,rxr. .r2WZGGZ22xrzB rsszsxr,,rr rBBWBBWWWWGWBZWZWZz...rzGGGGGZWG22r BWZZWWWZGGZZWBWWZZWBsxZZG222zGZ ,r xBBWBBBWZZGGG2Grrssxsssssssss')

    print('sssssssssssssr ,2BBBBBGz2ZZGs. 2Br,sxxsszzsssz ZBBBWBWWZZGzZBWGzGBBBBWG22222GG2222sBWWZGGGZWWZZG2zxsWZWZWZZGG222z2Z BBBBBBWZZZGG2Z,.rxxsssssxsss')

    print('ssssxsssszsr..sBBBBBBBBBBBZsrxxxxzG rsxxr,rxssss BBWWWWWWWZZGsWBZBW2szZWBBBZZ22GzzGxZWGGZZWWWZWWZGzzZWBGWsZZGGGG2zsszG .r ZBBBBBWWZZGG2Z, ,,,xsxxsssss')

    print('ssssssszsrrxGWBBZBBWWWWBBBBBBBBBWBB, ,,rxxxrxxsx BBWWWWWWZZGGzGWB2GBBBZ2zz2GWBZ2z2WrWBBWWWZWZGzz2ZBBWZGZW,WZZZGG2zzsxsG.x, BBBBBBWZZGG2Zr ,,xssxssssss')

    print('xssssssr,sss2BGGZ2GBBBBBBWWBBZBBWWBB xssx,,,xxsr,BBBWWBBWWWZGGBWWBGxsWBBBBWZG22zGzsrZGGGGG222GZBBWG2ZZZWxzZGGGGGG22zsxssxs BBBBBBBWWZG2Zx xxx,.....,xs')

    print('rxxsss.,z,,ZBx2szBBBWWBBWWWBWWBWZBBZx ,rrrxr,,r sBWWBWWWWWWZGB xzZBBGssssZBBBBBBBBBBBWZZWWWBBBZsxzWBZWZsrWGGGGGGGG22zsxz.x.,BBBBBBWZGGGZx xsxxxr .rsss')

    print('xsssx rBsrBZ xsWBBWWWBBBZBBBWWBB2BB22.r ... GBWBBWWWWWWZZB GssZBBBBW2szGZZZZZZZWWWWWWZG2ssZBBBGGZ22ZZGZGGG222zzsxxxsrx BBBBWBWWZZGG2 r,rxxxxssssx')

    print('ssss zBBrBsrzsBBBBBBBBBZWBBWWZBB2ZZrZ xxsxx,.. BBBBBBBWBWWZBz , BBZzzzZWBBBBBBBBBBBBBWWZZZZWBBBBBszWZZWWZGzzGGG2G222sr.2rz BBBBBWWWZGG2G xxxsssssxxxr')

    print('sss.rBBsBBWrs2z22BBBBBzZBBz ZBZZ2,xrz ..,rxsr,. BBWBBBBWWWWZB ,x ,BZZWZG2zzzzGZZZZGGGGZZWWBBBBBGsrGWWZZG2zzGBZZGGG2zzss rrsr,BBBBBBWWGG2Z sssssssxxxxs')

    print('xsr BBzBBWss.sZxGGWz2xxBB xGB,xGx,W rr,.,,. ,. BBWWWWBWWWZWW ss. BWWZGZZWWWWZZGGGZWWWWWWWWZGsxsZBBWWZGZZWWZ2zGZZGGGG2xxrrzs BBBBBBBBBBWB xszsszsssxxx')

    print('ss zBGZBGZZ BZ.xsx,2xrBz ZWxrWWWrr,xxsxr..,r. BBBBWWWBWWWB rx. ZBZWWBBBBBBBBBBBBBWWWWWWZZZWBBWZG2zszGZG2zssx,.rxzGGGGxs,,..WBBWWGzsxrr2..,xssssssxss')

    print('sx BBxBZZWrBBBsx,sZx.x,rxGBsZxBBWx .,,,rxrxxxs. BBBBBBWWWZWB zWBBWWZGG2zz22GZZWWWBBBBBBBBWZZZWWBWWWZZZG2GZWBBWGs,r22sG xBBZ2sxrszr..,rsGB,sssssxxss')

    print('sx B BZGBGBBBzxrWB2ZBBBBZGrZZBBsZ ,.rxrssssr. BBBBBBBBWZBx .rGBZsxxszGZWBBBBBBBBWWZGG2zzzz22222z222GGGGG22222zzZBBZ, sB. BWZWBWGr .xs2G2xrsxr,.,,,r')

    print('srrsGBZBBBBWWZ2BBBBBBB2x2GBBBG2WB ..,.. rx,,WBBBBBBBBBBBBs BZrsGWBBBBWZ2sr,rrxsz2222GGZWBBBBBBWG2GG2z2GZWZZG2GzrsBBB,x. 2BWWZGZWBWZzsxxW.xxrrr.rxxx')

    print('sxr.BBBBBWBBWBBBBBBBr sGBBBBBBBsG2.sxrssxsr . . ,sszsxr x xZ2WBBW2zssxsz2ZWWWBBWWBBBBBBWG2G2GGWBBWWWZGsxr..,xxsZBs,ZBB rrBBBBBBBBWWWZZBZ.xxxr,,xsxr')

    print('ss sBGBBBBWBBBWZBB, zGsBBz BBBGrG, ,xs..x .BBBGs, rzxxszZ, 2BBBWzz2GZZWBBBBBBWWWWWWZG2zss2WBBWZGZWWWWWBBBBBBWGx zBz,Brr,.B2,. z22r .,sssssxszss')

    print('xx BBGBBBZBWGzBB..2 .BB2 , BBzZ. B2 .,z BBWBBBBBBBBBBBBBBBWGGZWWWZZZZGZZZZZGG22z22ZBBBBBBBWZZ2zssssxx2ZBBBBBBBBBG,.xZrZ r ..rzG2BBs.sB22xssssxsssss')

    print('xx BZZBBs2.rBB , ZBB2 xssx sB2BZ BBZ zBzzxxr,rrxszszBZZWBBWZGGGGGZZG2zz2ZBBBBBBBWGx .2 ...... r2G2ZBBBBr2x.x BBBBBB rs s,xrxszzzsr')

    print('rr BZZBzxsrW ,. BBWB rr,rxr. ZBBBs sBBBB xBZzs2ZWZG222sBW2zsxsssszGWBBBBBBBBBZ2sxrs G,rrxrrrrrr,,... rGszBBB rx GBZZWBB Z, x rrsr..,.')

    print('rr 2ZZB2B.Zr.xsr WBBs,.sxr,.. rZBBW, BB2r,.xz222Z2sGWBBBBBBBBBBZ2sx,. ..,,rrzZGGBsrxxrrrrrr,...... .2xZG2.xxZWWGzxx,s ,GZBG rr,. .')

    print('xr.rxBBBs2W rxxr BBB2..,rxxsssss, .,, WZBBBWBBBZBGBBBZZ2szsr. .,,,rrrxxxxxxxrr,xz,xxxrrrrrr,...... szBZ.srBBBBBBs, rZx.xB .sr ,,')

    print('xx, .BBBGW rr,, B,BB .r,......,xssssxxr, 2 . rW2sxBBBW2ss,...,,rrxxxxxxxxxxxxxxxxxrrG,rxxxrrrr,,..... xGZ rxBWZBBBrr BBWBZZB ...')

    print('rrr, sBBBz ,,,,, B WB .rr.,xxr. .. ...rxx.,WBBZs.xrZBBGr ..,rrrrrrrrrrrxxxxrxxxrrrxrr,Gxrxxxrrrrr,....... Br . xrsBBBBZ,z. .,r.,')

    print(',,rr, WBBx xxrxx B B ..,rrxxssxr.,r. ., W.zZWBBBBBz..,rxxrrrrrrrrrrrrrrrxxxrrrrrrr,rZ,xxxrrrrr,....... Z ,,sssszzssx,rBBBB s rssx,r')

    print('rrrrx, BB, r,rrx.xG Zsrsxxxxxxxxxxxrxxr., ZrBWsZZBB..rxxxrrrrrrrrrrrrrrrrrrrrrrrrrrr.Z,rxxxrrrr,,....... W,,rx, x ,. ,ZZ s .rr')

    print('xxrr,. B, xx,,rr,zr,rrxxxxrrrrrrrrrrrrrx sZZZ rZBG ,rxrrrrrrrrrrr,,,,,,,,,.....,,rrr,G,xxrrrrrr,,....... ,r s ,x r r, Z r,2GGG2z')

    print('rxssxr, Z2 .,,,,.r.,.,xxxxxxxxrrrrrrrrrr. BGB2s.BZ.rxxxrrrrrrr,,,,,..................Gsrxrrrrrrr,........ sx,. ,BBB BBBBBB, . .r,rrrx')

    print(',,.,rrx,.z.. .rrxxrxxxxxxrr,,rrrrrr 2WWBB,rW ,xrrrrrrrrrr,,,,,,,.............. W,xxrxrrrr,,........ 2 z sZ WB2 BBBZx ,zrzGzsssss')

    print('rsxrrrr,.rrxx,rzssxxrxxxxxxxxxxxxxxxrrxr WZBBBxB,rrrrrrrrrr,,,,.,.................. .Grrxrrrrrr......... .. z .r r. 2. xx .rssz')

    print('xxxszzzss,,rxsrxrxxssxxxxxxrrrrr,,,,,,, xsZBWBZ.rrrrrrrrr,,,,.,,................... Gxrxrrrrrr,...... s .,rrsxzs xr BZx2Gzssxxsssz')

    print('xzsszzzszssxrr ,,. ..,r,,,xrrxxxrrrrrrr .WWBB2 rrrrrrrrrr,,.................... B,rrrrrrr,........ Zrs,,,,, .rrx,xzzxxxs222GGGG2222')

    print(',. .,rxssszzsszsz2sszsxrr,,. ....,. ., sBB2 rrrrrrrrrr,,,,.................... ,2rxrrrrrr,......... .. ,xx,..,rxxxxsssxs222GGGGGG')

    print(',rrrr,,. .,,,,,...,,,... .rssxxx, ...,r. rW.rxrrrrrrrrr,................ . . . . 2rrxrrrrrr,,........ zszs22szsxxsssssszzzzsxxrrrxssssz')

    print('rrrrrr,,,,..rrrr, ...,..... .rrxr. ., zr,rrrrrrrrrr,,............ . . . .Brxxxrrrr,......... .xx2zszssszzsxrxx, .rxssssssss')

    print('rrrrrrrxxxxxrr ... .........rr, ..,r,. 2srrxrrrrrrrrr,,............. ........ .2zrxxrxrrr,....... s.. ,rxssxzss22GGZ2zzz2z222zzz222')

    print('rrrr,,,,,,,,,,.....,.. ...... Gsrxrrrrrrrrr,,...................... rx.xrrxrrrr,........ . sxsszssxr .r,....,xszzszzzsszsssss')

    print('r..rrrrrr,rrrrrszzr,... ...,. Gsrrrrrrrrrrr,,,...................... sx Grxxrxrrrr......... s,xrrxxsxxrxssssr,,xsssssssszzszz22')

    print('xrr.....,rr, ..,xx,.... ..........rx,2srxrrrrrrrr,,,...................... zrx.W,xxxrrrrr,....... zrsssxxxxssssszzzGzx,,xszssz2z22zzs')

    print('sssssssr,.,,r,,....rr.... .. ..,... zzrxxxrrrrrrr,,,..,................... .z,x,rzrxrxrrrrr,..... ,sssssz22GG2z2GGG22zGZG2z222z2z2zzzz')

    print('sssssssxsxxrxx,,,,,,,,,,,,,... .. zzrrrrrrrrrrrr,,,............... .... ,2 rx 2xrrrrrrr,......... zxsssxxr,rrrr,rrrsszssszzzzzzz2222G2')

    print('szssssssssszssssxx....xsx. , z2rrrrr,rrrrrr,,................... xz .. Wrxxxrrr,,....... 2xzzszsx,rxxrr. .xxxxxxxssszzzzz2222')

    print('2222222zzzzssssssssssxxxxxsrrxr,r.x2rrrrrrrrrrr,,,,................ . .sr .,rr Wrxrrrrrr,,...... s, ,rxsxsssssssrrxsszzz22zzzzz222G')

    print('zs2GGGGGGGG222zzsszsssssssssssssr,Grrrrrrrrrrrr,,,................... xz ..xrx2rxxxxxrrrr,,....... 2.sxxss.,,.ss2zz2GGG222222222GGGGGGGG')

#tifa_ascii()

def cait_sith():
    print('                                  ,",')
    print('                       O    ,\': =')
    print('                 \"-._ __|\|\/\/ ;  )')
    print('                 =."-.".)\_,."/ /"  /')
    print('                   \ ,-""", .    "-/.')
    print('                (_=  ( / \,"`   )')
    print('                 ( ,-./   \  ,  )\'')
    print('               ==(  /_Y,-,. ``;<')
    print('___     ___,.    >: ( \7  )  `-.)>')
    print(' ,"".  ""o-"==_}/.    <`.  \_, _, ;')
    print(':    `    O-. ,""")     `-.__," _,." ",')
    print('|     )     ,"" J`        /,__,-) _,.`;,--.___')
    print('     ;  ,OL_,:      .-._\\  ,-.::,:__  --._    ,-,')
    print(' `.__;,"     \ (    , _( ))" \ \::::::..:----._ .)  / ;"-7')
    print('               \ :  / ,"" //\\"._ 7 ;;::::::::''``")/  / ;')
    print('                \ `" /___,) \'. "./ /''.::,        / ;')
    print('                 :  ,"/    `-.._.                ;;')
    print('                  ""    |      ) ;  }".             ; ;')
    print('                        |      ) ;  }  \         _," ;')
    print('                       ,`:     `;  /    ;--.___," _,"')
    print('                      /  :    _;__ }    )"-.____,"')
    print('                     (   `. _(____;    /')
    print('                 _____\____(_______;-ctr--------')

cait_sith()

