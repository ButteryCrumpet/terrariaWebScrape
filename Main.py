import requests
import json

import Scraper as sc
from query import SoupQuery
from formatter import row_format, serializer
import cleaners
import CSVstuff

URLS = {'Ancient Manipulator': 'Ancient_Manipulator',
        'Hardmode_Forge': 'Hardmode_Forge',
        'Autohammer': 'Autohammer',
        'Bookcase': 'Autohammer',
        'Bone Welder': 'Bone_Welder',
        'Blend-O-Matic': 'Blend-O-Matic',
        'By Hand': 'By_Hand',
        'Campfire': 'Campfire',
        'Cooking Pot': 'Cooking_Pot',
        'Crystal Ball': 'Crystal_Ball',
        'Altar': 'Altar',
        'Dye Vat': 'Dye_Vat',
        'Flesh Cloning Vat': 'Flesh_Cloning_Vat',
        'Furnace': 'Furnace',
        'Glass Kiln': 'Glass_Kiln',
        'Heavy Work Bench': 'Heavy_Work_Bench',
        'Hellforge': 'Hellforge',
        'Honey': 'Honey',
        'Honey Dispenser': 'Honey_Dispenser',
        'Ice Machine': 'Ice_Machine',
        'Imbuing Station': 'Imbuing_Station',
        'Pre-Hardmode_Anvil': 'Pre-Hardmode_Anvil',
        'Keg': 'Keg',
        'Lava': 'Lava',
        'Lihzahrd Furnace': 'Lihzahrd_Furnace',
        'Living Loom': 'Living_Loom',
        'Loom': 'Loom',
        'Meat Grinder': 'Meat_Grinder',
        'Hardmode_Anvil': 'Hardmode_Anvil',
        'Alchemy': 'Placed_Bottle',
        'Sawmill': 'Sawmill',
        'Sky Mill': 'Sky_Mill',
        'Solidifier': 'Solidifier',
        'Steampunk Boiler': 'Steampunk_Boiler',
        'Table Chair': 'Table',
        "Tinkerer's Workshop": "Tinkerer's_Workshop",
        'Water': 'Water',
        'Work Bench': 'Work_Bench',
       }

def refresh_api_data():
    errors = []
    recipes = get_recipes()
    item_list = get_item_list(recipes)
    for item in item_list:
        r = post_item_to_api(item)
        if r.status_code != 200 and r.status_code != 201:
            errors.append(r)
    for recipe in recipes:
        r = post_recipe_to_api(recipe)
        if r.status_code != 200 and r.status_code != 201:
            errors.append(r)
    return errors

def update_recipes():
    errors = []
    recipes = get_recipes()
    for recipe in recipes:
        r = post_recipe_to_api(recipe)
        if r.status_code != 200 and r.status_code != 201:
            errors.append(r)
    return errors

def get_recipes():
    recipes = []
    name_check = []
    for station in URLS:
        actionable_url = 'http://terraria.gamepedia.com/Recipes/' + URLS[station]
        print('Getting from ' + actionable_url)
        rows = grab_data(actionable_url)
        for row in rows:
            obj = serializer(row, station)
            if obj.created not in name_check:
                name_check.append(obj.created)
                recipes.append(obj)
    return recipes


def get_item_list(recipes):
    dicts = []
    items = get_all_items(recipes)
    count = 0
    for item in items:
        as_dict = {}
        as_dict['name'] = item
        as_dict['image'] = item_image(item)
        dicts.append(as_dict)
        if count % 10 == 0:
            print(count)
        count += 1

    return dicts

def recipes_list_to_csv(recipes):
    csv_vals = [recipe.format_csv() for recipe in recipes]
    CSVstuff.write_list(csv_vals, filename='recipes')


def grab_data(url):
    elements = sc.get_soup(url).find_all()
    query = SoupQuery('table')
    query.has_content('Result')
    query.has_content('Ingredients')

    found = []
    for element in elements:
        if sc.get_query(element, query):
            for item in row_format(element):
                if len(item) < 15:
                    found.append(item)

    cleaned = []
    for row in found:
        clean = cleaners.clean_extra_vals(row)
        clean = cleaners.list_filter(clean, [')', '('])
        if 'v' not in clean:
            cleaned.append(clean)

    return cleaned

def get_all_items(recipes):
    items = []
    for recipe in recipes:
        if r'^(' + recipe.created['Item'] + ')$' not in items:
            items.append(recipe.created['Item'])
        for ingredient in recipe.ingredients:
            if ingredient not in items:
                items.append(ingredient)
        if recipe.crafting_station not in items:
            items.append(recipe.crafting_station)
    return items

def item_image(item_name):
    url = 'http://terraria.gamepedia.com/File:' + item_name.replace(' ', '_') + '.png'
    soup = sc.get_soup(url)
    tag = soup.find('a', title=item_name + '.png')
    if tag != None:
        return tag['href']
    return 'no image'

def image_csv_to_dict(csvfile):
    list_dicts = []
    rows = CSVstuff.read_rows(csvfile)
    for row in rows:
        dicti = {}
        dicti['name'] = row[0]
        dicti['image'] = row[1]
        list_dicts.append(dicti)
    return list_dicts

def post_recipe_to_api(recipe):
    as_dict = recipe.format_dict()
    url = 'http://127.0.0.1:8000/manager/recipe/add/'
    data = json.dumps(as_dict)
    headers = {'Authorization': 'Token 1ea7ec39a27be022a048ffde1dd4ed7d7ebb4e47', 'Content-Type':'application/json'}
    r = requests.post(url, headers=headers, data=data)
    return r

def post_item_to_api(dictionary):
    url = 'http://127.0.0.1:8000/manager/item/add/'
    data = json.dumps(dictionary)
    headers = {'Authorization': 'Token 1ea7ec39a27be022a048ffde1dd4ed7d7ebb4e47', 'Content-Type':'application/json'}
    r = requests.post(url, headers=headers, data=data)
    return r
