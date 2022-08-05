import json

#<str> = json.dumps(<object>, ensure_ascil=True, indent = None)
#<object> = json.load(<str>)

#Read Object from JSON file

def read_json_file(filename):
    with open(filename, encoding = 'utf-8') as file:
        return json.load(file)

#Write Object to JSON file

def write_to_json_file(filename, an_object):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(an_object, file, ensure_ascii=False, indent=2)
