class Indirizzo:
    # l'underscore indica attributi protetti, possono accedere anche le sottoclassi di indirizzo
    _via: str
    _civico: int

    def __init__(self, via: str, civico: int) -> None:

        self._via = via
        self._civico = civico

    def via(self):

        return self._via
    
    def civico(self):

        return self._civico
    

    def __hash__(self):
        # l'hash si calcola con i campi dell'init
        return hash( (self._via, self._civico) )
    
    def __eq__(self, other) -> bool:

        if  other is None or  not isinstance(other, type(self)) or hash(self) != hash(other):

            return False
        
        return self._via == other._via and self._civico == other._civico
    



        
        