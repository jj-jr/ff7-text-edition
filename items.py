class item:
    def __init__(self, name, description, quantity=0):
        self.name = name
        self.description = description
        self.quantity = quantity

### Creating item functions

def use_potion(actor, target):

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

def use_hi_potion(actor, target):

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

def use_ether(actor, target):

    mp_remainder = target.max_mp - target.current_mp

    if target.current_mp <= target.max_mp - 40 and target.current_mp != target.max_mp and target.current_hp != 0:
        target.current_mp += 40
        if actor.name != target.name:
            print(actor.name + ' used an Ether on ' + target.name + ' and restored 40 MP! ' + target.name + ' currently has ' + str(target.current_mp) + ' MP.')
            return target.current_mp
        else:
            print(target.name + ' used an Ether and restored 40 MP! They currently have ' + str(target.current_mp) + ' MP.')
            return target.current_mp
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

def use_turbo_ether(actor, target):

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

def use_phoenix_down(actor, target):

    if target.current_hp == 0:
        target.current_hp = 100
        print(actor.name + ' used a Phoenix Down on ' + target.name + '! ' + target.name + ' has been revived and currently has ' + str(target.current_hp) + ' HP.')
        return target.current_hp
    else:
        print('Phoenix Down cannot be used on a target that is alive.')

def use_molotov_cocktail(actor, target):

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

### Creating item objects

potion = item('Potion', 'Restore 100 HP.')
phoenix_down = item('Phoenix Down', 'Revives a downed party member and restores 100 HP.')
ether = item('Ether', 'Restores 40 MP.')
hi_potion = item('Hi-Potion', 'Restores 500 HP.')
molotov_cocktail = item('Molotov Cocktail', 'Deal 100 damage to an enemy.')