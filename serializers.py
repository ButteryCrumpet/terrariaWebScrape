#!/usr/bin/python3

def weapon_row_to_dict(row):
    cells = row
    data = {}
    data['name'] = cells[1]
    data['type'] = cells[2]
    data['hardmode'] = cells[3]
    data['rarity'] = cells[4]
    data['damage'] = cells[5]
    data['damage_type'] = cells[6]
    data['auto_attack'] = cells[7]
    data['knockback'] = cells[8]
    data['speed'] = cells[9]
    data['use_time'] = cells[10]
    data['shoot_speed'] = cells[11]
    data['sell_price'] = cells[12]
    data['mana_cost'] = cells[13]
    data['ammo'] = cells[14]
    data['debuff'] = cells[15]
    return data