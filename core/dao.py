import json


def get_Categories():
    with open("data/categories.json", encoding="utf-8") as f:
        return json.load(f)
