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

    def get_shop_list_by_dishes(dishes, person_count):
        person_dict = {}
        count = 0
        for n in dishes:
            person_dict_list = []
            if n in cook_book.keys():
                for i in cook_book[n]:
                    person_dict_list.append(i['ingridient_name'])
                for k in person_dict_list:
                    person_dict[k] = {'quantity': cook_book[n][count]['quantity']*person_count, 'measure': cook_book[n][count]['measure']}
                    count += 1
            count = 0
        recipe_person = json.dumps(person_dict, ensure_ascii=False, indent=2)
        return recipe_person

    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))