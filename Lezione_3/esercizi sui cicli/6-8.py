pepi: dict[str, str] = {"Tipo di animale": "Gatto", "Padrone": "Lorenzo"}

milo: dict[str, str] = {"Tipo di animale": "Cane", "Padrone": "Tiziano"}

gnappa: dict[str, str] = {"Tipo di animale": "Tartaruga", "Padrone": "Gabriel"}

pets: list[dict] = [gnappa, milo, pepi]

for d in pets:
    print(d)