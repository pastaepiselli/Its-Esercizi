from typing import Any

popa: list[str, Any] = {"first_name": "Alessadro", "last_name": "Popa", "age": 20, "city": "Torvajanica"}

marco: list[str, Any] = {"first_name": "Marco", "last_name": "Pierleoni", "age": 27, "city": "Esquilino"}

pier: list[str, Any] = {"first_name": "Pier", "last_name": "Ramillano", "age": 20, "city": "torrino"}

people: list[dict] = [popa, marco, pier]

for n in people:
    print(n)