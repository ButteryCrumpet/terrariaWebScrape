#!/usr/bin/python3

class Recipe(object):

    def __init__(self, created, amount, ingredients, station):
        self.created = {'Item': created, 'Amount': amount}
        self.ingredients = ingredients
        self.crafting_station = station

    def format_csv(self):
        row = []
        row.append(self.created['Item'])
        row.append(str(self.created['Amount']))
        row.append(self.crafting_station)
        for item, amount in self.ingredients.items():
            row.append(item + '|' + str(amount))
        return row

    def __repr__(self):
        return self.created['Item']
