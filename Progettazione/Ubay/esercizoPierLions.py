from __future__ import annotations

class Film:
    __id:int
    __titolo:str
    def __init__(self, id:int, titolo:str):
        self.setId(id)
        self.setTitle(titolo)
    
    
    def setId(self, id: int)-> bool:
        if isinstance(id, int):
            self.__id = id 
            return True
        else: 
            self.__id = None
            raise ValueError('Errore! L\'ID inserito deve essere un numero')
    
    def setTitle(self, titolo)-> bool:
        if isinstance(titolo, str):
            self.__titolo = titolo
            return True
        else: 
            self.__titolo = None
            raise ValueError('Errore! Il titolo inserito deve essere una stringa')
    
    
    def ID(self)->int:
        return self.__id
    
    def Title(self)->str:
        return self.__titolo
    
    def isEqual(self, otherFilm: Film)-> bool:
        if self.ID() == otherFilm.ID():
            return True
        else:
            return False
    
    """ 
    Il metodo __eq__ compara le istanze della classe (equiparabile all'operatore ==)
    """
    def __eq__(self, otherFilm: object)-> bool:
        # Check: se l'attributo 'otherFilm' non è un istanza di film 
            # o gli ID tra i due oggetti Non sono uguali
        
        if not isinstance(otherFilm, Film) or self.ID() != otherFilm.ID():
            
            # Ritorna False
            return False
        
        # Altrimenti compara gli ID tra i due oggetti di defualt e restiuisce True
        return self.ID() == otherFilm.ID() and self.Title() == otherFilm.Title()


bo = Film(0, 'palle')
cosa = Film(1, 'palle')

if bo == cosa:
    print('no')