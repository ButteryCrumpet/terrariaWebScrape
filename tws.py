#!/usr/bin/python3
#terraria web scraper

import requests, bs4, csv

def get_soup(url):
    r = requests.get(url)
    s = bs4.BeautifulSoup(r.text, 'html.parser')
    return s

def get_tables(soup):
    tables = soup.select('table')
    return tables

def get_table_by_class(soup, t_class):
    tables = soup.select('table[class="{}"]'.format(t_class))
    return tables

def get_rows(table):
    rows = table.select('tr')
    return rows

def get_row_data(row):
    cells = row.select('td')
    data = []
    for cell in cells:
        data.append(cell.get_text().replace("\n", ""))
    return data

def get_urls(soup_section):
    urls = []
    for item in soup_section:
        links = item.find_all('a', href=True)
        for a in links:
            if a not in urls:
                urls.append(a['href'])
    return urls
