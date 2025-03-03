cities: dict[str, dict] = {
    "Roma": {"Popolazione": "2,76 milioni", "Nazione": "Italia"  , "Fatto": "Virginia raggi"},
    "Vienna": {"Popolazione": "2 milioni", "Nazione": "Austria", "Fatto": "Palle di mozart"},
    "Bruxelles": {"Popolazione": "183 mila", "Nazione": "Belgio", "Fatto": "Isis"}}

for key, values in cities.items():
    print(values)