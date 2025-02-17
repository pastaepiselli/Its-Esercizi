# esercizio 2-3

# name: str = "Lorenzo"
# print(f"Hello {name}, would you like to learn some Python today?")

# esercizio 2-4

# name: str = "Lorenzo"
# print(name.lower())
# print(name.upper())
# print(name.title())

# esercizio 2-5

# print("Jokerone once said, \" Boom baby bye, boom baby bye Boom baby, ho aspettato 'sto tempo più che maiPrenditi qualcosa solo se poi ci tienic finita la storia e sempre uguale\"")

# esercizio 2-6

# quote: str = "\"Mi levo la maglia per l'ultima volta, la piego per bene anche se non sono pronto a dire basta e forse non lo sarò mai.\""
# name: str = "Francesco Totti"

# print(f"{name} once said, {quote}")

# esercizio 3-1

# names: list = ["Luca", "Pier", "Alessandro"]
# print(names[0])
# print(names[1])
# print(names[2])

# # esercizio 3-2

# print(f"Ciao {names[0]}, come stai?")
# print(f"Ao {names[1]}, che dici?")
# print(f"Ciao {names[2]}, hai mangiato?")

# # esercizio 3-3

# trasporti: list = ["Nissan Micra K11", "Honda", "Lancia Y"]
# print(f"Guido una {trasporti[0]} e swaggo")
# print(f"Mi piacerebbe guidare una {trasporti[1]}")
# print(f"Mia madre guida una {trasporti[2]}")

# esercizio 3-4

invitati: list = ["Erald", "Nosferatu", "Iannone"]
print(f"{invitati[0]} vorresti venire a cena a trastevere?")
print(f"Bello {invitati[1]}, esci dal quel castello e vieni a cena a trast?")
print(f"Come te la passi {invitati[2]}, ci stai per una cena a trast?")

print("Erald non puo stasera.")

# esercizio 3-5

invitati[0] = "Simba la rue" # viene sostituito erald 

print(f"{invitati[0]} stiamo a trast a cena stase vieni?")
print(f"Bello {invitati[1]}, esci dal quel castello e vieni a cena a trast?")
print(f"Come te la passi {invitati[2]}, ci stai per una cena a trast?")


# esercizio 3-6

print("Rega ho trovato un tavolo piu grande!")

# inserisco i nuovi invitati

invitati.insert(0, "Alessandro Popa") 
invitati.insert(1, "Francesco Totti") 
invitati.append("Papa V")

print(f"{invitati[0]} stiamo a trast a cena stase vieni?")
print(f"Bello {invitati[1]}, esci dal quel castello e vieni a cena a trast?")
print(f"Come te la passi {invitati[2]}, ci stai per una cena a trast?")
print(f"Ciao {invitati[0]}, verresti a cena a trastevere?")
print(f" Buonasera signor {invitati[1]}, e disponibile per una cena a trastevere?")
print(f"{invitati[5]},, stai a trastevere per una cenetta?")

print("Posso invita solo 2 persone ")

print(invitati)


print(f"Scusami  {invitati[0]}, il tavolo non si libera in tempo.")
invitati.pop(0)

print(f"Scusami  {invitati[0]}, il tavolo non si libera in tempo.")
invitati.pop(0)

print(f"Scusami  {invitati[0]}, il tavolo non si libera in tempo.")
invitati.pop(0)

print(f"Scusami  {invitati[0]}, il tavolo non si libera in tempo.")
invitati.pop(0)

print(f"{invitati[0]} sei ancora invitato a cena.")
print(f"{invitati[1]} sei ancora invitato a cena.")

del invitati[0]
del invitati[0]

print(invitati)





 










