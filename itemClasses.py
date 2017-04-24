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

    def format_dict(self):
        dic = {}
        dic['item'] = self.created['Item'].replace(' ', '_')
        dic['amount'] = self.created['Amount']
        dic['station'] = self.crafting_station.replace(' ', '_')
        dic['ingredients'] = []
        for item in self.ingredients:
            ing = {'item': item.replace(' ', '_'), 'amount': self.ingredients[item]}
            dic['ingredients'].append(ing)
        return dic

    def __repr__(self):
        return self.created['Item']
