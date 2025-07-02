from persona import Persona
from mytipes import *
from Posizione_militare import PosizioneMilitare
from datetime import datetime, date
from typing import Self


# Creo posizione militare
pos_mil = PosizioneMilitare("Soldato")
nascita_mario = date(1984, 4, 6)
nascita_maria = date(1998, 3, 8)

# Creo un uomo
uomo = Persona(
    nome="Mario",
    cognome="Rossi",
    cf=CodiceFiscale("RSSMRA80A01H501Z"),
    nascita=nascita_mario,
    genere=Genere.uomo,
    posizione_militare=pos_mil
)

print("--- UOMO ---")
print(f"Nome: {uomo.nome()}")
print(f"Cognome: {uomo.cognome()}")
print(f"CF: {uomo.cf()}")
print(f"Nascita: {uomo.nascita()}")
print(f"Genere: {uomo.genere()}")
print(f"Posizione militare: {uomo.posizione_militare()}")

# Creo una donna
donna = Persona(
    nome="Maria",
    cognome="Bianchi",
    cf=CodiceFiscale("BNCMRA85E41H501G"),
    nascita=nascita_maria,
    genere=Genere.donna
)

print("\n--- DONNA ---")
print(f"Nome: {donna.nome()}")
print(f"Cognome: {donna.cognome()}")
print(f"CF: {donna.cf()}")
print(f"Nascita: {donna.nascita()}")
print(f"Genere: {donna.genere()}")

# Test maternità donna
print("Maternità iniziale:", donna.maternita())
donna.add_maternita()
print("Maternità dopo add:", donna.maternita())

# Test errore maternità uomo
try:
    print("Maternità uomo:", uomo.maternita())
except ValueError as e:
    print("Errore previsto su maternità uomo:", e)

# Test cambio genere con posizione militare
try:
    donna.set_genere(Genere.uomo, pos_mil)
    print("Cambio genere donna->uomo completato")
    print(f"Nuovo genere: {donna.genere()}")
    print(f"Nuova posizione militare: {donna.posizione_militare()}")
except Exception as e:
    print("Errore cambio genere donna->uomo:", e)
