import json
import traceback


def prettify_json(json_str):
    try:
        json_dict = json.loads(json_str)
        return json_dict
    except json.JSONDecodeError:
        raise Exception("Invalid JSON format")
    
def print_eachQ(json_dict: dict):
    print("Question:" + json_dict["question"])
    for label in json_dict['question']["choices"]:
        print(label['label'] + ": ", label['text'])

with open("Logic.json", "r") as file:
    json_list = json.load(file)
    
for json_obj in json_list:
    try:
        prettified_json = prettify_json(json.dumps(json_obj))
        print(prettified_json)
        print(type(prettified_json))
        print(type(prettified_json["question"]))
        print(type(prettified_json["question"]["choices"]))
        print(type(prettified_json["choices"][0]))
        print_eachQ(prettified_json)
    except Exception as e:
        print(f"Error occurred: {e}")
        traceback.print_exc()