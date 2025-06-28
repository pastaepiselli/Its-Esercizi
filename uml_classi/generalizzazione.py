# from abc import ABC, abstractmethod

# class Persona(ABC):

#     @abstractmethod
#     def __init__(self, nome: str) -> None:
#         if len(nome) > 2:
#             raise ValueError('Il nome deve avere almeno 2 caratteri')

#         # mettele la prima lettera uppercase
#         self._nome = nome.capitalize()


# class Studente(Persona):

#     _matricola: int

#     # studente non e una classe astratta
#     def __init__(self, nome: str, matricola: int) -> None:

#         # il metodo init che eredito con il super e un metodo astratto, da solo non puo essere invocato ma per
#         # creare altre classi OK!
#         super().__init__(nome)
#         self._matricola = matricola


def controllo_classe()

class Corso:
    
    def __init__(self): 
        pass



class Persona:

    def __init__(self, nome: str, is_studente: bool = False, matricola: int = None, corso: Corso = None):
        pass
        
    def diventa_studente(matricola: int, corso: Corso) -> None:

        # is_studente non corrisponde al fatto che ho la matricola allora errore, se studente F e la matricola non e vuoto allora il valore e uguale
        if is_studente != (matricola is not None) \
             or is_studente != (corso_iscritto is not None):
