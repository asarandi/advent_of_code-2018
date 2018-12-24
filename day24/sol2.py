#!/usr/bin/env python3

import  sys
import  re
from operator import itemgetter
from copy import deepcopy

#
#advent of code 2018
#day 24
#part 2
#

def get_input(search_str, data):    #data = list[] of input lines
    i = 0
    res = []
    while i < len(data):
        if data[i] == search_str:
            i += 1
            while i < len(data) and len(data[i]) > 0:
                pattern = r'(\d+) units each with (\d+) hit points(.*)with an attack that does (\d+) (\w+) damage at initiative (\d+)'
                m = re.search(pattern, data[i])
                units = int(m.group(1))
                hit_points = int(m.group(2))
                attack_damage = int(m.group(4))
                attack_type = m.group(5)
                initiative = int(m.group(6))
                weaknesses = []
                immunities = []
                m2 = re.search('.*\((.*)\).*', m.group(3))
                if m2:
                    part2 = m2.group(1)
                    if len(part2) > 0:
                        sp = part2.split('; ')
                        if sp[0][0:8] == 'weak to ': weaknesses = sp[0][8:].split(', ')
                        elif sp[0][0:10]  == 'immune to ': immunities = sp[0][10:].split(', ')
                        if len(sp) > 1:
                            if sp[1][0:8] == 'weak to ': weaknesses = sp[1][8:].split(', ')
                            elif sp[1][0:10]  == 'immune to ': immunities = sp[1][10:].split(', ')

                group = {
                        'army': search_str,
                        'units': units,
                        'hit_points': hit_points,
                        'weaknesses': weaknesses,
                        'immunities': immunities,
                        'attack_damage': attack_damage,
                        'attack_type': attack_type,
                        'initiative': initiative,
                        'effective_power': units * attack_damage,
                        'attacked_by': None,
                        'target_idx': None,
                }
                res.append(group)
                i += 1
        i += 1
    return res


def calc_damage(attacking_group, defending_group):
    ep = attacking_group['units'] * attacking_group['attack_damage']    #effective power
    at = attacking_group['attack_type']
    d = None
    if at in defending_group['immunities']:
        d = 0
    elif at in defending_group['weaknesses']:
        d = ep * 2
    else:
        d = ep
    return d

#------------------------------------------------------------------------------

def target_selection(attacking_group, defending_army):
    damages = []
    ati = defending_army.index(attacking_group)

    for i in range(len(defending_army)):
        v = defending_army[i]
        if v['army'] == attacking_group['army']:
            continue        #only fight enemy army
        if v['attacked_by'] != None:
            continue
        if v['units'] < 1:
            continue
        d = calc_damage(attacking_group, v)
        damages.append([i, d, v['units'] * v['attack_damage'], v['initiative']])    #

    damages = sorted(damages, key=itemgetter(3), reverse=True)    # sort by initiative
    damages = sorted(damages, key=itemgetter(2), reverse=True)    # sort by effective power
    damages = sorted(damages, key=itemgetter(1), reverse=True)    # sort by damages

    if len(damages) > 0 and damages[0][1] > 0:   #if d > 0
        dfi = damages[0][0]
        defending_army[dfi]['attacked_by'] = ati
        attacking_group['target_idx'] = dfi

#------------------------------------------------------------------------------

def army_update_ep(army):
    for g in army:
        g['effective_power'] = g['units'] * g['attack_damage']

def army_reset_targets(armies):
    for g in armies:
        g['attacked_by'] = None
        g['target_idx'] = None
    

def sort_army_for_attack(army):
    army_update_ep(army)
    army = sorted(army, key=itemgetter('initiative'), reverse=True)
    army = sorted(army, key=itemgetter('effective_power'), reverse=True)
    return army


def get_counts(armies):
    counts = {}
    for group in armies:
        if group['army'] not in counts:
            counts[group['army']] = 0

        if group['units'] > 0:
            counts[group['army']] += group['units']
    return counts


def is_game_over(armies):
    counts = get_counts(armies)
    for k,v in counts.items():
        if counts[k] <= 0:
            return True
    return False

def game(boost_value):
    fn = 'input.txt'
    if len(sys.argv) > 1:
        fn = sys.argv[1]

    with open(fn) as fp:
        data = fp.read().splitlines()
        fp.close()

    immune_system = get_input('Immune System:', data)
    for itm in immune_system:
        itm['attack_damage'] += boost_value

    infection = get_input('Infection:', data)
    armies = immune_system + infection

    while not is_game_over(armies):
        armies = sort_army_for_attack(armies)
        army_reset_targets(armies)
        for g in armies:
            target_selection(g, armies)

        clone = deepcopy(armies)
        clone = sorted(clone, key=itemgetter('initiative'), reverse=True)

        idx = []
        for i in range(len(clone)):
            c = clone[i]
            idx.append(armies.index(c))

        for i in idx:
            army_update_ep(armies)
            g = armies[i]
            if g['units'] > 0 and g['target_idx'] != None:
                enemy = armies[g['target_idx']]
                d = calc_damage(g, enemy)
                kill = int(d / enemy['hit_points'])
                enemy['units'] -= kill


    counts = get_counts(armies)
    return counts['Immune System:']

i = 46
res = 0
while res == 0 and i >= 0:
    res = game(i)
    print(i, res)
    i += 1
