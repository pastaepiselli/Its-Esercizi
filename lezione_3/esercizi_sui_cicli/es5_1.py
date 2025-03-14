pizza: str = "Margherita"

print("Is pizza == Crostino? I predict False")
print(pizza == "Crostino")

print("Is pizza == Margherita? I predict True")
print(pizza == "Margherita")

n: int = 3
print("Is n != 6? I predict True")
print(n != 6)

print("Is n > 9? I predict False")
print(n > 9)

nome: str = "Popa"
print("Is nome == Popa? I predict True")
print(nome == "Popa")

print("Is nome == Pier? I predict False")
print(nome == "Pier")

n: int = 9
print("Is 9 == 0? I predict False")
print(9 == 0)

print("Is 9 == 9? I predict True")
print(9 == 0)

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# esercizio 5-2

parola: str = "Nicholas"
print(parola == "Nicholas")
print(parola == "nicholas")

print(parola.lower() == "Nicholas")
print(parola.lower() == "nicholas") # True perche forzata in minuscolo 

m: int = 5
p: int = 9
print(m > 6)
print(m == 5)
print(m >= 4)
print(m > 7 and p < 19)
print(m > 7 or p < 19)

ls: list[int] = [4,7,9,3]
print(8 in ls)
print(4 not in ls)


