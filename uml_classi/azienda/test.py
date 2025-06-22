from beartype import beartype

from azienda.citta import Citta
from azienda.coinvolto import coinvolto
from azienda.progetto import Progetto
from custom_types import *
from dipartimento import Dipartimento
from impiegato import Impiegato
from datetime import date, timedelta

@beartype
def test():
    tel1: str = "3334445566"
    tel2: str = "3456789012"

    ind: Indirizzo = Indirizzo("Viale Cesare Pavese", "305f",
                               CAP("00144"))
    roma: Citta = Citta("Roma")
    dip1: Dipartimento = Dipartimento(nome="Acquisti",
                                      telefono=tel1,
                                      indirizzo=ind,
                                      citta=roma)
    print(dip1)
    dip2: Dipartimento = Dipartimento("Vendite", tel2, ind, roma)
    dip2.remove_indirizzo() # equivalente a dip2.set_indirizzo(None)
    dip2.add_telefono(tel1)
    print(dip2)
    alice: Impiegato = Impiegato(nome="Alice", cognome="Alessi",
                                 nascita=date.today()-timedelta(days=1),
                                 stipendio=RealGEZ(18000))

    bob: Impiegato = Impiegato(nome="Bob", cognome="Burnham",
                               nascita=date.today()-timedelta(days=2),
                               stipendio=RealGEZ(19000))
    print(alice)
    alice.set_nome("Alessia")
    print(alice)

    print(bob)


    pegaso: Progetto = Progetto("Pegaso", RealGEZ(25_000))
    prometeo: Progetto = Progetto("Prometeo", RealGEZ(75_000))
    phoenix: Progetto = Progetto("Phoenix", RealGEZ(24_000))
    # NO alice.add_progetto(pegaso, date.today())


    alice_in_pegaso: coinvolto._link = coinvolto.add(pegaso, alice, date.today())
    bob_in_pegaso: coinvolto._link =coinvolto.add(pegaso, bob, date.today())

    alice_in_prometeo: coinvolto._link =coinvolto.add(prometeo, alice, date.today())

    bob_in_phoenix: coinvolto._link =coinvolto.add(phoenix, bob, date.today())

    coinvolto.remove(alice_in_pegaso)
    try:
        coinvolto.remove(alice_in_pegaso)
    except KeyError as e:
        print(f"Ci siamo accorti del seguente errore:")
        print(f"\t ==> {e}")


if __name__ == "__main__":
    test()