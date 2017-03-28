#!usr/bin/python3

import tws, csvwrite
import specificParsers as specP
import identifiers as ids

BASE_URLS = ['https://terraria.gamepedia.com/List_of_items/a-d',
             'https://terraria.gamepedia.com/List_of_items/e-h',
             'https://terraria.gamepedia.com/List_of_items/i-l',
             'https://terraria.gamepedia.com/List_of_items/m-p',
             'https://terraria.gamepedia.com/List_of_items/q-t',
             'https://terraria.gamepedia.com/List_of_items/u-z']
ALL_URLS = []
TITLES = []
DATA = []

for url in BASE_URLS:
    soup = tws.get_soup(url)
    tables = tws.get_tables(soup)
    new_urls = tws.get_urls(tables)
    for new_url in new_urls:
        if new_url not in ALL_URLS:
            ALL_URLS.append(new_url)

print(len(ALL_URLS))
count = 0

for url in ALL_URLS:
    actionable_url = 'https://terraria.gamepedia.com' + url
    soup = tws.get_soup(actionable_url)
    title = specP.get_page_title(soup)
    tables = ids.identify_craftbox(soup)
    if tables and title not in TITLES:
        data = specP.get_craftbox_datas(tables)
        for row in data:
            DATA.append(row)
        TITLES.append(title)
        count += 1

    tables = ids.identify_multicraftbox(soup)
    if tables and title not in TITLES:
        data = specP.get_multicraft_table_data(tables)
        csvwrite.write_rows_to_csv(data, title)
        count += 1

    print(count)



csvwrite.write_rows_to_csv(DATA, 'recipes')
