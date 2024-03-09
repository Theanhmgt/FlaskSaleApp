import json


def get_Categories():
    with open("data/categories.json", encoding="utf-8") as f:
        return json.load(f)


def get_Products():
    with open("data/products.json", encoding="utf-8") as f:
        return json.load(f)
