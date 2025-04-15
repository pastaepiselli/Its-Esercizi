from typing import Callable
studenti: list[tuple] = [('Luca', 21), ('Anna', 19), ('Marco', 22)]
sorted_on_age: list[tuple] = sorted(studenti, key=lambda studenti: studenti[1])
print(sorted_on_age)