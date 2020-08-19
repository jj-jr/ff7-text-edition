import level, inventory, characters_playable as characters, enemies, common_functions as cf
import random

### Battle system handling

def battle (party, enemy):

    total_gil = 0
    total_exp = 0
    enemy_defeat = False
    party_defeat = False
    party_action = False
    enemy_action = False
    all_combatants = party + enemy
    last_party_member_alive = bool

    for bad_guy in enemy:
        bad_guy.current_hp = bad_guy.max_hp
        total_exp += bad_guy.exp
        total_gil += bad_guy.gil
        bad_guy.atb = 0

    for good_guys in party:
        good_guys.atb = 0

    def party_atb(character, atb):

        rate_party = character.spd * 1.2
        atb += rate_party
        return round(atb)

    def enemy_atb(enemy, atb):

        rate_enemy = enemy.spd * 1.2
        atb += rate_enemy
        return round(atb)

    def enemy_input_list(enemy):
        print('')
        counter = 1
        for bad_guy in enemy:
            print('* Press ' + str(counter) + ' for ' + bad_guy.name)
            counter += 1

    def enemy_target(party):
        return random.choice(party)

    def party_ko(party):
        ko_count = 0
        for good_guys in party:
            if good_guys.current_hp <= 0:
                ko_count += 1
            else:
                pass
        if ko_count == 2:
            last_party_member_alive = True
            return last_party_member_alive
        else:
            last_party_member_alive = False
            return last_party_member_alive


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

    if len(enemy) == 1:
        print('Your party encountered a ' + enemy[0].name + '!')
        #print('')
    elif len(enemy) == 2:
        print('Your party encountered ' + enemy[0].name + ' and ' + enemy[1].name + '!')
        #print('')
    else:
        print(f'Your party encountered {enemy[0].name}, {enemy[1].name}, and {enemy[2].name}!')


    while enemy_defeat is False and party_defeat is False:
        if party_action is False and enemy_action is False:
            for combatant in all_combatants:
                if combatant in party:
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
            print(f"It\'s {combatant.name}\'s turn.")
            attack_randomizer = round(random.randint(round(int((-1 * ((0.3 * combatant.str_))))), round(int(((0.3 * combatant.str_))))))
            party_attack = combatant.str_ * 3
            party_attack += attack_randomizer
            combatant.atb = 0
            answer = turn_input(combatant)

            if answer - 1 == 0:
                attack_answer = attack_input(combatant)
                enemy[attack_answer - 1].current_hp -= party_attack

                if enemy[attack_answer - 1].current_hp <= 0 and len(enemy) == 1:
                    # Have to add conditional if here for if the enemy is the last enemy in the combat or not - if so, the battle is over and if not then pop that enemy out of the array.
                    print(combatant.name + ' attacked and dealt ' + str(party_attack) + ' damage. ' + enemy[attack_answer - 1].name + ' has been defeated!')
                    print('Battle over.')
                    enemy_defeat = True

                elif enemy[attack_answer - 1].current_hp <= 0 and len(enemy) != 0:
                    # Have to add conditional if here for if the enemy is the last enemy in the combat or not - if so, the battle is over and if not then pop that enemy out of the array.
                    print(combatant.name + ' attacked and dealt ' + str(party_attack) + ' damage. ' + enemy[attack_answer - 1].name + ' has been defeated!')
                    del enemy[attack_answer - 1]
                    party_action = False
                else:
                    print('')
                    print(combatant.name + ' attacked and dealt ' + str(party_attack) + ' damage. ' + enemy[attack_answer - 1].name + ' has ' + str(enemy[attack_answer - 1].current_hp) + ' HP remaining.')
                    party_action = False

        else:
            # if the enemy has 100 ATB
            for combatant in enemy:
                enemy_attack = combatant.str_ * 3
                target = enemy_target(party)
                if combatant.atb >= 100:
                    print('')
                    print('*****')
                    print('ENEMY TURN')
                    print('*****')
                    target.current_hp -= enemy_attack
                    combatant.atb = 0
                    party_ko(party)
                    if target.current_hp <= 0 and last_party_member_alive is True:
                        # Have to add conditional code here if the party member killed is the last one in the party then it's game over, otherwise make it so the character can't be targeted.
                        party_defeat = True
                        cf.space()
                        print(combatant.name + ' attacked and dealt ' + str(enemy_attack) + ' damage. The party has been defeated!')
                        print('Game over.')
                        break
                    elif target.current_hp <= 0 and last_party_member_alive is False:
                        cf.space()
                        print(combatant.name + ' attacked ' + target.name + ' and dealt ' + str(enemy_attack) + ' damage. ' + target.name + ' has been defeated!')
                        enemy_action = False
                    else:
                        cf.space()
                        print(combatant.name + ' attacked ' + target.name + ' and dealt ' + str(enemy_attack) + ' damage. ' + target.name + ' has ' + str(target.current_hp) + ' HP remaining.')
                        enemy_action = False
                else:
                    continue
    else:
        pass

    if enemy_defeat == True:
        print('')
        print('The party gained ' + str(total_exp) + ' EXP and ' + str(total_gil) + ' gil.')
        print('')
        inventory.gil += total_gil

        for good_guys in party:
            good_guys.exp += total_exp
            if good_guys.exp > good_guys.level_threshold[0]:
                characters.level_up(good_guys)
            else:
                pass

        for bad_guy in enemy:
            if random.random() <= bad_guy.drop_rate:
                print(bad_guy.name + ' dropped a ' + bad_guy.item.name + ' and it has been added to your inventory.')
                print('')
                return inventory.add_to_inventory(bad_guy.item, 1)
            else:
                pass
    print('')
