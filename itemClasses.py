#!/usr/bin/python3

class Recipe(object):

    def __init__(self, item, amount, ingredients, station):
        self.created_item = item
        self.amount_created = amount
        self.ingredients = ingredients
        self.crafting_station = station

    def __repr__(self):
        return self.created_item