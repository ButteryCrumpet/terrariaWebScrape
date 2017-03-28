#!/usr/bin/python3

class Weapon:
    def __init__(self, data):
        self.name = data['name']
        self.type = data['type']
        self.hardmode = data['hardmode']
        self.rarity = data['rarity']
        self.damage = data['damage']
        self.damage_type = data['damage_type']
        self.auto_attack = data['auto_attack']
        self.knockback = data['knockback']
        self.speed = data['speed']
        self.use_time = data['use_time']
        self.shoot_speed = data['shoot_speed']
        self.self_price = data['sell_price']
        self.mana_cost = data['mana_cost']
        self.ammo = data['ammo']
        self.debuff = data['debuff']

    def __repr__(self):
        return self.name