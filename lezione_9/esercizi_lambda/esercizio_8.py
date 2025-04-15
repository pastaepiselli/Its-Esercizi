studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

list_order: list[dict] = sorted(studenti, key=lambda studenti: studenti['media'])
print(list_order)