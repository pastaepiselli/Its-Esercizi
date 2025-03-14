# giorno: int = int(input("Inserire giorno: "))
# mese: str = str(input("Inserire mese: ")).lower()

# data: tuple[int, str] = (giorno, mese)

# match data:
#     case (1, "gennaio"):
#         print(f" Il {giorno} / {mese} e Capodanno")
#     case (14, "febbraio"):
#         print(f"San Valentino")
#     case (2, "giugno"):
#         print("Festa della repubblica Italiana")
#     case (15, "agosto"):
#         print("Ferragosto")
#     case (31, "ottobre"):
#         print("Halloween")
#     case (25, "dicembre"):
#         print("Natale")
#     case _:
#         print("Nessuna festività importante in questa data.")


giorno: int = int(input("Inserire giorno: "))
mese: int = int(input("Inserire mese: "))

giorni_per_mese: list[int] = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

data: tuple[int, int] = (giorno, mese)

match data:
    case (1, 1):
        print(f" Il {giorno} / {mese} e Capodanno")
    case (14, 2):
        print(f"Il {giorno}/{mese} San Valentino")
    case (2, 6):
        print(f"Il {giorno}/{mese} Festa della repubblica Italiana")
    case (15, 8):
        print(f"Il {giorno}/{mese} e Ferragosto")
    case (31, 10):
        print(f"Il {giorno}/{mese} e Halloween")
    case (25, 12):
        print(f"Il {giorno}/{mese} e Natale")
    case (g, b) if mese > 12 or giorno > giorni_per_mese[mese - 1]:
        print(f"Il {giorno}/{mese} non esiste")
    case _:
        print(f"Nessuna festività importante il {giorno}/{mese} ")



