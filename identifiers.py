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

    parent_tables = []
    if len(identifiers):
        for identifier in identifiers:
            parent_table = identifier.find_parent('table')
            title = parent_table.find_parent("table").find_previous_sibling("h3")
            if title != None:
                title_text = title.get_text()
                if 'Used in' not in title_text:
                    parent_tables.append(parent_table)
            elif title is None:
                parent_tables.append(parent_table)
        return parent_tables
    else:
        return False
