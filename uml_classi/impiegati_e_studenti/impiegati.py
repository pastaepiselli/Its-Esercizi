from persona import *
from mytipes import *

class Impiegato(Persona):

    _stipendio: RealGEZ
    _ruolo: Ruolo
    _is_responsabile: bool # [0..1]

    _nome: str # mutabile, noto alla nascita
    _cognome: str # mutabile, noto alla nascita
    _cf: CodiceFiscale # mutabile, noto alla nascita
    _nascita: datetime.date # immutabile, noto alla nascita
    _maternita: IntGEZ # mutabile, probabilmente non noto alla nascita
    _genere: Genere # mutabile, noto alla nascita
    _posizione_militare: PosizioneMilitare # mutabile
