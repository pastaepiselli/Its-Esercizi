from typing import Callable
even_or_odd:Callable[[int], str]= lambda x: "Pari" if x % 2 == 0 else 'Dispari'

print(even_or_odd(3))
print(even_or_odd(4))