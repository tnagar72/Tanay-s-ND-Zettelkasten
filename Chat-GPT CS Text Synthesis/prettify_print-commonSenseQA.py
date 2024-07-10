import json
import traceback


def prettify_json(json_str):
    try:
        json_dict = json.loads(json_str)
        return json_dict
    except json.JSONDecodeError:
        raise Exception("Invalid JSON format")
    
def print_eachQ(json_dict: dict, counter: int):
    print(str.format("Question {}: ", counter) + json_dict["question"]['stem'])
    print(str.format("ID: {}", json_dict['id']))
    print()
    for label in json_dict['question']["choices"]:
        print(label['label'] + ": ", label['text'])
    print()

with open("/Users/tanaynagar/Desktop/Tanay's ND Zettelkasten/Chat-GPT CS Text Synthesis/train_rand_split.jsonl", "r") as file:
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