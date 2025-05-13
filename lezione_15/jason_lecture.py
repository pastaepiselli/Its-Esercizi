import json

PATH: str = 'lezione_15/aaa.json'
mode: str = 'r'
encoding: str = 'utf-8'

config = None

# def connected(host, port):

#     print(f'Connected to {host}: port = {port}')

# with open(PATH, mode=mode, encoding=encoding) as file:
#     # file sarebbe la path, il nostro file wrappato

#     config: dict = json.load(file)

# print(config['tasks'])

# come modificare json

# config["AGGIUNTA"] = "NUOVO"


# # ora devo salvare 

# with open(PATH, mode='w') as file:

#     json.dump(config, file, indent=4)



new_config: dict = {'GRGFLV...': {'name': 'Flavio', 'last_name': 'Giorgi', 'age': 30}}


with open(PATH, mode='w') as file:

    json.dump(new_config, file, indent=4)