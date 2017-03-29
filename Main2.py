import serializers as slzr
import os

FILES = []
RECIPES = []

for file in os.listdir("CSVs"):
    if file.endswith(".csv"):
        filename = 'CSVs/' + file
        FILES.append(filename)

for file in FILES:
    recipes = slzr.multi_csv_to_object(file)
    for recipe in recipes:
        RECIPES.append(recipe)

print(RECIPES)