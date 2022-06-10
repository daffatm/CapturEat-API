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
        title_list.append(recipe['{}'.format(i)]['Title'].lower())
    return title_list

def get_recommendation(food, title_list):
    find_close_match = difflib.get_close_matches(food, title_list, n=10, cutoff=0.4)
    return find_close_match

def get_result(food):
    result = {}
    recipe = load_json(DATA_DIR)
    title_list = get_title_list(recipe)
    recommendation = get_recommendation(food, title_list)

    for item in recommendation:
        for i in range(0, len(recipe)):
            if recipe["{}".format(i)]['Title'].lower() == item:
                key = recipe["{}".format(i)]["Id"]
                if key not in result:
                    result[recipe["{}".format(i)]["Id"]] = recipe["{}".format(i)]
    return result