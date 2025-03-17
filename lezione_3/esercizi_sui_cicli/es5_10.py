current_users: list[str] = ["Grax", "Zeb89", "Gabbodsqured", "Ciccogamer89", "Pantellas"]
new_users: list[str] = ["grax", "Me contro te", "Vanoss", "Pantellas", "Anima"]

for user in new_users:
    if user in current_users:
        print(f"{user} non e valido, nome gia inserito")
        