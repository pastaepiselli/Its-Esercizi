

# esercizio 13 

# auto_NS = int(input("Inserire macchine che vegono da NS: "))
# auto_EO = int(input("Inserie macchine che vengono da EO: "))
# soglia = int(input("Inserire soglia: "))
# tempo_priorita = int(input("Inserire tempo priorita: "))
# tempo: int = 100
# if auto_NS > soglia:
#     if auto_EO > soglia:
#          tempo_NS = 50
#          tempo_EO = 50
#     else:
#         tempo_NS = tempo_priorita
#         tempo_EO = tempo - tempo_priorita
# else:
#     if auto_EO > soglia:
#         tempo_EO = tempo_priorita
#         tempo_NS = tempo - tempo_priorita
#     else:
#         veicoli_tot = auto_NS + auto_EO
#         tempo_NS = auto_NS / veicoli_tot
#         tempo_EO = tempo - tempo_NS
# print(f"Il tempo assegnato alle auto NS è {tempo_NS} e il tempo assegnato alle auto EO è {tempo_EO}.")

#esercizio 14

# corso = str(input("Quale corso vorresti frequentare?: "))
# posti: int = 100
# opzione: str = None
# while opzione != "esci":
#     opzione = str(input("Inserire opzione: "))
#     if opzione.title() == "Iscriviti":
#         if posti > 0:
#             posti -= 1
#             print("Sei iscritto!!")
#         else:
#             print("Non ci sono posti disponibili")
#     elif opzione == "annulla":
#         if posti < 100:
#             print("Hai annullato l'iscrizione...")
#             posti +=1
#         else:
#             print("tutti i posti sono gia disponibili")
#     elif opzione == "visualizza":
#         print(f"I posti disponibili sono {posti} e i posti rimasti sono {100 - posti}")
#     else:
#         print("Inserire un opzione valida!")

# esercizio 15


# tutor: int = 2
# attesa: int = 0
# status: bool = True
# while status:
#     studente = str(input("Inserire studente: "))
#     if tutor > 0:
#         tutor -= 1
#         print("Tutor assegnato correttamente!")
#     else:
#         attesa += 1
#         print("Assegnato a lista di attesa")
#     if tutor == 0 and attesa == 3:
#         status: bool = False
# print("Posti esauriti!")

# esercizio 16

# sum: int = 0
# n = int(input("Inserire numero: "))
# if n % 1 == 0 and n > 0:
#     i = 1 
#     sum: int = 0
#     for i in range(1, n + 1):
#         sum = sum + i**2
# else:
#     print("Inserire un numedo valido!")
# print(sum)

# esercizio 17

# sum: int = 0
# i: int = 1
# x = int(input("Inserire numero positivo: "))
# if x > 0:
#     while i < 10:
#         n = int(input("Inserire numero: "))
#         if x % 2 == 0:
#             if n > x / 2:
#                 sum += n
#         else:
#             if n < x:
#                 sum += n
#         i += 1
#     print(sum)
# else:
#     print("Io ti avevo avvisato!")

# esercizio 18

