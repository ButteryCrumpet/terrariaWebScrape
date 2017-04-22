import Scraper as sc
from query import SoupQuery
from formatter import row_format, serializer
import cleaners
import CSVstuff

URLS = {'Ancient Manipulator': 'Ancient_Manipulator',
        'Adamantite Forge / Titanium Forge': 'Hardmode_Forges',
        'Autohammer': 'Autohammer',
        'Bookcase': 'Autohammer',
        'Bone Welder': 'Bone_Welder',
        'Blend-O-Matic': 'Blend-O-Matic',
        'By Hand': 'By_Hand',
        'Campfire': 'Campfire',
        'Cooking Pot / Cauldron': 'Cooking_Pot',
        'Crystal Ball': 'Crystal_Ball',
        'Demon Altar / Crimson Altar': 'Altar',
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
        'Iron Anvil / Lead Anvil': 'Pre-Hardmode_Anvils',
        'Keg': 'Keg',
        'Lava': 'Lava',
        'Lihzahrd Furnace': 'Lihzahrd_Furnace',
        'Living Loom': 'Living_Loom',
        'Loom': 'Loom',
        'Meat Grinder': 'Meat_Grinder',
        'Mythril Anvil / Orichalcum Anvil': 'Hardmode_Anvils',
        'Placed Bottle / Alchemy Station /   Alchemy Table': 'Placed_Bottle',
        'Sawmill': 'Sawmill',
        'Sky Mill': 'Sky_Mill',
        'Solidifier': 'Solidifier',
        'Steampunk Boiler': 'Steampunk_Boiler',
        'Table + Chair': 'Table',
        "Tinkerer's Workshop": "Tinkerer's_Workshop",
        'Water': 'Water',
        'Work Bench': 'Work_Bench',
       }

def Run():
    recipes = []
    name_check = []
    for station in URLS:
        actionable_url = 'http://terraria.gamepedia.com/Recipes/' + URLS[station]
        print('Getting ' + station + ' recipes')
        rows = grab_data(actionable_url)
        for row in rows:
            obj = serializer(row, station)
            if obj.created not in name_check:
                name_check.append(obj.created)
                recipes.append(obj)
    return recipes


def ItemList(recipes):
    item_list = []
    items = get_all_items(recipes)
    count = 0
    for item in items:
        image = item_image(item)
        item_list.append((item, image,))
        if count % 10 == 0:
            print(count)
        count+=1

    return item_list

def recipes_list_to_csv(recipes):
    csv_vals = [recipe.format_csv() for recipe in recipes]
    CSVstuff.write_list(csv_vals, filename='cmon')


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
        if recipe.created['Item'] not in items:
            items.append(recipe.created['Item'])
        for ingredient in recipe.ingredients:
            if ingredient not in items:
                items.append(ingredient)
    return items

def item_image(item_name):
    url = 'http://terraria.gamepedia.com/File:' + item_name.replace(' ', '_') + '.png'
    soup = sc.get_soup(url)
    a = soup.find('a', title=item_name + '.png')
    if a != None:
        return a['href']
    return 'no image'
