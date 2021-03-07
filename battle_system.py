import inventory, characters_playable as characters, art, common_functions as cf
import random

### Battle system handling

def battle (party, enemy):

    total_gil = 0
    total_exp = 0
    all_combatants = {}
    active_party = {}
    active_enemies = {}
    cf.space()

    for bad_guy in enemy:
        bad_guy.current_hp = bad_guy.max_hp
        total_exp += bad_guy.exp
        total_gil += bad_guy.gil
        bad_guy.atb = 0
        all_combatants[bad_guy] = bad_guy.name
        active_enemies[bad_guy] = bad_guy.name

    for good_guys in party:
        good_guys.atb = 0
        all_combatants[good_guys] = good_guys.name
        active_party[good_guys] = good_guys.name

    def party_atb(character, atb):

        rate_party = character.spd * 1.2
        atb += rate_party
        return round(atb)

    def enemy_atb(enemy, atb):

        rate_enemy = enemy.spd * 1.2
        atb += rate_enemy
        return round(atb)

    def enemy_input_list(enemies):
        print('')
        counter = 1
        for bad_guy in enemies:
            print('* Press ' + str(counter) + ' for ' + bad_guy.name)
            counter += 1

    def party_auto_target(enemy):
        enemy_list = []
        for k in enemy:
            enemy_list.append(k)
        return random.choice(enemy_list)

    def enemy_auto_target(party):
        active_party = []
        for good_guy in party:
            if good_guy.ko is False:
                active_party.append(good_guy)
        target = random.choice(active_party)
        return target

    def turn_input_list(actions):
        print('')
        counter = 1
        for action in actions.actions:
            print('* Press ' + str(counter) + ' for ' + action)
            counter += 1

    def turn_input(actor):
        print('')
        print(f'What would you like {actor.name} to do?')
        turn_input_list(actor)
        print('')
        answer = int(input('Enter: '))
        return answer


    def attack_input(actor):

        print('')
        print(f'Who is {actor.name} going to attack?')
        enemy_input_list(enemy)
        print('')
        answer = int(input('Enter: '))
        return answer

    def item_input(actor):

        ### NOT FINISHED. Used written input rather than numbers. Use a dictionary.
        print('')
        print(f'What item is {actor.name} going to use?')
        #item_input_list(enemy)
        answer = int(input('Enter: '))
        return answer

    ### Auto-battle code

    def auto_battle():

        enemy_defeat = False
        party_defeat = False
        party_action = False
        enemy_action = False
        cf.space()

        while enemy_defeat is False and party_defeat is False:
            if party_action is False and enemy_action is False:
                for combatant in all_combatants:
                    if combatant in active_party:
                        if combatant.atb < 100:
                            combatant.atb = party_atb(combatant, combatant.atb)
                        else:
                            party_action = True
                            break
                    else:
                        if combatant.atb < 100:
                            combatant.atb = enemy_atb(combatant, combatant.atb)
                        else:
                            enemy_action = True
                            break

            elif party_action is True:

                attack_randomizer = round(
                    random.randint(round(int((-1 * ((0.3 * combatant.str_))))), round(int(((0.3 * combatant.str_))))))
                party_attack = combatant.str_ * 3
                party_attack += attack_randomizer
                combatant.atb = 0
                target = party_auto_target(active_enemies)
                target.current_hp -= party_attack

                if target.current_hp <= 0 and len(active_enemies) == 1:
                    print(combatant.name + ' attacked and dealt ' + str(party_attack) + ' damage. ' + target.name + ' has been defeated!')
                    cf.space()
                    print('Battle over.')
                    del all_combatants[target], active_enemies[target]
                    enemy_defeat = True

                elif target.current_hp <= 0 and len(active_enemies) != 0:
                    print(combatant.name + ' attacked and dealt ' + str(party_attack) + ' damage. ' + target.name + ' has been defeated!')
                    del all_combatants[target], active_enemies[target]
                    party_action = False

                else:
                    print(combatant.name + ' attacked and dealt ' + str(party_attack) + ' damage. ' + target.name + ' has ' + str(
                        target.current_hp) + ' HP remaining.')
                    party_action = False

            else:
                # if the enemy has 100 ATB
                enemy_attack = combatant.str_ * 3
                target = enemy_auto_target(active_party)
                target.current_hp -= enemy_attack
                combatant.atb = 0

                if target.current_hp <= 0 and len(active_party) == 1:
                    target.ko = True
                    print(combatant.name + ' attacked and dealt ' + str(
                        enemy_attack) + ' damage. The party has been defeated!')
                    print('Game over.')
                    party_defeat = True
                elif target.current_hp <= 0 and len(active_party) > 1:
                    target.ko = True
                    target.current_hp = 0
                    del active_party[target], all_combatants[target]
                    print(combatant.name + ' attacked ' + target.name + ' and dealt ' + str(
                        enemy_attack) + ' damage. ' + target.name + ' has been defeated!')
                    enemy_action = False
                else:
                    print(combatant.name + ' attacked ' + target.name + ' and dealt ' + str(
                        enemy_attack) + ' damage. ' + target.name + ' has ' + str(
                        target.current_hp) + ' HP remaining.')
                    enemy_action = False

        if enemy_defeat is True:
            print('')
            print('The party gained ' + str(total_exp) + ' EXP and ' + str(total_gil) + ' gil.')
            print('')
            inventory.gil += total_gil

            for good_guys in party:
                good_guys.exp += total_exp
                if good_guys.exp > good_guys.level_threshold[0]:
                    characters.level_up(good_guys)

            for bad_guy in enemy:
                if random.random() <= bad_guy.drop_rate:
                    print(bad_guy.name + ' dropped a ' + bad_guy.item.name + ' and it has been added to your inventory.')
                    inventory.add_to_inventory(bad_guy.item, 1)
            #print(art.tifa_image)
            return inventory.item_inventory

    ### Manual battle code

    def manual_battle():

        enemy_defeat = False
        party_defeat = False
        party_action = False
        enemy_action = False
        last_party_member_alive = bool

        while enemy_defeat is False and party_defeat is False:
            if party_action is False and enemy_action is False:
                for combatant in all_combatants:
                    if combatant in active_party:
                        if combatant.atb < 100:
                            combatant.atb = party_atb(combatant, combatant.atb)
                        else:
                            party_action = True
                            break
                    else:
                        if combatant.atb < 100:
                            combatant.atb = enemy_atb(combatant, combatant.atb)
                        else:
                            enemy_action = True
                            break

            elif party_action is True:
                print('')
                print(f"It's {combatant.name}'s turn.")
                attack_randomizer = round(random.randint(round(int((-1 * ((0.3 * combatant.str_))))), round(int(((0.3 * combatant.str_))))))
                party_attack = combatant.str_ * 3
                party_attack += attack_randomizer
                combatant.atb = 0
                answer = turn_input(combatant)

                if answer - 1 == 0:
                    attack_answer = attack_input(combatant)
                    enemy[attack_answer - 1].current_hp -= party_attack

                    if enemy[attack_answer - 1].current_hp <= 0 and len(enemy) == 1:
                        print(combatant.name + ' attacked and dealt ' + str(party_attack) + ' damage. ' + enemy[attack_answer - 1].name + ' has been defeated!')
                        cf.space()
                        print('Battle over.')
                        enemy.pop(attack_answer - 1)
                        enemy_defeat = True
                        cf.cont()

                    elif enemy[attack_answer - 1].current_hp <= 0 and len(enemy) != 0:
                        cf.space()
                        print(combatant.name + ' attacked and dealt ' + str(party_attack) + ' damage. ' + enemy[attack_answer - 1].name + ' has been defeated!')
                        enemy.pop(attack_answer - 1)
                        party_action = False
                        cf.space()
                        cf.cont()
                    else:
                        print('')
                        print(combatant.name + ' attacked and dealt ' + str(party_attack) + ' damage. ' + enemy[attack_answer - 1].name + ' has ' + str(enemy[attack_answer - 1].current_hp) + ' HP remaining.')
                        party_action = False
                        print('')
                        cf.cont()

            else:
                # if the enemy has 100 ATB
                print('')
                print('*****')
                print(combatant.name.upper() + "'S TURN")
                print('*****')
                print('')
                cf.cont()
                enemy_attack = combatant.str_ * 3
                target = enemy_auto_target(party)
                target.current_hp -= enemy_attack
                combatant.atb = 0

                if target.current_hp <= 0 and last_party_member_alive is True:
                    party_defeat = True
                    cf.space()
                    print(combatant.name + ' attacked and dealt ' + str(enemy_attack) + ' damage. The party has been defeated!')
                    print('Game over.')
                elif target.current_hp <= 0 and last_party_member_alive is False:
                    target.current_hp = 0
                    target.atb = 0
                    cf.space()
                    print(combatant.name + ' attacked ' + target.name + ' and dealt ' + str(enemy_attack) + ' damage. ' + target.name + ' has been defeated!')
                    enemy_action = False
                    cf.space()
                    cf.cont()
                else:
                    cf.space()
                    print(combatant.name + ' attacked ' + target.name + ' and dealt ' + str(enemy_attack) + ' damage. ' + target.name + ' has ' + str(target.current_hp) + ' HP remaining.')
                    enemy_action = False
                    cf.space()
                    cf.cont()

        if enemy_defeat == True:
            print('')
            print('The party gained ' + str(total_exp) + ' EXP and ' + str(total_gil) + ' gil.')
            print('')
            inventory.gil += total_gil

            for good_guys in party:
                good_guys.exp += total_exp
                if good_guys.exp > good_guys.level_threshold[0]:
                    characters.level_up(good_guys)

            for bad_guy in enemy:
                if random.random() <= bad_guy.drop_rate:
                    print(bad_guy.name + ' dropped a ' + bad_guy.item.name + ' and it has been added to your inventory.')
                    inventory.add_to_inventory(bad_guy.item, 1)
            #print(art.tifa_image)
            return inventory.item_inventory

    ### Battle start dialogue

    if len(enemy) == 1:
        print('Your party encountered a ' + enemy[0].name + '!')
        #print('')
    elif len(enemy) == 2:
        print('Your party encountered ' + enemy[0].name + ' and ' + enemy[1].name + '!')
        #print('')
    else:
        print(f'Your party encountered {enemy[0].name}, {enemy[1].name}, and {enemy[2].name}!')

    ### Auto-battle check

    cf.space()
    print('Would you like to auto-battle or fight manually?')
    cf.space()
    print('* Press 1 for auto-battle')
    print('* Press 2 for manual battle')
    cf.space()
    auto_battle_answer = input('Enter: ')

    if auto_battle_answer == '1':
        auto_battle()
    else:
        manual_battle()