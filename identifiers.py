#!/usr/bin/python3

import tws, bs4

def identify_craftbox(soup):
    tables = tws.get_table_by_class(soup, 'craftbox')
    if len(tables):
        return tables
    else:
        return False

def identify_multicraftbox(soup):
    identifiers = soup.find_all("th", text="Ingredients")
    if not len(identifiers):
        identifiers = soup.find_all("a", title="Crafting Station")

    parent_tables = []
    if len(identifiers):
        for identifier in identifiers:
            parent_table = identifier.find_parent('table')
            parent_tables.append(parent_table)
        return parent_tables
    else:
        return False
