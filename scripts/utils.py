import json

def dump_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    
def load_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data