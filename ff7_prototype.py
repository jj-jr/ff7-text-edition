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

tifa_image = '''                                                                                                                        
                                                                                                                        
                                             ............................                                               
                                             ...:---==++++****+++==-::...                                               
                                       ...:-=+++=+++++++++***###########*=-....                                         
                                 .....:-==---===+***##########*#############+:.                                         
                              ......:-::-=+*#################%%#####%%%%#%####+..                                       
                           .. ...:::-=+*###******+++++**#########%###%%%%%%%%##*:....                                   
                           ....:--=+####***+=:::::-===+********#######%%#%%%%%###:....                                  
                           ..:--+*#%###*+-:.:-:.-----+++++++**********##******####*=:....                               
                        ....-=+##%%###+---==--==--=++=--==++++++***+****++++**+**####*-.....                            
                        ..:=+###%###*+=+++++++++*+=-:-=+=---=++**+==*######+-=++++*####*:...                            
                        .:+*###%###++********#*+===+*+=--=+***+=:..:=**###%%*--=*+=+****#=..                            
                     ...:**###%##****##***##*++**##*++**###*+-:....::-+*####%+:-=**=+***##*...                          
                     ...+#*##%%#**##%######**####*+*#####*=::.......:-=***##%#-:-=*++**##*#*...                         
                     ..:#*##%%#*##%%%#######*****#**+*#+-::........:--=+*###%%+--=**++**#**#*..                         
                     ..=**##%##%%%%%%#%%%*==*##*+-=**+--::........:-=-==*###%%*-+=+#++**##*##=.                         
                     ..+=###%%%%##==+##%#-=**=-:-*####********++=====-=+*####%#-+++#***###*###:...                      
                     ..++##%%%#%+*=-#***++=::::-++*#####%#*+==-====---=+*#%%%%#=++**#+**#*####+...                      
                     .:=+##%+*#*--====-:-..:::-:::--=--=#%%##*++-----=+*####%%#=****#******####...                      
                     .::*###=**-...........:--:.......*#####%%#*==-===**#####%#+#####****#*####=..                      
                     .::*#*#=**:.........:++-:.......-+*******#++=---=##%%###%#*#####*#**#*####*..                      
                     .:.***%*+*-........-##*=-:.........-===+====----*#%%#******#####*#**#*#####..                      
                     .:.+**###++:......+##*+=--:..........:-====----=*##+++++++:*#######***#####-....                   
                     ...=**#%%#*+:.....:-=-------::.....:----------=**+=#*++***-################=....                   
                     ..::++*###%*+=:--:..::------------------------++==*#*+==+=*#%##############*.        ..            
                     ..:.*+*#####-::.::-=====-====----------------====+++*+===*##%####%#######%#*.        ..            
                     ..:.+=+#####*:........:::::::::--------------=*##++==+*#%#######%%#######%##:...                   
                     ....-=+*#####*:.......::::::::-------------=+##%%%##%%%%%***#####%########%#-...                   
                     ....:==*####%#*:.....:::::----------------===+#%%#**%%%%%***#####%%#%%####%#+...                   
                     ...::==+####%###-..:::-----------======-----==####*#%%%%%*++****#%%#%%%%##%#*...                   
                     ....:--+**######%#**+++*****######*++==-----=+#%###*##%%%#==+***###%%%%%###%#:..                   
                     .....-:=***#####%%%%%%%%%%%###***++=---------*#####*##%%%%+-=++**##%%%%%%#%%%+..                   
                     .....-:=***#####%%%%%%%%%%#***+===-----------+*####**#%##%#--=*+*##%%%%%%%%%%#:.                   
                      ....:.=+**####%%%%%-+#%%%*+=====------------=***##*+**###%+.:+++*#%%%%%%%#%%#+.                   
                      ...::.==+**#####%%*..:*#%=::-------------:---**####+*+###%#-.-+++##%%%%%%%%%##:...                
                     ....-.:==+**#####%#=:-=+##=....::::::::::::::-=*#####+*+#####:.-==*#%%%%%%%%%%#*...                
                     ....-.:===**#######=-+**+++............::::::--=*####****####*.:-=+#%%%%%%%%%%%#-..                
                     ....-:-==++**#####*=*=====+............:::::::--=*#%%#***####%*::-=+%%%%%%%%%%%#*..                
                     ....-:===+**######*+--=-:--...........:::::::::---+#%%#*#######*::-=#%%%%%%%%%%##-.                
                     ...:--+==+**#####*-::.=-......::.....:::::::::::---=+*%%#######%*:--+#%%%%%%%%%%##:...             
                     ...:=-+==+**#####-::...--:::.:.....:--::::::::::-----=+*%#######%+:-+*%%%%%%%%%%%#*...             
                     ...:==++++*#####+::............:--=--:::::::::::-----=+*#*#####%%#=-=+#%%%%%%%%%###=..             
                     ..:+==+*++*###%#-:................:-----:::::::-----=*****#%%%##%%#==+*#%%%%%#######:.             
                  ....-:-+++****#####-...............:.....::---------=++*+++**###%%%#%%%+++*%%%%%%%%####*....          
               ..........=**#**#####*:................:::::::..:-==+++++===++**####**##%%#++*#%%%%##%#####*...          
               ..........:***#*#####*:..................:::--::---=+======+****+=---==+#%%**+*#%%%#########+..          
         .............  ..-#*#**####*=::.................::-===++*++++++***+=-::::::--=+*%#***#%%%%#########=.          
      .........         ..:+**######*.................::---==+********#*+-:::::::::::---=*%##*##%%%##########-...       
      .......           ..:-**#######....................:=*#########*=:::::.:::::::::---=*%#**#%%%######***##-..       
      ....              ..:-=*#######=..              ..=*#%%%%%%%#*=::::.....:::::::::---=###*##%%######*****#-.       
      ....              ...:-=*####%#*..           ...:*#%%%%%%%%#=::....   ...:::::::::--=+#####%%%%####******#:...    
      ....              ...:-===*#####+....       ...=#%%%%%%%%#+:.......   ....::::::::--==*#####%%######***+***...    
                        ....:-=-:=#####+...     ....*#%%%%%%%#*-......      ......:::::::--=+#####%%#####*****++*=..    
                           ..:--:.:+####+.....  ...+#%%%%%%%#=:....         ......:::::::-==+#####%######*****+++*..    
                           ....::...:+**++....  ..=*##%##%##-...               ....::::::-==+######%####******++++-.    
                           .....:.....:+*=-:..  ..=+++++**+:....               .........:---=###########*****+++==-.    
                              ..........:=-...  ..::..........           ...        .....:::=+*****####****+++++==-.    
                              .......  ......................            ...         .......::++++**+++++==---===-..    
                                          .......                                       ......:--:-:..:--.::..::....    
                                          ... . .                                       .. .......................      
...                                                                                           ....         . .          
'''

print(tifa_image)
