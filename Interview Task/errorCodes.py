import json
from decouple import config


def error():

    with open(config('ERROR')) as f:
        error = json.load(f)
    return error
