### Level handling

def level_up(character):
    print('******')
    print(character.name + ' leveled up!')
    print(character.name + ' is now level ' + str(character.level) + '.')
    print('******')
    print('')
    character.level += 1
    return character.level

cloud_exp_threshold = [10, 50, 150]
tifa_exp_threshold = [10, 50, 150]
barret_exp_threshold = [20, 60, 175]

cloud_str_level = [2, 3, 1]