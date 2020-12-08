import os
import json

def read_tokens():
    try:
        file = open(".tokens.json", "r")
        tokens = file.read()
        return json.loads(tokens)
    except:
        raise print("Something went wrong...")