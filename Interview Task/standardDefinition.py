import json
from decouple import config


def standard():

    with open(config('DEFINITION')) as f:
        data = json.load(f)
    return data

