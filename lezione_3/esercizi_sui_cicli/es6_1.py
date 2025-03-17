from typing import Any

persona: list[str, Any] = {"first_name": "Alessadro", "last_name": "Popa", "age": 20, "city": "Torvajanica"}

# for key, values in persona.items():
#     print(values)

for key in persona:
    print(key)
    print(persona[key])