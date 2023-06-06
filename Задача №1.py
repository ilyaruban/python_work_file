import json

with open('recipes.txt', 'r', encoding = 'UTF-8') as new_file:
    cook_book = {}
    for recipe_name in new_file:
        recipe_count = int(new_file.readline())
        recipe_list = []
        for n in range(recipe_count):
            ingridient_name, quantity, measure = new_file.readline().strip().split(' | ')
            recipe_list.append({
                'ingridient_name': ingridient_name, 'quantity': int(quantity), 'measure': measure
            })
        new_file.readline()
        cook_book[recipe_name.strip()] = recipe_list

    recipe = json.dumps(cook_book, ensure_ascii = False, indent = 2)
    print(recipe)