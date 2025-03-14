pizza: list[str] = ["Margherita", "Pistacchiosa", "Bianca"]
pizza.append("Boscaiola")
friend_pizza: list[str] = ["Margherita", "Pistacchiosa", "Peperoni"]
friend_pizza.append("Crostino")

print("My favourite pizzas are:")
for i in pizza:
    print(i)

print("My friend's favourite pizzas are:")

for i in friend_pizza:
    print(i)