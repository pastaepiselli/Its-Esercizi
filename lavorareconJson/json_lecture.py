import json

path: str= 'db.json'
with open(path, mode='r', encoding=encoding) as file:
    config: dict = json.load(file)