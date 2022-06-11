import json
import difflib
import os

ROOT_DIR = os.getcwd()
DATA_DIR = os.path.join(ROOT_DIR, "logs/data/recipes.json")

def load_json(file):
  with open(file) as json_file:
    data = json.load(json_file)
  return data

def get_title_list(recipe):
    title_list = []
    for i in range(0, len(recipe)):
        title_list.append("{} {}".format(recipe['{}'.format(i)]['title'].lower(), recipe['{}'.format(i)]['id']))
    return title_list

def get_recommendation(food, title_list):
    find_close_match = difflib.get_close_matches(food, title_list, n=10, cutoff=0.4)
    list_id = []
    for item in find_close_match:
        word = item.split()
        list_id.append(word[-1])
    return list_id

def get_result(food):
    result = []
    recipe = load_json(DATA_DIR)
    title_list = get_title_list(recipe)
    recommendation = get_recommendation(food, title_list)

    for item in recommendation:
        for i in range(0, len(recipe)):
            if str(recipe["{}".format(i)]['id']) == item:
                result.append(recipe["{}".format(i)])
    return result