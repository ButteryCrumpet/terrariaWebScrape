#!/usr/bin/python3

import tws

def get_craftbox_datas(tables):
    data = []
    for table in tables:
        table_data = []
        rows = tws.get_rows(table)
        for row in rows:
            row_data = tws.get_row_data(row)
            for item in row_data:
                if item:
                    table_data.append(item)
        data.append(table_data)
    return data

def get_multicraft_table_data(tables):
    data = []
    for table in tables:
        rows = tws.get_rows(table)
        count = 0
        for row in rows:
            row_data = tws.get_row_data(row)
            if len(row_data) == 2:
                data[count-1] += row_data
            else:
                data.append(row_data)
                count += 1
    return data

def get_page_title(soup):
    title = soup.find('h1', id='firstHeading')
    return title.get_text()
