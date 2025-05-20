
def subtract(a: int, b: int) -> int: # con questa scrittura definisco che il risultato sara un intero 
    subraction = a - b
    return subraction
print(subtract(89, 46))

def greet(name:str) -> None:
    print(f"Hello {name}!")

greet("angela")

# quando ho un return con piu valori i valori vengono inseriti in una tupla

def operations(a: int, b: int) -> int:
    sum: int = a + b
    diff: int = a - b
    return sum, diff

valore_sum, valore_diff = operations(15, 7)
print(valore_diff)
print(valore_sum)

def coordi(x: int, y: int):
    return x, y
print(type(coordi))