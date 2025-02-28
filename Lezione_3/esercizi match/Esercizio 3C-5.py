from typing import Any

credenziali: dict[str, Any] = {}

nome: str = str(input("Digitare nome dell'utente: "))
credenziali["Nome"] = nome

ruolo: str = str(input("Digitare ruolo dell'utente: "))
credenziali["Ruolo"] = ruolo.lower()

eta: int = int(input("Digitare eta dell'utente: "))
credenziali["Eta"] = eta

match credenziali:
    case credenziali if credenziali["Ruolo"] == "admin":
        print("Accesso completo a tutte le funzionalita")
    case credenziali if credenziali["Ruolo"] == "moderatore":
        print(f"Salve {credenziali['Nome']}, Può gestire i contenuti ma non modificare le impostazioni.")
    case credenziali if credenziali["Ruolo"] == "utente" and credenziali["Eta"] >= 18:
        print("Accesso standard a tutti i servizi")
    case credenziali if credenziali["Ruolo"] == "utente" and credenziali["Eta"] < 18:
        print("Accesso limitato! Alcune funzionalita sono limitate!")
    case credenziali if credenziali["Ruolo"] == "ospite":
        print("Accesso ristretto! Solo visualizzazione di contenuti")
    
    

