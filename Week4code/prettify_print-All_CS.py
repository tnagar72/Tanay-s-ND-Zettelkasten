import json
import traceback


def prettify_json(json_str):
    try:
        json_dict = json.loads(json_str)
        return json_dict
    except json.JSONDecodeError:
        raise Exception("Invalid JSON format")
    
def print_eachQ(json_dict: dict, counter: int):
    for mturk in json_dict['mturk']:
        print(mturk)
    print()

with open("/Users/tanaynagar/Downloads/All-CS/All-CS.json", "r") as file:
    json_list = json.load(file)

counter = 1

for json_obj in json_list:
    try:
        prettified_json = prettify_json(json.dumps(json_obj))
        print_eachQ(prettified_json, counter)
        counter += 1
    except Exception as e:
        print(f"Error occurred: {e}")
        traceback.print_exc()