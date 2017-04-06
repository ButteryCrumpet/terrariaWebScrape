import cleaners
import Scraper as sc
import utils
from itemClasses import Recipe

def serializer(row, station):
    recipe_dict = {}
    data = row
    created_item = data.pop(0)

    if '(' in data[0]:
        amount = utils.get_bracketed_value(row.pop(0))
    else:
        amount = '1'

    current_ing = ''
    for item in data:
        if '(' not in item:
            current_ing = item
            recipe_dict[item] = 1
        elif '(' in item:
            recipe_dict[current_ing] = utils.get_bracketed_value(item)

    return Recipe(created_item, amount, recipe_dict, station)


def row_format(table):
    data = []
    rows = table.find_all('tr')
    current_row = []

    for row in rows:
        if not row.has_attr('style'):
            for item in list(row.stripped_strings):
                current_row.append(item)
        else:
            data.append(current_row)
            current_row = []
            for item in list(row.stripped_strings):
                current_row.append(item)
    return data