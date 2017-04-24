import requests
import json

import Scraper as sc
from query import SoupQuery
from formatter import row_format, serializer
import cleaners

def test1():
    soup = sc.get_soup('http://terraria.gamepedia.com/Shroomite_Bar')
    tables = soup.find_all(class_='craftbox')
    for table in tables:
        data = craftbox_formatter(table)
        return(data)

def test2():
    soup = sc.get_soup('http://terraria.gamepedia.com/Chests')
    tables = soup.find('table', class_='inner')
    rows = tables.find_all('tr')
    for row in rows:
        content = sc.get_element_content(row, stripped=True)
        return(content)

def test3(url):
    elements = sc.get_soup(url).find_all()
    query = SoupQuery('table')
    query.has_content('Result')
    query.has_content('Ingredients')
    query.has_content('Crafting Station')
    query.has_attribute('class', 'inner')
    #parent = SoupQuery('table')
    #query.has_parent(parent)

    found = []
    for element in elements:
        if sc.get_query(element, query):
            if sc.multibox_test(element):
                for item in get_row_data(element):
                    found.append(item)
    return found

def test4(url):
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

def test_serialize(rows):
    recipes = []
    for i in rows:
        obj = serializer(i, 'Hardmode Anvil')
        recipes.append(obj)

    return recipes
