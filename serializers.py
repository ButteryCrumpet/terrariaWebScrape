#!/usr/bin/python3

import csv
from itemClasses import Recipe

JAMA_WORDS = ['Placed  Bottle', 'Alchemy  Table', ' or ']
JAMA_ID = 'Internal Item ID:'
JAMA_SELL = 'Sell:'

def craftbox_csv_to_object(csv_file):
    recipes = []
    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            amount = row.pop(len(row)-1)
            item = row.pop(len(row)-1)
            station = row.pop(0)
            ingredients = {}
            count = 0
            for i in row:
                if is_clean_string(i, JAMA_WORDS):
                    if count == 0 or count % 2 == 0:
                        ingredients[i] = row[count+1]
                count += 1
            recipe = Recipe(item, amount, ingredients, station)
            recipes.append(recipe)
    return recipes

def multi_csv_to_object(csv_file):
    recipes = []
    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        current_workstation = ''
        for row in reader:
            if len(row) >= 5:
                name_amount = get_mixedup_values(row.pop(1))
                item = name_amount[1]
                amount = name_amount[0]
                if row[3] != '':
                    current_workstation = row.pop(3)
                ingredients = {}
                for i in row:
                    if is_clean_string(i, JAMA_WORDS) and i != '':
                        i_name_amount = get_mixedup_values(i)
                        ingredients[i_name_amount[1]] = i_name_amount[0]
                recipe = Recipe(item, amount, ingredients, current_workstation)
                recipes.append(recipe)
    return recipes



def is_clean_string(string_clean, ng_words):
    for item in ng_words:
        if item in string_clean:
            return False
    return True

def destroy_substring(string, substring):
    if substring in string:
        return string.split(substring,1)[0]
    else:
        return string

def get_bracketed_value(string):
    step1 = string.split('(',1)[1]
    step2 = step1.split(')',1)[0]
    return step2

def get_mixedup_values(string):
    values = []
    name = destroy_substring(string, JAMA_ID)
    name = destroy_substring(name, JAMA_SELL)
    if '(' in name:
        amount = get_bracketed_value(name)
        name = destroy_substring(name, '(')
    else:
        amount = 1
    values.append(amount)
    values.append(name.replace(u'\xa0', u''))
    return values
        