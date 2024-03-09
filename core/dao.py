import json


def get_Categories():
    with open("data/categories.json", encoding="utf-8") as f:
        return json.load(f)


def get_Products(cate=None, kw=None):
    with open("data/products.json", encoding="utf-8") as f:
        data = json.load(f)

        if cate:
            data = [p for p in data if p['category'] == int(cate)]

        if kw:
            data = [p for p in data if p['name'].find(kw) > 0]
        return data
