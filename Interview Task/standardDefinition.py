import json

def standard():
    with open('standard_definition.json') as f:
        data = json.load(f)
    return data

