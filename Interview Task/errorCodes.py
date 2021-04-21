import json


def error():
    with open('error_codes.json') as f:
        error = json.load(f)
    return error
